#!/usr/bin/env python3

import json
import psycopg2
import sys

def query(i):
    sql1 = """
        select model->'result'->'model_name',
               model->'result'->'lora_names',
               created_at, updated_at,
               prompt, result
        from oobabooga.api
        where id = %s;
    """
    with psycopg2.connect() as db1:
        with db1.cursor() as cur1:
            cur1.execute(sql1, [ i ]) 
            for row1 in cur1:
                print("Model: {}".format(row1[0]))
                print("Loras: {}".format(row1[1]))
                print("Created at: {}". format(row1[2]))
                print("Updated at: {}". format(row1[3]))
                print("Prompt: {}". format(row1[4]))
                print("Result: {}". format(row1[5]))

if __name__ == '__main__':
    query(sys.argv[1])
