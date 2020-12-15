import sqlite3


def setup_db(filename='example.sqlite'):
    # SQL
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE whitefish (w
                        overnight_snow INTEGER,
                        settled_base INTEGER,
                        total_to_date INTEGER,
                        six_am_temp INTEGER,
                        twenty_four_hr_snow INTEGER,
                        seven_day_snow INTEGER,
                        current_conditions TEXT,
                        viz_wind TEXT)
                        ''')
        # c.execute("DROP TABLE whitefish")
        conn.commit()
    except sqlite3.Error:
        print("Fail")

    c.execute("""INSERT INTO whitefish (current_conditions)
        VALUES (0)
    
        """)
    conn.commit()


class DB:
    def __init__(self):
        pass
