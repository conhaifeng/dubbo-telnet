#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 15:45
# @Author  : hu

import telnetlib
import time


class Invoker(object):
    """
        Telnet to dubbo server, just manage the connection
    """

    PROMPT = b'dubbo>'
    NEXT = b'\n'
    ENCODING = 'utf-8'

    def __init__(self, ip, port, keep_alive=False):

        #: Connect to the server.
        self._connector = telnetlib.Telnet(ip, port)
        self._connector.write(Invoker.NEXT)

        #: Keep the tcp connection alive or not.
        self._keep_alive = keep_alive

    def _command(self, command):
        return command.encode(Invoker.ENCODING) + Invoker.NEXT

    def invoke(self, command):
        try:
            self._connector.write(self._command(command))
            resonse = self._connector.read_until(match=Invoker.PROMPT,timeout=2)
            return resonse.decode(Invoker.ENCODING)
        finally:
            if not self._keep_alive:
                self._connector.close()


