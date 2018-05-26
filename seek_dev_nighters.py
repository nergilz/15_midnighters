import requests
import pytz
from datetime import datetime
import timeit
import sys


def load_attempts(dev_url):
    page = 1

    while True:

        response = requests.get(
            dev_url,
            {'page': page}
            ).json()

        for page_with_users in response['records']:
            yield page_with_users

        page += 1

        if page > response['number_of_pages']:
            break


def get_local_user_time(data_user):

    time_zone = pytz.timezone(data_user['timezone'])
    return datetime.fromtimestamp(data_user['timestamp']).replace(tzinfo=time_zone)


def get_midnighters(page_with_users, time_from, time_to):
    midnighters = []

    for user in page_with_users:
        user_name = user['username']
        local_user_time = get_local_user_time(user)

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
        page_with_users = load_attempts(dev_url)
        midnighters = get_midnighters(
            page_with_users,
            time_from,
            time_to
            )
        pprint_night_owls(midnighters)

    except requests.HTTPError as error:
        sys.exit('ERROR: {}'.format(error))

    print(' Time script: {}'.format(timeit.default_timer() - start_time))
