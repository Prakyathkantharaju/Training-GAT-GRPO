"""
Pydantic Schema for Reasoning Agent Output
"""

from pydantic import BaseModel, Field
from typing import List, Optional


class ReasoningOutput(BaseModel):
    """Schema for Reasoning Agent output"""
    
    algorithm_breakdown: str = Field(
        ..., 
        description="Detailed breakdown of how the algorithm works",
        example="This hash map approach works by storing each number and its index as we iterate through the array. For each number, we calculate what value we need to find (target - current number) and check if it already exists in our hash map."
    )
    
    data_structures_needed: List[str] = Field(
        ..., 
        description="List of data structures and variables required",
        example=["Hash map/dictionary to store numbers and indices", "Integer variables for current number and complement", "Loop variable for array iteration"]
    )
    
    implementation_steps: List[str] = Field(
        ..., 
        description="Detailed step-by-step implementation plan",
        example=[
            "Initialize an empty dictionary to store number -> index mapping",
            "Iterate through the array with enumerate to get both index and value",
            "For each number, calculate the complement (target - current number)",
            "Check if complement exists in the dictionary",
            "If found, return [complement_index, current_index]",
            "If not found, add current number and index to dictionary",
            "If no solution found after iteration, return None or raise exception"
        ]
    )
    
    edge_cases: List[str] = Field(
        ..., 
        description="Edge cases to handle in the implementation",
        example=[
            "Empty array - should return None",
            "Array with only one element - should return None", 
            "No valid pair exists - should return None",
            "Multiple valid pairs - return the first one found",
            "Same number used twice - ensure we don't use same index twice"
        ]
    )
    
    complexity_analysis: str = Field(
        ..., 
        description="Analysis of time and space complexity with explanation",
        example="Time Complexity: O(n) - we iterate through the array once, and dictionary lookup is O(1) on average. Space Complexity: O(n) - in worst case we store all n elements in the dictionary."
    )
    
    potential_pitfalls: List[str] = Field(
        ..., 
        description="Common mistakes or issues to avoid",
        example=[
            "Don't add current number to dictionary before checking for complement",
            "Make sure to return indices, not the actual values",
            "Handle the case where same element appears multiple times",
            "Ensure we don't use the same array index twice"
        ]
    )
    
    pseudo_code: Optional[str] = Field(
        default=None,
        description="Optional pseudo-code representation of the algorithm",
        example="""
        function twoSum(nums, target):
            hash_map = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in hash_map:
                    return [hash_map[complement], i]
                hash_map[num] = i
            return None
        """
    )

    class Config:
        """Pydantic configuration"""
        validate_assignment = True
        extra = "forbid"  # Don't allow extra fields


# Example usage
if __name__ == "__main__":
    # Test the schema
    example = ReasoningOutput(
        algorithm_breakdown="Hash map approach: store numbers with their indices, then check for complements",
        data_structures_needed=["Dictionary/hash map", "Loop variables"],
        implementation_steps=[
            "Initialize empty dictionary",
            "Loop through array",
            "Calculate complement",
            "Check if complement in dictionary",
            "Return indices if found, otherwise continue"
        ],
        edge_cases=["Empty array", "No solution", "Multiple solutions"],
        complexity_analysis="Time: O(n), Space: O(n)",
        potential_pitfalls=["Don't use same index twice", "Return indices not values"]
    )
    
    print("Reasoning schema validation successful!")
    print(f"Algorithm: {example.algorithm_breakdown}")
    print(f"Steps: {len(example.implementation_steps)}")
    print(f"Edge cases: {len(example.edge_cases)}") 