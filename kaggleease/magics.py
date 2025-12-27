import argparse
import shlex
from typing import Any
import logging
from IPython.core.magic import Magics, magics_class, line_magic
from IPython.display import display, Markdown

from .load import load as core_load
from .search import search as core_search
from .errors import KaggleEaseError

logger = logging.getLogger(__name__)

class KaggleController:
    """
    Decoupled controller for handling %kaggle commands.
    Designed to be testable without an IPython kernel.
    """
    def __init__(self, load_fn=core_load, search_fn=core_search, user_ns=None):
        self.load_fn = load_fn
        self.search_fn = search_fn
        self.user_ns = user_ns if user_ns is not None else {}

    def handle_command(self, line: str) -> dict:
        """
        Parses the command line and executes the logic.
        Returns a dict: {'type': 'df'|'text'|'error', 'content': ..., 'message': str}
        """
        parser = argparse.ArgumentParser(prog="%kaggle", add_help=False)
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Load command
        load_parser = subparsers.add_parser("load", help="Load a dataset")
        load_parser.add_argument("dataset", type=str, help="Dataset handle (e.g., 'titanic')")
        load_parser.add_argument("--file", type=str, help="Specific file to load")
        load_parser.add_argument("--as", dest="dest_var", type=str, default="data", help="Variable name to store the DataFrame in")
        load_parser.add_argument("--timeout", type=int, default=300, help="Timeout in seconds for the operation")

        # Preview command
        preview_parser = subparsers.add_parser("preview", help="Preview a dataset")
        preview_parser.add_argument("dataset", type=str, help="Dataset handle")
        preview_parser.add_argument("--file", type=str, help="Specific file to preview")
        preview_parser.add_argument("--timeout", type=int, default=300, help="Timeout in seconds for the operation")

        # Search command
        search_parser = subparsers.add_parser("search", help="Search for datasets")
        search_parser.add_argument("query", type=str, help="Search query")
        search_parser.add_argument("--timeout", type=int, default=30, help="Timeout in seconds for the search operation")
        search_parser.add_argument("--top", type=int, default=5, help="Maximum number of results to return")

        try:
            if not line.strip() or line.strip() in ('-h', '--help'):
                 return {'type': 'help', 'content': parser.format_help()}

            args = parser.parse_args(shlex.split(line))

            if args.command == "load":
                df = self.load_fn(args.dataset, file=args.file, timeout=args.timeout)
                # Side effect: inject into namespace
                self.user_ns[args.dest_var] = df
                return {
                    'type': 'df', 
                    'content': df, 
                    'message': f"Dataset loaded into variable '{args.dest_var}'."
                }

            elif args.command == "preview":
                df = self.load_fn(args.dataset, file=args.file, timeout=args.timeout)
                return {
                    'type': 'df',
                    'content': df,
                    'message': "Previewing dataset:"
                }
                
            elif args.command == "search":
                results = self.search_fn(args.query, top=args.top, timeout=args.timeout)
                return {
                    'type': 'search_results',
                    'content': results,
                    'message': ""
                }
            
            return {'type': 'help', 'content': parser.format_help()}

        except KaggleEaseError as e:
            return {'type': 'error', 'content': e}
        except SystemExit:
            return {'type': 'help', 'content': parser.format_help()}
        except Exception as e:
            return {'type': 'fatal_error', 'content': str(e)}

@magics_class
class KaggleMagics(Magics):
    def __init__(self, shell: Any) -> None:
        super(KaggleMagics, self).__init__(shell)
        self.controller = KaggleController(user_ns=shell.user_ns)

    @line_magic
    def kaggle(self, line: str) -> None:
        """
        A magic command to interact with the KaggleEase library.
        """
        # Ensure namespace is up to date (though reference should be live)
        self.controller.user_ns = self.shell.user_ns
        
        result = self.controller.handle_command(line)
        
        if result['type'] == 'help':
            display(Markdown(f"<pre>{result['content']}</pre>"))
            
        elif result['type'] == 'df':
            logger.info(result['message'])
            display(result['content'].head(5))
            
        elif result['type'] == 'search_results':
            results = result['content']
            if results:
                md = "| Handle | Title | Size | Votes |\n"
                md += "|---|---|---|---|\n"
                for r in results:
                    md += f"| {r['handle']} | {r['title']} | {r['size']} | {r['votes']} |\n"
                display(Markdown(md))
            else:
                logger.info("No results found.")
                
        elif result['type'] == 'error':
            e = result['content']
            msg = f"### ❌ KaggleEase Error\n\n**{e.message}**\n\n"
            if hasattr(e, 'fix_suggestion') and e.fix_suggestion:
                msg += f"> **💡 Fix Suggestion:** {e.fix_suggestion}\n\n"
            if hasattr(e, 'docs_link') and e.docs_link:
                msg += f"🔗 [Documentation]({e.docs_link})\n"
            display(Markdown(msg))
            
        elif result['type'] == 'fatal_error':
             display(Markdown(f"**An unexpected error occurred:** {result['content']}"))

def register_magics() -> None:
    """
    Function to register the magics with IPython.
    """
    try:
        from IPython import get_ipython
        ipython = get_ipython()
        if ipython:
            ipython.register_magics(KaggleMagics)
    except ImportError:
        pass 
