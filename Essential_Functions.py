# ==========================================================================
# FUNÇÕES ESSENCIAIS DO PYTHON
# Este código demonstra várias funções importantes do Python organizadas por categoria
# ==========================================================================

# ==========================================================================
# FUNÇÕES PARA MANIPULAÇÃO DE STRINGS
# ==========================================================================

def demonstrar_strings():
    """Demonstra funções comuns para manipulação de strings"""
    texto = "Python é uma linguagem incrível"
    
    # upper() - Converte string para maiúsculas
    print(texto.upper())  # Resultado: PYTHON É UMA LINGUAGEM INCRÍVEL
    
    # lower() - Converte string para minúsculas
    print(texto.lower())  # Resultado: python é uma linguagem incrível
    
    # strip() - Remove espaços em branco do início e fim
    texto_com_espacos = "   texto com espaços   "
    print(texto_com_espacos.strip())  # Resultado: "texto com espaços"
    
    # replace() - Substitui parte da string
    print(texto.replace("incrível", "fantástica"))  # Resultado: Python é uma linguagem fantástica
    
    # split() - Divide a string em uma lista usando um separador
    print(texto.split(" "))  # Resultado: ['Python', 'é', 'uma', 'linguagem', 'incrível']
    
    # find() - Encontra a posição da primeira ocorrência de uma substring (-1 se não encontrar)
    print(texto.find("linguagem"))  # Resultado: 14
    
    # join() - Une elementos de uma lista em uma string
    palavras = ["Python", "é", "incrível"]
    print(" ".join(palavras))  # Resultado: Python é incrível
    
    # format() - Formata strings com placeholders
    nome = "Maria"
    idade = 30
    print("Nome: {}, Idade: {}".format(nome, idade))  # Resultado: Nome: Maria, Idade: 30
    
    # f-strings (Python 3.6+) - Método moderno de formatação
    print(f"Nome: {nome}, Idade: {idade}")  # Resultado: Nome: Maria, Idade: 30


# ==========================================================================
# FUNÇÕES PARA LISTAS, TUPLAS E DICIONÁRIOS
# ==========================================================================

def demonstrar_listas():
    """Demonstra funções relacionadas a listas"""
    numeros = [5, 2, 8, 1, 9]
    
    # append() - Adiciona um elemento ao fim da lista
    numeros.append(6)
    print(numeros)  # Resultado: [5, 2, 8, 1, 9, 6]
    
    # insert() - Insere um elemento em uma posição específica
    numeros.insert(0, 10)  # Insere 10 no início da lista
    print(numeros)  # Resultado: [10, 5, 2, 8, 1, 9, 6]
    
    # remove() - Remove a primeira ocorrência de um valor
    numeros.remove(8)
    print(numeros)  # Resultado: [10, 5, 2, 1, 9, 6]
    
    # pop() - Remove e retorna o elemento de um índice (último por padrão)
    removido = numeros.pop(1)  # Remove o segundo elemento (índice 1)
    print(f"Removido: {removido}, Lista: {numeros}")  # Removido: 5, Lista: [10, 2, 1, 9, 6]
    
    # sort() - Ordena a lista in-place
    numeros.sort()
    print(numeros)  # Resultado: [1, 2, 6, 9, 10]
    
    # reverse() - Inverte a ordem dos elementos
    numeros.reverse()
    print(numeros)  # Resultado: [10, 9, 6, 2, 1]
    
    # count() - Conta quantas vezes um elemento aparece
    print(numeros.count(9))  # Resultado: 1
    
    # index() - Retorna o índice da primeira ocorrência de um valor
    print(numeros.index(6))  # Resultado: 2
    
    # extend() - Estende a lista com outra sequência
    numeros.extend([20, 30])
    print(numeros)  # Resultado: [10, 9, 6, 2, 1, 20, 30]


def demonstrar_tuplas():
    """Demonstra operações com tuplas (imutáveis)"""
    # Tuplas são imutáveis, então têm menos métodos que listas
    tupla = (1, 2, 3, 4, 5, 5)
    
    # count() - Conta ocorrências de um elemento
    print(tupla.count(5))  # Resultado: 2
    
    # index() - Retorna índice da primeira ocorrência
    print(tupla.index(3))  # Resultado: 2
    
    # Desempacotamento de tupla
    a, b, *resto = tupla
    print(f"a = {a}, b = {b}, resto = {resto}")  # a = 1, b = 2, resto = [3, 4, 5, 5]


