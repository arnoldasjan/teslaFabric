from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'TC 2.1.3 Tesla Factory'
LONG_DESCRIPTION = 'TC 2.1.3 Tesla Factory Package'

setup(
    name="tesla",
    version=VERSION,
    author="Arnoldas Januska",
    author_email="<januska.arnoldas@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'tesla package'],
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ]
)
