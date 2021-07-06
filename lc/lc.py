#!/usr/bin/env python3
"""LeetCode CLI interface and helper functions.

Usage: lc [-h] [-v] command ...

positional arguments:
  command
    init         Initilize at a directory and set up remote GitHub repo.
    new          Create a new LeetCode solution from template.
    upload (u)   Commit a LeetCode solution and push to GitHub.
    template (t)
                 Set up a template file for writing solutions.
    category (c)
                 Add/Remove categories which LeetCode problems belong to.

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
"""

import argparse
from datetime import datetime
import os
import subprocess
import json

__version__ = "0.2.2"
__author__ = "Weiran Fu"
__license__ = "MIT"

this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.abspath(os.path.join(this_dir, "data.json"))
DEFAULT_TEMPLATE_PATH = os.path.abspath(os.path.join(this_dir, "template.md"))
data = {}
TEMPLATE_PATH = ""
BASE_DIR = ""
categories = []
# load data from data.json
with open(DATA_PATH, 'r') as f:
    data = json.load(f)
    TEMPLATE_PATH = data['template']
    BASE_DIR = data['base_dir']
    categories = data['categories']
if not TEMPLATE_PATH:
    TEMPLATE_PATH = DEFAULT_TEMPLATE_PATH


def init(args):
    """Initialize at current directory."""
    data['base_dir'] = os.path.abspath(args.directory)
    data['template'] = ""
    with open(DATA_PATH, 'w') as f:
        json.dump(data, f)
    subprocess.call(["git", "init"], cwd=args.directory)
    subprocess.call(["git", "remote", "rm", "origin"],
                    cwd=args.directory,
                    stderr=subprocess.DEVNULL)  # omit error in subprocess
    subprocess.call(["git", "remote", "add", "origin", args.remote_repo],
                    cwd=args.directory)


def create_file(args):
    """Create a new LeetCode solution from template."""
    filename = args.filename + ".md"
    target_path = "{}/Problems/{}/{}".format(
        BASE_DIR, args.category,
        filename) if args.category != "Summary" else "{}/Summary/{}".format(
            BASE_DIR, filename)
    # open the template and read lines
    lines = open(TEMPLATE_PATH, 'r').readlines()
    # update title && category && datetime in solution file
    title = " ".join([s.capitalize() for s in filename[:-3].split("-")])
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    # create a new file and write lines
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    if TEMPLATE_PATH != DEFAULT_TEMPLATE_PATH:
        with open(target_path, 'w') as fp:
            for line in lines:
                fp.write(line)
    else:
        with open(target_path, 'w') as fp:
            fp.write(lines[0])
            for line in lines[1:]:
                if "title:" in line:
                    fp.write("title: Easy Medium Hard | {}\n".format(title))
                elif "Graph" in line:
                    fp.write("  - {}\n".format(args.category))
                elif "date:" in line:
                    fp.write("date: {}\n".format(dt_string))
                elif "TITLE" in line:
                    fp.write("# {}\n".format(title))
                else:
                    fp.write(line)
    subprocess.call(["open", target_path])

def open_file(args):
    """Open a LeetCode solution contains this filename."""
    searchname = args.filename
    names = []
    paths = []
    for root, dirs, files in os.walk(BASE_DIR):
        for name in files:
            if searchname.lower() in name.lower():
                names.append(name)
                paths.append(os.path.join(root, name))
    if len(names) == 0:
        print("Cannot search any solution contains {}.".format(searchname))
        return
    for i in range(len(names)):
        print("{}. {}".format(i, names[i]))
    num = int(input("Please choose one to open:\n"))
    subprocess.call(["open", paths[num]])

def upload_files(args):
    """Commit a LeetCode solution and push to GitHub."""
    subprocess.call(["git", "add", "."], cwd=BASE_DIR)
    subprocess.call(["git", "commit", "-m", args.m], cwd=BASE_DIR)
    subprocess.call(["git", "push", "origin", "main"], cwd=BASE_DIR)


