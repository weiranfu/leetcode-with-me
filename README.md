# leetcode-with-me

[![lc on PyPI](https://img.shields.io/pypi/v/leetcode-with-me.svg?color=blue&style=for-the-badge)](https://pypi.org/project/leetcode-with-me/)

> A small tool for writing solutions to LeetCode problems.

## Features

* Initialize a directory with Git and connect to a GitHub repo.
* Create a solution from default [template](lc/template.md) for writing LeetCode solutions.
* Set up you own writing template.
* Add/Remove categories which LeetCode problems belong to.
* Upload solutions to GitHub repo.
* Support executing commands in any directory.
* Support markdown format.

## Installation

`$ pip install leetcode-with-me`

## Usage

* Initialize a directory and connect to GitHub repo.

  `$ lc init <directory> <remote repo>`

* Create a solution markdown for you.

  `$ lc new <solution name> <solution category>`

* Set up you own writing template.

  `$ lc template -set <template path>`

* Add/Remove a category.

  `$ lc category add <category>`

  `$ lc category rm  <category>`

* Upload solutions to the GitHub repo.

  `$ lc upload`

See `lc --help` for more command-line switches and usage instructions.

## Development

I would love to hear what you think about `leetcode-with-me` on issues page

Make pull requests, report bugs, suggest ideas and discuss `leetcode-with-me`. 

## License
MIT