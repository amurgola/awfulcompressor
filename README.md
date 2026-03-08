# Awful Compressor

A revolutionary compression algorithm that achieves near-zero file sizes. The only catch? Decompression may take an infinite amount of time.

## How It Works

Awful Compressor converts your data to base64, then stores only the character frequencies. This produces an incredibly compact representation — we're talking **90%-99%+ compression ratios**.

The decompression process simply needs to find the correct permutation of characters that reconstructs the original data. With only a few trillion possible arrangements to try, your file should be restored somewhere between now and the heat death of the universe.

## Requirements

- Python 3
- NumPy

## Usage

```bash
pip install numpy
python main.py
```

## Pros

- Lossless (in theory)
- Extraordinary compression ratios
- Very fast compression

## Cons

- Decompression time: O(n!)
