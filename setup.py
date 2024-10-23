from setuptools import setup, find_packages

# Read the long description from the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Constants for package metadata
REPO_NAME = "Book-Recommendation-System"
AUTHOR_USER_NAME = "SanketKoshti"
SRC_READ = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy', 'pandas', 'scikit-learn']  # Add any other required packages

# Setup configuration
setup(
    name=REPO_NAME.lower().replace(" ", "-"),  # Name of the package
    version='0.1',  # Version of the package
    author=AUTHOR_USER_NAME,  # Author's name
    description="A book recommendation system built using Streamlit",  # Short description
    long_description=long_description,  # Long description from README
    long_description_content_type="text/markdown",  # Specify the content type of long description
    packages=find_packages(where=SRC_READ),  # Look for packages inside the 'src' directory
    package_dir={"": SRC_READ},  # Directory for packages
    install_requires=LIST_OF_REQUIREMENTS,  # List of dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Python version requirement
)
