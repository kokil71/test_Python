import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import pythoncom
from pyautocad import Autocad, APoint
import win32com.client

#from setuptools import setup
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="draw_and_zoom",
    ext_modules=cythonize("draw_and_zoom.pyx"),
)