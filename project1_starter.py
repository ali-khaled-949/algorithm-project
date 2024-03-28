# Algorithm Project CPSC 335
# Author: Ali Khaled
# Author: Tasin Noor
# Date: 03/18/2024
# Description: This program calculates common free times between multiple individuals' schedules,
# considering their busy schedules, working hours, and a minimum meeting duration requirement.

import ast

def ti_to_min(t_str):
  hours, minutes = map(int, t_str.split(':'))
  return hours * 60 + minutes


def mrg_inv_sch(busy_sch, work_hrs):
  work_str, work_end = map(ti_to_min, work_hrs)
  mrgd = [(work_str, work_str)]
  for start, end in busy_sch:
    mrgd.append((ti_to_min(start), ti_to_min(end)))
  mrgd.append((work_end, work_end))
  mrgd.sort()
  fr_tim = []
  for i in range(1, len(mrgd)):
    if mrgd[i][0] > mrgd[i - 1][1]:
      fr_tim.append((mrgd[i - 1][1], mrgd[i][0]))
  return fr_tim


def find_common_fr_tim(fr_tim_list):
  common_fr_tim = fr_tim_list[0]
  for fr_tim in fr_tim_list[1:]:
    common_fr_tim = [(max(start1, start2), min(end1, end2))
                     for start1, end1 in common_fr_tim
                     for start2, end2 in fr_tim
                     if max(start1, start2) < min(end1, end2)]
  return common_fr_tim


def filter_by_minimum_duration(fr_tim, min_duration):
  return [(start, end) for start, end in fr_tim if end - start >= min_duration]


def find_group_free_time(busy_schs, work_hrs, min_duration):
  all_fr_tim = []
  for busy_sch, daily_hours in zip(busy_schs, work_hrs):
    fr_tim = mrg_inv_sch(busy_sch, daily_hours)
    all_fr_tim.append(fr_tim)
  common_fr_tim = find_common_fr_tim(all_fr_tim)
  final_fr_tim = filter_by_minimum_duration(common_fr_tim, min_duration)
  formatted_fr_tim = [(f"{start // 60:02d}:{start % 60:02d}",
                       f"{end // 60:02d}:{end % 60:02d}")
                      for start, end in final_fr_tim]
  return formatted_fr_tim


# Read  input.txt
with open('Input.txt', 'r') as file:
  content = file.read().strip()
  data = ast.literal_eval(content)

busy_schs = [data['person1_Schedule'], data['person2_Schedule']]
work_hrs = [data['person1_DailyAct'], data['person2_DailyAct']]
min_duration = data['duration_of_meeting']

fr_tim = find_group_free_time(busy_schs, work_hrs, min_duration)

formatted_output = '[' + ', '.join(
    [f"[{start}, {end}]" for start, end in fr_tim]) + ']'
print(formatted_output)  # Print to console

with open('Output.txt', 'w') as file:  # Write to Output.txt
  file.write(formatted_output)
