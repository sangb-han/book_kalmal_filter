from collections import deque


class MovAverageFilter:
    """
    이동 평균 필터
    """

    def __init__(self, n):
        self.n = n
        self.first_run = True

        self.prev_nums = [0 for x in range(self.n)]
        self.prev_avg = None

    def average(self, x):
        if self.first_run:
            self.prev_nums = deque([x for n in range(self.n)])
            self.prev_avg = x
            self.first_run = False
        else:
            first_x = self.prev_nums.popleft()
            self.prev_nums.append(x)
            self.prev_avg = self.prev_avg + (x-first_x)/self.n

        return self.prev_avg
