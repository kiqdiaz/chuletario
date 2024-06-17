import asyncio
import logging
from dotenv import load_dotenv
import os
import psycopg2
# IMPORT DE MODELO
# from Device.Modelo.DeviceClass import Device

async def connect_to_postgresdb():
    config = {
        "host": os.environ.get('POSTGRES_HOST'),
        "database": os.environ.get('POSTGRES_DB'),
        "user": os.environ.get('POSTGRES_USER'),
        "password": os.environ.get('POSTGRES_PASSWORD')
    }
    try:
        with psycopg2.connect(**config) as conn:
            return conn
    except (psycopg2.DatabaseError, Exception) as e:
        print('Error al conectar con Postgresql en connect_to_postgresdb(): '+str(e))

async def get_devices_from_postgresdb():
    # QUERY = "SELECT * FROM devices;" 
    devices = []
    try:
        mydb = await connect_to_postgresdb()
        postgres_cursor = mydb.cursor()
        postgres_cursor.execute("QUERY")
        rows = postgres_cursor.fetchall()
        postgres_cursor.close()
        mydb.close()
        for row in rows:
            # DO SOMETHING
            devices.append(row)
    except Exception as e:
        print('Error al conectar con Postgresql en get_devices_from_postgresdb(): '+str(e))
    return devices
    
async def post_device_to_postgresql(dev):
    QUERY = """INSERT INTO devices(
        comma,
        separated,
        keys
        ) 
        VALUES  (%s, %s, %s);"""
    data = ("dev.get_host",
            "dev.get_hostname",
            "dev.get_brand"
            )
    try:
        mydb = await connect_to_postgresdb()
        postgres_cursor = mydb.cursor()
        postgres_cursor.execute(QUERY,data)
        mydb.commit()
        postgres_cursor.close()
        mydb.close()
    except Exception as e:
        print('Error al conectar con Postgresql en post_device_to_postgresql(dev): '+str(e))

async def update_device_to_postgresql(dsolar,dpostgres):
    pass