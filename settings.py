from os.path import dirname, abspath, join
from glob import glob

base_dir = dirname(abspath(__file__))
data_dir = join(base_dir, 'data')
output_dir = join(base_dir, 'output')