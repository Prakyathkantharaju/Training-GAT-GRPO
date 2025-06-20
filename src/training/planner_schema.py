"""
Pydantic Schema for Planner Agent Output
"""

from pydantic import BaseModel, Field
from typing import List


class PlannerOutput(BaseModel):
    """Simple schema for Planner Agent output"""
    
    problem_description: str = Field(
        ..., 
        description="Problem description that will be passed to worker agents",
        example="Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."
    )
    
    approaches: List[str] = Field(
        ..., 
        description="List of different approaches to solve the problem",
        min_items=1,
        example=[
            "Brute force: Use nested loops to check all pairs of numbers until you find two that sum to the target. Time: O(n²), Space: O(1)",
            "Hash map: Store each number and its index in a hash map, then for each number check if its complement exists in the map. Time: O(n), Space: O(n)",
            "Two pointers: Sort the array while keeping track of original indices, then use two pointers from start and end moving based on sum comparison. Time: O(n log n), Space: O(n)"
        ]
    )

    class Config:
        """Pydantic configuration"""
        validate_assignment = True
        extra = "forbid"  # Don't allow extra fields


# Example usage
if __name__ == "__main__":
    # Test the schema
    example = PlannerOutput(
        problem_description="Given an array of integers nums and an integer target, return indices of the two numbers that add up to target.",
        approaches=[
            "Brute force: Check all pairs using nested loops. Time O(n²), Space O(1)",
            "Hash map: Use dictionary to store values and indices for O(1) lookup. Time O(n), Space O(n)",
            "Two pointers: Sort array first, then use two pointers technique. Time O(n log n), Space O(n)"
        ]
    )
    
    print("Schema validation successful!")
    print(f"Problem: {example.problem_description}")
    print(f"Number of approaches: {len(example.approaches)}")
    for i, approach in enumerate(example.approaches, 1):
        print(f"Approach {i}: {approach}")
    