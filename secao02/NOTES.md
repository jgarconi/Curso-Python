## Notas de aula

## Aula 1: Comentários de código em Python

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/comentarios.py)

Anotações:
* Replicar linhas no pycharm: Ctrl + D
* Abrir e fechar comentários com aspas simples ou duplas servem para
  documentação, mas também funcionam como comentários

---------------------------------------------------------------------

## Aula 2 : O comando print

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/comando_print.py)

Anotações:
* sep= : define um separador
* end= : o que vai no final do print (serve para tirar a quebra de linha)

---------------------------------------------------------------------

## Aula 3: Strings e aspas em Python

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/strings_e_aspas.py)

Anotações:
* As strings (str) podem ser escritas entre aspas simples ou duplas
* \  : carácter de escape, lê as aspas como parte da str
* \n : a ação executada dentro da str é uma quebra de linha
* r  : impede que ações sejam executadas dentro da str

---------------------------------------------------------------------

## Aula 4: Tipos de dados "primitivos"

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/tipos_de_dados.py) e
          [Atividade](https://github.com/jgarconi/CursoPython/blob/master/secao02/atividades/tipos_de_dados.py)

Anotações:
* Tipos de dados: 
   + str   : string -> textos
   + int   : inteiro -> números inteiros
   + float : real/ponto flutuante -> números com virgula
   + bool  : booleano/lógico -> true/false

---------------------------------------------------------------------

## Aula 5: Operadores Aritméticos

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/operadores_aritmeticos.py)

Anotações:
* Tipos de operadores: 
   + (+): adição
   + (-): subtração
   + (*): multiplicação
   + (/): divisão com resultado em float
   + (//): divisão com resultado em int
   + (%): divisão em módulo (retorna o resto)
   + (**): exponenciação
   + parêntesis: altera a precedência das operações

* Prioridade nas operações:
   + 1: parêntesis
   + 2: exponenciação
   + 3: multiplicação, divisão float e int, e módulo
   + 4: soma e subtração

* Lista de operadores:
https://docs.python.org/3/reference/expressions.html##operator-precedence

--------------------------------------------------------------------

## Aula 6: Variáveis

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/variaveis.py) e
          [Atividade](https://github.com/jgarconi/CursoPython/blob/master/secao02/atividades/calculadora_imc.py)

Anotações:
* Regras: inicia com letra, pode ter números, separa com _ e é escrito com letras minúsculas

--------------------------------------------------------------------

## Aula 7: Introdução à formatação de str

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/introd_formatacao.py)

Anotações:
* Tipos de formatação estudadas: f-strings, .format
* :.xf : formata o numero com x casas decimais, exemplo: peso = 75.8888 -> peso:.2f = 75.89

--------------------------------------------------------------------

## Aula 8: Desafio pratico

Arquivos: [Atividade](https://github.com/jgarconi/CursoPython/blob/master/secao02/atividades/variaveis_e_formatacao.py)

--------------------------------------------------------------------

## Aula 9: Entrada de dados do usuário

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/funcao_input.py) e
          [Atividade](https://github.com/jgarconi/CursoPython/blob/master/secao02/atividades/calculadora_soma.py)

Anotações:
* Função input(): o dado enviado pelo usuário sempre é interpretado como str

--------------------------------------------------------------------

## Aula 10: if, elif e esle + booleans

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/condicional_booleans.py)

Anotações:
* Uma condição abaixo só é verificada se a condição acima for falsa

--------------------------------------------------------------------

## Aula 11: if, elif e esle + operadores relacionais

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/condicional_relacionais.py)

Anotações:
* O resultados das comparações é um valor booleano
* Tipos de operadores:
   + (==) : igual á
   + (>)  : maior que
   + (>=) : maior ou igual à
   + (<)  : menor que
   + (<=) : menor ou igual à
   + (!=) : diferente de

-------------------------------------------------------------------

## Aula 12: if, elif e esle + operadores lógicos

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/condicional_logicos.py)

Anotações:
* Tipos de operadores: and, or, not, in, not in

-------------------------------------------------------------------

## Aula 13: Quantidade de caracteres

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/funcao_len.py) e 
          [Atividade](https://github.com/jgarconi/CursoPython/blob/master/secao02/atividades/soma_caracteres.py)

Anotações:
* Função len(): funciona com diversos tipos de dados menos com os numéricos
* Sempre retorna números inteiros

-------------------------------------------------------------------

## Aula 14: Documentação e funções built-in úteis

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/builtin_uteis.py)

Anotações:
* Built-in: https://docs.python.org/3/library/stdtypes.html
* Resolve o problema de float não ser considerado número: https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py
* Funções para str: 
   + isnumeric() : checa se os carácteres são números
   + isdigit()   : checa se os carácteres sao digitos

-------------------------------------------------------------------

## Aula 15: Pass e Ellipsis como placeholders

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/placeholders.py)

Anotações:
* Usar pass ou ... tem o mesmo efeito de "segurar" parte do código para uma futura utilização

-------------------------------------------------------------------

## Aula 16: Desafio pratico

Arquivos: [Atividade 1](https://github.com/jgarconi/CursoPython/blob/master/secao02/atividades/identifica_int.py), 
          [Atividade 2](https://github.com/jgarconi/CursoPython/blob/master/secao02/atividades/identifica_hora.py) e 
          [Atividade 3](https://github.com/jgarconi/CursoPython/blob/master/secao02/atividades/identifica_nome.py)

--------------------------------------------------------------------

# Aula 17: Formatando valores em Python

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/formatacao.py)

Anotações:
* Tipos de formatações:
   + (:s): Texto (strings)
   + (:d): Inteiros (int)
   + (:f): Números de ponto flutuante (float)
   
* Direção da formatação:
   + (>): Esquerda
   + (<): Direita
   + (^): Centro
   
* Padrões de formatação: 
   + (:carácter)(direção)(quantidade)
   + (.número)f: x casas decimais (float)
  
--------------------------------------------------------------------

# Aula 18: Índices e fatiamento de str em Python

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/fatiamento_str.py)

Anotações:
* Tipos Built-in: https://docs.python.org/3/library/stdtypes.html
* Funções Built-in: https://docs.python.org/3/library/functions.html

--------------------------------------------------------------------

# Aula 19: While - Estrutura de repetição em Python

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/laco_while.py) e
          [Atividade](https://github.com/jgarconi/CursoPython/blob/master/secao02/atividades/calculadora_simples.py)

Anotações:
* continue: quando a linha que contém esse comando é executada, as linhas 
            posteriores não são executadas, ou seja, pula para o próximo laço.
* break: as linhas posteriores também não são executadas, mas nesse caso,
         o programa não executa mais o laço.
  
--------------------------------------------------------------------

# Aula 20: While/Else - Repetição com acumuladores em Python

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/laco_while_else.py)

--------------------------------------------------------------------

# Aula 21: While - Iteração de str com while em Python

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/laco_while_e_str.py)

--------------------------------------------------------------------

# Aula 22: For in - Estrutura de repetição em Python

Arquivos: [Fundamento](https://github.com/jgarconi/CursoPython/blob/master/secao02/fundamentos/laco_for_in.py)

Anotação:
* while : executa ações sem um fim definido
* for in: executa ações com um fim definido