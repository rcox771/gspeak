import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="gspeak",
    version="1.0.0",
    description="Simple wrapper for gTTS and pygame to play audio directly from buffer",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rcox771/gspeak",
    author="rcox771",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["gspeak"],
    include_package_data=True,
    install_requires=["gTTS", "pygame"],
    entry_points={
    },
)
