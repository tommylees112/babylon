from IPython.core.debugger import Tracer
from vhi.utils import load_vhi, plot_vhi
from vhi.constants import paths

vhi_data = load_vhi(paths['csv_data'])
plot_vhi(vhi_data)

