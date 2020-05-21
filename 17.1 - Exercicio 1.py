# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date

def voto(anoNascimento):
    """
    ->Função voto() informa se a condição de voto de uma pessoa em uma prócima eleição

    :param anoNascimento: Ano de nascimento da pessoa que você deseja saber se podera votar
    :return: Retorna uma string que informara a situação do voto
    """
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    if idade<16:
        return  'VOTO NEGADO'
    elif idade >= 16 and idade < 18:
        return  'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'

situacao = voto(int(input('Insira sua idade de nascimento: ')))
print(situacao)