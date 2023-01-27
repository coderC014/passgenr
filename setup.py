from setuptools import setup, find_packages
import os
import codecs

VERSION = '0.0.1'
DESCRIPTION = '''a random password generator build with basic python coding
in the function we have to provide values as:
randompass(n_letter, n_digit, n_symbol)'''

# setting up module
setup(
    name='passgenr',
    version=VERSION,
    author="Coder014 (Chandan Kumar)",
    author_email="binary.commands@gmail.com"
    description=DESCRIPTION,
    packages=find_packages(),
    requires=["random"],
    keywords=['python', 'random', 'password generator', 'password'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)
