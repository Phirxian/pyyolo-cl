# pyyolo-cl
python yolo with opencl inference

# pyyolo
https://github.com/digitalbrain79/pyyolo

# yolo opencl
https://github.com/ganyc717/Darknet-On-OpenCL

# installation

```
git clone https://github.com/Phirxian/pyyolo-cl.git
cd pyyolo-cl/darknet_cl/
mkdir build ; cd build
cmake ..
make -j 4
make install
cd ../../..
python3 setup_gpu.py build
python3 setup_gpu.py install
```