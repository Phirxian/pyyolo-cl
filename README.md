# pyyolo-cl
python yolo with opencl inference

# pyyolo
https://github.com/digitalbrain79/pyyolo

# yolo opencl
https://github.com/ganyc717/Darknet-On-OpenCL

# installation

git clone https://github.com/Phirxian/pyyolo-cl.git
build yolo in the desired inference (cuda or opencl)

## opencl
```
cd pyyolo-cl/darknet_cl/
mkdir build ; cd build
cmake ..
make -j 4
make install
```

## cuda
setup the desired gcc version (compatible with nvcc)
```
export CC=/opt/gcc-4.8/bin/gcc
export CXX=/opt/gcc-4.8/bin/g++
```
compile and install
```
cd pyyolo-cl/darknet_cu/
mkdir build ; cd build
cmake ..
make -j 4
make install
```

## python module

build and install the python module
```
cd ../../..
python3 setup_gpu.py build
python3 setup_gpu.py install
```

we can switch between cuda and opencl with signle `make install` in the desired inference folder.