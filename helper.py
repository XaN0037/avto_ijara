import psycopg2
from contextlib import closing

dbname = 'daeg59ggrk3fjm'
user = 'xuipcmzmosgoer'
password = 'e0e130e9f4034c69a9d7d892cbd6d069f33fd075bb237d30c9f403a003a92e6b'
host = 'ec2-34-226-11-94.compute-1.amazonaws.com'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return []
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_user(msg):
    tg_id = msg.from_user.id
    tg_id = str(tg_id)
    result = None
    with closing(conn.cursor()) as cursor:
        cursor.execute(f"SELECT * from public.dashboard_botuser where tg_id=%s", (tg_id,))
        result = dictfetchone(cursor)
        cursor.close()

    if not result:
        with closing(conn.cursor()) as cursor:
            sql = f"insert into public.dashboard_botuser (tg_id,first_name,last_name,user_name,is_bot) values (%s,%s,%s,%s,%s)"
            cursor.execute(sql, (
            tg_id, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.username, msg.from_user.is_bot))
            conn.commit()
            cursor.execute(f"SELECT * from public.dashboard_botuser where tg_id=%s", (tg_id,))
            result = dictfetchone(cursor)
            cursor.close()

    return result


def update_user_steep(tg_id, steep):
    with closing(conn.cursor()) as cursor:
        cursor.execute(f"UPDATE public.dashboard_botuser SET steep = %s  WHERE tg_id=%s", (steep, tg_id))
        conn.commit()
        cursor.close()
        pass
