from setuptools import setup

setup(
    name='MultipleReturn',
    version='0.1.0a1',
    packages=[''],
    url='https://github.com/Gregory-Bell/MultipleReturn',
    license='GPLv3+',
    author='Gregory Bell',
    author_email='gregoryscottbell@gmail.com',
    description='An implementation of multiple return values.',
    long_description='Unlike Lisp\'s "values" function, Python lacks a way of creating a function that return multiple '
                     'values where the caller by default only sees the first one. Simply add the @multiplereturn '
                     'decorator to any function or method that return a tuple, and it will now return only the first '
                     'item in that tuple to its callers. Wrap the call to a @multiplereturn decorated function with '
                     'the values() function and the caller gets the original tuple.',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='multiple return values decorator'
)
