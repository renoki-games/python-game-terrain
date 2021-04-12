# Game Terrain

Generate Simplex-based procedural game terrain using Python.

Forked from [jpw1991/perlin-noise-2d-terrain-generation](https://github.com/jpw1991/perlin-noise-2d-terrain-generation)

# 🚀 Installation

```bash
$ pip install -r requirements.txt
```

To run the server in production:

```bash
$ uvicorn server:app
```

To run the server in development:

```bash
$ uvicorn server:app --reload
```

# 🙌 Usage

## CLI

To generate terrain with the CLI, simply run:

```bash
$ python . --file=map
```

You will then see the image that is going to be saved and you will be asked to save it:

```bash
$ python . --file=map
Save map? [y/N]:
```

This will create the following files:

- `maps/map.json` - metadata for the image containing biomes and tiles
- `maps/map.png` - the rendered map

To see the rest of the parameters, run:

```bash
$ python . --help
```

## HTTP

Making calls to the following URL will expose the generated image:

```
http://127.0.0.1:8000/{width}/{height}/{scale}/{tile_size}
```

For example, a 100x100 image with a factor of zoom of 20 and 10 pixels per tile would be:

```
http://127.0.0.1:8000/100/100/20/10
```

To get the JSON metadata regarding biomes, tiles and curent parameters for the same image, add `?json=1` to the end (it might take a while, there are 10.000 tiles in the JSON):

```
http://127.0.0.1:8000/100/100/20/10?json=1
```

For a full list of query parameters, you can check `server.py`'s `display_image` method parameters.