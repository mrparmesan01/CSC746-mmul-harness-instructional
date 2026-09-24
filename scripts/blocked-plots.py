import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Raw timing data for blocked DGEMM across all trials and problem sizes
data = {
    'N': [
        64, 64, 64, 64,  64, 64, 64, 64,
        128, 128, 128, 128,
        256, 256, 256, 256,
        512, 512, 512, 512,
        1024, 1024, 1024, 1024,
        2048, 2048, 2048, 2048
    ],
    'Time': [
        0.001078, 0.000174, 0.000186, 0.000226,
        0.000895, 0.000147, 0.000162, 0.000204,
        0.007175, 0.001099, 0.001292, 0.001591,
        0.058633, 0.009047, 0.009809, 0.011642,
        0.499152, 0.105014, 0.091715, 0.107430,
        4.229681, 0.745947, 0.705107, 0.916133,
        41.300170, 6.156877, 5.897486, 7.099573
    ]
}

df = pd.DataFrame(data)

# Group by N and take the mean runtime across all trials
df_grouped = df.groupby('N')['Time'].mean().reset_index()

# Calculate MFLOP/s
df_grouped['Total_FLOPs'] = 2 * (df_grouped['N'] ** 3)
df_grouped['MFLOPS'] = (df_grouped['Total_FLOPs'] / df_grouped['Time']) / 1e6

# Create plot
plt.figure(figsize=(9, 6))
plt.plot(
    df_grouped['N'], 
    df_grouped['MFLOPS'], 
    marker='s', 
    linestyle='-', 
    color='darkorange', 
    linewidth=2, 
    markersize=8, 
    label='Blocked DGEMM'
)

# Axis formatting
plt.xscale('log', base=2)
plt.yscale('log')
plt.xlabel('Problem Size ($N$)', fontsize=12)
plt.ylabel('Performance (MFLOP/s - Log Scale)', fontsize=12)
plt.title('Performance: Blocked DGEMM', fontsize=14, fontweight='bold')

# Clean major-only gridlines
plt.grid(True, which="major", linestyle="--", alpha=0.4)
plt.xticks(df_grouped['N'], labels=[str(n) for n in df_grouped['N']])
plt.legend(fontsize=11)
plt.tight_layout()

plt.show()