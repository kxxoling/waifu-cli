#!/usr/bin/env python
from setuptools import setup
from waifu import __version__ as version, description


def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()


setup(
    name='waifu-cli',
    version=version,
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    zip_safe=False,
    py_modules=['waifu'],
    entry_points={
        'console_scripts': [
            'waifu = waifu:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    license="MIT",
    description=description,
    long_description=fread('README.rst'),
    author='Kane Blueriver',
    author_email='kxxoling@gmail.com',
    url='https://github.com/kxxoling/waifu-cli',
)

