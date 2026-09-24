# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # 1. Load the raw timing data
# data = {
#     'N': [64, 64, 128, 256, 512, 1024, 2048],
#     'Time': [0.000328, 0.000199, 0.003227, 0.039882, 0.578160, 6.126028, 71.132531]
# }

# df = pd.DataFrame(data)

# # 2. Group by problem size N and calculate the mean runtime
# df_grouped = df.groupby('N')['Time'].mean().reset_index()

# # 3. Create the plot
# plt.figure(figsize=(9, 6))
# plt.plot(
#     df_grouped['N'], 
#     df_grouped['Time'], 
#     marker='o', 
#     linestyle='-', 
#     color='royalblue', 
#     linewidth=2, 
#     markersize=8, 
#     label='Mean Runtime'
# )

# # 4. Set logarithmic scales for better visualization of exponential growth
# plt.xscale('log', base=2)
# plt.yscale('log')

# # 5. Styling, labels, and grid
# plt.xlabel('Problem Size ($N$)', fontsize=12)
# plt.ylabel('Elapsed Time (seconds - Log Scale)', fontsize=12)
# plt.title('Algorithm Runtime vs. Problem Size ($N$)', fontsize=14, fontweight='bold')
# plt.grid(True, which="both", ls="--", alpha=0.7)
# plt.xticks(df_grouped['N'], labels=[str(n) for n in df_grouped['N']])
# plt.legend(fontsize=11)
# plt.tight_layout()

# # 6. Display the plot
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Load the raw timing data
data = {
    'N': [64, 64, 128, 256, 512, 1024, 2048],
    'Time': [0.000328, 0.000199, 0.003227, 0.039882, 0.578160, 6.126028, 71.132531]
}

df = pd.DataFrame(data)

# 2. Group by problem size N and calculate the mean runtime
df_grouped = df.groupby('N')['Time'].mean().reset_index()

# 3. Create the plot
plt.figure(figsize=(9, 6))
plt.plot(
    df_grouped['N'], 
    df_grouped['Time'], 
    marker='o', 
    linestyle='-', 
    color='royalblue', 
    linewidth=2, 
    markersize=8, 
    label='Mean Runtime'
)

# 4. Set logarithmic scales for better visualization of exponential growth
plt.xscale('log', base=2)
plt.yscale('log')

# 5. Styling, labels, and clean grid settings
plt.xlabel('Problem Size ($N$)', fontsize=12)
plt.ylabel('Elapsed Time (seconds - Log Scale)', fontsize=12)
plt.title('Algorithm Runtime vs. Problem Size ($N$)', fontsize=14, fontweight='bold')

# Only show major gridlines with a subtle alpha for a cleaner look
plt.grid(True, which="major", linestyle="--", alpha=0.4)

plt.xticks(df_grouped['N'], labels=[str(n) for n in df_grouped['N']])
plt.legend(fontsize=11)
plt.tight_layout()

# 6. Display the plot
plt.show()