import random

exclude = {40,41,42,43,45,9}

numbers = [n for n in range(1,46) if n not in exclude]

lotto = random.sample(numbers,6)
lotto.sort()
print(lotto)