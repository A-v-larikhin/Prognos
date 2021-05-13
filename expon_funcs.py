from grafs_funcs import make_png_expon
import csv

def expon_calculation(list):
    sigmax = 0
    for k in range(0, 101):
        a = k / 100; ft = []; yt = []; sig = []
        ft.append(list[0]) # ft.append(sum(list) / len(list))
        for i in range(1, len(list)):
            ft.append(a * list[i-1] + (1 - a) * ft[i-1])
            yt.append(ft[i])
            sig.append((list[i] - ft[i-1]) ** 2)
        yt.append(round(ft[-1]))
        sigma = (sum(sig) / (len(list) - 1)) ** 0.5
        if sigmax == 0 or sigma < sigmax:
            sigmax = round(sigma, 3)
            alfa = a
            prognos_list = yt
    return prognos_list, alfa, sigmax


def expon_main_func(main_list, png_dir, csv_file, x):
    with open(csv_file, 'w', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        csv_str = ['kod_gup', 'art.', 'name', 'prognos', 'alfa', 'sigma']
        writer.writerow(csv_str)
        for row in main_list:
            row_data = row[3:]
            row_prognos, alfa, sigmax = expon_calculation(row_data)
            data_list = row[0:3]
            data_list.extend(row_data)
            prognos_list = row[0:3]
            prognos_list.extend(row_prognos)
            csv_str = row[0:3]
            csv_str.extend([prognos_list[-1], alfa, sigmax])
            writer.writerow(csv_str)
            make_png_expon(data_list, prognos_list, png_dir, x, alfa, sigmax)
    print('Exponential smoothing success!')
