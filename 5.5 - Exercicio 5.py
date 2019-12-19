#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).lower() #faz com que eu n precise criar um contador de 'a' e 'A'
fraseSemEspacoNoInicioEFim = frase.strip().strip()
numeroA = fraseSemEspacoNoInicioEFim.count('a')
print(f'Quantas vezes aparece a letra a: {numeroA}')
fraseAinicio = fraseSemEspacoNoInicioEFim.find('a') + 1
print(f'A primeira letra "a" aparece em: {fraseAinicio}')
fraseAfinal = fraseSemEspacoNoInicioEFim.rfind('a') + 1
print(f'A primeira ultima "a" aparece em: {fraseAfinal}')