from random import randint

LottoNumbers = []
while len(LottoNumbers) < 6:
    LottoNumbers.append(randint(1, 50))
LottoNumbers.sort(key=int)
print(LottoNumbers)
