import aioodbc
import asyncio
import logging
from dotenv import load_dotenv
import os

load_dotenv('./env.secret')

async def connect_to_mssqlserver():
    MSSQLSERVER_DRIVER = os.environ.get('MSSQLSERVER_DRIVER')
    MSSQLSERVER_SERVER = os.environ.get('MSSQLSERVER_SERVER')
    MSSQLSERVER_DATABASE = os.environ.get('MSSQLSERVER_DATABASE')
    MSSQLSERVER_UID = os.environ.get('MSSQLSERVER_UID')
    MSSQLSERVER_PWD = os.environ.get('MSSQLSERVER_PWD')
    CERTIFICATE = os.environ.get('CERTIFICATE')
    cnx_script = f"DRIVER={MSSQLSERVER_DRIVER};SERVER={MSSQLSERVER_SERVER};DATABASE={MSSQLSERVER_DATABASE};UID={MSSQLSERVER_UID};PWD={MSSQLSERVER_PWD};TRUSTSERVERCERTIFICATE={CERTIFICATE}"
    sql_server_conn = None
    try:
        sql_server_conn = await aioodbc.connect(dsn=cnx_script)
    except Exception as e:
        logger.critical('Error al conectar con mssqlserver: '+str(e))
    return sql_server_conn

async def get_from_mssqlserver(pais):
    QUERY = os.environ.get('QUERY')
    devices = []
    try:
        sql_server_conn = await connect_to_mssqlserver()
        sql_server_cursor = await sql_server_conn.cursor()
        # Obtener datos de la base de datos SQL Server
        await sql_server_cursor.execute(QUERY)
        rows = await sql_server_cursor.fetchall()
        await sql_server_cursor.close()
        await sql_server_conn.close()
        for row in rows:
            # Do Something
            devices.append({"diccionary":row})
    except Exception as e:
        logger.critical('Error al conectar con mssqlserver en mssqlserver: '+str(e))
    return devices