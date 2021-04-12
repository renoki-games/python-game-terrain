import json

from biome import Biome, HeightMapBiome
from noise import pnoise2, snoise2
from tile import Tile
from noiserange import NoiseRange
from PIL import Image, ImageFont, ImageDraw

class HeightMap:
    def __init__(
        self,
        width,
        height,
        noise_ranges,
        scale,
        octaves,
        persistence=0.5,
        lacunarity=2.0,
        x_offset=0.0,
        y_offset=0.0,
        base_x_offset=0.0,
        base_y_offset=0.0,
    ):
        self.width = width
        self.height = height
        self.noise_ranges = noise_ranges
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.base_x_offset = base_x_offset
        self.base_y_offset = base_y_offset

        self.tiles = []
        self.image = None
        self.biome = Biome(self.noise_ranges)
        self.generated = False

    def moisturize(self, moisture_map):
        if not moisture_map.generated:
            moisture_map = moisture_map.generate()

        if not self.generated:
            self.generate()

        for tile_index in range(len(self.tiles)):
            tile = self.tiles[tile_index]
            moisture_tile = moisture_map.tiles[tile_index]

            self.tiles[tile_index].moisture_noise_value = moisture_tile.noise_value
            self.tiles[tile_index].biome_name = self.biome.get_biome_name(tile.noise_value, moisture_tile.noise_value)

    def generate(self):
        if self.generated:
            return self

        for y in range(self.height):
            for x in range(self.width):
                noise_value = snoise2(
                    x=(x/self.scale) + self.x_offset + self.base_x_offset,
                    y=(y/self.scale) + self.y_offset + self.base_y_offset,
                    octaves=self.octaves,
                    persistence=self.persistence,
                    lacunarity=self.lacunarity
                )

                self.tiles.append(Tile(x, y, noise_value))

        self.generated = True

        return self

    def draw_image(self, tile_size):
        if not self.generated:
            self.generate()

        self.image = Image.new(
            'RGBA',
            size=(self.width * tile_size, self.height * tile_size),
            color=(0, 0, 0)
        )

        image = ImageDraw.Draw(self.image)

        for tile_index in range(len(self.tiles)):
            tile = self.tiles[tile_index]
            biome_color = self.biome.get_color(tile.noise_value, tile.moisture_noise_value)

            image.rectangle([
                tile.x * tile_size,
                tile.y * tile_size,
                tile.x * tile_size + tile_size,
                tile.y * tile_size + tile_size
            ], fill=biome_color)

    def show_image(self):
        if self.get_image() is not None:
            self.get_image().show()

    def save_image(self, file_name):
        if self.get_image() is not None:
            self.get_image().save(file_name + ".png")

    def save_json(self, file_name, indent=None):
        with open(file_name + ".json", 'w', encoding='utf8') as file:
            print(self.get_json())
            json.dump(self.get_json(), file, indent=indent)
            file.close()

    def get_json(self):
        return dict(self)

    def get_image(self):
        return self.image

    def save(self, file_name, indent=None):
        self.save_image(file_name)
        self.save_json(file_name, indent=indent)

    def __iter__(self):
        yield 'width', self.width
        yield 'height', self.height
        yield 'scale', self.scale
        yield 'octaves', self.octaves
        yield 'noise_ranges', [dict(noise_range) for noise_range in self.noise_ranges]

        yield 'offsets', {
            "current": {
                "x": self.x_offset,
                "y": self.y_offset,
            },
            "base": {
                "x": self.base_x_offset,
                "y": self.base_y_offset,
            },
        }

        yield 'biomes', {biome.name: {
            "name": biome.name,
            "value": biome.value,
        } for name, biome in HeightMapBiome.__members__.items()}

        yield 'tiles', [dict(tile) for tile in self.tiles]