def demonstrar_dicionarios():
    """Demonstra operações com dicionários"""
    pessoa = {
        "nome": "João", 
        "idade": 25, 
        "cidade": "São Paulo"
    }
    
    # keys() - Retorna um objeto view com as chaves do dicionário
    print(list(pessoa.keys()))  # Resultado: ['nome', 'idade', 'cidade']
    
    # values() - Retorna um objeto view com os valores do dicionário
    print(list(pessoa.values()))  # Resultado: ['João', 25, 'São Paulo']
    
    # items() - Retorna um objeto view com pares (chave, valor)
    print(list(pessoa.items()))  # Resultado: [('nome', 'João'), ('idade', 25), ('cidade', 'São Paulo')]
    
    # get() - Retorna o valor de uma chave, com valor padrão opcional
    print(pessoa.get("profissão", "Não informada"))  # Resultado: Não informada
    
    # update() - Atualiza o dicionário com outro dicionário ou pares chave-valor
    pessoa.update({"profissão": "Desenvolvedor", "idade": 26})
    print(pessoa)  # Adiciona 'profissão' e atualiza 'idade'
    
    # pop() - Remove e retorna o valor de uma chave
    idade = pessoa.pop("idade")
    print(f"Idade removida: {idade}, Dicionário: {pessoa}")
    
    # setdefault() - Retorna valor de uma chave, inserindo-a se não existir
    hobby = pessoa.setdefault("hobby", "Programação")
    print(f"Hobby: {hobby}, Dicionário: {pessoa}")
    
    # clear() - Remove todos os elementos
    pessoa.clear()
    print(pessoa)  # Resultado: {}


# ==========================================================================
# FUNÇÕES MATEMÁTICAS E NUMÉRICAS
# ==========================================================================

def demonstrar_funcoes_matematicas():
    """Demonstra funções matemáticas internas"""
    numeros = [15, 6, 89, 2, 45, 37]
    
    # abs() - Valor absoluto
    print(abs(-10))  # Resultado: 10
    
    # max() - Maior elemento
    print(max(numeros))  # Resultado: 89
    
    # min() - Menor elemento
    print(min(numeros))  # Resultado: 2
    
    # sum() - Soma os elementos
    print(sum(numeros))  # Resultado: 194
    
    # round() - Arredonda um número
    print(round(3.75))  # Resultado: 4
    print(round(3.75, 1))  # Resultado: 3.8 (arredonda para 1 casa decimal)
    
    # pow() - Potência
    print(pow(2, 3))  # Resultado: 8 (2³)
    
    # Importando funções matemáticas mais avançadas do módulo math
    import math
    
    # math.floor() - Arredonda para baixo
    print(math.floor(4.9))  # Resultado: 4
    
    # math.ceil() - Arredonda para cima
    print(math.ceil(4.1))  # Resultado: 5
    
    # math.sqrt() - Raiz quadrada
    print(math.sqrt(16))  # Resultado: 4.0
    
    # math.factorial() - Fatorial
    print(math.factorial(5))  # Resultado: 120 (5!)
    
    # math.gcd() - Máximo divisor comum
    print(math.gcd(12, 18))  # Resultado: 6


# ==========================================================================
# FUNÇÕES DE CONVERSÃO DE TIPOS
# ==========================================================================

def demonstrar_conversoes():
    """Demonstra funções para conversão de tipos de dados"""
    # int() - Converte para inteiro
    print(int("123"))  # Resultado: 123
    print(int(12.8))  # Resultado: 12 (trunca a parte decimal)
    
    # float() - Converte para ponto flutuante
    print(float("12.5"))  # Resultado: 12.5
    print(float(5))  # Resultado: 5.0
    
    # str() - Converte para string
    print(str(123))  # Resultado: "123"
    print(type(str(123)))  # <class 'str'>
    
    # bool() - Converte para booleano (False: 0, "", None, [], {}, set())
    print(bool(0))  # Resultado: False
    print(bool(1))  # Resultado: True
    print(bool(""))  # Resultado: False
    print(bool("Python"))  # Resultado: True
    
    # list() - Converte para lista
    print(list("Python"))  # Resultado: ['P', 'y', 't', 'h', 'o', 'n']
    print(list((1, 2, 3)))  # Resultado: [1, 2, 3]
    
    # tuple() - Converte para tupla
    print(tuple([1, 2, 3]))  # Resultado: (1, 2, 3)
    
    # set() - Converte para conjunto (remove duplicatas)
    print(set([1, 2, 2, 3, 3, 3]))  # Resultado: {1, 2, 3}
    
    # dict() - Converte para dicionário
    print(dict([("nome", "Ana"), ("idade", 25)]))  # Resultado: {'nome': 'Ana', 'idade': 25}


