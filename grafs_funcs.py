# import matplotlib
import matplotlib.pyplot as plt


def make_png_holt(data_list, prognos_list, png_dir, x, alfa, beta, sigma):
    '''
    Make graf with data and "Exponential smoothing based on the trend" and save it to png file.
    :param data_list: ['kod_gup', 'art.', 'name', data_1, ... data_n]
    :param prognos_list: ['kod_gup', 'art.', 'name', prognos_1, ... prognos_n]
    :param png_dir: directory
    :param x: month list
    :return: make png file (filename = 'kod_gup')
    '''
    x_data = x
    x_prognos = x[1:]
    x_prognos.append('след. шаг')
    graf_name = f'''{prognos_list[0]}, {data_list[2]}'''
    filename = data_list[0]
    y = prognos_list[3:]
    z = data_list[3:]
    fig, ax1 = plt.subplots(figsize=(12, 8))
    fig.subplots_adjust(bottom=0.2, left=0.1)
    ax1.set_title(graf_name)
    ax1.annotate(f'''Экспоненциальное сглаживание с учетом тренда. Метод Хольта.
    Прогноз на следующий шаг: {prognos_list[-1]}, при a = {alfa}, b = {beta}, sigma = {sigma}. Исходные данные за период с {x[0]} по {x[-1]}''',
                 xy=(25, 25), xycoords='figure pixels')
    ax1.annotate(
    f'{prognos_list[-1]}',
    xy=(x_prognos[-1], y[-1]), xycoords='data',
    xytext=(15, 0), textcoords='offset points')
    plt.plot(x_data, z, label='Исходные данные', color='#98FB98')
    plt.plot(x_prognos, y, label='Скользящая средняя', color='#006400')
    plt.xlabel('Среднемесячные значения')
    plt.ylabel('Количество')
    plt.tick_params(axis='x', rotation=70)
    line_up, = ax1.plot(x_data, z, label='Исходные данные', color='#98FB98')
    line_down, = ax1.plot(x_prognos, y, label=f'Скользящая средняя', color='#006400')
    plt.legend(handles=[line_up, line_down])
    plt.xlim(0, len(x_data))
    plt.savefig(f'{png_dir}{filename}.png', dpi=200)
    plt.close('all')


def make_png_expon(data_list, prognos_list, png_dir, x, alfa, sigma):
    x_data = x
    x_prognos = x[1:]
    x_prognos.append('след. шаг')
    graf_name = f'''{prognos_list[0]}, {data_list[2]}'''
    filename = data_list[0]
    y = prognos_list[3:]
    z = data_list[3:]
    fig, ax1 = plt.subplots(figsize=(12, 8))
    fig.subplots_adjust(bottom=0.2, left=0.1)
    ax1.set_title(graf_name)
    ax1.annotate(
        f'''Экспоненциальное сглаживание простое
        Прогноз на следующий шаг: {prognos_list[-1]}, при a = {alfa}, sigma = {sigma}. Исходные данные за период с {x[0]} по {x[-1]}''',
        xy=(25, 25), xycoords='figure pixels')
    ax1.annotate(
        f'{prognos_list[-1]}',
        xy=(x_prognos[-1], y[-1]), xycoords='data',
        xytext=(15, 0), textcoords='offset points')
    plt.plot(x_data, z, label='Исходные данные', color='#98FB98')
    plt.plot(x_prognos, y, label='Скользящая средняя', color='#006400')
    plt.xlabel('Среднемесячные значения')
    plt.ylabel('Количество')
    plt.tick_params(axis='x', rotation=70)
    line_up, = ax1.plot(x_data, z, label='Исходные данные', color='#98FB98')
    line_down, = ax1.plot(x_prognos, y, label=f'Скользящая средняя', color='#006400')
    plt.legend(handles=[line_up, line_down])
    plt.xlim(0, len(x_data))
    plt.savefig(f'{png_dir}{filename}.png', dpi=200)
    plt.close('all')


def make_png_holtvint(data_list, prognos_list, png_dir, x, alfa, beta, seas, sigma):
    '''
    Make graf with data and "Exponential smoothing based on the trend" and save it to png file.
    :param data_list: ['kod_gup', 'art.', 'name', data_1, ... data_n]
    :param prognos_list: ['kod_gup', 'art.', 'name', prognos_1, ... prognos_n]
    :param png_dir: directory
    :param x: month list
    :return: make png file (filename = 'kod_gup')
    '''
    x_data = x
    x_prognos = x[1:]
    x_prognos.append('след. шаг')
    graf_name = f'''{prognos_list[0]}, {data_list[2]}'''
    filename = data_list[0]
    y = prognos_list[3:]
    z = data_list[3:]
    fig, ax1 = plt.subplots(figsize=(12, 8))
    fig.subplots_adjust(bottom=0.2, left=0.1)
    ax1.set_title(graf_name)
    ax1.annotate(f'''Экспоненциальное сглаживание с учетом тренда и сезонности. Метод Хольта-Винтерса.
    Прогноз на следующий шаг: {prognos_list[-1]}, при a = {alfa}, b = {beta}, s = {seas}, sigma = {sigma}. Исходные данные за период с {x[0]} по {x[-1]}''',
                 xy=(25, 25), xycoords='figure pixels')
    ax1.annotate(
    f'{prognos_list[-1]}',
    xy=(x_prognos[-1], y[-1]), xycoords='data',
    xytext=(15, 0), textcoords='offset points')
    plt.plot(x_data, z, label='Исходные данные', color='#98FB98')
    plt.plot(x_prognos, y, label='Скользящая средняя', color='#006400')
    plt.xlabel('Среднемесячные значения')
    plt.ylabel('Количество')
    plt.tick_params(axis='x', rotation=70)
    line_up, = ax1.plot(x_data, z, label='Исходные данные', color='#98FB98')
    line_down, = ax1.plot(x_prognos, y, label=f'Скользящая средняя', color='#006400')
    plt.legend(handles=[line_up, line_down])
    plt.xlim(0, len(x_data))
    plt.savefig(f'{png_dir}{filename}.png', dpi=200)
    plt.close('all')


