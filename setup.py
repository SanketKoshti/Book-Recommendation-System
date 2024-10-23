from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Book-Recommendation-System"
AUTHOR_USER_NAME = "SanketKoshti"
SRC_READ = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']

setup(
    name=SRC_READ,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommendation System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="sanketkoshti1802@gmail.com",
    packages=[SRC_READ],
    license="MIT",
    python_requires=">=3.0",
    install_requires=LIST_OF_REQUIREMENTS
)
