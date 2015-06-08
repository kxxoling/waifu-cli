===============
Waifu CLI
===============

Waifu CLI is a command line wrapper for `waifu2x <https://github.com/nagadomi/waifu2x>`_ .


Sample Usage
------------

Just input this command::

    waifu images/sample.png --scale=0 --noise=2

Will get::

    $ ls images
    sample.high@0.png sample.png

Image before:

.. image:: images/sample.png
    :alt: after

After:

.. image:: images/sample.high@0.png
    :alt: after
