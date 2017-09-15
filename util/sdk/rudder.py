#!/usr/bin/python
# -*- coding: utf-8 -*-
from requests import HTTPError

__author__ = 'xiwei'

import requests


class RudderError(Exception):
    def __init__(self, message):
        self.message = message


class Rudder(object):
    def __init__(self, host):
        self._host = host

    def _request(self, path, api, args=None):
        uri = f'{self._host}/{path}'
        res = requests.post(
            uri, data={"sijax_rq": api, "sijax_args": args}
        )

        if res.status_code != 200:
            raise HTTPError(res.status_code, res.text)

        try:
            response = res.json()[0]
        except ValueError:
            pass
        else:
            if response['type'] == 'alert':
                raise RudderError(response['alert'])

    def alert(self):
        return self._request('alert', 'emit', ('name', 'test'))


if __name__ == '__main__':
    print(Rudder('http://localhost:5000').alert())
