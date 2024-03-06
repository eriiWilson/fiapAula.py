valor_inicial = float (input('qual o valor inicial da sua conta:'))
rentabilidade = float (input('qual a rentabilidade :'))
meses_investidos = float(input('quantos meses investidos:'))
rentabilidade  = rentabilidade / 100
valor_final = valor_inicial * (1 + rentabilidade) **meses_investidos

print (f'''valor depois {meses_investidos:.0f} meses: R${valor_final:.2f}''')
