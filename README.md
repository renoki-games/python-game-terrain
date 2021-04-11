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