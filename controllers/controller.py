import sys

sys.path.append('/')

from models import whitefish


def find_by_date(find_date):
    model = whitefish.WhiteFishModel()
    model_list = model.find_by_date(find_date=find_date)
    return [vars(models) for models in model_list]


def delete_all_entries():
    model = whitefish
    model = model.delete()


def get_recent_web(resort="wf", refresh=False):
    model = whitefish.WhiteFishModel()
    model = model.get_recent_web()
    return model


def web_to_sql(resort="wf", refresh=False):
    model = whitefish.WhiteFishModel()
    model = model.get_recent_web(refresh=refresh)
    model.commit_to_SQL()
    return model.get_recent_sql()


def get_recent_SQL():
    # returns the most recent data from the database
    # with time stamp
    model = whitefish.WhiteFishModel()
    model = model.get_recent_sql()
    # model.print()
    return model


def get_all():
    # returns list of all Models from SQL
    model = whitefish.WhiteFishModel()
    model_list = model.all()
    return [vars(models) for models in model_list]


def update():
    pass


def main():
    # web_to_sql()
    # get_recent_SQL().print()
    # delete_all_entries()
    # get_all()
    web_to_sql(refresh=False)


if __name__ == '__main__':
    main()
