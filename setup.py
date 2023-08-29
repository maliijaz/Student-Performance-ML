from setuptools import find_packages, setup

Hyphen_e_dot = 'e .'
def get_requirements(filename):
    with open(filename) as f:
        requirements = f.read().splitlines()
        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Ali',
    author_email = 'maliijaz2001@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)
