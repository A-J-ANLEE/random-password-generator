import secrets
import string
def random_strong_password(length=15):
    letters=string.ascii_letters
    digits=string.digits
    symbols=string.punctuation
    total=letters+digits+symbols
    password=[secrets.choice(letters),secrets.choice(digits),secrets.choice(symbols)]
    password += [secrets.choice(total)
                  for _ in range(length - 3)]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)
print("Secure 15-character password:",random_strong_password(15))


