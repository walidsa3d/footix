from setuptools import find_packages
from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print "warning: pypandoc module not found, could not convert Markdown to RST"
    read_md = lambda f: open(f, 'r').read()
requires = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='footix',
    version='1.1.0',
    description="soccer schedule",
    long_description=read_md('README.md'),
    author='Walid Saad',
    author_email='walid.sa3d@gmail.com',
    url='https://github.com/walidsa3d/footix',
    license="MIT",
    keywords="football soccer",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    entry_points={"console_scripts": ["footix=footix.footix:main"]},
    classifiers=[
        'Development Status :: 4  - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Utilities'
    ]
)
