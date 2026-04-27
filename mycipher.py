import sys

def main():
    shift = int(sys.argv[1])

    letters_only = ""

    for line in sys.stdin:
        line = line.upper()

        for char in line:
            if 'A' <= char <= 'Z':
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                letters_only += new_char

    block_size = 5
    blocks_per_line = 10

    for i in range(0, len(letters_only), block_size * blocks_per_line):
        line_chunk = letters_only[i:i + block_size * blocks_per_line]

        blocks = [
            line_chunk[j:j + block_size]
            for j in range(0, len(line_chunk), block_size)
        ]

        print(" ".join(blocks))

if __name__ == "__main__":
    main()