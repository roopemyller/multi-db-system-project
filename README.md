# multi-db-system-project

## Plan

Stack:
Python + Postgres + Typer

### Python + Postgres

Three separeate DBs in one PostgreSQL server, populate the DBs with python and connection via python (`psycopq2`)

### Typer

Create a CLI application using Typer

### Step by step

1. Setup environments and tools
2. Create DBs
3. Populate DBs
4. Typer CLI
   1. Choose DB to use
   2. Print and update data within DB
   3. Option to restore the original DBs

## Quickstart:

Create .env file

```python
USER=user
DB_PORT=0001
```

Create and activate

```bash
python -m venv .venv
source .venv/bin/activate
```

Install requirements

```bash
pip install -r requirements.txt
```

Create 3 databases named db1, db2, db3 to one postgres server

Populate postgre databases

```bash
python dbsetup/populate_dbs.py
```

Install dbaccess cli

```bash
pip install -e .
```

Use dbaccess

```bash
dbaccess --help
```