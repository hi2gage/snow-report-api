import sqlite3
import sys
import datetime
import json
from json import JSONEncoder
from datetime import date

sys.path.append('/')
import scraper


def sql_connection():
    conn = sqlite3.connect("example.sqlite")
    c = conn.cursor()
    return c, conn


def print_list(model_lists):
    for r in model_lists:
        r.print()


def delete():
    c, conn = sql_connection()
    c.execute("Delete FROM whitefish where wind IS NOT NULL")
    conn.commit()
    conn.close()


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class WhiteFishModel:
    def __init__(self, tuple_value=None):
        if tuple_value is None:
            self.day_id = None
            self.data_time = None
            self.overnight_snow = None
            self.settled_base = None
            self.total_to_date = None
            self.six_am_temp = None
            self.twenty_four_hr_snow = None
            self.seven_day_snow = None
            self.current_conditions = None
            self.visibility = None
            self.wind = None

        elif len(tuple_value) > 9:
            self.day_id = tuple_value[0]
            self.data_time = tuple_value[1]
            self.overnight_snow = tuple_value[2]
            self.settled_base = tuple_value[3]
            self.total_to_date = tuple_value[4]
            self.six_am_temp = tuple_value[5]
            self.twenty_four_hr_snow = tuple_value[6]
            self.seven_day_snow = tuple_value[7]
            self.current_conditions = tuple_value[8]
            self.visibility = tuple_value[9]
            self.wind = tuple_value[10]

        else:
            self.day_id = None
            self.data_time = None
            self.overnight_snow = tuple_value[0]
            self.settled_base = tuple_value[1]
            self.total_to_date = tuple_value[2]
            self.six_am_temp = tuple_value[3]
            self.twenty_four_hr_snow = tuple_value[4]
            self.seven_day_snow = tuple_value[5]
            self.current_conditions = tuple_value[6]
            self.visibility = tuple_value[7]
            self.wind = tuple_value[8]

    def __str__(self):
        return str(self.overnight_snow)

    def toDict(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def print(self):
        print('--------------------------------------------------------')
        attrs = vars(self)
        print('\n'.join("%-25s %-28s |" % item for item in attrs.items()))
        print('--------------------------------------------------------')

    @staticmethod
    def get_recent_sql():
        c, conn = sql_connection()
        c.execute("SELECT *, max(dayId) FROM whitefish")
        results = c.fetchone()
        # print(results)
        return WhiteFishModel(results)

    @staticmethod
    def get_recent_web(refresh=False):
        return WhiteFishModel(scraper.scrape_wf(refresh=refresh))

    @staticmethod
    def find_by_date(find_date):
        c, conn = sql_connection()
        c.execute("""SELECT * from whitefish
                     WHERE Date(dateTime) is ?""",
                  (str(find_date),)
                  )
        results = c.fetchall()
        model_list = []
        for r in results:
            model_list.append(WhiteFishModel(r))
        conn.close()
        # print(model_list)
        return model_list

    def commit_to_SQL(self):
        c, conn = sql_connection()
        c.execute("""INSERT INTO whitefish 
                    (dateTime,
                    overnight_snow,
                    settled_base,
                    total_to_date,
                    six_am_temp_F,
                    twenty_four_hr_snow,
                    seven_day_snow,
                    current_conditions,
                    visibility,
                    wind)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                  (datetime.datetime.now(),
                   self.overnight_snow,
                   self.settled_base,
                   self.total_to_date,
                   self.six_am_temp,
                   self.twenty_four_hr_snow,
                   self.seven_day_snow,
                   self.current_conditions,
                   self.visibility,
                   self.wind)
                  )
        conn.commit()
        conn.close()

    # Getters
    def get_overnight(self):
        return self.overnight_snow

    def get_settled_base(self):
        return self.settled_base

    def get_total_to_date(self):
        return self.total_to_date

    def get_six_am_temp(self):
        return self.six_am_temp

    def get_24hr_snow(self):
        return self.twenty_four_hr_snow

    def get_7day_snow(self):
        return self.seven_day_snow

    def get_current_condition(self):
        return self.current_conditions

    def get_wind_visibility(self):
        return self.viz_wind

    def all(self):
        c, conn = sql_connection()
        c.execute("SELECT * FROM whitefish")
        results = c.fetchall()
        model_list = []
        for r in results:
            model_list.append(WhiteFishModel(r))
        conn.close()
        return model_list


def main(key=None, refresh=False):
    scrap_dict = scraper.main(refresh=refresh)
    # print(result_list)
    model = WhiteFishModel(scrap_dict)
    model.commit_to_SQL()
    # print("committed to SQL")
    # model.get_recent_SQL("example.sqlite")
    return model


if __name__ == '__main__':
    main()
