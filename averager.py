"""
Averager
the second implementation works more reliably
"""


class Averager():
    def __init__(self):
        self.n = 0  # sequence length
        self.x = 0  # current avg value
    
    def __call__(self, value):
        self.n += 1
        self.x += (value - self.x) / self.n
        return self.x


def make_averager():
    n = 0
    total = 0
    def closure(value):
        nonlocal n, total
        n += 1
        total += value
        return total / n
    return closure


avg1 = Averager()
avg2 = make_averager()


# demo
if __name__ == '__main__':
    from random import randint
    for value in (randint(-5, 10) for _ in range(25)):
        test = (v1 := avg1(value)) == (v2 := avg2(value))
        print(f"test = {test}: v1={v2}, v2={v2}")
