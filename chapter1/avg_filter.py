
class AverageFilter(object):
    """
    평균을 계산하는 Filter
    """

    def __init__(self):
        self.k = 0
        self.prev_avg = 0.0

    def average(self, x) -> float:
        self.k = self.k+1

        alpha: float = (self.k-1)/self.k
        self.prev_avg = alpha * self.prev_avg + (1-alpha) * x

        return self.prev_avg
