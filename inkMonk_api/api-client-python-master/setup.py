from setuptools import setup

setup(
    name='inkmonk',
    version='1.0.0',
    long_description=__doc__,
    packages=['inkmonk'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests>=2.2.1']
)
