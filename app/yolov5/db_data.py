import psycopg2
from psycopg2 import sql
#Демо
from time import time, sleep

AVG_FOR_FRAME = 'dsfdfsdf'
OBJECTS_TOTAL = 214
STARTTIME = 4
# print(STARTTIME)
sleep(2)
ENDTIME = 5
#Демо кончается

class Data_db:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="172.28.1.3",
            database="siz_db",
            user="darina",
            password="123456",
            connect_timeout=5)

        self.cursor = self.conn.cursor()
        self.table_exists()

    def __del__(self):
        pass

    def table_exists(self):
        self.cursor.execute("select exists(select * from information_schema.tables where table_name=%s)",
                            ('website_analysis',))
        check_row = self.cursor.fetchone()[0]

        if check_row == False:
            self.cursor.execute('''create table website_analysis(id_check int GENERATED ALWAYS AS IDENTITY,
                                                            detected_object numeric null,
                                                            time_to_detect numeric null,
                                                            im_path VARCHAR(100) null)''')

    def insert_data(self, starttime, endtime, avg_for_frame):
        avg_for_frame = "'" + avg_for_frame + "'"
        print(avg_for_frame)
        SQL_Insert = sql.SQL(f"INSERT INTO website_analysis (detected_object, time_to_detect, im_path) values ({starttime}, {endtime}, {avg_for_frame});")
        # SQL_Insert = sql.SQL("insert into {} values (%s,%s, %s)").format(sql.Identifier('website_analysis')),[starttime, endtime, avg_for_frame]
        self.cursor.execute(SQL_Insert)
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    DB = Data_db()
    DB.insert_data(STARTTIME, ENDTIME, AVG_FOR_FRAME)