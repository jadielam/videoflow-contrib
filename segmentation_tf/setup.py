from setuptools import setup
from setuptools import find_packages
import os.path

name = 'videoflow_contrib_segmentation_tf'
install_requires = ['videoflow']

setup(name=name,
      version='0.1',
      description='Tensorflow Segmentation Component for Videoflow Library',
      author='Jadiel de Armas',
      author_email='jadielam@gmail.com',
      url='https://github.com/videoflow/videoflow-contrib',
      license='MIT',
      packages = ['videoflow_contrib.segmentation_tf'],
      zip_safe = False,
      install_requires=install_requires,
      extras_require={
          'visualize': ['pydot>=1.2.0'],
          'tests': ['pytest',
                    'pytest-pep8',
                    'pytest-xdist',
                    'pytest-cov'],
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ]
)