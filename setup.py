
from setuptools import setup

setup(
    name="mypackage",
    version="0.1",
    packages=["helloworld"],
    author="Alexander Procton",
    license="GPLv3",
    entry_points={
        'console_scripts': ['helloworld = helloworld.__main__:main']
        },
    classifiers=["Programming Language :: Python :: 3"],
)