# ==========================================================================
# FUNÇÕES DE ORDEM SUPERIOR E PROGRAMAÇÃO FUNCIONAL
# ==========================================================================

def demonstrar_programacao_funcional():
    """Demonstra funções de ordem superior e programação funcional"""
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # map() - Aplica uma função a cada elemento da sequência
    quadrados = list(map(lambda x: x**2, numeros))
    print(quadrados)  # Resultado: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
    # filter() - Filtra elementos que satisfazem uma condição
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(pares)  # Resultado: [2, 4, 6, 8, 10]
    
    # reduce() - Reduz uma sequência a um único valor
    from functools import reduce
    soma = reduce(lambda x, y: x + y, numeros)
    print(soma)  # Resultado: 55 (soma de 1 a 10)
    
    # sorted() - Ordena uma sequência
    palavras = ["banana", "maçã", "laranja", "uva"]
    ordenadas = sorted(palavras)
    print(ordenadas)  # Resultado: ['banana', 'laranja', 'maçã', 'uva']
    
    # Ordenação personalizada (por tamanho)
    ordenadas_tamanho = sorted(palavras, key=len)
    print(ordenadas_tamanho)  # Resultado: ['uva', 'maçã', 'banana', 'laranja']
    
    # any() - Retorna True se pelo menos um elemento for verdadeiro
    print(any([False, False, True, False]))  # Resultado: True
    
    # all() - Retorna True se todos os elementos forem verdadeiros
    print(all([True, True, False]))  # Resultado: False
    
    # zip() - Combina sequências em tuplas
    nomes = ["Ana", "Carlos", "Maria"]
    idades = [25, 30, 22]
    combinados = list(zip(nomes, idades))
    print(combinados)  # Resultado: [('Ana', 25), ('Carlos', 30), ('Maria', 22)]
    
    # enumerate() - Adiciona contadores a uma sequência
    for i, nome in enumerate(nomes):
        print(f"{i}: {nome}")  # Saída: 0: Ana, 1: Carlos, 2: Maria


# ==========================================================================
# FUNÇÕES PARA INPUT/OUTPUT
# ==========================================================================

