from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

ext_modules = [
    Extension(
        "calc",
        sources=["calc.pyx"],
    )
]

setup(
    name="calc",
    ext_modules=cythonize(ext_modules),
)