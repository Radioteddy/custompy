# %%
# modules to be used
import numpy as np
from itertools import groupby
import pathlib as pl
# %%
def read_to_arrs(filename, *args, **kwargs):
    """
    read_to_arrs reads content of file consisting of data 
    separated by empty lines to list of arrays.

    Returns
    -------
    list
        list of multiple numpy arrays
    """    
    arrs =[]
    with open(filename, 'r') as inpf:
        for k, g in groupby(inpf, lambda x: x.startswith('\n')):
            if not k:
                arrs.append(np.loadtxt(g, *args, **kwargs))
    return arrs
    
def multiarr(filename, *args, **kwargs):
    """
    multiarr reads content of file consisting of data 
    separated by empty lines to 3d array.

    Parameters
    ----------
    filename : str or Pathlib.path
        name of file or its absolute path

    Returns
    -------
    numpy.array
        3d array, axis=0 corresponds to number of empty line separators
    """    
    data = np.loadtxt(filename, *args, **kwargs)
    unique_vals = np.unique(data[:,0])
    i1 = unique_vals.shape[0]
    i2 = data.shape[0]//i1
    i3 = data.shape[1]
    data = np.reshape(data, (i1, i2, i3))
    return data


def save_figures(fig, filename, path='./', mode='vec', 
                    ext=None, dpi=300, scale=1, backend='Matplotlib'):
    """
    Saving figures repeatly without manual changing name,\n 
    e.g. filename_0, filename_1,...
    
    
    Parameters
    ----------
    fig : obj
        Figure object 
    filename : str
        name of an image to save
    path : str, optional
        path to saving directory, by default './'
    mode : str, optional
        type of image 
        supported types are: 'vec', 'raster', 'html', by default 'vec'
    ext : str, optional
        custom extension of image, by default None
    dpi : int, optional
        resolution in dots per inch (for Matplotlib), by default 300
    scale : int, optional
        resolution in scale (for Plotly), by default 1
    backend : str, optional
        what is the plottling backend of figure, by default 'Matplotlib'
    """
    path = pl.Path(path).resolve()    
    if not path.exists():
        path.mkdir()
    i = 0
    while sorted(path.glob(f'{filename}_{i:d}.*')) != []:
        i += 1
    if backend == 'Matplotlib':    
    # use for saving of matplotlib figures
        if ext:
            file_to_save = path / f'{filename}_{i:d}.{ext}'
        elif mode == 'vec':
                file_to_save = path / f'{filename}_{i:d}.svg'
                dpi = None
        elif mode == 'raster':
            file_to_save = path / f'{filename}_{i:d}.png'
        else:
            raise ValueError("""supported modes are:
                            1) 'ext' is exact set of extesion
                            2) 'vec' is vector image in .svg and .eps formats
                            3) 'raster' is raster image in .png format
                            """)
        fig.savefig(file_to_save, dpi=dpi, bbox_inches='tight')
    
    elif backend == 'Plotly':    
    # use for saving of Plotly figures
        if ext:
            file_to_save = path / f'{filename}_{i:d}.{ext}'
        elif mode == 'vec':
            file_to_save = path / f'{filename}_{i:d}.svg'
            scale = None
        elif mode == 'raster':
            file_to_save = path / f'{filename}_{i:d}.png'
        elif mode=='html':
            file_to_save = path / f'{filename}_{i:d}.html'
            scale=None
        else:
            raise ValueError("""supported modes are:
                            1) 'ext' is exact set of extesion
                            2) 'vec' is vector image in .svg and .eps formats
                            3) 'raster' is raster image in .png format
                            4) 'html' is interactive image in .html format
                            """)
        fig.write_image(file_to_save, scale=scale)
    else:
        raise ValueError("Currently only Matplotlib and Plotly are supported")       
    
