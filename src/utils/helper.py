
from sqlalchemy import create_engine



def init_engine():
    cred = {
        'host': 'ep-red-bar-a1rghkov.ap-southeast-1.aws.neon.tech',
        'user': 'siswa_bfp',
        'pass': 'bfp_aksel_keren',
        'db': 'ecommerce_db',
        'port': 5432
    }

    uri = f"postgresql://{cred['user']}:{cred['pass']}@{cred['host']}:{cred['port']}/{cred['db']}?sslmode=require"

    conn = create_engine(uri,echo=True)

    return conn


def init_dest_engine():
    cred = {
        'host': "ep-square-pond-a5h66kcl.us-east-2.aws.neon.tech",
        'user': "neondb_owner",
        'pass': "Kd2w6OvIiUtr",
        'db': "neondb",
        'port': 5432
    }

    uri = f"postgresql://{cred['user']}:{cred['pass']}@{cred['host']}:{cred['port']}/{cred['db']}?sslmode=require"

    conn = create_engine(uri,echo=True)

    return conn
