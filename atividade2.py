numero1 = float (input('fala um numero 1 ai:'))
numero2 = float (input('fala um numero 2 ai:',))

if numero1 > numero2:
    print (f''' {numero1} maior que {numero2:}, ''')
elif numero2 > numero1:
    print (f''' {numero2} maior que {numero1:}, ''')
elif numero1 == numero2:
    print (f''' {numero1} igual a {numero2}''')
    
