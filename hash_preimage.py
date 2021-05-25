import hashlib
import os

NUM_BYTES=4

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    nonce = b'\x00'

    target_string_length = len(target_string)

    match = False
    while match == False:
        x = os.urandom(NUM_BYTES)
        x_sha = hashlib.sha256(x).hexdigest()
        x_bits = bin(int(x_sha, base=16))[-target_string_length:]
        if x_bits == target_string:
            match = True

    return x
