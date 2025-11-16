import typer
import psycopg2
from typing_extensions import Annotated
from typing import Optional
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

# get env variables for DB connection
DB_USER = os.getenv('DB_USER')
DB_PORT = os.getenv('DB_PORT')

# create the Typer app
app = typer.Typer()

# function to get a database connection
def get_connection(dbname:str):
    try:
        connection = psycopg2.connect(dbname=dbname, user=DB_USER, port=DB_PORT)
        return connection
    except Exception as e:
        typer.echo(f"Error connecting to {dbname}: {e}")
        raise typer.Exit(1)
    
def print_table(cursor, table_name: str):
    """Helper function to print a table with headers and formatting"""
    # get column names and rows
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    
    if not rows:
        typer.echo(f"  No records found in table '{table_name}'.")
        return
    
    # calculate column widths
    col_widths = []
    for i, col in enumerate(columns):
        max_width = len(col)
        for row in rows:
            if row[i] is not None:
                max_width = max(max_width, len(str(row[i])))
        col_widths.append(min(max_width + 2, 50))  # Cap at 50 chars
    
    # headers
    typer.echo(f"\n Table: {table_name}")
    typer.echo("─" * (sum(col_widths) + len(columns) * 3 + 1))
    header = "│"
    for col, width in zip(columns, col_widths):
        header += f" {col:<{width}} │"
    typer.echo(header)
    typer.echo("─" * (sum(col_widths) + len(columns) * 3 + 1))
    
    # rows
    for row in rows:
        row_str = "│"
        for val, width in zip(row, col_widths):
            val_str = str(val) if val is not None else "NULL"
            if len(val_str) > width:
                val_str = val_str[:width-3] + "..."
            row_str += f" {val_str:<{width}} │"
        typer.echo(row_str)
    
    typer.echo("─" * (sum(col_widths) + len(columns) * 3 + 1))
    typer.echo(f"Total records: {len(rows)}\n")
    return


########################################
############# CLI Commands #############
########################################

@app.command()
def get_db(brand_name: Annotated[str, typer.Argument(help="Camera brand name to search for")]):
    """Find which database contains items from a specific camera brand

    Args:
        brand_name (str): The camera brand name to search for
    """

    # valid databases
    databases = ["db1", "db2", "db3"]
    found_in = []

    # serach each database for the brand
    for db in databases:
        connection = get_connection(db)
        cursor = connection.cursor()
        
        # query for the brand
        cursor.execute("SELECT id FROM brands WHERE LOWER(name) = LOWER(%s)", (brand_name,))
        brand_results = cursor.fetchone()

        # if brand found, check if there are cameras associated with it
        if brand_results:
            brand_id = brand_results[0]
            cursor.execute("SELECT COUNT(*) FROM cameras WHERE brand_id = %s", (brand_id,))
            count = cursor.fetchone()[0]
            if count > 0:
                found_in.append(db)

        cursor.close()
        connection.close()
    
    if found_in:
        typer.echo(f"Brand '{brand_name}' found in database: {', '.join(found_in)}")
        typer.echo(f"\nYou can use the db name to use other commands in this CLI.")
    else:
        typer.echo(f"Brand '{brand_name}' not found in any database.")
    return

@app.command()
def list(dbname: Annotated[str, typer.Argument(help="Database name to list brands from")], 
         table: Annotated[Optional[str], typer.Argument(help="Table name to list items from (choices: brands, camera_types, cameras, lenses, accessories)")] = None
    ):
    """List all items from a specified table in the given database

    Args:
        dbname (str): The database name to connect to
        table (str): The table name to list items from
    """

    valid_tables = ["brands", "camera_types", "cameras", "lenses", "accessories"]
    connection = get_connection(dbname)
    cursor = connection.cursor()

    try:
        # if table specified, validate and query that table
        if table:

            # validate table name
            if table not in valid_tables:
                typer.echo(f"Invalid table name '{table}'. Valid options are: {', '.join(valid_tables)}")
                raise typer.Exit(1)
            
            # query and print the specified table
            cursor.execute(f"SELECT * FROM {table}")
            print_table(cursor, table)
        
        # if no table specified, list all tables
        else:
            typer.echo(f"\nDatabase: {dbname}")
            typer.echo("=" * 80)
            
            # query and print each valid table
            for tbl in valid_tables:
                cursor.execute(f"SELECT * FROM {tbl}")
                print_table(cursor, tbl)

    except Exception as e:
        typer.echo(f"Error querying table '{table}' in database '{dbname}': {e}")
    cursor.close()
    connection.close()
    return

