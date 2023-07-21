#!/bin/python
from datetime import datetime, timedelta
import os
import random
import string
from trace_generator import Trace


def gen_random_kstnm(num_kstnm: int):
    if num_kstnm > 26 ** 4:
        raise ValueError("Can't generate more than 26^4 unique strings.")

    sta_list = []
    while len(sta_list) < num_kstnm:
        sta = ''.join(random.choices(string.ascii_uppercase, k=4))
        if sta not in sta_list:
            sta_list.append(sta)
    return sta_list


def generate_random_string_and_coordinates():
    # set the range of latitude and longitude
    stla = random.uniform(0, 90)
    stlo = random.uniform(0, 180)
    stel = random.uniform(0, 1000)

    coordinate = {'stla': stla, 'stlo': stlo, 'stel': stel}

    return coordinate


# Generate a random time list
def gen_random_time_list(start_time: datetime, end_time: datetime, time_delta: timedelta):
    timeList = []
    while start_time < end_time:
        timeList.append(start_time)
        start_time += time_delta
    return timeList


def gen_sac_path(stnm: str, t: datetime, c: str, home_dir: str):
    year_str = str(t.year)
    jdate_str = t.strftime("%j")
    hour_min_str = t.strftime("%H%M")
    file_name = stnm + '.' + year_str + '.' + jdate_str + '.' + hour_min_str + '.' + c + ".sac"
    file_dir = os.path.join(home_dir, stnm, year_str + jdate_str)
    os.makedirs(file_dir, exist_ok=True)
    file_path = os.path.join(file_dir, file_name)
    return file_path


if __name__ == "__main__":
    home = '/mnt/c/Users/think8/Desktop/PseudoArray3'
    os.makedirs(home, exist_ok=True)
    start = datetime(2018, 1, 1)  # the first date of 2018
    end = datetime(2018, 3, 2)  # the last date of 2018 spring
    delta = timedelta(days=1)
    kstnm_list = gen_random_kstnm(30)
    time_list = gen_random_time_list(start, end, delta)
    component_list = ['E', 'N', 'Z']
    for kstnm in kstnm_list:
        coordinate_dict = generate_random_string_and_coordinates()
        for time in time_list:
            for component in component_list:
                sac_path = gen_sac_path(kstnm, time, component, home)
                print(sac_path)
                sac = Trace(kstnm, time, component, coordinate_dict, 1, 86400, sac_path)
                sac.gen()
