def solution(nums):
    answer = 0
    set_nums = len(set(nums))
    maxlen = len(nums) // 2
    if maxlen > set_nums:
        answer = set_nums
    else:
        answer = maxlen
    return answer