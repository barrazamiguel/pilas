#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright 2017 - Miguel Barraza
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

from accessible_output import speech

Speaker = speech.Speaker()

def leer(texto, interrumpir=True):
    Speaker.output(texto, interrupt=interrumpir)
