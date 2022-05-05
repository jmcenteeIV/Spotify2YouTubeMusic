
def twoSum(self, nums: List[int], target: int) -> List[int]:
    int nums_len = (len(nums)-1)
    int first_number = 0
    for range(0, nums_len):
        int second_number = (first_number + 1) 
        if nums[first_number] < target:
            for range(first_number, nums_len):
                if nums[second_number] < target:
                    if nums[first_number] + nums[second_number] == target:
                        return [first_number, second_number]
                else
                    second_number += 1
        else
            first_number += 1