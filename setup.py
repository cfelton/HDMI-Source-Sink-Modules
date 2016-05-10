from pkgutil import walk_packages

from setuptools import setup

import hdmi


def _find_packages(path='.', prefix=''):

        yield prefix
        prefix += "."
        for _, name, ispkg in walk_packages(path,
                                            prefix,
                                            onerror=lambda x: x):
            if ispkg:
                yield name


def find_packages():

    return list(_find_packages(hdmi.__path__, hdmi.__name__))

setup(name='hdmi',
      version=hdmi.__version__,
      install_requires=['myhdl'],
      description='Implementation of HDMI Source/Sink Modules in MyHDL',
      url='https://github.com/srivatsan-ramesh/HDMI-Source-Sink-Modules',
      author='srivatsan-ramesh',
      author_email='sriramesh4@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,)
