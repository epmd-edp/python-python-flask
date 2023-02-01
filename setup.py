from version import __version__
from setuptools import setup
from setuptools import find_packages, setup

setup(
    name='hello_world',
    version=__version__,
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
