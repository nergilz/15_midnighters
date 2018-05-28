import requests
import pytz
from datetime import datetime
import timeit
import sys


def load_attempts(dev_url):
    page = 1

    while True:

        users_records = requests.get(
            dev_url,
            {'page': page}
            ).json()

        for attempts in users_records['records']:
            yield attempts

        page += 1

        if page > users_records['number_of_pages']:
            break


def get_local_user_time(attempt):

    time_zone = pytz.timezone(attempt['timezone'])
    return datetime.fromtimestamp(attempt['timestamp'], time_zone)


def get_midnighters(attempts, time_from, time_to):
    midnighters = []

    for attempt in attempts:
        user_name = attempt['username']
        local_user_time = get_local_user_time(attempt)

        if time_from < local_user_time.hour < time_to:
            midnighters.append(user_name)

    return set(midnighters)


def pprint_night_owls(midnighters):

    for user_name in midnighters:
        print(user_name)


if __name__ == '__main__':
    start_time = timeit.default_timer()
    dev_url = 'https://devman.org/api/challenges/solution_attempts/'
    time_from = 0
    time_to = 5

    try:
        attempts = load_attempts(dev_url)
        midnighters = get_midnighters(
            attempts,
            time_from,
            time_to
            )

    except requests.HTTPError as error:
        sys.exit('ERROR: {}'.format(error))

    pprint_night_owls(midnighters)

    print(' Time script: {}'.format(timeit.default_timer() - start_time))
