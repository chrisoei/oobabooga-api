#!/usr/bin/env python3

import json
import os
import psycopg2
import requests

def run(cur1, prompt):
    print(f"PROMPT={prompt}")
    uri0 = os.getenv("OOBABOOGA_BASE_URI")
    print(f"OOBABOOGA_BASE_URI={uri0}")
    uri1 = f'{uri0}/api/v1/model'
    uri2 = f'{uri0}/api/v1/generate'

    response1 = requests.post(uri1, json={"action":"info"})
    assert response1.status_code == 200, "Status code = {}".format(response1.status_code)
    r1j = response1.json()
    print(f'MODEL_NAME={r1j["result"]["model_name"]}')
    with open(os.getenv("OOBABOOGA_REQUEST_FILE"), "r") as fh1:
        j2a = fh1.read()
    request2 = json.loads(j2a)
    request2["prompt"] = prompt

    response2 = requests.post(uri2, json=request2)
    assert response2.status_code == 200, "Status code = {}".format(response2.status_code)
    r2j = response2.json() 
    result = r2j['results'][0]['text']
   
    print(f"RESULT={result}")
    sql1 = """
        insert into oobabooga.api (prompt, result, model, params, response)
        values (%s, %s, %s, %s, %s) returning id;
    """
    cur1.execute(sql1, [
        prompt,
        result,
        json.dumps(r1j),
        j2a,
        json.dumps(r2j)
    ]) 
    print(f"ID={cur1.fetchone()[0]}")


if __name__ == '__main__':
    with open(os.getenv("OOBABOOGA_PROMPT_FILE"), "r") as fh2:
        prompt = fh2.read().strip()
    with psycopg2.connect("postgresql://") as db1:
        with db1.cursor() as cur1:
            run(cur1, prompt)

# vim: set et ff=unix ft=python nocp sts=4 sw=4 ts=4:
