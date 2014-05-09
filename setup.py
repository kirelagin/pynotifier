#!/usr/bin/env python3

from distutils.core import setup


setup(name='pynotifier',
      version='0.1',

      description='Convenience library for developing scripts that send notifications',
      long_description='''
          This library lets you quickly and easily develop scripts that send you
          notifications, statistics or some other data.
          
          It has two basic modes of output: printing on the console and sending emails,
          but you are free to add more.

          See README_ for more details.

          .. _README: https://github.com/kirelagin/pynotifier/blob/master/README.md
          ''',


      author='Kirill Elagin',
      author_email='kirelagin@gmail.com',

      url='https://github.com/kirelagin/pynotifier',

      classifiers = ['Development Status :: 4 - Beta',
                     'Environment :: Console',
                     'Intended Audience :: Developers',
                     'Intended Audience :: System Administrators',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: Unix',
                     'Programming Language :: Python :: 3',
                     'Topic :: Communications :: Email',
                     'Topic :: Software Development :: Libraries',
                    ],
      keywords = ['notification', 'display', 'send', 'email'],

      packages=['notifier'],

      requires=['pyxdg'],
     )
