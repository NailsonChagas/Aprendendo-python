#sempre que vc for colocar cor no terminal usando o padrão ANSI vc vai usar esse codigo \033[style(extilo); text(texto); back(cor de fundo)m
#style: 0 = sem formatação, 1 = negrito, 4 = sublinhar, 7 = inverte a configuração com back
#text: 30 = branco, 31 = vermelho, 32 = verde, 33 = amarelo, 34 = azul, 35 = majenta, 36 = ciano, 37 = cinza
#text: 40 = branco, 41 = vermelho, 42 = verde, 43 = amarelo, 44 = azul, 45 = majenta, 46 = ciano, 47 = cinza

a = 5
b = 3

print('\033[1;35m Ola mundo!')
print('\033[1;32;40m Ola mundo!')
print('\033[1;32;40m Ola mundo!\033[m')
print('\033[1;31;42m Ola mundo!\033[m')
print(f'Os valores são \033[1;35m{a}\033[m e \033[1;36;43m{a}\033[m')