#!/usr/bin/env python

sdict = {
    'name' : 'rdbtools',
    'version' : __version__,
    'description' : 'Utilities to convert Redis RDB files to JSON or SQL formats',
    'long_description' : long_description,
    'url': 'https://github.com/sripathikrishnan/redis-rdb-tools',
    'download_url': 'https://github.com/sripathikrishnan/redis-rdb-tools/archive/rdbtools-%s.tar.gz' % __version__,
    'author': 'Sripathi Krishnan, Redis Labs',
    'author_email' : 'Sripathi.Krishnan@gmail.com',
    'maintainer': 'Sripathi Krishnan, Redis Labs',
    'maintainer_email': 'oss@redislabs.com',
    'keywords' : ['Redis', 'RDB', 'Export', 'Dump', 'Memory Profiler'],
    'license' : 'MIT',
    'packages' : ['rdbtools', 'rdbtools.cli'],
    'package_data' : {
        'rdbtools': ['templates/*'],
    },
    'test_suite' : 'tests.all_tests',
    'install_requires': ['redis'],
    'entry_points' : {
        'console_scripts' : [
            'rdb = rdbtools.cli.rdb:main',
            'redis-memory-for-key = rdbtools.cli.redis_memory_for_key:main',
            'redis-profiler = rdbtools.cli.redis_profiler:main'],
    },
    'classifiers' : [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'],
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**sdict)
