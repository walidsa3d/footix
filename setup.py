from os import path

from setuptools import find_packages
from setuptools import setup


setup(
    name='footix',
    version='2.0.1',
    description="soccer schedule",
    long_description="xxx",
    author='Walid Saad',
    author_email='walid.sa3d@gmail.com',
    url='https://github.com/walidsa3d/footix',
    license="MIT",
    keywords="football soccer",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['lxml', 'beautifulsoup4', 'requests==2.6.2', 'requests-cache'],
    entry_points={"console_scripts": ["footix=footix.cli:main"]},
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
