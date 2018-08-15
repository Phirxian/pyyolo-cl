cmake_minimum_required(VERSION 2.8)
set(CMAKE_CXX_FLAGS "-std=c++11 -O2 -DNDEBUG " )

set(OPENCV   ON)
set(GPU      ON)
set(BUILDLIB ON)

find_package(CUDA)
find_package(OpenCV)
find_package(OpenCL)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DGPU=1")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DOPENCV")

add_definitions(-DGPU)
add_definitions(-O4 -g)
add_definitions(-DOPENCV)

set(CUDA_NVCC_FLAGS ${CUDA_NVCC_FLAGS}; -O3 -gencode arch=compute_30,code=sm_30)

include_directories(${CUDA_TOOLKIT_INCLUDE})
include_directories(${OpenCV_INCLUDE_DIR})

link_libraries(${OpenCV_LIBRARIES})
link_libraries(${OpenCL_LIBRARY})
link_libraries(${CUDA_CUDA_LIBRARY})
link_libraries(${CUDA_CUDART_LIBRARY})
link_libraries(${CUDA_cublas_LIBRARY})
link_libraries(${CUDA_curand_LIBRARY})
link_libraries(${CUDA_culibos_LIBRARY})

aux_source_directory(./darknet/app DIR_APP_SRC)
aux_source_directory(./darknet/src DIR_LIB_SRC)
aux_source_directory(./darknet/kernels DIR_KER_SRC)
include_directories(./darknet/include)
include_directories(./darknet/kernels)
include_directories(./darknet/src)

link_libraries(libpthread.so)

if (BUILDLIB)
	cuda_add_library(darknet SHARED ${DIR_LIB_SRC} ${DIR_KER_SRC})
else(BUILDLIB)
	cuda_add_executable(darknet ${DIR_LIB_SRC} ${DIR_APP_SRC} ${DIR_KER_SRC} ${DIR_EXAMPLE_SRC})
endif()
