import psycopg2 as psycopg2
import pandas as pd
import random


def connection():
    conn = psycopg2.connect(
        host="localhost",
        database="DotaScope",
        user="postgres",
        password="kir54678199"
    )
    return conn


query_user = """
    CREATE TABLE IF NOT EXISTS users(
        id_user SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        password varchar(30) NOT NULL,
        games INTEGER CHECK (games >= 0),
        score_sum INTEGER CHECK (score_sum >= 0)
    );
    """

query_players_in_team = """
    CREATE TABLE IF NOT EXISTS invoker_game(
      id_game SERIAL PRIMARY KEY,
      id_user INTEGER,
      score INTEGER CHECK (score >= 0),
      FOREIGN KEY(id_user) REFERENCES users(id_user)
    );
    """


def create_bd():
    conn = connection()
    cursor = conn.cursor()
    queries = [query_user, query_players_in_team]
    for func in queries:
        cursor.execute(func)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_bd()
