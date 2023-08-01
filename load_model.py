#!/usr/bin/env python3

import json
import os
import requests
import sys

def load_model(m):
    uri0 = os.getenv("OOBABOOGA_BASE_URI")
    uri1 = f'{uri0}/api/v1/model'

    response1 = requests.post(uri1, json = {
        "action":"load",
        "model_name": m
    })
    print(response1)

if __name__ == '__main__':
    load_model(sys.argv[1])

# vim: set et ff=unix ft=python nocp sts=4 sw=4 ts=4:
