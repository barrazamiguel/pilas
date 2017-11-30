# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
from pilasengine.escenas.escena import Escena
import pyperclip as clipboard

class Error(Escena):
    """Representa la escena de errores de pilas.

    Esta escena muestra el tipo de error en la pantalla,
    junto con una descripción y el archivo que ocasionó
    el error.
    """

    def iniciar(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fondo = self.pilas.fondos.Plano()
        self.actor_error = self.pilas.actores.MensajeError(self.titulo,
                                                           self.descripcion)
        self.pilas.leer("error: {}. {}".format(titulo, descripcion))
        clipboard.copy("{}\n\n{}".format(titulo, descripcion))
        self.enfocarTexto = True
        self.pilas.eventos.pulsa_tecla.conectar(self.interpretaTeclado)

    def interpretaTeclado(self, evento):
        if evento.codigo == self.pilas.simbolos.ABAJO:
            self.leerTexto()
        elif evento.codigo == self.pilas.simbolos.ARRIBA:
            self.leerTexto()

    def leerTexto(self):
        if self.enfocarTexto:
            self.enfocarTexto = False
            self.pilas.leer(self.actor_error.titulo_error)
        else:
            self.enfocarTexto = True
            self.pilas.leer(self.actor_error.descripcion_error)

    def actualizar(self):
        pass

    def terminar(self):
        pass
