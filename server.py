from biome import Biome, HeightMapBiome
from fastapi import FastAPI
from heightmap import HeightMap
from io import BytesIO
from moisturemap import MoistureMap
from noiserange import NoiseRange
from fastapi.responses import Response

app = FastAPI()

@app.get("/{width}/{height}/{scale}/{tile_size}")
def read_root(
    width: int,
    height: int,
    lacunarity: float = 3.0,
    octaves: int = 8,
    persistence: float = 0.5,
    scale: float = 200,
    x_offset: float = 0.0,
    y_offset: float = 0.0,
    tile_size: int = 4,
    waterLevel: float = -0.72,
    shoreLevel: float = -0.44,
    sandLevel: float = -0.16,
    landLevel: float = 0.12,
    mountainLevel: float = 0.44,
    peakLevel: float = 0.72,
    json: bool = False
):
    noise_ranges = [
        NoiseRange('peak', peakLevel),
        NoiseRange('mountain', mountainLevel),
        NoiseRange('land', landLevel),
        NoiseRange('sand', sandLevel),
        NoiseRange('shore', shoreLevel),
        NoiseRange('water', waterLevel),
    ]

    height_map = HeightMap(
        width=width,
        height=height,
        noise_ranges=noise_ranges,
        scale=scale,
        octaves=octaves,
        persistence=persistence,
        lacunarity=lacunarity,
        x_offset=x_offset,
        y_offset=y_offset
    )

    moisture_map = MoistureMap(
        width=width,
        height=height,
        noise_ranges=[], # dont specify noise ranges
        scale=scale,
        octaves=octaves,
        persistence=persistence,
        lacunarity=lacunarity,
        x_offset=x_offset,
        y_offset=y_offset
    )

    height_map.moisturize(moisture_map)
    height_map.draw_image(tile_size)

    if json:
        return height_map.get_json()

    memoryStorage = BytesIO()

    height_map.get_image().save(memoryStorage, format="png")

    return Response(
        content=memoryStorage.getvalue(),
        media_type="image/png"
    )
