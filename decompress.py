import zlib
from base64 import b64decode

def decompress_file(filepath):

    with open(filepath,'r') as f:
        data = f.read()
    
    data = zlib.decompress(b64decode(data))
    print(len(data))

    
if __name__ == "__main__":
    decompress_file("file_compress/compressed.txt")