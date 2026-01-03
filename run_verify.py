import os
import sys
import logging
import pandas as pd

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("VERIFY")

def run_verification():
    # Insert local path to ensure we use current code
    sys.path.insert(0, os.getcwd())
    
    import kaggleease
    print(f"DEBUG: Running against KaggleEase Version: {kaggleease.__version__ if hasattr(kaggleease, '__version__') else 'Unknown'}")
    
    from kaggleease import load, search
    from kaggleease.errors import KaggleEaseError
    
    print("\n" + "="*50)
    print("STEP 1: Testing search command")
    print("="*50)
    try:
        results = search("nlp disaster", top=3)
        print(f"PASS: Found {len(results)} results.")
        for r in results:
            print(f" - {r['handle']} ({r['votes']} votes)")
    except Exception as e:
        print(f"FAIL: Search failed: {e}")

    print("\n" + "="*50)
    print("STEP 2: Testing implicit resolution ('titanic')")
    print("="*50)
    try:
        df = load("titanic")
        print(f"PASS: Loaded implicit handle. Shape: {df.shape}")
    except Exception as e:
        print(f"FAIL: Implicit load failed: {e}")

    print("\n" + "="*50)
    print("STEP 3: Testing fuzzy intelligence ('kaggle/titanik')")
    print("="*50)
    try:
        load("kaggle/titanik")
    except KaggleEaseError as e:
        print(f"VERIFIED: Caught expected error with suggestions.")
        print(f"Message: {e.message}")
        print(f"💡 Suggestion: {e.fix_suggestion}")
    except Exception as e:
        print(f"FAIL: Unexpected error type: {type(e)} -> {e}")

    print("\n" + "="*50)
    print("STEP 4: Stress Testing Universal Resolution (v1.3.8)")
    print("="*50)
    stress_handles = [
        "titanic",                     # Competition (DataFrame)
        "heptapod/titanic",            # Obscured Dataset (DataFrame)
        "rtatman/iris-dataset-json",   # JSON support
        "keras/resnet50",              # Non-tabular (Returns Path String)
    ]
    
    for h in stress_handles:
        print(f"\n--- Testing: {h} ---")
        try:
            result = load(h)
            if isinstance(result, pd.DataFrame):
                print(f"✅ SUCCESS: Loaded {h} as DataFrame. Shape: {result.shape}")
                print(f"Columns: {list(result.columns[:3])}")
            else:
                print(f"✅ SUCCESS: Loaded {h} as Path. Path: {result}")
        except Exception as e:
            print(f"❌ ERROR: {e}")

    print("\n" + "="*50)
    print("STEP 5: Testing Search Integrity")
    print("="*50)
    try:
        results = search("titanic", top=5)
        for r in results:
            print(f"Ref: {r['handle']} | Title: {r['title']} | Votes: {r['votes']}")
            # Proactively try to list files for the top result to verify search-to-load pipeline
            try:
                from kaggleease.client import KaggleClient
                c = KaggleClient()
                files = c.list_files(r['handle'])
                print(f"   -> Found {len(files)} files. (Link Valid)")
            except Exception as le:
                print(f"   !! Link Invalid: {le}")
    except Exception as e:
        print(f"FAIL: Search integrity failed: {e}")

if __name__ == "__main__":
    run_verification()
