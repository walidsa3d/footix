import os

from setuptools import find_packages
from setuptools import setup

#req_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
#requires = [i.strip() for i in open(req_file).readlines()]

setup(
    name='footix',
    version='1.2.0',
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
    install_requires=['lxml', 'beautifulsoup4', 'requests', 'requests-cache'],
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
