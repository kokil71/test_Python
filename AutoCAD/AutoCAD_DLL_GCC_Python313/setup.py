#from setuptools import setup
from distutils.core import setup
from Cython.Build import cythonize

#setup(
#    name="acad_control",
#    ext_modules=cythonize("acad_control.pyx"),
#)

setup(
    ext_modules=cythonize(
        "acad_control.pyx",
        compiler_directives={'language_level': "3"},
    ),
)