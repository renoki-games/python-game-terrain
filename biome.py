import enum

class HeightMapBiome(enum.Enum):
    OCEAN = 1
    SHALLOWS = 2
    BEACH = 3
    SCORCHED = 4
    BARE = 5
    TUNDRA = 6
    TEMPERATE_DESERT = 7
    SHRUBLAND = 8
    GRASSLAND = 9
    TEMPERATE_DECIDUOUS_FOREST = 10
    TEMPERATE_RAIN_FOREST = 11
    SUBTROPICAL_DESERT = 12
    TROPICAL_SEASONAL_FOREST = 13
    TROPICAL_RAIN_FOREST = 14
    SNOW = 15
    TAIGA = 16
    SWAMP = 17

class Biome:
    def __init__(self, noise_ranges):
        self.noise_range = {}

        for noise_range in noise_ranges:
            self.noise_range[noise_range.name] = noise_range

    def get_biome(self, elevation, moisture):
        """ Determine the biome from the elevation & moisture of the tile """

        """ Water/Shore"""
        if elevation <= self.noise_range['water'].threshold:
            return HeightMapBiome.OCEAN

        if elevation <= self.noise_range['sand'].threshold and moisture >= 0.2:
            return HeightMapBiome.SWAMP

        if elevation <= self.noise_range['shore'].threshold:
            return HeightMapBiome.SHALLOWS

        if elevation <= self.noise_range['sand'].threshold:
            return HeightMapBiome.BEACH

        """ High mountain """
        if elevation > self.noise_range['peak'].threshold:
            if moisture < 0.1:
                return HeightMapBiome.SCORCHED
            elif moisture < 0.2:
                return HeightMapBiome.BARE
            elif moisture < 0.5:
                return HeightMapBiome.TUNDRA

            return HeightMapBiome.SNOW

        """ Mountain """
        if elevation > self.noise_range['mountain'].threshold:
            if moisture < 0.33:
                return HeightMapBiome.TEMPERATE_DESERT
            elif moisture < 0.66:
                return HeightMapBiome.SHRUBLAND

            return HeightMapBiome.TAIGA

        """ Land """
        if moisture < 0.16:
           return HeightMapBiome.SUBTROPICAL_DESERT
        if moisture < 0.33:
           return HeightMapBiome.GRASSLAND
        if moisture < 0.66:
           return HeightMapBiome.TROPICAL_SEASONAL_FOREST

        return HeightMapBiome.TROPICAL_RAIN_FOREST

    def get_biome_name(self, elevation, moisture):
        return HeightMapBiome(self.get_biome(elevation, moisture)).name

    def get_color(self, elevation, moisture):
        value = self.get_biome(elevation, moisture)

        if value == HeightMapBiome.OCEAN:
            return (54, 62, 150) # dark blue
        elif value == HeightMapBiome.SHALLOWS:
            return (88, 205, 237) # cyan
        elif value == HeightMapBiome.BEACH:
            return (247, 247, 119) # yellow
        elif value == HeightMapBiome.SCORCHED:
            return (247, 149, 119) # peach
        elif value == HeightMapBiome.BARE:
            return (168, 166, 165) # grey
        elif value == HeightMapBiome.TUNDRA:
            return (132, 173, 158) # grey green
        elif value == HeightMapBiome.TEMPERATE_DESERT:
            return (227, 155, 0) # orange
        elif value == HeightMapBiome.SHRUBLAND:
            return (62, 110, 58) # olive
        elif value == HeightMapBiome.GRASSLAND:
            return (55, 181, 43) # green
        elif value == HeightMapBiome.TEMPERATE_DECIDUOUS_FOREST:
            return (62, 138, 55) # darker green
        elif value == HeightMapBiome.TEMPERATE_RAIN_FOREST:
            return (161, 38, 255) # violet
        elif value == HeightMapBiome.SUBTROPICAL_DESERT:
            return (255, 214, 153) # fleuro yellow
        elif value == HeightMapBiome.TROPICAL_SEASONAL_FOREST:
            return (102, 153, 0) # some kind of green
        elif value == HeightMapBiome.TROPICAL_RAIN_FOREST:
            return (255, 0, 119) # rose
        elif value == HeightMapBiome.SNOW:
            return (255, 255, 255) # white
        elif value == HeightMapBiome.TAIGA:
            return (62, 87, 71) # dark olive
        elif value == HeightMapBiome.SWAMP:
            return (92, 112, 104) # grey green
        else:
            return (0, 0, 0) # black