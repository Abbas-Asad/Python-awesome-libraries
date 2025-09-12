from tqdm import tqdm
import time
import random

# 1. Basic progress bar with custom description
print("=== Basic Progress Bar ===")
for i in tqdm(range(100), desc="Processing items", unit="item"):
    time.sleep(0.01)  # Simulate work

# 2. Nested progress bars
print("\n=== Nested Progress Bars ===")
for i in tqdm(range(5), desc="Outer loop"):
    for j in tqdm(range(10), desc=f"Inner loop {i}", leave=False):
        time.sleep(0.1)

# 3. Progress bar with dynamic updates
print("\n=== Dynamic Progress Bar ===")
pbar = tqdm(total=100, desc="Dynamic updates")
for i in range(100):
    pbar.update(1)
    pbar.set_postfix({"Current": i, "Status": "Processing"})
    time.sleep(0.02)
pbar.close()

# 4. Progress bar with custom formatting
print("\n=== Custom Formatting ===")
for i in tqdm(range(50), 
               desc="Custom format", 
               bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"):
    time.sleep(0.05)

# 5. Progress bar with different styles
print("\n=== Different Styles ===")
# ASCII style
for i in tqdm(range(30), desc="ASCII style", ascii=True):
    time.sleep(0.03)

# Unicode style (default)
for i in tqdm(range(30), desc="Unicode style"):
    time.sleep(0.03)

# 6. Progress bar with manual control
print("\n=== Manual Control ===")
with tqdm(total=100, desc="Manual control") as pbar:
    for i in range(100):
        if i % 10 == 0:
            pbar.set_description(f"Step {i}")
        pbar.update(1)
        time.sleep(0.01)

# 7. Progress bar with file processing simulation
print("\n=== File Processing Simulation ===")
files = [f"file_{i}.txt" for i in range(20)]
for file in tqdm(files, desc="Processing files"):
    # Simulate file processing
    time.sleep(0.1)

# 8. Progress bar with error handling
print("\n=== Error Handling ===")
for i in tqdm(range(10), desc="With errors"):
    try:
        if random.random() < 0.3:  # 30% chance of error
            raise ValueError("Random error")
        time.sleep(0.1)
    except Exception as e:
        tqdm.write(f"Error at step {i}: {e}")

# 9. Progress bar with position control
print("\n=== Position Control ===")
for i in tqdm(range(10), desc="Top bar", position=0):
    for j in tqdm(range(5), desc=f"Bottom bar {i}", position=1, leave=False):
        time.sleep(0.05)

# 10. Progress bar with custom colors (if colorama is available)
print("\n=== Advanced Features ===")
try:
    from tqdm.auto import tqdm as tqdm_auto
    for i in tqdm_auto(range(15), desc="Auto progress bar"):
        time.sleep(0.05)
except ImportError:
    print("tqdm.auto not available, using regular tqdm")
    for i in tqdm(range(15), desc="Regular progress bar"):
        time.sleep(0.05)

print("\n=== All examples completed! ===")