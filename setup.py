from setuptools import setup, find_packages

def parse_requirements(filename:str) -> list:
    """Reads the requirements.txt file and returns a list of packages."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

setup(
    name='excel_utils',
    version='0.3.1',
    packages=find_packages(where='lib'),
    package_dir={'' : 'lib'},
    include_package_data=True,
    license='unlincense',
    description='A package that can extract or edit data from a column.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Nando2003/db2excel.git',
    python_requires='>=3.10',
    install_requires=parse_requirements('requirements.txt'),
    extra_require={
        "dev" : ["pytest>=7.0"]
    },
    tests_require=[
        'pytest>=7.0',
    ],
    author='Fernando Fontes',
    author_email='nandofontes30@gmail.com',
)