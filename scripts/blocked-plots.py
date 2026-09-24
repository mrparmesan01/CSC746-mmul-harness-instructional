import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ns = [64, 128, 256, 512, 1024, 2048]
total_flops = [2 * (n ** 3) for n in ns]


b64_t1 = [0.001078, 0.000174, 0.000186, 0.000226]
b64_t2 = [0.000895, 0.000147, 0.000162, 0.000204]
b64_avg = [(a + b) / 2 for a, b in zip(b64_t1, b64_t2)]

# Grouping times by block size variant (columns represent the 4 block sizes)
bmmco_data = {
    'Block_Var_1': [b64_avg[0], 0.007175, 0.058633, 0.499152, 4.229681, 41.300170],
    'Block_Var_2': [b64_avg[1], 0.001099, 0.009047, 0.105014, 0.745947, 6.156877],
    'Block_Var_3': [b64_avg[2], 0.001292, 0.009809, 0.091715, 0.705107, 5.897486],
    'Block_Var_4': [b64_avg[3], 0.001591, 0.011642, 0.107430, 0.916133, 7.099573]
}

blas_raw = {
    64: [(0.020380 + 0.000033) / 2], # averaged or take individual; let's list by N order matching ns
    128: [0.000253],
    256: [0.001683],
    512: [0.007093],
    1024: [0.054468],
    2048: [0.452343]
}
blas_times = [
    (0.020380 + 0.000033) / 2, 
    0.000253, 
    0.001683, 
    0.007093, 
    0.054468, 
    0.452343
]

# MFLOP/s = (2 * N^3) / (Time * 1e6)
mflops_cblas = [(f / t) / 1e6 for f, t in zip(total_flops, blas_times)]

mflops_blocks = {}
block_labels = ['Block Size A', 'Block Size B', 'Block Size C', 'Block Size D']
colors = ['darkorange', 'dodgerblue', 'purple', 'deeppink']
markers = ['o', 's', '^', 'd']

for i, key in enumerate(bmmco_data.keys()):
    mflops_blocks[key] = [(f / t) / 1e6 for f, t in zip(total_flops, bmmco_data[key])]

plt.figure(figsize=(11, 7))


for i, key in enumerate(bmmco_data.keys()):
    plt.plot(
        ns, 
        mflops_blocks[key], 
        marker=markers[i], 
        linestyle='-', 
        color=colors[i], 
        linewidth=1.8, 
        markersize=7, 
        label=f'BMMCO ({block_labels[i]})'
    )

# Plot the CBLAS reference implementation (Distinct thick dashed line)
plt.plot(
    ns, 
    mflops_cblas, 
    marker='*', 
    linestyle='--', 
    color='forestgreen', 
    linewidth=2.5, 
    markersize=10, 
    label='CBLAS Reference'
)

plt.xscale('log', base=2)
plt.yscale('log')

plt.xlabel('Problem Size ($N$)', fontsize=12)
plt.ylabel('Performance (MFLOP/s)', fontsize=12)
plt.title('BMMCO (4 Block Sizes) vs. CBLAS', fontsize=14, fontweight='bold')

# Clean major-only gridlines with subtle alpha
plt.grid(True, which="major", linestyle="--", alpha=0.4)

plt.xticks(ns, labels=[str(n) for n in ns])
plt.legend(fontsize=10, loc='upper left', framealpha=0.9)
plt.tight_layout()

plt.show()