from random import randint
computador = randint (0, 5)#FAZ A MAQUINA PENSAR!
print('pensei em numero {} '.format(computador))
print('-=-' *24)
print('VOU PENSAR EM UM NUMERO DE 0, ao  5,')
print('-=-' *24)
jogador = int(input('em que numero eu pensei? '))#jogador tenta adivinhar
if jogador == computador:
 print('PARABEMS VOCE ME VENCEU')
else:
 print('GANHEI!! EU PENSEI NO {} E NAO NO {} '.format(computador, jogador))
