from PIL import Image
import clipboard


def get_tetr(index: int):
    im = Image.open(f'frames/{index:0>4}.png')

    tetrio_map_string = ''
    width, height = im.size

    for y in range(height):
        for x in range(width):
            pixel = im.getpixel((x, y))
            if pixel == (0, 0, 0):
                tetrio_map_string += '#'
            else:
                tetrio_map_string += '_'
    tetrio_map_string += '?oo?oo,oo,oo,oo,oo'
    return tetrio_map_string

if __name__ == '__main__':
    im = Image.open('frames/0001.png')

    tetrio_map_string = ''
    width, height = im.size

    for y in range(height):
        for x in range(width):
            pixel = im.getpixel((x, y))
            if pixel == (0, 0, 0):
                tetrio_map_string += '#'
            else:
                tetrio_map_string += '_'

    print(tetrio_map_string)
    print(len(tetrio_map_string))
    tetrio_map_string += '?oo?oo,oo,oo,oo,oo'


    clipboard.copy(tetrio_map_string)