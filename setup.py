from setuptools import setup
from lc import lc

with open("README.md", 'r') as fp:
    long_description = fp.read()



setup(
    name="leetcode-with-me",
    version=lc.__version__,
    license=lc.__license__,
    author=lc.__author__,
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
