import random

esqueletico = random.randint(50,120)
corcunda = random.randint(20,20)
um_braco = random.randint(50,120)
vidente = random.randint(50,120)

soma = esqueletico + corcunda + um_braco + vidente
if soma > 119:
    print('A porta abriu com', soma,'F')