NVCC = nvcc
NVCC_FLAGS = -fPIC
LINK_FLAGS = -shared

TARGET_LIB = libtest_sum.so

SRC = test_sum.cu
OBJ = $(SRC:.cu=.o)

all: $(TARGET_LIB)

%.o: %.cu
	$(NVCC) $(NVCC_FLAGS) -c $< -o $@

$(TARGET_LIB): $(OBJ)
	$(NVCC) $(LINK_FLAGS) -o $@ $^

clean:
	rm -f $(OBJ) $(TARGET_LIB)

.PHONY: all clean