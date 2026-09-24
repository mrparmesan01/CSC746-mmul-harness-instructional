import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Raw timing data for BLAS reference DGEMM
data = {
    'N': [64, 64, 128, 256, 512, 1024, 2048],
    'Time': [0.020380, 0.000033, 0.000253, 0.001683, 0.007093, 0.054468, 0.452343]
}

df = pd.DataFrame(data)

# Group by N and average runtimes for duplicates (e.g., N=64)
df_grouped = df.groupby('N')['Time'].mean().reset_index()

# Calculate MFLOP/s
df_grouped['Total_FLOPs'] = 2 * (df_grouped['N'] ** 3)
df_grouped['MFLOPS'] = (df_grouped['Total_FLOPs'] / df_grouped['Time']) / 1e6

# Create plot
plt.figure(figsize=(9, 6))
plt.plot(
    df_grouped['N'], 
    df_grouped['MFLOPS'], 
    marker='^', 
    linestyle='-', 
    color='forestgreen', 
    linewidth=2, 
    markersize=8, 
    label='CBLAS Reference DGEMM'
)

# Axis formatting
plt.xscale('log', base=2)
plt.yscale('log')
plt.xlabel('Problem Size ($N$)', fontsize=12)
plt.ylabel('Performance (MFLOP/s - Log Scale)', fontsize=12)
plt.title('Performance: CBLAS Reference DGEMM', fontsize=14, fontweight='bold')

# Clean major-only gridlines
plt.grid(True, which="major", linestyle="--", alpha=0.4)
plt.xticks(df_grouped['N'], labels=[str(n) for n in df_grouped['N']])
plt.legend(fontsize=11)
plt.tight_layout()

plt.show()