def demonstrar_io():
    """Demonstra funções para entrada e saída"""
    # print() - Imprime na saída padrão
    print("Olá, Mundo!")
    print("Múltiplos", "argumentos", "são", "separados", "por", "espaços")
    print("Usando", "separador", "personalizado", sep="---")
    print("Sem quebra de linha", end=" ")
    print("na mesma linha")
    
    # Saída formatada
    print(f"Formatação com f-strings: {10 * 5}")
    
    # input() - Lê entrada do usuário
    # nome = input("Digite seu nome: ")
    # print(f"Olá, {nome}!")
    
    # Trabalhando com arquivos
    print("\nEscrevendo em arquivo:")
    with open("exemplo.txt", "w") as arquivo:
        arquivo.write("Linha 1\n")
        arquivo.write("Linha 2\n")
    
    print("Lendo arquivo:")
    with open("exemplo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
    
    # Lendo linha por linha
    print("Lendo linha por linha:")
    with open("exemplo.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())  # strip() remove \n no final


# ==========================================================================
# FUNÇÕES PARA CLASSES E OBJETOS
# ==========================================================================

def demonstrar_funcoes_classe_objeto():
    """Demonstra funções para trabalhar com classes e objetos"""
    # type() - Retorna o tipo de um objeto
    print(type(10))  # <class 'int'>
    print(type("texto"))  # <class 'str'>
    
    # isinstance() - Verifica se um objeto é instância de uma classe
    print(isinstance(10, int))  # True
    print(isinstance("texto", list))  # False
    
    # issubclass() - Verifica se uma classe é subclasse de outra
    print(issubclass(bool, int))  # True (bool é subclasse de int)
    
    # getattr() - Obtém um atributo de um objeto
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
    
    pessoa = Pessoa("João", 30)
    print(getattr(pessoa, "nome"))  # João
    
    # hasattr() - Verifica se um objeto tem um atributo
    print(hasattr(pessoa, "nome"))  # True
    print(hasattr(pessoa, "profissao"))  # False
    
    # setattr() - Define um atributo em um objeto
    setattr(pessoa, "profissao", "Programador")
    print(pessoa.profissao)  # Programador
    
    # delattr() - Remove um atributo de um objeto
    delattr(pessoa, "profissao")
    print(hasattr(pessoa, "profissao"))  # False


# ==========================================================================
# FUNÇÕES PARA DATA E HORA
# ==========================================================================

def demonstrar_data_hora():
    """Demonstra funções para manipulação de data e hora"""
    import datetime
    
    # Obtendo data e hora atual
    agora = datetime.datetime.now()
    print(f"Data e hora atual: {agora}")
    
    # Criando um objeto de data
    data = datetime.date(2023, 5, 15)
    print(f"Data: {data}")
    
    # Criando um objeto de hora
    hora = datetime.time(14, 30, 15)
    print(f"Hora: {hora}")
    
    # Formatando datas
    print(agora.strftime("%d/%m/%Y %H:%M:%S"))  # Formato brasileiro
    print(agora.strftime("%Y-%m-%d %H:%M:%S"))  # Formato ISO
    
    # Operações com datas
    amanha = datetime.date.today() + datetime.timedelta(days=1)
    print(f"Amanhã: {amanha}")
    
    # Diferença entre datas
    diferenca = amanha - datetime.date.today()
    print(f"Diferença: {diferenca.days} dias")


# ==========================================================================
# FUNÇÕES PARA SISTEMAS E ARQUIVOS
# ==========================================================================

def demonstrar_sistema_arquivos():
    """Demonstra funções para operações com sistema e arquivos"""
    import os
    import shutil
    
    # Obtendo diretório atual
    print(f"Diretório atual: {os.getcwd()}")
    
    # Listando arquivos e diretórios
    print(f"Conteúdo do diretório: {os.listdir('.')}")
    
    # Criando um diretório
    if not os.path.exists("teste_dir"):
        os.mkdir("teste_dir")
        print("Diretório criado")
    
    # Verificando se um caminho existe
    print(f"'teste_dir' existe? {os.path.exists('teste_dir')}")
    
    # Verificando se é um arquivo ou diretório
    print(f"'teste_dir' é diretório? {os.path.isdir('teste_dir')}")
    print(f"'exemplo.txt' é arquivo? {os.path.isfile('exemplo.txt')}")
    
    # Renomeando um arquivo ou diretório
    if os.path.exists("exemplo.txt"):
        os.rename("exemplo.txt", "exemplo_renomeado.txt")
        print("Arquivo renomeado")
    
    # Copiando arquivo
    if os.path.exists("exemplo_renomeado.txt"):
        shutil.copy("exemplo_renomeado.txt", "exemplo_copia.txt")
        print("Arquivo copiado")
    
    # Removendo arquivo
    if os.path.exists("exemplo_copia.txt"):
        os.remove("exemplo_copia.txt")
        print("Arquivo removido")
    
    # Removendo diretório
    if os.path.exists("teste_dir"):
        os.rmdir("teste_dir")
        print("Diretório removido")


# ==========================================================================
# FUNÇÃO PRINCIPAL PARA EXECUTAR TODAS AS DEMONSTRAÇÕES
# ==========================================================================

def main():
    """Função principal que executa todas as demonstrações"""
    print("\n===== DEMONSTRAÇÃO DE STRINGS =====")
    demonstrar_strings()
    
    print("\n===== DEMONSTRAÇÃO DE LISTAS =====")
    demonstrar_listas()
    
    print("\n===== DEMONSTRAÇÃO DE TUPLAS =====")
    demonstrar_tuplas()
    
    print("\n===== DEMONSTRAÇÃO DE DICIONÁRIOS =====")
    demonstrar_dicionarios()
    
    print("\n===== DEMONSTRAÇÃO DE FUNÇÕES MATEMÁTICAS =====")
    demonstrar_funcoes_matematicas()
    
    print("\n===== DEMONSTRAÇÃO DE CONVERSÕES DE TIPOS =====")
    demonstrar_conversoes()
    
    print("\n===== DEMONSTRAÇÃO DE PROGRAMAÇÃO FUNCIONAL =====")
    demonstrar_programacao_funcional()
    
    print("\n===== DEMONSTRAÇÃO DE INPUT/OUTPUT =====")
    demonstrar_io()
    
    print("\n===== DEMONSTRAÇÃO DE CLASSES E OBJETOS =====")
    demonstrar_funcoes_classe_objeto()
    
    print("\n===== DEMONSTRAÇÃO DE DATA E HORA =====")
    demonstrar_data_hora()
    
    print("\n===== DEMONSTRAÇÃO DE SISTEMA E ARQUIVOS =====")
    demonstrar_sistema_arquivos()


if __name__ == "__main__":
    main()