import base64
import hashlib
import json
import random
import sys
import time

if len(sys.argv) != 3:
    print("Usage: python decompress.py <compressed_file> <output_file>")
    sys.exit(1)

compressed_path = sys.argv[1]
output_path = sys.argv[2]

# Load the compressed data
with open(compressed_path, "r") as f:
    compressed = json.load(f)

target_hash = compressed["hash"]
target_length = compressed["length"]
frequencies = compressed["frequencies"]

# Rebuild the pool of characters from frequencies
char_pool = []
for char, count in frequencies.items():
    char_pool.extend([char] * count)

print(f"Target hash: {target_hash}")
print(f"Characters to arrange: {len(char_pool)}")
print(f"Possible permutations: a lot. Good luck.")
print()

# Randomly shuffle until the hash matches
attempts = 0
start_time = time.time()

while True:
    random.shuffle(char_pool)
    candidate = "".join(char_pool)
    candidate_hash = hashlib.sha256(candidate.encode("ascii")).hexdigest()
    attempts += 1

    if attempts % 100000 == 0:
        elapsed = time.time() - start_time
        print(f"Attempt {attempts:,} | Elapsed: {elapsed:.1f}s | Still looking...")

    if candidate_hash == target_hash:
        # We found it! Decode from base64 back to original bytes
        raw_data = base64.b64decode(candidate)
        with open(output_path, "wb") as f:
            f.write(raw_data)

        elapsed = time.time() - start_time
        print(f"\nMatch found after {attempts:,} attempts ({elapsed:.1f}s)!")
        print(f"Restored file saved to {output_path}")
        break
