from setuptools import setup

try:
    long_description = open("README.md").read()
except:
    long_description = ""

setup(
    name='pycodeexec',
    version='0.0.1',
    description='Execute arbitrary code from a multitude of supported languages',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/3jackdaws/pycodeexec',
    author='Ian Murphy',
    author_email='3jackdaws@gmail.com',
    license='MIT',
    packages=['sclib'],
    python_requires='>=3.6',
    install_requires=['docker'],
    test_suite='pytest',
    tests_require=['pytest', 'pytest-asyncio'],
)