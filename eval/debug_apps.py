import json
from datasets import load_dataset
from pprint import pprint

# Load just one sample from the dataset
try:
    print("Loading dataset...")
    dataset = load_dataset("codeparrot/apps", split="test[0:5]")
    
    # Examine each problem
    for i, problem in enumerate(dataset):
        print(f"\n--- Problem {i} ---")
        print(f"Keys in problem: {problem.keys()}")
        
        # Check solutions format
        print(f"Solutions type: {type(problem['solutions'])}")
        print(f"Solutions preview: {problem['solutions'][:100] if isinstance(problem['solutions'], str) else '[complex data]'}")
        
        # Try parsing if it's a string
        if isinstance(problem['solutions'], str):
            try:
                parsed = json.loads(problem['solutions'])
                print(f"Successfully parsed solutions as JSON. Result type: {type(parsed)}")
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
        
        # Check input_output format
        print(f"Input_output type: {type(problem['input_output'])}")
        print(f"Input_output preview: {problem['input_output'][:100] if isinstance(problem['input_output'], str) else '[complex data]'}")
        
        # Try parsing if it's a string
        if isinstance(problem['input_output'], str):
            try:
                parsed = json.loads(problem['input_output'])
                print(f"Successfully parsed input_output as JSON. Result type: {type(parsed)}")
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")

except Exception as e:
    print(f"Exception during dataset loading: {type(e).__name__}: {e}")