import csv
from grafs_funcs import make_png_trend


def aver_calculation(list):
    sig = []
    aver = sum(list) / len(list)
    for i in range(len(list)):
        sig.append((list[i] - aver) ** 2)
    sigma = (sum(sig) / len(list)) ** 0.5
    return aver, sigma


def aver_main_func(main_list, x, csv_file):
    with open(csv_file, 'w', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        csv_str = ['kod_gup', 'art.', 'name', 'average', 'sigma']
        writer.writerow(csv_str)
        for row in main_list:
            row_data = row[3:]
            aver, sigmax = aver_calculation(row_data)
            csv_str = row[0:3]
            csv_str.extend([aver, sigmax])
            writer.writerow(csv_str)
    print('Average success!')


def linear_calculation(list, x_aver, xx):
    xy_sum = 0
    sig = []
    trend_list = []
    y_aver = sum(list ) / len(list)
    for i in range(1, len(list)):
        xy = i * list[i-1]
        xy_sum += xy
    b = (xy_sum - len(list) * x_aver * y_aver) / (xx - len(list) * x_aver * x_aver)
    a = y_aver - b * x_aver
    for i in range(1, len(list)):
        yt = a + b * i
        trend_list.append(yt)
        sig.append((list[i] - trend_list[i-1])**2)
    trend_list.append(round(a + b * len(list)))
    sigma = (sum(sig) / (len(sig) - 1)) ** 0.5
    return trend_list, sigma


def linear_main_func(main_list, png_dir, period_list, csv_file):
    with open(csv_file, 'w', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        csv_str = ['kod_gup', 'art.', 'name', 'prognos', 'sigma']
        writer.writerow(csv_str)
        # ------- begin pre-calculation
        x = 0; xx = 0
        for i in range(1, len(main_list[1][3:]) + 1):
            x += i
            xx += i*i
        x_aver = x / len(main_list[1][3:])
        # ------- end pre-calculation
        for row in main_list:
            row_data = row[3:]
            trend_list, sigma = linear_calculation(row_data, x_aver, xx)
            data_list = row[0:3]
            data_list.extend(row_data)
            prognos_list = row[0:3]
            prognos_list.extend(trend_list)
            csv_str = row[0:3]
            csv_str.extend([trend_list[-1], sigma])
            writer.writerow(csv_str)
            make_png_trend(data_list, prognos_list, png_dir, period_list, sigma)
    print('Linear success!')
