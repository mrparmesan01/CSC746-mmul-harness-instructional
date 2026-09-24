import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

basic_data = {
    'N': [64, 64, 128, 256, 512, 1024, 2048],
    'Time': [0.000328, 0.000199, 0.003227, 0.039882, 0.578160, 6.126028, 71.132531]
}
df_basic = pd.DataFrame(basic_data)
df_basic_grouped = df_basic.groupby('N')['Time'].mean().reset_index()

# Calculate MFLOP/s for Basic: (2 * N^3) / (Time * 1e6)
df_basic_grouped['Total_FLOPs'] = 2 * (df_basic_grouped['N'] ** 3)
df_basic_grouped['MFLOPS'] = (df_basic_grouped['Total_FLOPs'] / df_basic_grouped['Time']) / 1e6

blas_data = {
    'N': [64, 64, 128, 256, 512, 1024, 2048],
    'Time': [0.020380, 0.000033, 0.000253, 0.001683, 0.007093, 0.054468, 0.452343]
}
df_blas = pd.DataFrame(blas_data)
df_blas_grouped = df_blas.groupby('N')['Time'].mean().reset_index()

# Calculate MFLOP/s for CBLAS
df_blas_grouped['Total_FLOPs'] = 2 * (df_blas_grouped['N'] ** 3)
df_blas_grouped['MFLOPS'] = (df_blas_grouped['Total_FLOPs'] / df_blas_grouped['Time']) / 1e6

plt.figure(figsize=(10, 6))

# Plot Basic MM curve
plt.plot(
    df_basic_grouped['N'], 
    df_basic_grouped['MFLOPS'], 
    marker='o', 
    linestyle='-', 
    color='crimson', 
    linewidth=2, 
    markersize=8, 
    label='Basic MM ($O(N^3)$)'
)

# Plot CBLAS curve
plt.plot(
    df_blas_grouped['N'], 
    df_blas_grouped['MFLOPS'], 
    marker='s', 
    linestyle='--', 
    color='forestgreen', 
    linewidth=2, 
    markersize=8, 
    label='CBLAS Reference'
)

plt.xscale('log', base=2)
plt.yscale('log')

plt.xlabel('Problem Size ($N$)', fontsize=12)
plt.ylabel('Performance (MFLOP/s)', fontsize=12)
plt.title('Basic Matrix Multiplication vs. CBLAS', fontsize=14, fontweight='bold')

# Clean major-only gridlines with subtle opacity
plt.grid(True, which="major", linestyle="--", alpha=0.4)

# Set ticks to match the exact problem sizes
unique_n = df_basic_grouped['N']
plt.xticks(unique_n, labels=[str(n) for n in unique_n])

plt.legend(fontsize=11, loc='upper left')
plt.tight_layout()

plt.show()