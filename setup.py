import os
from setuptools import setup

# macmon
# Listen for new wireless devices


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="macmon",
    version="0.0.1",
    description="Listen for new wireless devices",
    author="Johan Nestaas",
    author_email="johannestaas@gmail.com",
    license="GPLv3+",
    keywords="",
    url="https://www.github.com/johannestaas/macmon",
    packages=['macmon'],
    package_dir={'macmon': 'macmon'},
    long_description=read('README.rst'),
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'License :: OSI Approved :: GNU General Public License v3 or later '
        '(GPLv3+)',
        'Environment :: Console',
        'Environment :: X11 Applications :: Qt',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
    ],
    install_requires=[
        'scapy',
    ],
    entry_points={
        'console_scripts': [
            'macmon=macmon.scanner:main',
        ],
    },
    # If you get errors running setup.py install:
    # zip_safe=False,
    #
    # For including non-python files:
    # package_data={
    #     'macmon': ['templates/*.html'],
    # },
    # include_package_data=True,
)
