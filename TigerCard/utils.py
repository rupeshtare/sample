from datetime import datetime


def get_time_object(string):
    return datetime.strptime(string, '%H:%M').time()


def check_time_in_between(given_time, start_time, end_time):
    given_time = given_time
    start_time = get_time_object(start_time)
    end_time = get_time_object(end_time)
    
    return start_time <= given_time < end_time


def get_date_time(string):
    return datetime.strptime(string, '%d/%m/%Y %H:%M')


def get_date(datetime_obj):
    return datetime_obj.date()


def get_time(datetime_obj):
    return datetime_obj.time()


def get_day(datetime_obj):
    return datetime_obj.strftime("%A")


def get_week_number(datetime_obj):
    return datetime_obj.strftime("%W")
