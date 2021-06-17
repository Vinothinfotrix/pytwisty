from setuptools import setup
with open("README.md","r") as fh:
    long_description=fh.read()
setup(
    name='pytwisty',
    version='0.0.1',
    description="Solve 1x2x2, 1x2x3, and 2x2x2 Rubik's cube puzzles",
    py_modules=["pytwisty"],
    package_dir={'':'src'},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Prakhar Gupta",
    author_email="pkrdps@gmail.com",
)
