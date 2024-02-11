import random

nove_dig = ''
for i in range(9):
    nove_dig += str(random.randint(0, 9))

cont = 10
resultado = 0
for i in nove_dig:
    resultado += int(i) * cont
    cont -= 1
i = (resultado * 10) % 11
i = i if i <= 9 else 0

dec_dig = nove_dig + str(i)
resultado_2 = 0
cont2 = 11
for i2 in dec_dig:
    resultado_2 += int(i2) * cont2
    cont2 -= 1
i2 = (resultado_2 * 10) % 11
i2 = i2 if i2 <= 9 else 0

cpf_gerado = f'{nove_dig}{i}{i2}'

print(cpf_gerado)
