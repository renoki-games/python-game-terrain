
class NoiseRange:
    def __init__(self, name, threshold):
        self.name = name
        self.threshold = threshold

    def __iter__(self):
        yield 'name', self.name
        yield 'threshold', self.threshold
