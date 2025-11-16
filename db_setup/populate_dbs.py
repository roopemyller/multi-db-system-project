
import psycopg2
from psycopg2 import sql
from schema import SCHEMA
from sample_data import (
    REPLICATED_BRANDS,
    REPLICATED_CAMERA_TYPES,
    DB1_CAMERAS,
    DB1_LENSES,
    DB1_ACCESSORIES,
    DB2_CAMERAS,
    DB2_LENSES,
    DB2_ACCESSORIES,
    DB3_CAMERAS,
    DB3_LENSES,
    DB3_ACCESSORIES,
)
import os
from dotenv import load_dotenv

load_dotenv()

# Get env variables for DB connection
DB_USER = os.getenv('DB_USER')
DB_PORT = os.getenv('DB_PORT')

def populate_database(db_name, cameras, lenses, accessories):
    """Populate the database with sample data.
    
    Args:
        connection: A psycopg2 database connection object.
        cameras: A list of camera data tuples.
        lenses: A list of lens data tuples.
        accessories: A list of accessory data tuples.
    """

    connection = psycopg2.connect(dbname=db_name, user=DB_USER, port=DB_PORT)

    cursor = connection.cursor()

    cursor.execute(SCHEMA)

    cursor.executemany(
        "INSERT INTO brands (name, country, founded_year) VALUES (%s, %s, %s)",
        REPLICATED_BRANDS
    )

    cursor.executemany(
        "INSERT INTO camera_types (type_name, description) VALUES (%s, %s)",
        REPLICATED_CAMERA_TYPES
    )
    cursor.executemany(
        "INSERT INTO cameras (brand_id, type_id, model_name, release_year, price) VALUES (%s, %s, %s, %s, %s)",
        cameras
    )
    cursor.executemany(
        "INSERT INTO lenses (brand_id, focal_length, aperture, lens_type, price) VALUES (%s, %s, %s, %s, %s)",
        lenses
    )
    cursor.executemany(
        "INSERT INTO accessories (name, category, price, compatible_brands) VALUES (%s, %s, %s, %s)",
        accessories
    )

    connection.commit()
    cursor.close()
    connection.close()
    print(f"DB {db_name} populated successfully.")

populate_database('db1', DB1_CAMERAS, DB1_LENSES, DB1_ACCESSORIES)
populate_database('db2', DB2_CAMERAS, DB2_LENSES, DB2_ACCESSORIES)  
populate_database('db3', DB3_CAMERAS, DB3_LENSES, DB3_ACCESSORIES)