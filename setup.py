from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='fullhunt_api',
    version='0.6',
    author='egor251',
    author_email='',
    description='Library for working with Fullhunt.io API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/egor251/fullhunt_api',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
      'Programming Language :: Python :: 3.11',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent'
    ],
    keywords='files speedfiles ',
    project_urls={
      'GitHub': 'https://github.com/egor251/fullhunt_api',
    },
    python_requires='>=3.8'
)
