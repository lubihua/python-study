def print_welcome(*names):
    for name in names:
        print('Welcome '+name)


def print_bye(next_time='Next Year',*names):
    for name in names:
        print("See you, "+name+' '+next_time)


