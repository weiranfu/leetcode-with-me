#!/usr/bin/env python3
"""LeetCode CLI interface and helper functions.

Usage:
  lc new <filename> <category>
  lc (u | upload) <filename>

Arguments:
  filename          the name of this LeetCode solution
  category          the category this LeetCode solution belongs to

Categories:
  Array, Backtracking, 
"""

import argparse
from datetime import datetime, timedelta
import sys
import subprocess
import re

BASE_DIR = "/Users/aranne/Documents/LeetCode"
TEMPLATE_FILE = "leetcode.md"


def create_file(args):
    """Create a new LeetCode solution from template."""
    filename = args.filename + ".md"
    target_dir = "{}/LeetCode/{}".format(BASE_DIR, args.category)
    target_dir_summary = "{}/Summary".format(BASE_DIR)
    template_path = "{}/{}".format(BASE_DIR, TEMPLATE_FILE)
    target_path = "{}/{}".format(target_dir, filename) if args.category != "Summary" else "{}/{}".format(target_dir_summary, filename)
    # open the template and read lines
    lines = open(template_path, 'r').readlines()
    # update title && category && datetime in solution file
    title = " ".join([s.capitalize() for s in filename[:-3].split("-")])
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    # create a new file and write lines 
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

def upload_files(args):
    """Commit a LeetCode solution and push to GitHub."""
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", args.m])
    subprocess.call(["git", "push", "origin", "main"])

def main():
    parser = argparse.ArgumentParser(
        description="LeetCode CLI interface and helper functions.",
        prog="lc",
        epilog=
        "Further documentation is available at <https://github.com/weiranfu/leetcode-with-me>."
    )
    parser.add_argument("-v",
                        "--version",
                        action="version",
                        version="LeetCode v0.0.1")
    subparsers = parser.add_subparsers(metavar="command",
                                       help="Available commands: ")

    parser_new = subparsers.add_parser(
        "new", help="Create a new LeetCode solution from template.")
    parser_new.add_argument("filename",
                            help="The filename of LeetCode solution.")
    parser_new.add_argument(
        "category",
        choices=[
            "Array", "Backtracking", "Binary Search", "Bit", "BST", "Design",
            "DP", "Geometry", "Graph", "Greedy", "KMP", "Linked List", "Math",
            "Prefix", "Search", "Segment Tree", "Set", "Sort", "SQL", "Stack",
            "String", "Tree", "TreeMap", "Trie", "Two Pointers", "Union Find",
            "Summary"
        ],
        help="The category LeetCode solution belongs to.")
    parser_new.set_defaults(func=create_file)

    parser_upload = subparsers.add_parser(
        "upload",
        aliases=["u"],
        help="Commit a LeetCode solution and push to GitHub.")
    parser_upload.add_argument("-m", metavar="message", default=":pencil: LeetCode with Me!", help="Git commit message")
    parser_upload.set_defaults(func=upload_files)

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()