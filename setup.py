from setuptools import setup
import json

with open("README.md", 'r') as fp:
    long_description = fp.read()

data = json.loads("./lc/data.json")

setup(
    name="leetcode-with-me",
    version=data['version'],
    license=data['license'],
    author=data['author'],
    description="LeetCode CLI interface and helper functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weiranfu/leetcode-with-me",
    packages=['lc'],
    package_dir={'lc': 'lc'},
    package_data={'lc': ['template.md', 'data.json']},
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3 :: Only',
    ],
    entry_points={
        "console_scripts": [
            "lc = lc.lc:main"
        ]
    },
    install_requires=[
        "markdown >= 3.0",
    ],
    python_requires='>= 3.6',
)
