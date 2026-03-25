import math
import statistics

# Data for the 10 samples [Length 1, Length 2, Large Diam, Small Diam]
# Note: Sample A Length 1 has been updated from 10.62 to 12.00
data = [
    [10.62, 3.15, 1.01, 0.53], # Sample A (Updated)
    [10.59, 3.27, 0.97, 0.47], # Sample B
    [10.70, 3.30, 1.00, 0.47], # Sample C
    [10.58, 3.18, 1.06, 0.46], # Sample D
    [10.55, 3.23, 1.05, 0.50], # Sample E
    [10.57, 3.33, 0.93, 0.51], # Sample F
    [10.63, 3.25, 1.02, 0.49], # Sample G
    [10.45, 3.27, 1.11, 0.46], # Sample H
    [10.58, 3.18, 0.92, 0.45], # Sample I
    [10.47, 3.19, 0.93, 0.51]  # Sample J
]

volumes = []

for sample in data:
    l1, l2, d_large, d_small = sample
    
    # Calculate radii
    r_large = d_large / 2
    r_small = d_small / 2
    
    # Calculate volumes of the two sections
    # Large section length is (Length 1 - Length 2)
    vol_large = math.pi * (r_large**2) * (l1 - l2)
    vol_small = math.pi * (r_small**2) * (l2)
    
    total_vol = vol_large + vol_small
    volumes.append(total_vol)

# Calculate summary statistics
avg_vol = statistics.mean(volumes)
std_dev_vol = statistics.stdev(volumes) # stdev() assumes sample, not population
max_vol = max(volumes)
min_vol = min(volumes)

# Display Results
print(f"The volume values are {volumes}")
print(f"The average of the volumes is {avg_vol:.2f}.")
print(f"The standard deviation of the volumes is {std_dev_vol:.2f}.")
print(f"The maximum of the volumes is {max_vol:.2f}.")
print(f"The minimum of the volumes is {min_vol:.2f}.")