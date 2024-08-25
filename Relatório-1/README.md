# Introdução ao Python


# Declaração de variáveis

Ao contrário das outras linguagens onde para imprimir qualquer coisa no terminal era necessário ter uma função principal e até mesmo uma classe, no Python basta usar o comando print() e colocar o que se deseja mostrar entre os parênteses:

```python
# Declaração de variáveis
nome = "João"
idade = 30
altura = 1.75
profissao = "Desenvolvedor"

# Impressão das variáveis
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Profissão:", profissao)
```

# Entrada de dados

```python
# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
profissao = input("Digite sua profissão: ")

# Impressão das variáveis
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Profissão:", profissao)
```

## Exemplo IMC

```python
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print("Seu IMC é: ", imc)
```

## Estruturas

A linguagem Python, como mencionado anteriormente não utiliza chaves para definir qual comando está dentro ou fora de uma determinada estrutura, é utilizado a identação do código (organização correta), ela é essencial para que tudo funcione corretamente.
• Estruturas de decisão: Seria o bloco if – else (se - senão) e seus intermediários elif (senão se), equivalente ao else if em C++ e Java.

## if else

```python
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Obesidade grau 1")
elif imc >= 35 and imc < 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")
```

## Listas

As listas em Python são uma das estruturas de dados mais utilizadas, pois permitem armazenar uma coleção de objetos de diferentes tipos em uma única variável. Elas são representadas por colchetes `[]` e podem ser modificadas ao longo do tempo.

Criando uma lista
Para criar uma lista em Python, basta colocar os elementos separados por vírgulas dentro de colchetes.

```python
frutas = ["maçã", "banana", "laranja"]
print(frutas) # Imprime: ['maçã', 'banana', 'laranja']
```

## **Acessando elementos da lista**

Para acessar um elemento de uma lista, basta informar o índice do elemento desejado entre colchetes, lembrando que o índice começa a partir do 0.

Exemplo:

```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[1]) # Imprime: 'banana'

```

## **Adicionando elementos a uma lista**

Para adicionar um elemento a uma lista, pode-se usar o método **`append()`**.

Exemplo:

```python
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")
print(frutas) # Imprime: ['maçã', 'banana', 'laranja', 'uva']

```

## **Removendo elementos de uma lista**

Para remover um elemento de uma lista, pode-se usar o método **`remove()`**.

Exemplo:

```python

frutas = ["maçã", "banana", "laranja"]
frutas.remove("banana")
print(frutas) # Imprime: ['maçã', 'laranja']

```

## **Modificando elementos de uma lista**

Para modificar um elemento de uma lista, basta acessá-lo pelo índice e atribuir um novo valor a ele.

Exemplo:

```python

frutas = ["maçã", "banana", "laranja"]
frutas[1] = "mamão"
print(frutas) # Imprime: ['maçã', 'mamão', 'laranja']

```

Essas são as principais funções que você precisa conhecer para começar a trabalhar com listas em Python.

# **Dicionários**

Os dicionários em Python são estruturas de dados que permitem armazenar pares de chaves e valores, de forma que cada chave mapeia para um valor específico. Eles são representados por chaves **`{}`** e são úteis quando precisamos armazenar informações não numéricas, como por exemplo nomes e idades.

## **Criando um dicionário**

Para criar um dicionário em Python, basta colocar os pares de chaves e valores separados por dois pontos **`:`** dentro de chaves.

```python
pessoas = {'João': 25, 'Maria': 22, 'Pedro': 30}
print(pessoas) # Imprime: {'João': 25, 'Maria': 22, 'Pedro': 30}

```

## **Acessando elementos do dicionário**

Para acessar um elemento de um dicionário, basta informar a chave desejada entre colchetes.

```python

pessoas = {'João': 25, 'Maria': 22, 'Pedro': 30}
print(pessoas['João']) # Imprime: 25

```

## **Adicionando elementos a um dicionário**

Para adicionar um elemento a um dicionário, basta atribuir um novo valor a uma chave não existente.

```python

pessoas = {'João': 25, 'Maria': 22, 'Pedro': 30}
pessoas['Ana'] = 28
print(pessoas) # Imprime: {'João': 25, 'Maria': 22, 'Pedro': 30, 'Ana': 28}

```

## **Removendo elementos de um dicionário**

Para remover um elemento de um dicionário, pode-se usar o método **`pop()`**.

```python

pessoas = {'João': 25, 'Maria': 22, 'Pedro': 30}
pessoas.pop('João')
print(pessoas) # Imprime: {'Maria': 22, 'Pedro': 30}

```

## **Modificando elementos de um dicionário**

Para modificar um elemento de um dicionário, basta acessá-lo pelo a chave e atribuir um novo valor.

```python

pessoas = {'João': 25, 'Maria': 22, 'Pedro': 30}
pessoas['João'] = 28
print(pessoas) # Imprime: {'João': 28, 'Maria': 22, 'Pedro': 30}

```

# **Orientação a Objetos em Python**

A orientação a objetos é um paradigma de programação que se baseia em representar conceitos do mundo real como objetos em um programa de computador. Em Python, objetos são instâncias de classes, que são definições de tipos de objetos.

## **Criando uma classe**

Para criar uma classe em Python, utiliza-se a palavra-chave **`class`**.

```python

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

```

O método **`__init__`** é um método especial chamado de construtor, que é responsável por inicializar as variáveis de instância de uma classe.

## **Criando objetos**

Para criar objetos de uma classe, basta chamar a classe como se fosse uma função.

```python
joão = Pessoa('João', 25)
maria = Pessoa('Maria', 22)

```

## **Acessando variáveis de instância**

Para acessar as variáveis de instância de um objeto, basta usar o ponto **`.`**.

```python
joão = Pessoa('João', 25)
print(joão.nome) # Imprime: 'João'
print(joão.idade) # Imprime: 25

```

## **Métodos de classe**

Além de variáveis de instância, as classes podem ter métodos, que são funções que pertencem a uma classe.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f'Olá, meu nome é {self.nome}!')

joão = Pessoa('João', 25)
joão.cumprimentar() # Imprime: Olá, meu nome é João!

```

A orientação a objetos permite a criação de programas mais organizados e reutilizáveis, já que é possível criar classes que representem conceitos comuns e instanciá-las sempre que precisarmos.