"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Seu nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba: "Desculpe, você deixou um ou mais campos vazios."
"""

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print(f'Seu nome tem {nome.count(" ")} espaços')
    else:
        print("Seu nome não contém espaços")
    print(f"Seu nome contém {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0:1]}")
    print(f"A ultima letra do seu nome é {nome[-1:]}")
else:
    print("Desculpe, você deixou um ou mais campos vazios.")
