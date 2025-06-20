"""
Format Verifier Algorithm
Simple regex-based function to check for <think> and <answer> tags
"""

import re
from typing import Optional
from pydantic import BaseModel, ValidationError

def verify_coding_solution(candidate_func, test_string: str) -> bool:
    """
    Executes a test string and runs it against a candidate function.
    
    Args:
        candidate_func: The function to test (your solution)
        test_string: String containing Python code that defines a 'check' function
        
    Returns:
        bool: True if all tests pass, False if any test fails
    """
    try:
        # Create a local namespace for executing the test
        local_namespace = {}
        
        # Execute the test string to define the 'check' function
        exec(test_string, {}, local_namespace)
        
        # Get the check function from the local namespace
        check_function = local_namespace.get('check')
        
        if check_function is None:
            print("Error: No 'check' function found in test string")
            return False
        
        # Run the check function with our candidate
        check_function(candidate_func)
        
        print("All tests passed!")
        return True
        
    except AssertionError as e:
        print(f"Test failed: {e}")
        return False
    except Exception as e:
        print(f"Error executing test: {e}")
        return False

def verify_format_solution(data: str, candidate_format: BaseModel) -> bool:

    """
    Verify that the candidate format is valid for the given data.
    """
    try:
        candidate_format.model_validate_json(data)
        return True
    except ValidationError as e:
        print(f"Validation error: {e}")
        return False

    

def verify_format(text: str) -> bool:
    """
    Verify that text contains <think>...</think> followed by <answer>...</answer>
    
    Args:
        text: The text to verify
        
    Returns:
        bool: True if format is valid, False otherwise
    """
    # Pattern to match <think>content</think> followed by <answer>content</answer>
    pattern = r'<think>.*?</think>\s*<answer>.*?</answer>'
    
    # Check if the pattern exists in the text
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    
    return match is not None


def extract_think_content(text: str) -> Optional[str]:
    """Extract content from <think> tags"""
    match = re.search(r'<think>(.*?)</think>', text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else None


def extract_answer_content(text: str) -> Optional[str]:
    """Extract content from <answer> tags"""
    match = re.search(r'<answer>(.*?)</answer>', text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else None


# Test the function
if __name__ == "__main__":
    test_cases = [
        "<think>This is my thinking</think><answer>This is my answer</answer>",
        "<think>Thinking here</think>\n<answer>Answer here</answer>",
        "<think>Only thinking</think>",
        "<answer>Only answer</answer>",
        "No tags at all",
        "<think>Thinking</think> some other text <answer>Answer</answer>",
    ]
    
    for i, test in enumerate(test_cases):
        result = verify_format(test)
        print(f"Test {i+1}: {result} - {test[:50]}...")
        
        if result:
            think = extract_think_content(test)
            answer = extract_answer_content(test)
            print(f"  Think: {think}")
            print(f"  Answer: {answer}")
        print()



   