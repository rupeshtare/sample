''' Module which defines Day Journey. '''
from abc import ABC, abstractmethod
from constants import WEEKEND_PEAK_HOURS, WEEKDAY_PEAK_HOURS, WEEKEND_OFF_PEAK_HOURS, WEEKDAY_OFF_PEAK_HOURS
from utils import check_time_in_between


class DayJourney(ABC):
	PEAK_HOURS = []
	OFF_PEAK_HOURS = []

	def __init__(self, time, from_zone, to_zone):
		self.time = time
		self.from_zone = from_zone
		self.to_zone= to_zone

	def check_journey_with_time_and_zones(self, kwargs):
		from_zone = kwargs.get("from_zone", "*")
		to_zone = kwargs.get("to_zone", "*")
		timings = kwargs.get("timings", [])

		return [
			i for i in timings if
			(
				i.from_zone == str(from_zone) and 
				i.to_zone == str(to_zone) and
				check_time_in_between(self.time, i.start_time, i.end_time)
			)
		]

	@property
	def is_peak_hours_from_zone_to_zone(self):
		return self.check_journey_with_time_and_zones({"from_zone": self.from_zone, "to_zone": self.to_zone, "timings": self.PEAK_HOURS})

	@property
	def is_off_peak_hours_from_zone_to_zone(self):
		return self.check_journey_with_time_and_zones({"from_zone": self.from_zone, "to_zone": self.to_zone, "timings": self.OFF_PEAK_HOURS})

	@property
	def is_peak_hours_from_zone(self):
		return self.check_journey_with_time_and_zones({"from_zone": self.from_zone, "timings": self.PEAK_HOURS})

	@property
	def is_off_peak_hours_from_zone(self):
		return self.check_journey_with_time_and_zones({"from_zone": self.from_zone, "timings": self.OFF_PEAK_HOURS})

	@property
	def is_peak_hours_to_zone(self):
		return self.check_journey_with_time_and_zones({"to_zone": self.to_zone, "timings": self.PEAK_HOURS})

	@property
	def is_off_peak_hours_to_zone(self):
		return self.check_journey_with_time_and_zones({"to_zone": self.to_zone, "timings": self.OFF_PEAK_HOURS})

	@property
	def is_peak_hours(self):
		return self.check_journey_with_time_and_zones({"timings": self.PEAK_HOURS})

	@property
	def is_off_peak_hours(self):
		if self.is_peak_hours_from_zone_to_zone:
			return False
		elif self.is_off_peak_hours_from_zone_to_zone:
			return True
		elif self.is_peak_hours_from_zone or self.is_peak_hours_to_zone:
			return False
		elif self.is_off_peak_hours_from_zone or self.is_off_peak_hours_to_zone:
			return True
		elif self.is_peak_hours:
			return False
		return True

class WeekdayJourney(DayJourney):
	PEAK_HOURS = WEEKDAY_PEAK_HOURS
	OFF_PEAK_HOURS = WEEKDAY_OFF_PEAK_HOURS

class WeekendJourney(DayJourney):	
	PEAK_HOURS = WEEKEND_PEAK_HOURS
	OFF_PEAK_HOURS = WEEKEND_OFF_PEAK_HOURS
