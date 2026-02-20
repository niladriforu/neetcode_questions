class Countdown:
    def __init__(self, start):
        self.current = start
        print(self.current)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# it = iter(Countdown(5))
obj = Countdown(5)
print(obj.__iter__())





