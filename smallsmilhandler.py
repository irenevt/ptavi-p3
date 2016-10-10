#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.listaEtiquetas = []
        self.dicionarioEtiquetas = {'root-layout': ['width', 'height', 'background-color'], 'region': ['id', 'top', 'bottom', 'left', 'right'], 'img': ['src', 'region', 'begin', 'dur'], 'audio': ['src', 'begin', 'dur'], 'textstream': ['src', 'region']}

    def startElement(self, clave, atributos):

        if clave in self.dicionarioEtiquetas:
            dicionarioAlmacenado = {}

            for valor in self.dicionarioEtiquetas[clave]:
                dicionarioAlmacenado[valor] = atributos.get(valor, "")

            dicValor = {valor: dicionarioAlmacenado}
            self.listaEtiquetas.append(dicValor)

    def guardadoEtiquetas(self):

        return self.listaEtiquetas

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.guardadoEtiquetas())
