from read_file import main_list, make_index_list, index_dict, make_gup_kods
from data_funcs import *
from holt_funcs import *
from expon_funcs import *
from holtvint_funcs import *

# INPUT MAIN SOURCE DATA
date_range = [2018, 1, 2020, 12]    # exmpl: [2020, 1, 2020, 12] <-> 2020, january - 2020, december
col_name = 'rashod_i'   # 'nach_ostatok_i' or 'prihod_i' or 'rashod_i' or 'kon_ostatok_i'
data_type = 'count'   # 'must be "count" or "cost"'
period = 3      # Number of months for the average (month = 1, quarter = 3, half_year = 6 )
vblborka = True     # Use vblborka = True, or not  = False
vblborka_filename = './files/x.csv'
# ---------------------

# Input Exponential sorce data
expon_png_dir = './png_expon/'
expon_csv_file = './result/expon_01_half_year_2021.csv'

# Input Holt sorce data
holt_png_dir = './png_holt/'
holt_csv_file = './result/holt_01_half_year_2021.csv'
# ----------------------------

# Input Holt-Vinters sorce data
holtvint_png_dir = './png_holtvint/'
holtvint_csv_file = './result/holtvint_01_quarter_2021.csv'
# ----------------------------

index_list = make_index_list(index_dict, date_range, col_name, data_type)
period_list = make_period_list(index_dict, date_range, period)
main_list = make_clear_list(main_list, index_list)

if vblborka:
    gup_kods = make_gup_kods(vblborka_filename)
    main_list = list_from_vblborka(main_list, gup_kods)

if period > 1:
    main_list = make_average_list(main_list, period)

# Main Block
if __name__ == '__main__':
    # HOLT BLOCK
    # holt_main_func(main_list, holt_png_dir, holt_csv_file, period_list)
    # Exponential Block
    # expon_main_func(main_list, expon_png_dir, expon_csv_file, period_list)
    # Holt-Vinters Block
    holtvint_main_func(main_list, holtvint_png_dir, holtvint_csv_file, period_list, period)
