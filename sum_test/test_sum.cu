#include <stdio.h>
#include <stdlib.h>

__global__ void cu_add(int* a, int* b, int* sum) {
    *sum = *a + *b;
}


void c_add(int a, int b, int* sum) {
    *sum = a + b;
}

void cu_add(int a, int b, int* sum) {

    int *d_a, *d_b, *d_sum;

    int size = sizeof(int);
    cudaMalloc((void**)&d_a, size);
    cudaMalloc((void**)&d_b, size);
    cudaMalloc((void**)&d_sum, size);

    cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, &b, size, cudaMemcpyHostToDevice);

    cuda_add<<<1, 1>>>(d_a, d_b, d_sum);
    cudaMemcpy(sum, d_sum, size, cudaMemcpyDeviceToHost);
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_sum);

    printf("Cuda result: %d\n", *sum);
}