def make_png_trend(data_list, prognos_list, png_dir, x, sigma):
    x_data = x
    x_prognos = x[1:]
    x_prognos.append('след. шаг')
    graf_name = f'''{prognos_list[0]}, {data_list[2]}'''
    filename = data_list[0]
    y = prognos_list[3:]
    z = data_list[3:]
    fig, ax1 = plt.subplots(figsize=(12, 8))
    fig.subplots_adjust(bottom=0.2, left=0.1)
    ax1.set_title(graf_name)
    ax1.annotate(
        f'''Линейный тренд
        Прогноз на следующий шаг: {prognos_list[-1]}, sigma = {sigma}. Исходные данные за период с {x[0]} по {x[-1]}''',
        xy=(25, 25), xycoords='figure pixels')
    ax1.annotate(
        f'{prognos_list[-1]}',
        xy=(x_prognos[-1], y[-1]), xycoords='data',
        xytext=(15, 0), textcoords='offset points')
    plt.plot(x_data, z, label='Исходные данные', color='#98FB98')
    plt.plot(x_prognos, y, label='Линейный тренд', color='#006400')
    plt.xlabel('Среднемесячные значения')
    plt.ylabel('Количество')
    plt.tick_params(axis='x', rotation=70)
    line_up, = ax1.plot(x_data, z, label='Исходные данные', color='#98FB98')
    line_down, = ax1.plot(x_prognos, y, label=f'Линейный тренд', color='#006400')
    plt.legend(handles=[line_up, line_down])
    plt.xlim(0, len(x_data))
    plt.savefig(f'{png_dir}{filename}.png', dpi=200)
    plt.close('all')


def make_png_merged(row_pr_hv, hv_alfa, hv_beta, hv_seas, hv_sigma,
            row_pr_lt, lt_sigma,
            row_pr_h, h_alfa, h_beta, h_sigma,
            row_pr_ex, ex_alfa, ex_sigma,
            png_dir, period_list, data_row,
            comb_pr, comb_sigma):
    '''
    Make graf with different prognosis and save it to png file.
    :param:
    :return: make png file (filename = 'kod_gup')
    '''
    x_data = period_list
    x_prognos = period_list[1:]
    x_prognos.append('след. шаг')
    graf_name = f'''{data_row[0]}, {data_row[2]}'''
    filename = data_row[0]
    ex = row_pr_ex
    h = row_pr_h
    hv = row_pr_hv
    lt = row_pr_lt
    z = data_row[3:]
    plt.figure(figsize=(9, 6), dpi=150)
    plt.subplots_adjust(bottom=0.32)
    plt.plot(x_data, z, color='#555555', linestyle=':', label='Исходные данные')
    plt.plot(x_prognos, lt, color='#18af00', label='Линейный тренд')
    plt.plot(x_prognos, ex, color='#53acff', label='Экспоненциальное сглаживание')
    plt.plot(x_prognos, h, color='#ff8c38', label='Метод Хольта')
    plt.plot(x_prognos, hv, color='#c64390', label='Метод Хольта-Винтерса')
    plt.title(graf_name, fontsize=12)
    plt.legend()
    plt.grid(color='#DDDDDD', linewidth=1, linestyle=':')
    plt.annotate(comb_pr, xy=(x_prognos[-1], comb_pr),# xycoords='axes fraction',
             xytext=(50, 0), textcoords='offset points',
             ha="right", va="top",
             arrowprops=dict(arrowstyle="->"))
    plt.xlabel('Период', fontsize=12, color='green')
    plt.tick_params(axis='x', labelsize=8, rotation=70)
    plt.ylabel('Количество', fontsize=12, color='green')
    plt.annotate(f'''Исходные данные за период с {x_data[0]} по {x_data[-1]}.
            Линейный тренд:   Прогноз = {row_pr_lt[-1]},   СКО = {lt_sigma}. 
            Экспоненциальное сглаживание:   Прогноз = {row_pr_ex[-1]},   СКО = {ex_sigma},   при a = {ex_alfa}.
            Метод Хольта:   Прогноз = {row_pr_h[-1]},   СКО = {h_sigma},   при a = {h_alfa},   b = {h_beta}.
            Метод Хольта-Винтерса:   Прогноз = {row_pr_hv[-1]},   СКО = {hv_sigma},   при a = {hv_alfa},   b = {hv_beta},   c = {hv_seas}.
''',
    xy=(25, 35), xycoords='figure pixels', fontsize=8)
    plt.annotate(f'''-- Комбинированный прогноз на следующий шаг: {comb_pr}, СКО: {comb_sigma}. --''',
                 xy=(25, 25), xycoords='figure pixels', fontsize=9)
    plt.savefig(f'{png_dir}{filename}.png')
    plt.close('all')