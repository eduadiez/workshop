from setuptools import setup

setup(
    name='to_checksum_address',
    version='1.0',
    description='',
    long_description='',
    author='Eduardo Antuña',
    author_email='edu@dappnode.io',
    license='MIT',
    zip_safe=False,
    install_requires=[
        'click==6.7',
        'eth-keyfile==0.5.1',
        'eth-utils==1.5.2',
        'requests==2.20.0',
    ],
    entry_points={
        'console_scripts': [
            'to_checksum_address = to_checksum_address:main'
        ]
    }
)
