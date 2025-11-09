# -*- coding: utf-8 -*-
# импорт модуля работы с БД
import sqlite3


def read(base, table, *select):
    # функция чтения из БД
    con = sqlite3.connect(base)
    cur = con.cursor()
    query = ''
    for x in select:
        query += f"{x}, "
    query = query[: -2]
    result = cur.execute(f"""
        SELECT
            {query}
        FROM
            {table}
    """).fetchall()
    con.close()
    return result


def delete(base, table, id):
    # функция удаления из ДБ по id
    con = sqlite3.connect(base)
    cur = con.cursor()
    cur.execute(f"""
        DELETE
            FROM 
                {table}
        WHERE
            {table}.id = {id}
    """).fetchall()
    con.commit()
    con.close()


def writer(base, table, columns, data):
    # функция записи в бд
    con = sqlite3.connect(base)
    cur = con.cursor()
    cur.execute(f"""
        INSERT INTO
            {table} {columns}
        VALUES
            {data}
    """).fetchall()
    con.commit()
    con.close()
