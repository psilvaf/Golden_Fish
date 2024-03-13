from setuptools import setup

setup(name='golden_fish',
	version='0.1.0',
   	author='Paula Ferreira',
   	author_email='psilf12@gmail.com',
   	packages=['golden_fish',],
   	#scripts=['bin/script1','bin/script2'],
   	#url='http://pypi.python.org/pypi/PackageName/',
   	license='LICENSE.txt',
   	description='Fisher Forecast plots.',
  	#long_description=open('README.txt').read(),
  	install_requires=[
	"astropy",
	"numpy",
	'scipy',
	'pandas',
	'matplotlib'],)
