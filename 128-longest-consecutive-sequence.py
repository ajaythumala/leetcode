def longestConsecutive(self, nums: List[int]) -> int:
    long_streak = 0
    h_set = set()
    for num in nums:
        h_set.add(num)
    print(h_set)

    for num in nums:
        if num - 1 in h_set:
            continue
        cur_num = num
        cur_streak = 1;
        while cur_num + 1 in h_set:
            cur_num += 1
            cur_streak += 1
        long_streak = max(long_streak, cur_streak)
    return long_streak
