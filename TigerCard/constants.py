from collections import namedtuple

# named tuple for journey hours which has from zone, to zone, start and end time
journey_hours = namedtuple("JourneyHours", ("from_zone", "to_zone", "start_time", "end_time"))

WEEKEND_EXCEPTION_PEAK_HOURS = [journey_hours("1", "1", "18:00", "22:00")]
WEEKDAY_EXCEPTION_PEAK_HOURS = [journey_hours("1", "1", "17:00", "20:00")]

WEEKEND_PEAK_HOURS = [journey_hours("*", "*", "09:00", "11:00"), journey_hours("*", "*", "18:00", "22:00")] + WEEKEND_EXCEPTION_PEAK_HOURS
WEEKDAY_PEAK_HOURS = [journey_hours("*", "*", "07:00", "10:30"), journey_hours("*", "*", "17:00", "20:00")] + WEEKDAY_EXCEPTION_PEAK_HOURS

WEEKEND_EXCEPTION_OFF_PEAK_HOURS = [journey_hours("*", "1", "18:00", "22:00")]
WEEKDAY_EXCEPTION_OFF_PEAK_HOURS = [journey_hours("*", "1", "17:00", "20:00")]

WEEKEND_OFF_PEAK_HOURS = [] + WEEKEND_EXCEPTION_OFF_PEAK_HOURS
WEEKDAY_OFF_PEAK_HOURS = [] + WEEKDAY_EXCEPTION_OFF_PEAK_HOURS


class Fare:
	PEAK_HOURS = [[30, 35], [35, 25]]
	OFF_PEAK_HOURS = [[25, 30], [30, 20]]


class Capping:
	DAILY_CAPPING = [[100, 120], [120, 80]]
	WEEKLY_CAPPING = [[500, 600], [600, 400]]


WEEKEND_DAYS = ("Saturday", "Sunday")
