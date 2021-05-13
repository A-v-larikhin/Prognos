from aver_funcs import aver_calculation, linear_calculation
from holtvint_funcs import holtvint_calculation
from holt_funcs import holt_calculation
from expon_funcs import expon_calculation
from grafs_funcs import make_png_merged


def combined_calculation_func(prognosbl, sigmas):
    n_list = []
    x = 1
    comb_pr = 0
    comb_sigma = 0
    for i in range(len(sigmas)):
        for k in range(len(sigmas)):
            if i != k:
                x = (x ** 2) * (sigmas[k] ** 2)
        n_list.append(x)
        x = 1
    for j in range(len(n_list)):
        m = (n_list[j] / sum(n_list))
        comb_pr += prognosbl[j]*m
        comb_sigma += ((sigmas[j]**2)*(m**2))**0.5
    return round(comb_pr), round(comb_sigma, 3)


def main_merge_func(main_list, png_dir, period_list, period):
    for row in main_list:
        data_row = row
        row_data = row[3:]
        print(row[0:3])
        print('start Holt-Vinters')
        row_pr_hv, hv_alfa, hv_beta, hv_seas, hv_sigma = holtvint_calculation(row_data, period)
        print('start Holt')
        row_pr_h, h_alfa, h_beta, h_sigma = holt_calculation(row_data)
        print('start Exponential')
        row_pr_ex, ex_alfa, ex_sigma = expon_calculation(row_data)
        print('start Linear')
        row_pr_lt, lt_sigma = linear_calculation(row_data)
        prognosbl = [row_pr_lt[-1], row_pr_ex[-1], row_pr_h[-1], row_pr_hv[-1]]
        sigmas = [lt_sigma, ex_sigma, h_sigma, hv_sigma]
        comb_pr, comb_sigma = combined_calculation_func(prognosbl, sigmas)
        make_png_merged(row_pr_hv, hv_alfa, hv_beta, hv_seas, hv_sigma,
                        row_pr_lt, lt_sigma,
                        row_pr_h, h_alfa, h_beta, h_sigma,
                        row_pr_ex, ex_alfa, ex_sigma,
                        png_dir, period_list, data_row,
                        comb_pr, comb_sigma)