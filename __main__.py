
import argparse
import click
import random
import sys

from heightmap import HeightMap
from moisturemap import MoistureMap
from noiserange import NoiseRange

def register_parsers():
    parser = argparse.ArgumentParser(description='Generate a Height Map using Procedural noise.')

    parser.add_argument('-W', '--width', help="Map width to generate.", type=int, default=600)
    parser.add_argument('-H', '--height', help="Map height to generate.", type=int, default=200)

    parser.add_argument('-l', '--lacunarity', help="The level of detail on each octave (adjusts frequency).", type=float, default=3.0)
    parser.add_argument('-o', '--octaves', help="Octaves used for generation.", type=int, default=8)
    parser.add_argument('-p', '--persistence', help="How much an octave contributes to overall shape (adjusts amplitude).", type=float, default=0.5)
    parser.add_argument('-s', '--scale', help="Higher=zoomed in, Lower=zoomed out.", type=float, default=200)

    parser.add_argument('-ox', '--x_offset', help="X-range offset.", type=float, default=0.0)
    parser.add_argument('-oy', '--y_offset', help="Y-range offset.", type=float, default=0.0)

    parser.add_argument('-box', '--base_x_offset', help="Base X-range offset.", type=float, default=0.0)
    parser.add_argument('-boy', '--base_y_offset', help="Base Y-range offset.", type=float, default=0.0)

    parser.add_argument('-ts', '--tilesize', help="Size in pixels of tiles on the map.", type=int, default=4)
    parser.add_argument('-m', '--minify', help="Minify the JSON output.", type=bool, default=False)
    parser.add_argument('-f', '--file', help="Give a name to the output files.", type=str, default=None)

    parser.add_argument('--water', help="Height level of the water.", type=float, default=-0.72)
    parser.add_argument('--shore', help="Height level of the shallow water.", type=float, default=-0.44)
    parser.add_argument('--sand', help="Height level of the sand.", type=float, default=-0.16)
    parser.add_argument('--land', help="Height of normal grass/land/forest.", type=float, default=0.12)
    parser.add_argument('--mountain', help="Height of mountains.", type=float, default=0.44)
    parser.add_argument('--peak', help="Height of huge mountains.", type=float, default=0.72)

    parser.add_argument('-r', '--random', help="Generate random offsets.", type=bool, default=False)

    return parser

def main():
    parser = register_parsers()
    args = parser.parse_args()

    x_offset = int(random.random() * pow(10, 3) if args.random else args.x_offset)
    y_offset = int(random.random() * pow(10, 3) if args.random else args.y_offset)

    noise_ranges = [
        NoiseRange('peak', args.peak),
        NoiseRange('mountain', args.mountain),
        NoiseRange('land', args.land),
        NoiseRange('sand', args.sand),
        NoiseRange('shore', args.shore),
        NoiseRange('water', args.water),
    ]

    height_map = HeightMap(
        width=args.width,
        height=args.height,
        noise_ranges=noise_ranges,
        scale=args.scale,
        octaves=args.octaves,
        persistence=args.persistence,
        lacunarity=args.lacunarity,
        x_offset=x_offset,
        y_offset=y_offset,
        base_x_offset=args.base_x_offset,
        base_y_offset=args.base_y_offset,
    )

    moisture_map = MoistureMap(
        width=args.width,
        height=args.height,
        noise_ranges=[], # dont specify noise ranges
        scale=args.scale,
        octaves=args.octaves,
        persistence=args.persistence,
        lacunarity=args.lacunarity,
        x_offset=x_offset,
        y_offset=y_offset,
        base_x_offset=args.base_x_offset,
        base_y_offset=args.base_y_offset,
    )

    height_map.moisturize(moisture_map)

    height_map.draw_image(args.tilesize)

    height_map.show_image()

    if click.confirm('Save map?', default=False):
        file_name = 'maps/' + args.file

        height_map.save(
            file_name,
            indent=4 if args.minify == False else None
        )

        print('Saved to: %s' % file_name + '.json')

if __name__ == '__main__':
    sys.exit(main())