from sqlalchemy import create_engine, inspect
from sqlalchemy import text

db_connection_string = "postgresql://postgres:27Poni.74@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert 'subject' in names, "Таблица 'subject' должна существовать"


def test_select():
    # Создаем уникальный ИД для теста
    test_subject_id = 9999
    test_subject_title = "TestSubject"

    connection = db.connect()
    try:
        # Вставляем тестовые данные
        sql_insert = text("INSERT INTO subject(subject_id, subject_title) VALUES (:id, :title)")
        connection.execute(sql_insert, {'id': test_subject_id, 'title': test_subject_title})

        # Выполняем выборку по ИД
        sql_select = text("SELECT * FROM subject WHERE subject_id = :id")
        result = connection.execute(sql_select, {'id': test_subject_id})
        rows = result.mappings().all()

        assert len(rows) == 1, "Должен быть найден ровно один ряд"
        row = rows[0]
        assert row['subject_id'] == test_subject_id
        assert row['subject_title'] == test_subject_title
    finally:
        # Удаляем тестовые данные
        sql_delete = text("DELETE FROM subject WHERE subject_id = :id")
        connection.execute(sql_delete, {'id': test_subject_id})
        connection.close()


def test_insert():
    test_subject_id = 10000
    test_subject_title = "Anatomy"

    connection = db.connect()
    try:
        # Вставляем данные
        sql_insert = text("INSERT INTO subject(subject_id, subject_title) VALUES (:id, :title)")
        connection.execute(sql_insert, {'id': test_subject_id, 'title': test_subject_title})

        # Проверяем вставку
        sql_select = text("SELECT * FROM subject WHERE subject_id = :id")
        result = connection.execute(sql_select, {'id': test_subject_id})
        rows = result.mappings().all()

        assert len(rows) == 1
        row = rows[0]
        assert row['subject_title'] == test_subject_title
    finally:
        # Удаляем созданные данные
        sql_delete = text("DELETE FROM subject WHERE subject_id = :id")
        connection.execute(sql_delete, {'id': test_subject_id})
        connection.close()


def test_update():
    test_subject_id = 10001
    initial_title = "InitialTitle"
    updated_title = "UpdatedTitle"

    connection = db.connect()
    try:
        # Создаем начальную запись
        sql_insert = text("INSERT INTO subject(subject_id, subject_title) VALUES (:id, :title)")
        connection.execute(sql_insert, {'id': test_subject_id, 'title': initial_title})

        # Обновляем запись
        sql_update = text("UPDATE subject SET subject_title = :title WHERE subject_id = :id")
        connection.execute(sql_update, {'title': updated_title, 'id': test_subject_id})

        # Проверяем обновление
        sql_select = text("SELECT * FROM subject WHERE subject_id = :id")
        result = connection.execute(sql_select, {'id': test_subject_id})
        row = result.mappings().first()

        assert row is not None
        assert row['subject_title'] == updated_title
    finally:
        # Удаляем тестовые данные
        sql_delete = text("DELETE FROM subject WHERE subject_id = :id")
        connection.execute(sql_delete, {'id': test_subject_id})
        connection.close()


def test_delete():
    test_subject_id = 10002
    title_to_delete = "ToBeDeleted"

    connection = db.connect()
    try:
        # Создаем запись для удаления
        sql_insert = text("INSERT INTO subject(subject_id, subject_title) VALUES (:id, :title)")
        connection.execute(sql_insert, {'id': test_subject_id, 'title': title_to_delete})

        # Удаляем запись
        sql_delete = text("DELETE FROM subject WHERE subject_id= :id")
        connection.execute(sql_delete, {'id': test_subject_id})

        # Проверяем удаление
        sql_select = text("SELECT * FROM subject WHERE subject_id= :id")
        result = connection.execute(sql_select, {'id': test_subject_id})

        rows_after_delete = result.mappings().all()

        assert len(rows_after_delete) == 0

    finally:
         connection.close()


