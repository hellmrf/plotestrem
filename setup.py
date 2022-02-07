import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plotestrem",
    version="0.0.2",
    author="Heliton Martins Reis Filho",
    author_email="helitonmrf@gmail.com",
    license="GPL-v3.0",
    description="A simple Python script to plot and fit data (similar to Origin or SciDavis), but free, open source and LaTeX-friendly.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hellmrf/plotestrem",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
