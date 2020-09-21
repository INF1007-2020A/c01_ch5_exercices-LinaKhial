#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import itertools


def convert_to_absolute(valeur : float) -> float:
    return abs(valeur)


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    names = list()
    prefixes = itertools.cycle("JKLMNOP")
    for i in range(len("JKLMNOP")): 
        names.append(next(prefixes) + suffixes)
    return names

#une methode que j'ai rajouter pour verifier si un entier est premier ou non
def entier_premier(value : int) -> bool :
    is_premier = None
    cpt = 0
    for i in range(2, (value // 2) + 1 ) :
        if (value % i == 0) : 
            cpt += 1 
    if cpt == 0 :
        is_premier = True
    else :
        is_premier = False
    return is_premier
#end of function

def prime_integer_summation() -> int:
    number , somme , cpt = 1, 0, 0
    while cpt <= 100 :
        number += 1
        if entier_premier(number) :
            somme += number
            cpt += 1
    return somme


def factorial(number: int) -> int:
    facto = 0
    for i in range(1,number) :
        facto = number * i
        number = facto 
    return facto


def use_continue() -> None:
    for i in range(1,10) :
        if i == 5 :
            continue
        print("i :", i)


def main() -> None:
    #my add-in
    value = input("Donner un nombre.")
    value = float(int(value))
    #end of add-in
    print(f"La valeur absolue du nombre est {convert_to_absolute(value)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
