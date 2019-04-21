#!/usr/bin/env python

from distutils.core import setup
import sys, os, multiprocessing
import colorweave

requires = []

py_version = sys.version_info[:2]

PY3 = py_version[0] == 3

if PY3:
    raise RuntimeError('colorweave runs only on Python 2.6 or Python 2.7')
else:
    if py_version < (2, 6):
        raise RuntimeError('On Python 2, colorweave requires Python 2.6 or better')
    if py_version > (2, 6):
        pass

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='colorweave',
    version='0.1',
    description="Extract dominant colors from an image as a color palette",
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: Free for non-commercial use",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    install_requires=[
	    'Pillow>=3.3.2',
            'PIL>=1.1.6',
            'colormath>=1.0.8',
            'numpy>=1.6.1',
	    'webcolors>=1.4',
        ],
    keywords='color dominant palette colorweave kmeans css3 css21 name webcolors',
    author='Jyotiska NK',
    author_email='jyotiska123@gmail.com',
    url='http://github.com/jyotiska/colorweave',
    py_modules=['colorweave'],
    scripts=['colorweave.py'],
)
