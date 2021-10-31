import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cravision",
    version="0.0.1",
    author="shizuku",
    author_email="2112165916@qq.com",
    description="Computer vision using CraNet.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shizuku/cravision",
    project_urls={
        "Bug Tracker": "https://github.com/shizuku/cravision/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
