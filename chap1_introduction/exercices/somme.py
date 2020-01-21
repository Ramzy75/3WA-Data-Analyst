

from argparse import ArgumentParser
parser = ArgumentParser()
print(parser)
parser.add_argument(dest="nombre_1", type=int, help="Premier nombre ")
parser.add_argument(dest="nombre_2", type=int, help="Deuxieme nombre ")
parser.add_argument(dest="nombre_3", type=int, help="Troisieme nombre ")
input_args = parser.parse_args()
print(input_args)

nombre_1 = input_args.nombre_1
nombre_2 = input_args.nombre_2
nombre_3 = input_args.nombre_3


resultat = nombre_1 + nombre_2 + nombre_3

if not (bool (resultat)) :
    print ("le nombre", nombre_1,"est divisible par", nombre_2)
else :
    print ("le nombre", nombre_1,"n'est pas divisible par", nombre_2)
# importe tout le module si besoin de tout
# import argparse


# initilisation de l analyseur syntaxique




