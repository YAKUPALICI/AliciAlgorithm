import math
import time

# --- PROJECT: THE ALICI ALGORITHM ---
# Author: Yakup Alici
# Description: Performance benchmark comparing Traditional Iteration vs. Alıcı Algorithm

# --- TEST PARAMETERS ---
# We use a micro-increment to force a high number of steps (approx. 1 Billion).
a1 = 5             # Initial Value
d = 0.000001       # Increment (Micro-step)
Limit = 1000       # Hard Cap (Limit)

print(f"--- BENCHMARK STARTED ---\nParameters: a1={a1}, d={d}, Limit={Limit}\n")
print("Calculating... (This may take a few seconds for the loop)\n")

# ---------------------------------------------------------
# METHOD 1: TRADITIONAL ITERATIVE LOOP (Brute Force)
# Complexity: O(n) - Linear Time
# ---------------------------------------------------------
start_time_loop = time.time()

current_val = a1
total_sum_loop = 0
step_count_loop = 0

# The standard way computers handle this without optimization:
while current_val <= Limit:
    total_sum_loop += current_val
    current_val += d
    step_count_loop += 1

end_time_loop = time.time()
duration_loop = end_time_loop - start_time_loop

print(f"[METHOD 1] Traditional Loop Results:")
print(f"Total Sum: {total_sum_loop:.4f}")
print(f"Steps Processed: {step_count_loop}")
print(f"Execution Time: {duration_loop:.6f} seconds")
print("-" * 40)

# ---------------------------------------------------------
# METHOD 2: THE ALICI ALGORITHM (Optimized Math)
# Complexity: O(1) - Constant Time
# ---------------------------------------------------------
start_time_alici = time.time()

# Step 1: Boundary Control (Autonomous 'n' calculation)
# Formula: floor((L - a1) / d) + 1
n = math.floor((Limit - a1) / d) + 1

# Step 2: Unified Summation
# Formula: n * (2*a1 + (n-1)*d) / 2
total_sum_alici = n * (2 * a1 + (n - 1) * d) / 2

end_time_alici = time.time()
duration_alici = end_time_alici - start_time_alici

# Correction for practically zero time to prevent division by zero in speedup calc
if duration_alici == 0: duration_alici = 1e-9 

print(f"[METHOD 2] Alıcı Algorithm Results:")
print(f"Total Sum: {total_sum_alici:.4f}")
print(f"Steps Processed: 1 (Analytical Step)")
print(f"Execution Time: {duration_alici:.10f} seconds")
print("-" * 40)

# ---------------------------------------------------------
# FINAL COMPARISON
# ---------------------------------------------------------
speed_up = duration_loop / duration_alici

print(f"CONCLUSION:\nThe Alıcı Algorithm is approx. {speed_up:,.0f} TIMES faster than the loop.")
