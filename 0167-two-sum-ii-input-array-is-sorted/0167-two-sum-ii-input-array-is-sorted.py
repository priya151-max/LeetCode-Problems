class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at opposite ends
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-based indices as required
                return [left + 1, right + 1]
            elif current_sum < target:
                # If sum is too small, move left pointer right to increase it
                left += 1
            else:
                # If sum is too large, move right pointer left to decrease it
                right -= 1
        
        return []
