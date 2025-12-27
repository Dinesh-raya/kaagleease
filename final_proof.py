import pandas as pd
from kaggleease import load, search, __version__
import os

print(f"--- KaggleEase Verification Suite v{__version__} ---")

def test_load(handle, description):
    print(f"\n[TEST] {description} ('{handle}')")
    try:
        result = load(handle)
        if isinstance(result, pd.DataFrame):
            print(f"✅ SUCCESS: Loaded as DataFrame. Columns: {list(result.columns[:3])}")
        elif isinstance(result, str):
            print(f"✅ SUCCESS: Loaded as Path: {result}")
        else:
            print(f"❓ UNEXPECTED TYPE: {type(result)}")
    except Exception as e:
        print(f"❌ FAILED: {str(e)}")

# 1. Competition Test
test_load("titanic", "Official Competition Detection")

# 2. Obscured Metadata Test
test_load("heptapod/titanic", "Obscured REST API Bypass")

# 3. Path Fallback Test (Images)
test_load("resnet50", "Non-tabular Path Fallback")

# 4. JSON Test
test_load("rtatman/iris-dataset-json", "JSON Format Support")

print("\n--- Verification Complete ---")
