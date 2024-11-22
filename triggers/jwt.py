import base64
import hashlib

def trigger_jwt_tampering(jwt):
    header, payload, signature = jwt.split(".")
    new_signature = base64.b64encode(hashlib.sha256(payload.encode()).digest())
    return f"{header}.{payload}.{new_signature}"
