from setuptools import find_packages, setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fortnite-python',
    version='0.3.1',
    description='Python wrapper for http://fortnitetracker.com/ api.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/xcodinas/fortnite-python',
    author='Xavier Codinas',
    author_email='xavier19966@gmail.com',
    license='MIT',
    packages=find_packages(exclude=('tests*',)),
    install_requires=[
        'requests>=2.18.4',
        'furl>=1.0.1',
    ],
    extras_require={
        ":python_version<='3.4'": ['enum34>=1.1.6'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
