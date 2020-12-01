from setuptools import setup
from Cython.Build import cythonize

setup(
    name='cython_primes',
    ext_modules=cythonize("cython_primes.pyx", language_level="3"),
    version='0.1.0',
    author='Stephan Wiesenhütter',
    author_email='wiesenyhuetter@gmail.com',
)


