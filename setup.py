from setuptools import setup, find_packages

data_files = [
    ('share/doc/footix', ['README.md'])
]

setup(
    name='footix',
    version='0.9',
    description="soccer schedule",
    long_description=open('README.md').read(),
    author='Walid Saad',
    author_email='walid.sa3d@gmail.com',
    url='https://github.com/walidsa3d/footix',
    # download_url='',
    license="GPL",
    keywords="football soccer",
    packages=find_packages(),
    include_package_data=True,
    data_files=data_files,
    entry_points={"console_scripts": ["footix=footix.footix:main"]},
    classifiers=[
        'Development Status :: 4  - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Video',
        'Topic :: Utilities'
    ]
)
