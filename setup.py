from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='anipy',
      version='0.1a1',
      description='A python library for the Anilist.co API.',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Internet',
          'Topic :: Utilities',
      ],
      keywords='anipy twissell anime anilist manga',
      url='https://github.com/twissell-/anipy',
      author='Damian Maggio Esne',
      author_email='dmaggioesne@gmail.com',
      license='MIT',
      packages=['anipy'],
      install_requires=[
          'urllib3',
          'urllib3_mock',
          'requests'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
