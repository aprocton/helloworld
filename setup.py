
from setuptools import setup

setup(
    name="mypackage",
    version="0.1",
    packages=["helloworld"],
    entry_points={
        'console_scripts': ['helloworld = helloworld.__main__:main']
        }
)

