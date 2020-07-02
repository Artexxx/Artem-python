# coding=utf-8

import os
from setuptools import setup
from sys import version_info

if version_info.major != 3 or version_info.minor < 5:
    raise RuntimeError('nfriction requires python 3.5 or newer')

setup(
    name='nfriction',
    version='1.0.0',
    description=(
        'a browser-based gallery viewer tailored for viewing large collections of pornographic manga'
    ),
    long_description=(
        'please visit the homepage: https://github.com/Artexxx/Artem-python/tree/master/Application%7CWeb/FrictionOflineHentaiViewer'
    ),
    long_description_content_type='text/markdown',
    url='https://github.com/Artexxx/Artem-python/tree/master/Application%7CWeb/FrictionOflineHentaiViewer',
    author='Artexxx',
    author_email='HIDEN@gmail.com',
    packages=['nfriction'],
    scripts=[
        os.path.join('scripts', 'nfriction'),
        #os.path.join('scripts', 'nfriction-ui'),
    ],
    app=[
        os.path.join('scripts', 'nfriction'),
    ],
    license='MIT',
    platforms=['any'],
    install_requires=[
        'flask>=1.1,<1.2',
        'pillow',
        'python-magic',
        'rarfile',
    ],
    setup_requires=[
        'py2app',
    ],
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    include_package_data=True,
    options={
        'py2app': {
            'iconfile': 'scripts/icon.icns',
            'plist': {
                'NSHumanReadableCopyright': '©2020 Artexxx',
            },
        }
    },
)