def template(args):
    template_path = ""
    if args.set:
        if os.path.isabs(args.set):
            template_path = args.set
        else:
            template_path = os.path.abspath(args.set)
    else:
        template_path = DEFAULT_TEMPLATE_PATH
    data['template'] = template_path
    with open(DATA_PATH, 'w') as f:
        json.dump(data, f)


def category_add(args):
    if args.category in categories:
        return
    categories.append(args.category)
    data['categories'] = sorted(categories)
    with open(DATA_PATH, 'w') as f:
        json.dump(data, f)


def category_rm(args):
    if args.category not in categories:
        return
    categories.remove(args.category)
    data['categories'] = categories
    with open(DATA_PATH, 'w') as f:
        json.dump(data, f)


# Construct the CLI
parser = argparse.ArgumentParser(
    description="LeetCode CLI interface and helper functions.",
    prog="lc",
    epilog=
    "Further documentation is available at <https://github.com/weiranfu/leetcode-with-me>."
)
parser.add_argument("-v",
                    "--version",
                    action="version",
                    version='%(prog)s version ' + __version__)


def parser_help(args):
    parser.print_help()


parser.set_defaults(func=parser_help)
subparsers = parser.add_subparsers(metavar="command")

parser_init = subparsers.add_parser(
    'init', help="Initilize at a directory and set up remote GitHub repo.")
parser_init.add_argument("directory",
                         metavar="<directory>",
                         help="The path to the directory to initialize at.")
parser_init.add_argument(
    "remote_repo",
    metavar="<remote_repo>",
    help="The link of remote GitHub repo to connect with.")
parser_init.set_defaults(func=init)

parser_new = subparsers.add_parser(
    "new", help="Create a new LeetCode solution from template.")
parser_new.add_argument("filename",
                        metavar="<filename>",
                        help="The filename of LeetCode solution.")
parser_new.add_argument(
    "category",
    metavar="<category>",
    choices=categories,
    help="The category which LeetCode solution belongs to.")
parser_new.set_defaults(func=create_file)

parser_open = subparsers.add_parser("open", help="Open an existing solution.")
parser_open.add_argument("filename", metavar="<filename>", help="The filename of the solution.")
parser_open.set_defaults(func=open_file)

parser_upload = subparsers.add_parser(
    "upload",
    aliases=["u"],
    help="Commit a LeetCode solution and push to GitHub.")
parser_upload.add_argument("-m",
                           metavar="<message>",
                           default=":pencil: LeetCode with Me!",
                           help="The Git commit message")
parser_upload.set_defaults(func=upload_files)

parser_template = subparsers.add_parser(
    "template",
    aliases=['t'],
    help="Set up a template file for writing solutions.")
group = parser_template.add_mutually_exclusive_group(
    required=True)  # One of -set and --use-default must be chosen
group.add_argument("-set",
                   metavar="<template path>",
                   help="The path to the template file.")
group.add_argument("--use-default",
                   action="store_true",
                   help="Use default template file.")
group.set_defaults(func=template)

parser_category = subparsers.add_parser(
    'category',
    aliases=['c'],
    help="Add/Remove categories which LeetCode problems belong to.")


def parser_category_help(args):
    parser_category.print_help()


parser_category.set_defaults(func=parser_category_help)
category_subparsers = parser_category.add_subparsers(metavar="command")

category_parser_add = category_subparsers.add_parser(
    'add', help="Add a new category.")
category_parser_add.add_argument("category",
                                 metavar="<category name>",
                                 help="The name of the category.")
category_parser_add.set_defaults(func=category_add)

category_parser_rm = category_subparsers.add_parser('rm',
                                                    help="Remove a category.")
category_parser_rm.add_argument("category",
                                metavar="<category name>",
                                help="The name of the category.")
category_parser_rm.set_defaults(func=category_rm)


def main():
    args = parser.parse_args()
    if "remote_repo" not in args and not BASE_DIR:
        parser.error(
            "Please first initialize at a directory using `lc init <directory> <remote repo>`."
        )
    if "set" in args and args.set:
        if args.set[-3:] != ".md":
            parser.error(
                "Please use markdown file as template, e.g. ~/path/to/template.md"
            )
    args.func(args)


if __name__ == "__main__":
    main()