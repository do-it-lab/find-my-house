"""

"""

import time


def save(a):
    """

    :return:
    """


def evaluate(a):
    """

    :return:
    """


def process(a, b):
    """

    :return:
    """

    return {}


def main():
    """

    :return:
    """

    start_time = time.time()

    # load configuration
    config = {
        'market': {}
    }
    sites = ['market']

    # loops
    for site in sites:

        info = config[site]
        output = process(site, info)
        evaluate(output)
        save(output)

    end_time = time.time()

    print("Elapsed Time = {}".format(end_time-start_time))


if __name__ == '__main__':
    main()
