#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


def abrirFichero():
    try:
        fichero = open(sys.argv[1], 'r')
        return fichero
    except IndexError:
        sys.exit("Usar: python3 karaoke.py archivo.smil")
  

def obtenerFichero(fichero):
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(fichero)
    list = cHandler.guardadoEtiquetas()
    return listaEtiquetas


def imprimirEtiquetas(listaEtiquetas):
    pass
    linea = ""
    for elemento in listaEtiquetas:
        linea = linea + elemento[0]
        atributos = elemento[1].valor()
        for clave, valor in atributos:
            linea = linea + '\t' + clave + ' = ' + '"' + valor + '"'
        linea = linea + '\n'
    print (linea)
   
if __name__ == '__main__':
    fichero = abrirFichero()
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(fichero)
    print(cHandler.guardadoEtiquetas())
