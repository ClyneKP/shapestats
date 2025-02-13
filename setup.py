from setuptools import setup
import os.path

from distutils.command.build_py import build_py


initpath = os.path.join(os.path.dirname(__file__), 'shapestats_kc/__init__.py')
with open('shapestats_kc/__init__.py') as f:
    version = f.readline().split('=')[1].strip()
print(version)


setup(name='shapestats_kc', # name of package
      version=eval(version),
      description='tools & methods to measure shape regularity', #short <80chr description
      url='https://github.com/ljwolf/shapestats', #github repo
      maintainer='Levi John Wolf',
      maintainer_email='levi.john.wolf@gmail.com',
      tests_require=['pytest'],
      keywords='spatial statistics',
      classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        ],
      license='MIT',
      packages=['shapestats_kc'], # add your package name here as a string
      install_requires=['scipy','shapely','libpysal'],
      zip_safe=False,
      cmdclass = {'build.py':build_py})
