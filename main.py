import numpy as np
import base64
import sys

# Generate X amount of bfloat16 random numbers and put them into an array
num_values = 1000
random_array = np.random.randn(num_values).astype(np.float16)
print(f"Number of values: {num_values}")

# Put the array into string format.
array_string = random_array.tobytes()

# Create a second variable to hold the base64 encoding of the string
base64_encoded = base64.b64encode(array_string)

# Print the file size of the string and also the base64 encoding
print(f"Raw bytes size: {sys.getsizeof(array_string)} bytes")
print(f"Base64 encoded size: {sys.getsizeof(base64_encoded)} bytes")

# Now do a sort of compression by first looping through the base64 string, creating a dictionary of the characters and their counts
b64_str = base64_encoded.decode('ascii')
char_counts = {}
for char in b64_str:
    char_counts[char] = char_counts.get(char, 0) + 1

# Then create a final variable that is a representation of the dictionary, where each character is replaced by its count and the character itself
compressed = ''.join(f"{count}{char}" for char, count in char_counts.items())

# Finally, print the file size of the final variable and compare it to the original string and the base64 encoding
print(f"Compressed size: {sys.getsizeof(compressed)} bytes")
print()
print(f"Compression ratio vs raw: {sys.getsizeof(compressed) / sys.getsizeof(array_string):.2%}")
print(f"Compression ratio vs base64: {sys.getsizeof(compressed) / sys.getsizeof(base64_encoded):.2%}")
print()
print(f"Compressed representation: {compressed}")
