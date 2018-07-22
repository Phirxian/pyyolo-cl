GPU=1
CUDNN=0
DEBUG=0
OPENCV=1

# ARCH= -gencode arch=compute_20,code=[sm_20,sm_21] \
# 	  -gencode arch=compute_30,code=sm_30 \
# 	  -gencode arch=compute_35,code=sm_35 \
# 	  -gencode arch=compute_50,code=[sm_50,compute_50] \
# 	  -gencode arch=compute_52,code=[sm_52,compute_52]

# This is what I use, uncomment if you know your arch and want to specify
ARCH= -gencode arch=compute_30,code=sm_30
# ARCH= -gencode arch=compute_61,code=compute_61 # Titan Xp
# ARCH= -gencode arch=compute_61,code=compute_61 # Tegra TX2

VPATH=./darknet/src/:./darknet/examples
LIB=libyolo.a
OBJDIR=./obj/

CC=gcc
AR=ar
OPTS=-Ofast
COMMON= 
CFLAGS=-Wall -Wfatal-errors -Wno-unused-result -fPIC
CFLAGS+=-I./darknet_cl/darknet_cl/src
CFLAGS+=-I./darknet_cl/darknet_cl/include
CFLAGS+=-I./darknet_cl/darknet_cl/clBLAS/
CFLAGS+=-I/opt/gcc-4.8/include/c++/4.8.2/

ifeq ($(DEBUG), 1) 
OPTS=-O0 -g
endif

CFLAGS+=$(OPTS)

ifeq ($(OPENCV), 1) 
COMMON+= -DOPENCV
CFLAGS+= -DOPENCV
COMMON+= `pkg-config --cflags opencv` 
endif

ifeq ($(GPU), 1) 
CFLAGS+= -DGPU -ldarknet
endif

OBJ=libyolo.o

OBJS = $(addprefix $(OBJDIR), $(OBJ))
DEPS = $(wildcard src/*.h) Makefile

all: obj $(LIB)

$(LIB): $(OBJS)
	$(AR) rcs $@ $^

$(OBJDIR)%.o: %.cpp $(DEPS)
	$(CC) $(COMMON) $(CFLAGS) -c $< -o $@

$(OBJDIR)%.o: %.cu $(DEPS)
	$(NVCC) $(ARCH) $(COMMON) --compiler-options "$(CFLAGS)" -c $< -o $@

obj:
	mkdir -p obj

.PHONY: clean

clean:
	rm -rf $(OBJS) $(LIB)

