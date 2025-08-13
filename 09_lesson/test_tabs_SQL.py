from sqlalchemy import create_engine, inspect
from sqlalchemy import text


db_connection_string = "postgresql://postgres:27Poni.74@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject'


def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()
    row1 = rows[14]

    assert row1['subject_id'] == 1
    assert row1['subject_title'] == "English"

    connection.close()


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO subject(subject_id, subject_title ) "
               "VALUES (:nev_subject_id, :nev_subject_title)")
    connection.execute(sql, {'nev_subject_id': 16,
                             'nev_subject_title': 'Anatomy'})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE subject SET subject_title = :descr "
               "WHERE subject_id = :id")
    connection.execute(sql, {"descr": 'Zoology', "id": 16})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(sql, {"id": 16})

    transaction.commit()
    connection.close()


def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM subject WHERE subject_id = :_id")
    result = connection.execute(sql_statement, {"_id": 16})
    rows = result.mappings().all()

    assert len(rows) == 0
    connection.close()
