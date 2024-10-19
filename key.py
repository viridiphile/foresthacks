import secrets
secret_key = secrets.token_hex(32)  # Generates a random 64-character string
print(secret_key)
