class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for item in self.iterable:
            pos = sum(f(item) for f in self.funcs)
            neg = len(self.funcs) - pos
            if self.judge(pos, neg):
                yield item
                