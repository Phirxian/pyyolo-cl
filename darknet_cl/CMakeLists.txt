cmake_minimum_required(VERSION 2.8)
set(CMAKE_CXX_FLAGS "-std=c++11 -O2 -DNDEBUG " )

set(OPENCV   ON)
set(GPU      ON)
set(BUILDLIB ON)

find_package(OpenCL)
find_package(OpenCV)

ADD_DEFINITIONS(-DGPU=1)
include_directories(${OpenCL_INCLUDE_DIR})
link_libraries(${OpenCL_LIBRARY})
link_libraries(${PROJECT_SOURCE_DIR}/darknet/clBLAS/libclBLAS.so)

ADD_DEFINITIONS(-DOPENCV)
include_directories(${OpenCV_INCLUDE_DIR})
link_libraries(${OpenCV_LIBRARIES})

aux_source_directory(./darknet/src DIR_LIB_SRC)
aux_source_directory(./darknet/example DIR_EXAMPLE_SRC)

include_directories(./darknet/include)
include_directories(./darknet/clBLAS)

link_libraries(libpthread.so)

if (BUILDLIB)
	add_library(darknet SHARED ${DIR_LIB_SRC})
else(BUILDLIB)
	add_executable(darknet ${DIR_LIB_SRC} ${DIR_EXAMPLE_SRC})
endif()
