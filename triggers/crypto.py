import hashlib
from typing import Dict

def trigger_crypto(data: Dict):
    return hashlib.md5(data['input'].encode()).hexdigest()
