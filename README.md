# Hash tables

## Introduction

The purpose of this program is to benchmark and compare various hashing methods and collision strategies. It utilizes the following files:

- README.md: This file
- hash_functions.py: A module containing three hash functions.
- hash_tables.py: The main script, contains collision resolution strategies and argument parsing.
- scatter.py: A matplotlib based module for creating a scatterplot.

Tests are included in the following files

- fxn_tests.sh: Bash functional testing using sssh.
- test_hash_functions.py: Unittesting for hash_functions.py
- test_hash_tables.py: Unittesting for hash_tables.py

Data used for this program are included in the files:

- non_rand_words.txt: a list of non-random words
- rand_words.txt: a list of random words

Please note the directory:

- img: contains images referenced in benchmarking.

## Methods

## Installation

The following builtin python libraries are used:

- os
- sys
- argparse
- random
- time

pycodestyle is required to run the verification tests: `pip install pycodestyle pip install --upgrade pycodestyle pip uninstall pycodestyle`

Future functional testing may involve ssshtest, which can be installed with: `test -e ssshtest || wget -qhttps://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest . ssshtest`

Matplotlib is required and can be installed with: `conda activate swe4s conda install matplotlib`
