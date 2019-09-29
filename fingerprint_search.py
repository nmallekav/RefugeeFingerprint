
from app import is_match
from hash import get_hash

def has_match(new_fingerprint_file, fingerprint_files):
    for fingerprint_file in fingerprint_files:
        if is_match(new_fingerprint_file, fingerprint_file):
            return get_hash(fingerprint_file) 
    return None