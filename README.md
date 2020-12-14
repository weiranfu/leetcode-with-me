# leetcode-with-me

[![lc on PyPI](https://img.shields.io/pypi/v/leetcode-with-me.svg?color=blue&style=for-the-badge)](https://pypi.org/project/leetcode-with-me/)

> A small tool for writing solutions to LeetCode problems.

## Features

* Initialize current directory with Git and connect to a GitHub repo.
* Create a markdown file from [template.md](lc/template.md) to write LeetCode solutions.
* Upload solutions to GitHub repo.
* Support executing commands in any directory once you have initialized.

## Installation

`$ pip install leetcode-with-me`

## Usage

* Initialize a directory and connect to GitHub repo.

  `$ lc init <repo link>`

* Create a solution markdown for you.

  `$ lc new <solution name> <solution category>`

* Upload solutions to the GitHub repo.

  `$ lc upload`

See `lc --help` for more command-line switches and usage instructions.

## License
MIT