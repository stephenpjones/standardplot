"""
Setup script for StandardPlot package
"""
from setuptools import setup, find_packages

setup(
    name="standardplot",
    version="1.0.0",
    author="User",
    description="Consistent plotting configuration for data analysis",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "pandas>=1.3.0",
        "numpy>=1.21.0"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: Python :: 3",
    ],
)
