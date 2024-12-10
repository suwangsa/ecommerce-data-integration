from sqlalchemy import create_engine


def init_engine():
    cred = {
        'host': "DB_HOST",
        'user': "DB_USER",
        'pass': "DB_PASS",
        'db': "DB_NAME",
        'port': "DB_PORT"
    }

    uri = f"postgresql://{cred['user']}:{cred['pass']}@{cred['host']}:{cred['port']}/{cred['db']}?sslmode=require"

    conn = create_engine(uri)

    return conn


def init_dest_engine():
    cred = {
        'host': "DB_HOST",
        'user': "DB_USER",
        'pass': "DB_PASS",
        'db': "DB_NAME",
        'port': "DB_PORT"
    }

    uri = f"postgresql://{cred['user']}:{cred['pass']}@{cred['host']}:{cred['port']}/{cred['db']}?sslmode=require"

    conn = create_engine(uri)

    return conn
