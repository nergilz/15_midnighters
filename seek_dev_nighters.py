import requests
import pytz
from datetime import datetime
import timeit
import sys


def load_attempts(dev_url):

    pages = requests.get(
        dev_url,
        {'page': 1}
        ).json()['number_of_pages']

    for page in range(1, int(pages)):

        yield requests.get(
            dev_url,
            {'page': page}
            ).json()['records']


def get_local_user_time(data_user):

    time_utc = datetime.fromtimestamp(data_user['timestamp'])
    time_zone = pytz.timezone(data_user['timezone'])
    return time_zone.localize(time_utc)


def get_midnighters(response):
    midnighters = []
    time_form = '%H'
    before = 0
    after = 6

    for page in response:
        for user in page:
            user_name = user['username']
            local_user_time = get_local_user_time(user)

            if before < int(datetime.strftime(local_user_time, time_form)) < after:
                midnighters.append(user_name)
    return set(midnighters)


def pprint_night_owls(midnighters):

    for user_name in midnighters:
        print(user_name)


if __name__ == '__main__':
    start_time = timeit.default_timer()
    dev_url = 'https://devman.org/api/challenges/solution_attempts/'

    try:
        response = load_attempts(dev_url)

    except requests.HTTPError as error:
        sys.exit('ERROR: {}'.format(error))

    midnighters = get_midnighters(response)
    pprint_night_owls(midnighters)

    print(' Time script: {}'.format(timeit.default_timer() - start_time))
