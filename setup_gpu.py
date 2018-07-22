from distutils.core import setup, Extension
import numpy

module = Extension('pyyolo',
	library_dirs=['.', '/usr/local/', './darknet_cl/build/'],
	libraries=[
      'clBLAS',
      'darknet',
      'opencv_tracking',
      'opencv_video',
      'opencv_ximgproc',
      'opencv_imgproc',
      'opencv_core'
  ],
	include_dirs=[numpy.get_include(), './darknet_cl/darknet_cl/include'],
	sources = ['module.cpp'])

setup (name = 'pyyolo',
	version = '0.1',
	description = 'YOLO wrapper',
	ext_modules = [module])
