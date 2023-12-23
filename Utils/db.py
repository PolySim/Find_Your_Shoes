import flask
import mysql.connector
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

HOST = os.getenv('DATABASE_HOST')
NAME = os.getenv('DATABASE_NAME')
USER = os.getenv('DATABASE_USER')
PASSWORD = os.getenv('DATABASE_PASSWORD')


class Request(BaseModel):
    trail: int
    size: int
    weight: int
    level: int
    length: int
    usefulness: int
    result: int


def get_shoes():
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=NAME
    )

    cursor = mydb.cursor()
    sql_request = """SELECT 
    trail_id, 
    size, 
    weight,
    level_id, 
    length, 
    usefulness_id, 
    result
    FROM request"""
    cursor.execute(sql_request)

    result = cursor.fetchall()

    result_json = {
        "request": [],
        "results": []
    }

    for i in range(len(result)):
        result_json["request"].append((
            result[i][0],
            result[i][1],
            result[i][2],
            result[i][3],
            result[i][4],
            result[i][5]
        ))
        result_json["results"].append(result[i][6])

    return result_json
