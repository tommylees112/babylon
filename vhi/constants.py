import os

paths = dict()
paths['babylon'] = os.path.join('/', 'Users', 'TommyLees', 'Desktop',
 'babylon')
paths['mat_data'] = os.path.join(paths['babylon'], 'VHI_data.mat')
paths['csv_data'] = os.path.join(paths['babylon'], 'VHI_Landsat_Sep2016-Sep17_cut4Steve.csv')

dt_formats = dict()
dt_formats['vhi_input'] = '%Y%m%d'
