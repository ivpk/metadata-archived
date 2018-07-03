from setuptools import setup, find_packages


setup(
    name='inventorizacija',
    version='0.1',
    packages=find_packages(),
    scripts=['manage.py', 'inven/wsgi.py'],
    license='AGPL',
    keywords='open-data',
    url='https://gitlab.com/ivpk/metadata',
    project_urls={
        'Bug Tracker': 'https://gitlab.com/ivpk/metadata/issues',
        'Source Code': 'https://gitlab.com/ivpk/metadata',
    }
)
