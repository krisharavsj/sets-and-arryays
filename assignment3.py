import string
import random

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    full_pool = string.ascii_letters + string.digits
    password_chars += random.choices(full_pool, k=length - len(password_chars))

    # Shuffle to avoid predictable order
    random.shuffle(password_chars)

    return ''.join(password_chars)
if __name__ == "__main__":
    pw = generate_password(12)
    print("Generated password:", pw)
