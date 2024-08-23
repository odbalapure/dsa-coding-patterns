def sum_three(nums: list[int], target: int):
    """
    If sum triplet exist
    :nums: Number array
    :target: Target sum
    :flag: Flag to indicate if triple exists
    """
    nums.sort()
    triplets = []
    for i in range(len(nums) - 2):
        low, high = i + 1, len(nums) - 1
        while low < high:
            triple = nums[i] + nums[low] + nums[high]
            triplets.append([nums[i], nums[low], nums[high]])
            if triple == target:
                return True
            elif triple < triple:
                low += 1
            else:
                high -= 1
    return False

def sum_three_zero(nums: list[int]) -> list[list[int]]:
    """
    Find set of sum zero triplet
    :nums: Number array
    :list: Triplet set list
    """
    nums.sort()
    triplets = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        low, high = i + 1, len(nums) - 1
        while low < high:
            total = nums[i] + nums[low] + nums[high]
            if total < 0:
                low += 1
            elif total > 0:
                high -= 1
            else:
                triplets.append([nums[i], nums[low], nums[high]])
                while low < high and nums[low] == nums[low + 1]:
                    low += 1
                while low < high and nums[high] == nums[high - 1]:
                    high -= 1
                low += 1
                high -= 1
    return triplets

print(three_sum_zero([-1,0,1,2,-1,-4])) # [-1,-1,2],[-1,0,1]]