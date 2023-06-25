from setuptools import setup, find_packages

long_description = open('README.md', "rt").read()

setup(
    name='bayfile_uploader',
    version='1.1.3',    
    description='File Uploader, uploads files to bayfiles.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/roymanigley/bayfile-uploader',
    author='Roy Manigley',
    author_email='roy.manigley@gmail.com',
    license='MIT',
    packages=['bayfile_uploader'],
    install_requires=[
        'requests>=2.28.1',
        'click>=8.1.3',
    ],
    entry_points = {
        'console_scripts': [
            'bayfile_upload = bayfile_uploader.uploader:main',
        ],
    },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.10',
    ],
)
