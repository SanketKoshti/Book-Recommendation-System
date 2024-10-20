from idlelib.autocomplete_w import LISTUPDATE_SEQUENCE

from setuptools import setup

with open("README.md","r",encoding="utf-8")as f:
    long_description=f.read()

    REPO_NAME="Book-Recommendation-System"
    AUTHOR_USER_NAME="SanketKoshti"
    SRC_READ="src"
    LIST_OF_REQUIREMENTS=['streamlit','numpy']


    setup(
        name=SRC_READ,
        version="0.0.1",
        author=AUTHOR_USER_NAME,
        description="A small package for Book recommendation System",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=f"https://github.com/SanketKoshti/Book-Recommendation-System",
        author_email="sanketkoshti1802@gmail.com",
        packages=[SRC_REPO],
        license="MIT",
        python_requires=">=3.0",
        install_requires=LIST_OF_REQUIREMENTS
    )