from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="rarCracker",
    version="0.0.1",
    author="hanerx",  # 作者名字
    author_email="",
    description="A simple compressed file cracker",
    license="MIT",
    url="https://github.com/hanerx/rarCracker",  # github地址或其他地址
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'fastzipfile==2.2',
        'rarfile==4.0'
    ],
    zip_safe=True,
)
