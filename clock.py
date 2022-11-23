import datetime


def get_time():
    date_time_now = datetime.datetime.now()
    return date_time_now.strftime('%d/%m/%Y %H:%M:%S')


if __name__ == '__main__':
    get_time()
