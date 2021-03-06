from flask import Flask, jsonify, request
from controllers import whitefish
from flask_restful import Resource, Api
from apscheduler.schedulers.background import BackgroundScheduler
import time
import datetime


# Checks to see if it is the proper time to check the plant
def is_it_time_yet(beginning_hour, ending_hour):
    year, month, day, hour, minute, second = map(int, time.strftime("%Y %m %d %H %M %S").split())
    # print(str(hour) + " " + str(minute))
    return beginning_hour < hour < ending_hour


def run_scrap():
    if is_it_time_yet(5, 20):
        print(datetime.datetime.now())
        whitefish.web_to_sql(refresh=True)


# Making sure that the scraper runs every hour
scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(run_scrap, 'interval', hours=1)
print("job starting")
scheduler.start()

app = Flask(__name__)
app.debug = True
api = Api(app)


# returns all of the entries in the database
class fetchAll(Resource):
    @staticmethod
    def get():
        model = whitefish.get_all()
        return jsonify(model)


# Returns the most recent entry in the database
class fetchRecentSQL(Resource):
    @staticmethod
    def get():
        model = whitefish.get_recent_SQL()
        # print(type(vars(model)))
        return vars(model)


# Returns all entries from specified date
class fetchByDate(Resource):
    @staticmethod
    def get():
        args = request.args
        date_str = args.get('d')
        results = whitefish.find_by_date(date_str)
        return jsonify(results)


# Runs scraper and returns the most recent entry
class scrap(Resource):
    @staticmethod
    def get():
        return vars(whitefish.web_to_sql(refresh=True))


class FetchNew(Resource):
    @staticmethod
    def get():
        return vars(whitefish.get_recent_web(refresh=True))


api.add_resource(fetchAll, '/')
api.add_resource(fetchRecentSQL, '/recent-sql')
api.add_resource(fetchByDate, '/date')
api.add_resource(scrap, '/scrap')

api.add_resource(FetchNew, '/fetch-new')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
