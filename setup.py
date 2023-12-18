from setuptools import setup, find_namespace_packages


setup(
    name="baby-yoda-bot",
    version="0.0.1",
    description="A personal Baby Yoda's bot that helps you manage your contacts and notes.",
    url="https://github.com/orm81zp/project-BabyYodaBot",
    author="Roman Onishchenko <orm81zp@gmail.com>, Antonina Sych <antoninasych@gmail.com>, Bogdan Onoyko <bogdan.onoyko@gmail.com>, Vitalii Pavelko <pavelko.vetal@gmail.com>",
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
    entry_points={"console_scripts": ["yoda_say = baby_yoda_bot.main:yoda_say"]},
    install_requires=[],
)
