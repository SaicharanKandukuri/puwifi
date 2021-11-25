import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puwifi",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Saicharan Kandukuri",                     # Full name of the author
    description="login to parul university with python",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL V3",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["loginpu"],             # Name of the python package
    package_dir={'':'modules'},     # Directory of the source code of the package
    install_requires=["rich", "requests"]                     # Install other dependencies if any
)