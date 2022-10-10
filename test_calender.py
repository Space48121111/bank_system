from calender import Calender
from schedule_database import ScheduleDatabase
import pytest
from unittest.mock import MagicMock
import itertools

# >> pytest -s
# to print all the elements

# week_days = {
#    weeks: weeks[0]
#    timing: start_time[0]
#    date: date[0]
# }
weeks = [0, 1]
week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']



@pytest.fixture
def s():
    # s = Calender(5)
    return Calender(7)


def test_can_add_schedule_to_calender(s):
    # s.add('Tue')

    for w in week_days:
        s.add(w)

    assert s.size() == 7

def test_when_schedule_added_then_calender_contains_schedule(s):
    # s.add({'week_days': 'Tue'})

    # add 6 0-5 6 times overflow #add 5 0-4 5 times not overflow
    # pre-fill 5 items
    for _ in range(7):
        s.add('Tue')
    # raises error ONLY on the 6th
    # should pass the test on error, if not, code bugs
    with pytest.raises(OverflowError):
        s.add('Tue')

    assert 'Tue' in s.get_schedules()


# >> pytest test_calender.py::test_can_get_gross_income -s
def test_can_get_timing(s):
    # print('Print test_can_get_gross_income ONLY')
    start_time = ['5:45', '9:00', '12:30']
    end_time = ['13:15', '16:30', '20:00']

    # s.add('Tue')
    # s.add('Sat')

    for w in week_days:
        s.add(w)


    # timing_map = {
    #     'Tue': '5:45',
    #     'Sat': '9:00',
    # }
    # timing_map['Tue'] = '5:45'


    # [('Mon', '5:45'), ('Mon', '9:00'),
    # itertools to get all the combs 
    timing_map = list(itertools.product(week_days, start_time))
    # timing_map = zip(week_days, start_time)

    # {'Mon': '5:45', 'Tue': '9:00
    # timing_map = dict(zip(week_days, start_time))
    print(timing_map)

    schedule_database = ScheduleDatabase()
    # schedule_database.get_timing = MagicMock(return_value = ['5:45', '9:00'])

    def mock_get_timings(schedule):
        timings = []

        # if schedule == 'Tue':
        #     return '5:45'
        # if schedule == 'Sat':
        #     return '9:00'
        for t in timing_map:
            # print('t', t)
            sch, ti = t
            if schedule == sch:
                timings.append(ti)
        print('timings', timings, type(timings))
        return timings
        print('schedule, timing', schedule, s.get_timing(schedule_database))

    schedule_database.get_timings = MagicMock(side_effect = mock_get_timings)

    assert '9:00' in s.get_timing(timing_map)
    # assert '9:00' in s.get_timing(schedule_database)


def test_can_get_date(s):
    date = 23
    dates = []
    for _ in range(7):
        date += 1
        dates.append(date)
    # print('dates', dates)

    date_map = {}
    for w in week_days:
        s.add(w)

    # date_map = {
    #     'Sat': 24,
    # }
    # date_map['Sat'] = 24

    # for w in week_days:
    #     for dt in dates:
    #         date_map[w] = dt
    #         dates.remove(dt)
    #         break

    # date_map = {week_days[i]: dates[i] for i in range(len(week_days))}
    date_map = dict(zip(week_days, dates))

    # for k, v in date_map.items():
    #     print('Key :: value', k, v)

    # print('date_map', date_map)

    assert 30 in s.get_date(date_map)
    # assert 25 in s.get_date(schedule_database)












# end
