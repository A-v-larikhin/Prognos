from grafs_funcs import make_png_holtvint
import csv


def holtvint_calculation(list, period):
    '''
    Calculation with iteration of parameters a,b,s in "Exponential smoothing based on trend and seasonality"
    :param list: data list
    :return: prognosis list
    '''
    sigmax = 0
    cycle_length = int (12 / period)
    for k in range(0, 101):
        for j in range(0, 101):
            for m in range(0, 101):
                a = k / 100; b = j / 100; s = m / 100; ft = []; st = []; yt = []; ss = []; sig = []
                ft.append(list[0]) # ft.append(sum(list)/len(list))
                st.append(0)
                ss.append(1)
                for i in range(1, len(list)):
                    if i < cycle_length:
                        ss.append(1)
                        ft.append(a*list[i] + (1 - a)*(ft[i-1] + st[i-1]))
                        st.append(b * (ft[i] - ft[i - 1]) + (1 - b) * st[i - 1])
                        yt.append(ft[i - 1] + st[i - 1])
                    elif i >= cycle_length and ss[i-cycle_length] == 0:
                        ss.append(1)
                        ft.append(a * list[i] + (1 - a) * (ft[i - 1] + st[i - 1]))
                        st.append(b * (ft[i] - ft[i - 1]) + (1 - b) * st[i - 1])
                        yt.append((ft[i - 1] + st[i - 1]) * ss[i - cycle_length])
                    else:
                        ft.append(a * list[i] / ss[i - cycle_length] + (1 - a) * (ft[i - 1] + st[i - 1]))
                        if ft[i] == 0:
                            ss.append(1)
                        else:
                            ss.append(s * list[i] / ft[i] + (1 - s) * ss[i - cycle_length])
                        st.append(b * (ft[i] - ft[i-1]) + (1-b) * st[i-1])
                        yt.append((ft[i-1] + st[i-1]) * ss[i-cycle_length])
                    sig.append((list[i] - yt[i-1])**2)
                yt.append(round((ft[-1] + st[-1]) * ss[-cycle_length]))
                sigma = (sum(sig)/(len(sig) - 1))**0.5
                if sigmax == 0 or sigma < sigmax:
                    sigmax = round(sigma, 3)
                    alfa = a
                    beta = b
                    seas = s
                    prognos_list = yt
    return prognos_list, alfa, beta, seas, sigmax


def holtvint_main_func(main_list, png_dir, csv_file, x, period):
    '''
    Make csv with prognosis and *.png files
    :param main_list:
    :param x: period list
    '''
    with open(csv_file, 'w', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        csv_str = ['kod_gup', 'art.', 'name', 'prognos', 'alfa', 'beta', 'seas', 'sigma']
        writer.writerow(csv_str)
        for row in main_list:
            row_data = row[3:]
            row_prognos, alfa, beta, seas, sigmax = holtvint_calculation(row_data, period)
            data_list = row[0:3]
            data_list.extend(row_data)
            prognos_list = row[0:3]
            prognos_list.extend(row_prognos)
            csv_str = row[0:3]
            csv_str.extend([prognos_list[-1], alfa, beta, seas, sigmax])
            writer.writerow(csv_str)
            make_png_holtvint(data_list, prognos_list, png_dir, x, alfa, beta, seas, sigmax)
    print('Holt-Vinters success!')
