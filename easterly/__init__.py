#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jared Roberts'
__email__ = 'jr595@drexel.edu'
__version__ = '0.1.0'

## Because you haven't split this up into classes, this is a small hack.
## This is so you can do "from easterly import bla" when using the actual package
from easterly import WebSocketServer, ServerEvent, ServerProtocol, WebSocket
