from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup

config = generate_distutils_setup(packages=["aws_publisher"], package_dir={"": "src"})
setup(**config)
