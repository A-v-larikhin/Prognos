from grafs_funcs import make_png_holt
import csv


def holt_calculation(list):
    '''
    Calculation with iteration of parameters alfa & betta in "Exponential smoothing based on the trend"
    :param list: data list
    :return: prognosis list
    '''
    sigmax = 0
    for k in range(0, 101):
        for j in range(0, 101):
            a = k / 100; b = j / 100; ft = []; st = []; yt = []; sig = []
            ft.append(sum(list)/len(list)) # ft.append(list[0])
            st.append(0)
            for i in range(1, len(list)):
                ft.append(a*list[i] + (1 - a)*(ft[i-1] + st[i-1]))
                st.append(b * (ft[i] - ft[i-1]) + (1-b)*st[i-1])
                yt.append(ft[i-1] + st[i-1])
                sig.append((list[i] - yt[i-1])**2)
            yt.append(round(ft[-1] + st[-1]))
            sigma = (sum(sig)/(len(sig) - 1))**0.5
            if sigmax == 0 or sigma < sigmax:
                sigmax = sigma
                alfa = a
                beta = b
                prognos_list = yt
    return prognos_list, alfa, beta, sigmax


def holt_main_func(main_list, png_dir, csv_file, x):
    '''
    Make csv with prognosis and *.png files
    :param main_list:
    :param x: period list
    '''
    with open(csv_file, 'w', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        csv_str = ['kod_gup', 'art.', 'name', 'prognos', 'alfa', 'beta', 'sigma']
        writer.writerow(csv_str)
        for row in main_list:
            row_data = row[3:]
            row_prognos, alfa, beta, sigmax = holt_calculation(row_data)
            data_list = row[0:3]
            data_list.extend(row_data)
            prognos_list = row[0:3]
            prognos_list.extend(row_prognos)
            csv_str = row[0:3]
            csv_str.extend([prognos_list[-1], alfa, beta, sigmax])
            writer.writerow(csv_str)
            print(data_list)
            print(prognos_list)
            print(x)
            make_png_holt(data_list, prognos_list, png_dir, x, alfa, beta, sigmax)
    print('Holt success!')
