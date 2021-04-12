# Game Terrain

Generate Simplex-based procedural game terrain using Python.

Forked from [jpw1991/perlin-noise-2d-terrain-generation](https://github.com/jpw1991/perlin-noise-2d-terrain-generation)

## 🚀 Installation

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

## 🙌 Usage

### 🖥 CLI

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

## 🔗 HTTP REST API

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

## 🐳 Docker

### Supported Python Versions

The following Python versions are deployed on an day-to-day basis:

- `3.7`
- `3.8`
- `3.9`

## Versioning

The project builds support multiple Python versions for each Github tag. The format for container tags is the following:

```
renokigames/python-game-terrain:[pyton_version]-[repo_tag]
```

For example, this is going to be the latest tag for Python `3.9`:

```
renokigames/python-game-terrain:3.9-latest
```

### Version Specific Tags

For version-specific tags, you might use the following image and tag, `1.0.0` being the repo tag:

```
renokigames/python-game-terrain:3.9-1.0.0
```

### Python Majors and Minor versions

You can also specify major repo versions, where `1.0` means `1.0.x`:

```
renokigames/python-game-terrain:3.9-1.0
```

You can also specify major.minor repo versions, where `1` means `1.x` (all 1.x versions):

```
renokigames/python-game-terrain:3.9-1
```

### Latest Tags

For latest tags, use `latest` instead any other version:

```
renokigames/python-game-terrain:3.9-latest
```