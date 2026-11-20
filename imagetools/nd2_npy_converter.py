import nd2
import numpy as np 
import glob 
import os 
from tqdm import tqdm 
# ---- User settings: set this to your own folder ----
folder = "path/to/nd2_files"   # searched recursively for .nd2 files
npy_folder = os.path.join(folder, "npy_files")


if not os.path.isdir(npy_folder): 
    os.mkdir(npy_folder)


for file in tqdm(glob.glob(os.path.join(folder, "**/*.nd2"), recursive = True)): 
    name = os.path.splitext(os.path.basename(file))[0]
    out_file = os.path.join(npy_folder, name + ".npy")
    if not os.path.isfile(out_file):
        img = nd2.imread(file)
        np.save(out_file, img.data if hasattr(img, "data") else img)
    
    
    
    
    