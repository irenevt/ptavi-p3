#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.datos = cHandler.guardadoEtiquetas()

    def __str__(self):
        pass
        linea = ""
        for elemento in listaEtiquetas:
            linea = linea + elemento[0]
            atributos = elemento[1].valor()
            for clave, valor in atributos:
                linea = linea + '\t' + clave + ' = ' + '"' + valor + '"'
            linea = linea + '\n'
        print(linea)

    def to_json(self, ficheroSmil, new=''):
        if new == '':
            new = ficheroSmil.split('.')[0] + '.json'
        with open(new, 'w') as ficheroJson:
            json.dump(self.datos, ficheroJson, sort_keys=True,
                      indent=4, separators=(' ', ': '))

    def do_local(self):
        for elemento in listaEtiquetas:
            atributos = elemento[1]
            try:
                url = atributos['src']
                if url != "cancion.ogg":
                    nombreArchivo = url[url.rfind("/") + 1:]
                    data = urllib.request.urlretrieve(url, nombreArchivo)
                    atributos['src'] = "http://" + data[0]
            except KeyError as e:
                pass


def abrirFichero():
    try:
        fichero = sys.argv[1]
        return fichero
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    except FileNotFoundError:
        sys.exit("Not file with this name")


if __name__ == '__main__':
    fichero = abrirFichero()
    karaoke = KaraokeLocal(fichero)
    karaoke.to_json(fichero)
    karaoke.do_local()
    karaoke.to_json(fichero, 'local.json')
    print(karaoke)
