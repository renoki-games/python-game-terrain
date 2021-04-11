
class Tile:
    def __init__(self, x, y, noise_value):
        self.x = x
        self.y = y
        self.noise_value = noise_value
        self.moisture_noise_value = None
        self.biome = None
        self.biome_name = None

    def __iter__(self):
        yield 'x', self.x
        yield 'y', self.y
        yield 'noise_value', self.noise_value
        yield 'moisture_noise_value', self.moisture_noise_value
        yield 'biome', self.biome
        yield 'biome_name', self.biome_name
