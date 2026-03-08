# Awful Compressor

A revolutionary compression algorithm that achieves near-zero file sizes. The only catch? Decompression may take an infinite amount of time.

## How It Works

Awful Compressor converts your data to base64, then stores only the character frequencies. This produces an incredibly compact representation — we're talking **90%-99%+ compression ratios**.

The decompression process simply needs to find the correct permutation of characters that reconstructs the original data. With only a few trillion possible arrangements to try, your file should be restored somewhere between now and the heat death of the universe.

## Requirements

- Python 3
- NumPy

## Usage

### Demo

```bash
pip install numpy
python main.py
```

### Compress a file

```bash
python example/compress.py <input_file> <output_file>
```

Example:

```bash
python example/compress.py photo.png photo.awful
```

### Decompress a file

```bash
python example/decompress.py <compressed_file> <output_file>
```

Example:

```bash
python example/decompress.py photo.awful photo.png
```

Note: Decompression randomly shuffles characters until the SHA-256 hash matches. Results may vary between now and the end of time.

## Pros

- Lossless (in theory)
- Extraordinary compression ratios
- Very fast compression

## Cons

- Decompression time: O(n!)
