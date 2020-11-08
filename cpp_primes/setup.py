from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import setuptools
import sys
import pybind11 as pb11

the_module = Extension(
    "cpp_primes",
    define_macros=[("_USE_MATH_DEFINES", None)],
    include_dirs=[".", pb11.get_include(),],
    sources=["pybind_wrapper.cpp", "primes.cpp"],
    language="c++",
)

extra_compile_args = ["-std=c++11", "-Wall", "-Wextra"]

setup(
    name="cpp_primes",
    version="0.0.1",
    packages="",
    description="primes test example cpp module",
    extra_compile_args=extra_compile_args,
    ext_modules=[the_module],
    setup_requires=["pybind11"],
)
