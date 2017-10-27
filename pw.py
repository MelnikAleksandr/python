myrg = random.SystemRandom();
length = 10
alphabet = string.ascii_letters + string.digits + string.punctuation
pw = str().join(myrg.choice(alphabet) for _ in range(length));
print pw()
