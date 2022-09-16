from setuptools import setup

setup(
    name='flip',
    version='1.0.0',
    description='A ChRIS plugin to flip images horizontally, vertically or both',
    author='bn222',
    author_email='bnemeth@redhat.com',
    url='https://github.com/rh-impact/pl-',
    py_modules=['flip'],
    install_requires=['chris_plugin'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'flip = flip:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require={
        'none': [],
        'dev': [
            'pytest~=7.1',
            'pytest-mock~=3.8'
        ]
    }
)
