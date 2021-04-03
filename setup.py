import re
from pathlib import Path

import setuptools

# -- Constants --
BASE_DIR = Path(__file__).resolve().parent
README = Path(BASE_DIR / "README.md").read_text()
URL = "https://github.com/Rohith04MVK/Mini-Keras"

# -- Version config --
VERSION = re.search(
    r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    Path(BASE_DIR / "mini_keras/__init__.py").read_text(),
    re.MULTILINE
).group(1)

if not VERSION:
    raise RuntimeError("VERSION is not set!")

# -- Setup --
setuptools.setup(
    name="Mini-Keras",
    version=VERSION,

    author="Mini-Keras Team",
    author_email="warriordefenderz@gmail.com",

    description="An advanced and lightweight ML and Deep learning library for python.",
    long_description=README,
    long_description_content_type="text/markdown",
    license="GPL v3",

    url=URL,

    project_urls={
        "Documentation": URL,
        "Issue tracker": f"{URL}/issues",
    },

    packages=setuptools.find_packages(
        exclude=["tests", "tests.*", "tools", "tools.*"]
    ),

    install_requires=[
        "numpy==1.20.2",
        "matplotlib==3.4.1",
        "scipy==1.6.2",
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Programming Language :: Python :: Implementation :: CPython",

        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",

        "Operating System :: OS Independent",

        "Intended Audience :: Developers",

        "Topic :: Scientific/Engineering :: Artificial Intelligence",

        "Natural Language :: English",
    ],

    python_requires='>=3.6',
)