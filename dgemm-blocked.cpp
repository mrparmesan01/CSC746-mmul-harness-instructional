#include <cmath>
#include <vector>

const char* dgemm_desc = "Blocked dgemm.";

/*
* This routine calculates a basic square dgemm operation
* C := C + A * B
* where A, B, and C are n-by-n matrices stored in row-major format.
* On exit, A and B maintain their input values.
*/
// void square_dgemm(int n, double* A, double* B, double* C) {
//    for (int i = 0; i < n; i++) {
//       for (int j = 0; j < n; j++) {
//          double square_sum = C[i*n + j];
//          for (int k = 0; k < n; k++) {
//             // C[i, j] = C[i, j] + A[i, n] * B[n, j];
//             square_sum += A[i*n + k] * B[k*n + j];
//          }
//          C[i*n + j] = square_sum;
//       }
//    }
// }

/* This routine copies a block from src to dest */
void copy_block(double *dest, double *src, int n, int block_size) {
   for (int y = 0; y < block_size; y++) {
      std::memcpy(&dest[y * block_size],
         &src[y * n],
         block_size * sizeof(double));
   }
}

/*
* This routine writes a block from src to dest
* where dest is a larger matrix and src is a smaller block
* dest is the larger matrix, src is the smaller block
*/
void write_block(double *dest, double *src, int n, int block_size) {
   for (int y = 0; y < block_size; y++) {
      // copy the block from src to dest
      // dest[y * n] is the starting point of the row in the larger matrix
      // src[y * block_size] is the starting point of the row in the smaller block
      std::memcpy(&dest[y * n],
         &src[y * block_size],
         block_size * sizeof(double));
   }
}

/* This routine performs a dgemm operation
 *  C := C + A * B
 * where A, B, and C are n-by-n matrices stored in row-major format.
 * On exit, A and B maintain their input values. */
void square_dgemm_blocked(int n, int block_size, double* A, double* B, double* C) 
{
   // insert your code here
   int total_block_size = n / block_size;
   int block_arr_size = std::pow(block_size, 2);

   std::vector<double> An(block_arr_size);
   std::vector<double> Bn(block_arr_size);
   std::vector<double> Cn(block_arr_size);

   for (int i = 0; i < total_block_size; i++) {
      for (int j = 0; j < total_block_size; j++) {
         // calculate this so we store it in register
         int Cpos = i * n * block_size + j * block_size;
         copy_block(An.data(), &C[Cpos], n, block_size);

         for (int k = 0; k < total_block_size; k++) {
            copy_block(An.data(), &A[(i * block_size * n) + (k * block_size)], n, block_size);
            copy_block(Bn.data(), &B[(k * block_size * n) + (j * block_size)], n, block_size);

            square_dgemm(block_size, An.data(), Bn.data(), Cn.data());
         }

         write_block(&C[Cpos], &Cn[0], n, block_size);
      }
   }
}
