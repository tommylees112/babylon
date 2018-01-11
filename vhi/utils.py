from IPython.core.debugger import Tracer
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from scipy.io import loadmat
import datetime as dt

from vhi.constants import paths, dt_formats

def plot_vhi_data(vhi_data, title="VHI"):
  """ Plot the VHI data matrix with a pixel colour representing the value at a given index """
  plt.imshow(vhi_data, clim=(-3, 3))
  plt.title(f"{title}")
  plt.colorbar()
  plt.show()

def plot_errors(error_matrix):
  """ plot an error matrix """
  plt.imshow(error_matrix)
  plt.title("Error Matrix")
  plt.colorbar()
  plt.show()

def test_transform(vhi_transformed, vhi):
  """ check that the matrix operations done on batch match the ordinary ones """
  vhi_t0 = np.reshape(vhi[:,0], (1000,1000)) # np.ravel()
  error_matrix = vhi_t0 == vhi_transformed[0]

  plot_vhi_data(vhi_t0, title="Real Data")
  input(f"Showing 'real data'. Press Enter to continue...")
  plt.close()

  plot_vhi_data(vhi_transformed[0], title="Transformed Data")
  input(f"Showing 'transformed data'. Press Enter to continue...")
  plt.close()

  plot_errors(error_matrix)
  input(f"Showing error matrix. Press Enter to continue...")
  plt.close()

def clean_date_columns(column_series):
  try:
    output = dt.datetime.strptime( column_series[:8], dt_formats['vhi_input'] )
  except:
    output = column_series
  return output

def load_vhi(path):
  """ Read in the VHI data and store  """
  if path.endswith("mat"):
    vhi_mat_dict = loadmat(paths['mat_data'])
    vhi = vhi_mat_dict['VHI']
  elif path.endswith(".csv"):
    vhi_data = pd.read_csv(paths['csv_data'], header=1)
    vhi_data.columns = vhi_data.columns.to_series().apply(clean_date_columns)
    vhi = np.array(vhi_data)
    print("vhi shape = ",vhi.shape)
  else:
    raise RuntimeError('Unrecognised file type')
  assert(vhi.shape ==(1000000, 41))

  vhi = vhi.T.reshape(41,1000,1000)
  assert(vhi.shape == (41,1000,1000))
  # print(vhi.shape) # [1,000,000 rows x 41 columns] .T --> [41 columns x 1,000,000 rows]
                   # 41 time slices of 1,000 * 1,000 grid (how do i unpack it?)
                   # first series of 1000 pix in the CSV column correspond to the first row of the image
  return vhi

def plot_vhi(vhi_transformed):
  """ plot each of the VHI matrices in turn """
  for i in np.arange(0,41):
    plt.imshow(vhi_transformed[i], clim=(-3, 3))
    plt.title(f"Time {i}")
    plt.colorbar()
    plt.show()
    input(f"Showing time-{i}. Press Enter to continue...")
    plt.close()
  # [11, 17, 21, 23, 27, 30, 32, 34, 38, 40] = NANs
  # 25, 26 doing something weird