@app.command()
def find(
        dbname: Annotated[str, typer.Argument(help="Database name to list brands from")],
        brand_name: Annotated[str, typer.Argument(help="Camera brand name to search for")]
    ):
    """Find all items associated with a specific camera brand in the given database

    Args:
        dbname (str): The database name to connect to
        brand_name (str): The camera brand name to search for
    """

    connection = get_connection(dbname)
    cursor = connection.cursor()

    try:
        # get brand id
        cursor.execute("SELECT id FROM brands WHERE LOWER(name) = LOWER(%s)", (brand_name,))
        brand_results = cursor.fetchone()
        if not brand_results:
            typer.echo(f"Brand '{brand_name}' not found in database '{dbname}'.")
            return

        brand_id = brand_results[0]    

        table = "cameras"
        cursor.execute("SELECT * FROM cameras WHERE brand_id = %s", (brand_id,))
        print_table(cursor, table)

        table = "lenses"
        cursor.execute("SELECT * FROM lenses WHERE brand_id = %s", (brand_id,))
        print_table(cursor, table)
        
        table = "accessories"
        cursor.execute("SELECT * FROM accessories WHERE compatible_brands ILIKE %s OR compatible_brands ILIKE %s", (f"%{brand_name}%", "%All Brands%"))
        print_table(cursor, table)

    except Exception as e:
        typer.echo(f"Error querying items for brand '{brand_name}' in database '{dbname}': {e}")
    cursor.close()
    connection.close()
    return

