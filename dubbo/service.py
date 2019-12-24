#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 17:17
# @Author  : hu
import json
from dubbo.connector import Invoker
import dubbo.config as config

class Dubbo(object):
    """
        Manage dubbo service.
    """

    SEPRATOR = '\r\n'
    PROVIDER = 'PROVIDER:'
    PRMPOT = "dubbo>"

    def __init__(self, server_ip=config.SERVER_IP, server_port=config.SERVER_PORT):
        self._invoker = Invoker(server_ip, server_port)

    def list_service(self, interface_name=''):
        """
            command: ls -l interface.
        :param interface_name: i
        :return: active servcies or None if no service avaliable
        """
        command = 'ls -l {}'.format(interface_name)
        resp = self._invoker.invoke(command)
        try:
            resp = resp.strip(Dubbo.PROVIDER+Dubbo.PRMPOT).strip()
            return resp.split('->')[0]
        except:
            return resp

    def invoke_service(self, interface_name, method, **kargs):
        """
            command: invoke com.xx.yy.interface.method(args)
            invoke service.
        :param interface_name:
        :param method:
        :param kargs:
        :return: result of service.
        """
        arg_list = [json.dumps(value) for value in kargs.values()]
        args = ','.join(arg_list)
        command = 'invoke {interface}.{method}({args})'.format(interface=interface_name, method=method, args=args)
        resp = self._invoker.invoke(command)
        data = resp.split(Dubbo.SEPRATOR)[0]

        try:
            return json.loads(data)
        except:
            return data

