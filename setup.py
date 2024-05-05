from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A python package that helps to convert HTML to XML like formal supported by the ReportLab Paragraph module.'
LONG_DESCRIPTION = open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read()

# Setting up
setup(
    name="html2rl",
    version=VERSION,
    author="ValiantDoge (Agnelo Fernandes)",
    author_email="<agnelofernandes475@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/ValiantDoge/html2rl.git",
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'reportlab'],
    license='MIT',
    keywords=['python','python3', 'pdf', 'HTML', 'HTML to PDF', 'ReportLab', 'convert HTML', 'to ReportLab', 'ReportLab XML', 'HTML to ReportLab XML', 'HTML to ReportLab XML'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    extras_require = {
        "dev": ["pytest>=7.0", "twine"]
    },
)