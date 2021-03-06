# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
sys.path.append("..")

import os
import string
import json
import requests
from tsuru.utils import login_required, readkey
from tsuru.configs import KEY_FN

class EnvManager(object):

    def __init__(self, target, dbn):
        self.target = target
        self.dbn = dbn  # must set it, login_required will use it

    def _guessAppName(self):
        return None

    @login_required
    def get(self, app, *vars):
        response = requests.get(
            "{0}/apps/{1}/env".format(self.target, app),
            data=string.join(vars, " "),
            headers = self.auhd # must use login_required
        )
        if response.ok:
            print(response.content)
            #print("Key successfully removed!")
        else:
            print("Get env failed!\nReason: %s" % response.content)
        return response.content

    @login_required
    def unset(self, app, *vars):
        '''Unset environment variables for an app.
        '''
        response = requests.delete(
            "{0}/apps/{1}/env".format(self.target, app),
            data=string.join(vars, " "),
            headers = self.auhd # must use login_required
        )
        if response.ok:
            print("Unset environment variables successfully!")
        else:
            print("Unset environment failed!\nReason: %s" % response.content)
        return response.content

    @login_required
    def set(self, app, *vars): 
        '''set environment variables for an app.
        '''
        # vars is a name-value pair tuple
        response = requests.post(
            "{0}/apps/{1}/env".format(self.target, app),
            data=string.join(vars, " "),
            headers = self.auhd # must use login_required
        )        
        if response.ok:
            print("Set environment variables successfully!")
        else:
            print("Set environment failed!\nReason: %s" % response.content)
        return response.content
