from datetime import date


def make_clear_list(main_list, index_list):
    '''
    Keep only needed data in main list
    '''
    new_list = []
    for row in main_list:
        tmp_list = row[1:4]
        for i in index_list:
            tmp_list.append(row[i])
        new_list.append(tmp_list)
    return new_list


def list_from_vblborka(main_list, gup_kods):
    '''
    Keep only rows from vblborka in main list
    '''
    new_list =[]
    for row in main_list:
        for gup_kod in gup_kods:
            if row[0] == gup_kod:
                new_list.append(row)
    return new_list


def make_average_list(main_list, period):
    '''
    Make list with average for the period
    :return: ['kod_gup', 'art.', 'name', count1, count2, ...., count_n]
    '''
    new_main_list = []
    cols = len(main_list[0])
    for row in main_list:
        tmp_list = row[0:3]
        for col in range(3, cols, period):
            period_sum = 0
            for i in range(period):
                period_sum += row[col + i]
            average = round(period_sum / period)
            tmp_list.append(average)
        new_main_list.append(tmp_list)
    return new_main_list


def make_period_list(index_dict, date_range, period):
    tmp_list =[]
    date1 = date(date_range[0], date_range[1], 15)
    date2 = date(date_range[2], date_range[3], 15)
    for item in index_dict['rashod_i']:
        if date1 <= item[0] <= date2:
            tmp_list.append(item[0])
    period_list = []
    list_length = len(tmp_list)
    section = f'/{round(12 / period)}'
    x = 0
    for i in range(0, list_length, period):
        x += 1
        if x > round(12 / period):
            x = 1
        period_list.append(f'{x}{section} {tmp_list[i].strftime("%Y")}')
    return period_list
