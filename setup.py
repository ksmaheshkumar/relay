#!/usr/bin/env python

from setuptools import setup

setup(
    name='relay',
    version='0.0.7',
    description='Meta-magical SSH tunnels for remote developers behind firewalls.',
    long_description=open('README.rst').read(),
    author='Christopher Groskopf',
    author_email='staringmonkey@gmail.com',
    url='http://blog.apps.npr.org/',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ],
    py_modules = [
        'relay'
    ],
    scripts = [
        'relay'
    ],
    data_files = [
        ('/usr/local/lib/relay/', ['relay.py'])
    ],
    install_requires = [
        'paramiko>=1.1.0'
    ]
)
