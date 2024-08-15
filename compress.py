import os
import zlib
from base64 import b64encode

def compress_file(filepath,compression_level=5):

    with open(filepath,'r') as f:
        data = f.read()

    bytes_data = bytes(data,'UTF-8')

    # compressing the data
    compressed_bytes_data = zlib.compress(bytes_data,level=compression_level)

    # encoding the compressed data
    encoded_data = b64encode(compressed_bytes_data)

    output_file_path = os.path.dirname(filepath)
    output_file_path = f'{output_file_path}/{os.path.basename(filepath)+'_compressed.txt'}'
    print(output_file_path)

    with open(output_file_path,'w') as f:
        f.write(encoded_data.decode('UTF-8'))

    print(f"Compression file size -->{len(encoded_data) / 1000}KB")

    return output_file_path

if __name__ == "__main__":
    compress_file("file_compress/demo.txt")