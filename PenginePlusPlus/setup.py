from distutils.core import setup, Extension

module1 = Extension('test', sources = ['PenginePlusPlus/main.cpp'])

setup(name = 'PenginePlusPlus',
      version = '1.0',
      description = 'Imporves Pengine's functionality and speed.',
      ext_modules = [module1])