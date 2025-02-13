class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        starting_interval = 0
        ending_interval = 0
        for index, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                starting_interval = newInterval[0]
            print(starting_interval)
