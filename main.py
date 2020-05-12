import json

import mysql.connector
from fastapi import FastAPI
from pydantic import BaseModel


def genConntent(host, port, user, password, database):
    return mysql.connector.connect(user='root', password='mysql',
                                   host='10.65.193.30',
                                   database='')


def dbQuery(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    rows = cursor.fetchall()
    json_data = []
    for result in rows:
        json_data.append(dict(zip(row_headers, result)))
    cursor.close
    return json.dumps(json_data)


def queryResult(q):
    con = genConntent(q.host, q.port, q.user, q.password, q.database)
    rs_json = dbQuery(con, q.text)
    con.close()
    return rs_json


class Query(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str
    sqltext: str


app = FastAPI()


@app.post("/query")
def mysql_query(query: Query):
    return queryResult(query)
