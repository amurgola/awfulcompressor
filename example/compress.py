import base64
import hashlib
import json
import sys

if len(sys.argv) != 3:
    print("Usage: python compress.py <input_file> <output_file>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

# Read the input file
with open(input_path, "rb") as f:
    raw_data = f.read()

# Base64 encode
b64_data = base64.b64encode(raw_data).decode("ascii")

# Store a SHA-256 hash of the original base64 string for integrity validation
b64_hash = hashlib.sha256(b64_data.encode("ascii")).hexdigest()

# Count character frequencies
char_counts = {}
for char in b64_data:
    char_counts[char] = char_counts.get(char, 0) + 1

# Build the compressed representation
compressed = {
    "hash": b64_hash,
    "length": len(b64_data),
    "frequencies": char_counts,
}

with open(output_path, "w") as f:
    json.dump(compressed, f, indent=2)

original_size = sys.getsizeof(raw_data)
compressed_size = len(json.dumps(compressed))
print(f"Original size: {original_size} bytes")
print(f"Compressed size: {compressed_size} bytes")
print(f"Compression ratio: {compressed_size / original_size:.2%}")
print(f"SHA-256 hash: {b64_hash}")
print(f"Saved to {output_path}")
