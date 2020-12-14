#!/usr/bin/env python3
"""LeetCode CLI interface and helper functions.

Usage:
  lc new <filename> <category>
  lc (u | upload)

Arguments:
  filename          the name of this LeetCode solution
  category          the category this LeetCode solution belongs to
"""

import argparse
from datetime import datetime
import sys, os
import subprocess
import json

__version__ = "0.1.1"
__author__ = "Weiran Fu"
__license__ = "MIT"

this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "data.json")
TEMPLATE_PATH = os.path.join(this_dir, "template.md")


def init(args):
    """Initialize at current directory."""
    data = {}
    data['base_dir'] = os.getcwd()
    with open(DATA_PATH, 'w') as f:
        json.dump(data, f)
    subprocess.call(["git", "init"])
    subprocess.call(["git", "remote", "rm", "origin"])
    subprocess.call(["git", "remote", "add", "origin", args.remote_repo])


def create_file(args):
    """Create a new LeetCode solution from template."""
    BASE_DIR = ""
    with open(DATA_PATH, 'r') as f:
        data = json.load(f)
        BASE_DIR = data['base_dir']
    if not BASE_DIR:
        print("Please first initialize at a directory.\n")
        subprocess.call(["lc", "--help"])
        return
    filename = args.filename + ".md"
    target_dir = "{}/Problems/{}".format(BASE_DIR, args.category)
    target_dir_summary = "{}/Summary".format(BASE_DIR)
    target_path = "{}/{}".format(
        target_dir,
        filename) if args.category != "Summary" else "{}/{}".format(
            target_dir_summary, filename)
    # open the template and read lines
    lines = open(TEMPLATE_PATH, 'r').readlines()
    # update title && category && datetime in solution file
    title = " ".join([s.capitalize() for s in filename[:-3].split("-")])
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    # create a new file and write lines
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
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


def upload_files(args):
    """Commit a LeetCode solution and push to GitHub."""
    BASE_DIR = ""
    with open(DATA_PATH, 'r') as f:
        data = json.load(f)
        BASE_DIR = data['base_dir']
    if not BASE_DIR:
        print("Please first initialize at a directory.\n")
        subprocess.call(["lc", "--help"])
        return
    subprocess.call(["git", "add", "."], cwd=BASE_DIR)
    subprocess.call(["git", "commit", "-m", args.m], cwd=BASE_DIR)
    subprocess.call(["git", "push", "origin", "main"], cwd=BASE_DIR)


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
                    version='%(prog)s ' + __version__)
subparsers = parser.add_subparsers(metavar="command")

parser_init = subparsers.add_parser('init',
                                    help="Initilize at current directory.")
parser_init.add_argument("remote_repo",
                         help="The GitHub remote repo to connect with.")
parser_init.set_defaults(func=init)

parser_new = subparsers.add_parser(
    "new", help="Create a new LeetCode solution from template.")
parser_new.add_argument("filename", help="The filename of LeetCode solution.")
parser_new.add_argument("category",
                        choices=[
                            "Array", "Backtracking", "Binary Search", "Bit",
                            "BST", "Design", "DP", "Geometry", "Graph",
                            "Greedy", "KMP", "Linked List", "Math", "Prefix",
                            "Search", "Segment Tree", "Set", "Sort", "SQL",
                            "Stack", "String", "Tree", "TreeMap", "Trie",
                            "Two Pointers", "Union Find", "Summary"
                        ],
                        help="The category LeetCode solution belongs to.")
parser_new.set_defaults(func=create_file)

parser_upload = subparsers.add_parser(
    "upload",
    aliases=["u"],
    help="Commit a LeetCode solution and push to GitHub.")
parser_upload.add_argument("-m",
                           metavar="message",
                           default=":pencil: LeetCode with Me!",
                           help="Git commit message")
parser_upload.set_defaults(func=upload_files)


def main():
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()