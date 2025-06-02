#from setuptools import setup
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="mymath",
    ext_modules=cythonize("mymath.pyx"),
)