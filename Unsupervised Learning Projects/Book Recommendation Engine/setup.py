"""Package metadata for the Book Recommendation Engine demo."""

from setuptools import find_packages, setup


setup(
    name="tajamul-book-recommendation-engine",
    version="1.0.0",
    author="Tajamul Khan",
    description="An item-based Book-Crossing recommendation demo",
    url="https://github.com/tajamulkhann/Machine-Learning-Projects",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.26,<3",
        "pandas>=2.1,<3",
        "scikit-learn>=1.4,<2",
        "streamlit>=1.36,<2",
    ],
)
