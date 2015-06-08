from __future__ import print_function
import argparse

import requests


__version__ = '0.0.4'
description = 'A simple wrapper for waifu2x.'
DEMO_API_URL = 'http://waifu2x.udp.jp/api'
NOISE = ('none', 'low', 'high',)


def post_image(img, filename='', **kwargs):
    url = DEMO_API_URL
    data = dict(scale='none', noise='high')
    data.update(kwargs)
    print('Uploading... Please sit down and relax!')
    res = requests.post(url, data=data, files={'file': (filename, img, 'image/jpeg', {'Expires': '0'})})
    return res.content


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('filename', help='Image file name')
    parser.add_argument('--scale', type=int, default=0, help='Scale times, 0 means 1x, 1 to 1.6x, 2 to 2x. Default value is 0.')
    parser.add_argument('--noise', type=int, default=2, help='Noise reduction: 0-2, higher is better. Default 2.')

    args = parser.parse_args()
    filename = args.filename
    scale = args.scale
    noise = args.noise
    if scale not in (0, 1, 2):
        raise ValueError, 'scale should be 0, 1 or 2'
    if noise not in (0, 1, 2):
        raise ValueError, 'noise should be 0, 1 or 2'

    file_name_set = filename.rsplit('.')
    file_save_name = '.'.join((file_name_set[0], '%s@%d'%(NOISE[noise], scale), file_name_set[-1]))

    with open(filename) as img:
        try:
            res = post_image(img, filename=filename, scale=scale, noise=noise)
        except requests.HTTPError:
            print('Something wrong with the Internet, please try again later.')
        else:
            with open(file_save_name, 'wb') as hand:
                hand.write(res)


if __name__ == '__main__':
    main()
