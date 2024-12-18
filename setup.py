from setuptools import setup
from pip._internal.req import parse_requirements

requirements = parse_requirements('requirements.txt', session=False)
install_requires = [str(req.requirement) for req in requirements]

setup(
    name='hifuku',
    version='0.0.1',
    author='onnonuro',
    packages=['hifuku'],
    install_requires=install_requires,
    license='MIT',
)