from setuptools import setup, find_packages
import pktools as pk


setup(
    name = pk.__name__,
    packages = pk.__all__,   
    include_package_data=True,
    version = pk.__version__,
    description = 'Utilities for development',
    author='katmai',
    author_email="katmai.mobil@gmail.com",
    license="GPLv3",
    url="https://github.com/katmai1/pktools",
    classifiers = ["Programming Language :: Python :: 3",\
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        ],
    )