valor_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f'''
          Salário Bruto: R$ {salario_bruto:.2f}
          IR (11%): R$ {ir:.2f}
          INSS (8%): R$ {inss:.2f}
          Sindicato (5%): R$ {sindicato:.2f}
          Salário Líquido: R$ {salario_liquido:.2f}''')