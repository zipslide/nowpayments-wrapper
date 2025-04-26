from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name                          = 'nowpayments-api',
    version                       = '0.1.0',
    author                        = 'dracc',
    author_email                  = 'netdev0@proton.me',
    description                   = 'Python wrapper for the NOWPayments cryptocurrency payment gateway API',
    long_description              =  long_description,
    long_description_content_type = 'text/markdown',
    url                           = 'https://github.com/zipslide/nowpayments_wrapper',
    project_urls={
        'Bug Tracker': 'https://github.com/zipslide/nowpayments_wrapper/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GNU v3',  # No specific CC classifier in PyPI
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.0',
    ],
    license='GNU v3',
    license_files=['LICENSE'],
) 