from day_journey import WeekdayJourney, WeekendJourney
from constants import Fare, Capping, WEEKEND_DAYS
from utils import get_date_time, get_week_number, get_day, get_time


class TigerCard:

	def __init__(self):
		self._datetime = None
		self._week = None
		self._day = None
		self.current_fare = 0
		self.daily_fare = 0
		self.weekly_fare = 0
		self.total_fare = 0

	def start_journey(self, datetime, from_zone, to_zone):
		self._set_initial_data(datetime, from_zone, to_zone)
		self.current_fare = self._get_calculated_fare()
		print(f"The fair calculated on {self._day} {self._time} from zone {from_zone} to zone {to_zone} is {self.current_fare} with daily fair {self.daily_fare}/{self.daily_capping} and weekly fair {self.weekly_fare}/{self.weekly_capping}")

	def _set_initial_data(self, datetime, from_zone, to_zone):
		self._datetime = get_date_time(datetime)
		self._set_unset_daily_fare()
		self._set_unset_weekly_fare()
		self._from_zone = from_zone
		self._to_zone =  to_zone
		self._day = get_day(self._datetime)
		self._time = get_time(self._datetime)
		self._week = get_week_number(self._datetime)

	def _set_unset_daily_fare(self):
		if self._week == get_week_number(self._datetime) and self._day != get_day(self._datetime):
			self.daily_fare = 0

	def _set_unset_weekly_fare(self):
		if self._week != get_week_number(self._datetime):
			self.weekly_fare = 0	

	def _get_fare(self):
		if self._day in WEEKEND_DAYS:
			wj = WeekendJourney(self._time, self._from_zone, self._to_zone)
		else:				
			wj = WeekdayJourney(self._time, self._from_zone, self._to_zone)

		fare = Fare.OFF_PEAK_HOURS if wj.is_off_peak_hours else Fare.PEAK_HOURS
		return fare[self._from_zone - 1][self._to_zone - 1]
	
	def _get_calculated_fare(self):
		fare = self._get_minimum_fare()

		self.weekly_fare += fare
		self.daily_fare += fare
		self.total_fare += fare

		return fare

	def _get_minimum_fare(self):
		max_fare_for_weekly_capping = self.weekly_capping - self.weekly_fare
		max_fare_for_daily_capping = self.daily_capping - self.daily_fare

		if max_fare_for_weekly_capping < max_fare_for_daily_capping:
			fare = self._calculate_fare(self.weekly_capping, self.weekly_fare)
		else:
			fare = self._calculate_fare(self.daily_capping, self.daily_fare)

		return fare
		
	@property
	def daily_capping(self):
		return Capping.DAILY_CAPPING[self._from_zone - 1][self._to_zone - 1]

	@property
	def weekly_capping(self):
		return Capping.WEEKLY_CAPPING[self._from_zone - 1][self._to_zone - 1]

	def _calculate_fare(self, capping, total_fare):
		if capping <= total_fare:
			return 0
		fare = self._get_fare()
		if capping < total_fare + fare:
			fare = capping - total_fare
		return fare
	

if __name__ == "__main__": 

	tc = TigerCard()
	tc.start_journey(datetime="08/02/2021 10:20", from_zone=2, to_zone=1)
	tc.start_journey(datetime="08/02/2021 10:45", from_zone=1, to_zone=1)
	tc.start_journey(datetime="08/02/2021 16:15", from_zone=1, to_zone=1)
	tc.start_journey(datetime="08/02/2021 18:15", from_zone=1, to_zone=1)
	tc.start_journey(datetime="08/02/2021 19:00", from_zone=1, to_zone=2)
