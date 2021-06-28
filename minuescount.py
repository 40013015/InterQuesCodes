

def twelve2twenty(time_12):
    x, y = time_12[:-2], time_12[-2:]

    hours, minutes = x.split(':')

    if y == 'am':
        if hours == '12':
            return int(minutes)
        else:
            return 60 * int(hours) + int(minutes)
    else:  # y == 'pm'
        if hours == '12':
            return 60 * int(hours) + int(minutes)
        else:
            return 60 * (12 + int(hours)) + int(minutes)


def CountingMinutesI(str):
    start, end = str.split('-')

    start = twelve2twenty(start)
    end = twelve2twenty(end)

    period = end - start
    if period >= 0:
        return period
    else:
        return period + 60 * 24


# keep this function call here
print(CountingMinutesI(input()))