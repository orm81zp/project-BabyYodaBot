from setuptools import setup, find_namespace_packages


def get_long_description():
    """
    Returns string of the README.md file
    """
    with open("README.md", encoding="utf8") as fh:
        return fh.read()


setup(
    name="baby-yoda-bot",
    version="0.0.3",
    description="Your personal Baby Yoda Bot that helps you manage your contacts and notes.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/orm81zp/project-BabyYodaBot",
    author="Roman Onishchenko <orm81zp@gmail.com>, Antonina Sych <antoninasych@gmail.com>, Vitalii Pavelko<pavelko.vetal@gmail.com>, Bogdan Onoyko<bogdan.onoyko@gmail.com>",
    maintainer="Roman Onishchenko",
    maintainer_email="orm81zp@gmail.com",
    license="MIT",
    packages=find_namespace_packages(exclude=("tests.*", "tests")),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
    ],
    entry_points={"console_scripts": ["yoda_bot = baby_yoda_bot.main:yoda_say"]},
    install_requires=["rich", "prompt_toolkit"],
)
