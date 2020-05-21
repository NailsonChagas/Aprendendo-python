# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*entrada, situação = True):
    """
    Recebe notas de alunos de retorna os um dicionario com a maior e menor nota, a média da turma e a situação deste grupo de aluno
    :param entrada: uma ou mais notas de alunos
    :param situação: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com as insformações da turma
    """
    dicionario = dict()
    dicionario['tamanhoTupla'] = len(entrada)
    dicionario['maior'] = max(entrada)
    dicionario['menor'] = min(entrada)
    soma = 0
    for item in entrada:
        soma += item
    dicionario['media'] = soma / dicionario['tamanhoTupla']
    if situação:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'BOA'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario

r = notas(4.5,9,4,5,9,6,situação=0)
print(r)