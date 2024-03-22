def parse_schedule(schedule):
    # Converts schedule strings to minutes since midnight
    pass

def merge_schedules(schedules):
    # Merges all schedules into one sorted list of busy intervals
    pass

def find_free_intervals(daily_act, busy_intervals):
    # Finds free intervals within daily activity periods, excluding busy intervals
    pass

def intersect_intervals(intervals_list):
    # Finds common free intervals across all members
    pass

def filter_by_duration(intervals, duration):
    # Filters intervals by minimum duration requirement
    pass

def find_meeting_times(schedules, daily_acts, duration):
    parsed_schedules = [parse_schedule(s) for s in schedules]
    merged_schedule = merge_schedules(parsed_schedules)
    free_intervals = [find_free_intervals(act, merged_schedule) for act in daily_acts]
    common_intervals = intersect_intervals(free_intervals)
    meeting_times = filter_by_duration(common_intervals, duration)
    return meeting_times

# Sample usage with input data
schedules = [
    [['7:00', '8:30'], ['12:00', '13:00'], ['16:00', '18:00']],
    [['9:00', '10:30'], ['12:20', '13:30'], ['14:00', '15:00'], ['16:00', '17:00']]
]
daily_acts = [['9:00', '19:00'], ['9:00', '18:30']]
duration = 30

meeting_times = find_meeting_times(schedules, daily_acts, duration)
print(meeting_times)
