import mysql.connector
from fastapi import FastAPI
from pydantic import BaseModel
from typing import  Union,Optional,List



def dbQuery(host, port, user, password, database, sqltext, args):
    print(host, port, user, password, database, sqltext, args)
    con = mysql.connector.connect(user=user, password=password, host=host,port=port, database=database)
    cur = con.cursor()
    cur.execute(sqltext, tuple(args))
    row_headers = [x[0] for x in cur.description]
    rows = cur.fetchall()
    json_data = []
    for result in rows:
        json_data.append(dict(zip(row_headers, result)))
    cur.close
    con.close()
    return json_data




class QueryModel(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str
    sqltext: str
    args: Optional[List[Union[float,str]]]


app = FastAPI()

def test(host):
    print(host)

@app.post("/query")
def mysql_query(query: QueryModel):
    try:
        query_rs =dbQuery(**query.__dict__)
        return {"error":0,"result":query_rs}
    except  BaseException as e:
        return {"error":1,"result":e}



