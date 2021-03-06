#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import os
import re
from os.path import dirname
from os.path import join
from os.path import expanduser


from setuptools import find_packages
# from setuptools import setup
from numpy.distutils.core import setup, Extension

def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


# Set the C-code logging level.
# If DEBUG is set, we default to the highest level, but if not,
# we set it to the level just above no logging at all.
log_level = os.environ.get("LOG_LEVEL", 3 if "DEBUG" in os.environ else 1)
available_levels = ["NONE","ERROR", "WARNING", "INFO", "DEBUG", "SUPER_DEBUG", "ULTRA_DEBUG"]


if isinstance(log_level, str) and log_level.upper() in available_levels:
    log_level = available_levels.index(log_level.upper())

try:
    log_level = int(log_level)
except ValueError:
    # note: for py35 support, can't use f strings.
    raise ValueError("LOG_LEVEL must be specified as a positive integer, or one of {}".format(available_levels))


setup(
    name='py21cmmc_wv',
    version='0.1.0',
    license='MIT license',
    description='A plugin for py21cmmc that offers likelihoods based on wavelet decomposition',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Steven Murray',
    author_email='steven.murray@curtin.edu.au',
    url='https://github.com/steven-murray/py21cmmc_wv',
    packages=find_packages(),
#    package_dir={'': 'src'},
#    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=[
        'py21cmmc',
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    ext_modules=[
       Extension(
            'py21cmmc_wv.ctransforms',
            ['py21cmmc_wv/transforms.c'],
            extra_compile_args = ['-Ofast', '-fopenmp', "-DLOG_LEVEL=%s"%log_level],

        ),
    ],
)
