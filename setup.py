from setuptools import setup, find_packages

# directory structure:
# yourpackage/
#     __init__.py
#     main.py
#     utils.py
#     scripts/
#     __init__.py
#         yourscript.py

setup(
    name='tracepkg',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
        # script = package[.subdir].module:function
        'trace = tracepkg.main:cli',
        ],
    },
)