@app.command()
def add(dbname: Annotated[str, typer.Argument(help="Database name to add to")]):
    """Interactively add a new item to the specified database
    
    Args:
        dbname (str): The database name to connect to
    """

    connection = get_connection(dbname)
    cursor = connection.cursor()

    while True:
        valid_tables = ["brands", "camera_types", "cameras", "lenses", "accessories"]
        typer.echo("\nAvailable tables to add to:")
        for table in valid_tables:
            typer.echo(f" - {table}")
        
        table = typer.prompt("\nEnter the table name to add a new record to")
        if table not in valid_tables:
            typer.echo(f"Invalid table name '{table}'. Please try again.")
            continue
        else:
            break
    
    try:
        # get column information from PostgreSQL
        cursor.execute("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = %s AND table_schema = 'public'
            ORDER BY ordinal_position
        """, (table,))
        
        columns = cursor.fetchall()
        
        # repare values to insert
        insert_columns = []
        insert_values = []
        
        for col_name, data_type, is_nullable in columns:
            # skip auto-generated ID columns
            if col_name == 'id':
                continue
            
            # show brand options if applicable
            if col_name == 'brand_id':
                cursor.execute("SELECT id, name FROM brands ORDER BY id")
                brands = cursor.fetchall()
                typer.echo("\nAvailable brands:")
                for brand in brands:
                    typer.echo(f"  {brand[0]}. {brand[1]}")
            
            # show camera type options if applicable
            elif col_name == 'type_id':
                cursor.execute("SELECT id, type_name FROM camera_types ORDER BY id")
                types = cursor.fetchall()
                typer.echo("\nAvailable camera types:")
                for cam_type in types:
                    typer.echo(f"  {cam_type[0]}. {cam_type[1]}")
            
            # prepare prompt text
            prompt_text = f"{col_name} ({data_type})"
            
            value = None

            # determine the appropriate type for the prompt
            if 'int' in data_type.lower():
                value = typer.prompt(prompt_text, type=int)
            elif 'numeric' in data_type.lower() or 'decimal' in data_type.lower():
                value = typer.prompt(prompt_text, type=float)
            else:
                value = typer.prompt(prompt_text, type=str)

            if value is not None and value != "":
                insert_columns.append(col_name)
                insert_values.append(value)
        
        # construct and execute insert query
        columns_str = ", ".join(insert_columns)
        placeholders = ", ".join(["%s"] * len(insert_values))
        query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"

        cursor.execute(query, tuple(insert_values))
        connection.commit()
        
        typer.echo(f"\nSuccessfully added new record to '{table}' in {dbname}")
    
    except Exception as e:
        typer.echo(f"Error adding record: {e}")
        connection.rollback()
    
    cursor.close()
    connection.close()
    return

@app.command()
def update(dbname: Annotated[str, typer.Argument(help="Database name to update")]):
    """Interactively update a record in the specified database
    
    Args:
        dbname (str): The database name to connect to
    """

    connection = get_connection(dbname)
    cursor = connection.cursor()

    while True:
        valid_tables = ["brands", "camera_types", "cameras", "lenses", "accessories"]
        typer.echo("\nAvailable tables to update a record in:")
        for table in valid_tables:
            typer.echo(f" - {table}")
        
        table = typer.prompt("\nEnter the table name to update a record in")
        if table not in valid_tables:
            typer.echo(f"Invalid table name '{table}'. Please try again.")
            continue
        else:
            break

    try:
        # print the table to help user choose record
        cursor.execute(f"SELECT * FROM {table}")
        print_table(cursor, table)

        

        # get column information from PostgreSQL
        cursor.execute("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = %s AND table_schema = 'public'
            ORDER BY ordinal_position
        """, (table,))  

        columns = cursor.fetchall()

        # prepare update values
        update_clauses = []
        update_values = []

        while True:
            # get record ID to update
            record_id = typer.prompt(f"Enter the ID of the record to update in '{table}'", type=int)
            cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE id = %s", (record_id,))
            count = cursor.fetchone()[0]
            if count == 0:
                typer.echo(f"Record ID {record_id} not found in table '{table}'. Please try again.")
                continue
            else:
                break

        # fetch current record values
        cursor.execute(f"SELECT * FROM {table} WHERE id = %s", (record_id,))
        current_record = cursor.fetchone()
        current_values = dict(zip([desc[0] for desc in cursor.description], current_record))

        for col_name, data_type, is_nullable in columns:
            # skip ID column
            if col_name == 'id':
                continue
            
            # prepare prompt text
            current_value = current_values.get(col_name, "NULL")
            prompt_text = f"New value for {col_name} (current: {current_value}) ({data_type})[leave blank to keep current]"

            # prommpt for new value
            value = typer.prompt(prompt_text, default="", show_default=False)


            # skip if no change
            if not value:
                continue
            try:
                if 'int' in data_type.lower():
                    value = int(value)
                elif 'numeric' in data_type.lower() or 'decimal' in data_type.lower():
                    value = float(value)

                update_clauses.append(f"{col_name} = %s")
                update_values.append(value)
            except ValueError:
                typer.echo(f"Invalid value for column '{col_name}'. Expected type: {data_type}. Skipping update for this column.")
                continue

        # construct and execute update query
        if update_clauses:
            update_values.append(record_id)
            update_str = ", ".join(update_clauses)
            query = f"UPDATE {table} SET {update_str} WHERE id = %s"

            cursor.execute(query, tuple(update_values))
            connection.commit()
            
            typer.echo(f"\nSuccessfully updated record ID {record_id} in '{table}' in {dbname}")
        else:
            typer.echo("No changes made.")
    except Exception as e:
        typer.echo(f"Error updating record: {e}")
        connection.rollback()

    cursor.close()
    connection.close()
    return

@app.command()
def restore():
    """Restore the databases to their initial state with the populate_dbs.py"""

    confirm = typer.confirm("Are you sure you want to restore all databases to their initial state? This will erase all current data.", default=False)
    if not confirm:
        typer.echo("Restore operation cancelled.")
        return

    try:
        typer.echo("Restoring databases to initial state...")
        
        databases = ["db1", "db2", "db3"]
        for db in databases:
            connection = get_connection(db)
            cursor = connection.cursor()
            cursor.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
            connection.commit()
            cursor.close()
            connection.close()

        subprocess.run(["python", "db_setup/populate_dbs.py"], check=True)
        typer.echo("Databases restored to initial state.")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error restoring databases: {e}")
    return


if __name__ == "__main__":
    app()