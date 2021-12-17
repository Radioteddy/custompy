# %%
# modules to be used
import os
import glob

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
    path = os.path.abspath(path)    
    if not os.path.exists(path):
        os.makedirs(path)
    file = os.path.join(os.path.abspath(path), filename) 
    i = 0
    if backend == 'Matplotlib':    
    # use for saving of matplotlib figures
        if ext:
            while glob.glob('{}_{:d}.*'.format(file, i)) != []:
                i += 1
            fig.savefig('{}_{:d}.{}'.format(file, i, ext), dpi=dpi, bbox_inches='tight')
            fig.savefig('{}_{:d}.{}'.format(file, i, ext), dpi=dpi, bbox_inches='tight')
        elif mode == 'vec':
            while glob.glob('{}_{:d}.*'.format(file, i)) != []:
                i += 1
            fig.savefig('{}_{:d}.eps'.format(file, i), bbox_inches='tight')
            fig.savefig('{}_{:d}.svg'.format(file, i), bbox_inches='tight')
        elif mode == 'raster':
            while glob.glob('{}_{:d}.*'.format(file, i)) != []:
                i += 1
            fig.savefig('{}_{:d}.png'.format(file, i), dpi=dpi, bbox_inches='tight')
        else:
            raise ValueError("""supported modes are:
                            1) 'ext' is exact set of extesion
                            2) 'vec' is vector image in .svg and .eps formats
                            3) 'raster' is raster image in .png format
                            """)
                    
    elif backend == 'Plotly':    
    # use for saving of Plotly figures
        if ext:
            while glob.glob('{}_{:d}.*'.format(file, i)) != []:
                i += 1
            fig.write_image('{}_{:d}.{}'.format(file, i, ext), scale=scale)
            fig.write_image('{}_{:d}.{}'.format(file, i, ext), scale=scale)
        elif mode == 'vec':
            while glob.glob('{}_{:d}.*'.format(file, i)) != []:
                i += 1
            fig.write_image('{}_{:d}.svg'.format(file, i))
        elif mode == 'raster':
            while glob.glob('{}_{:d}.*'.format(file, i)) != []:
                i += 1
            fig.write_image('{}_{:d}.png'.format(file, i), scale=scale)
        elif mode=='html':
            fig.write_html('{}_{:d}.html'.format(file, i))
        else:
            raise ValueError("""supported modes are:
                            1) 'ext' is exact set of extesion
                            2) 'vec' is vector image in .svg and .eps formats
                            3) 'raster' is raster image in .png format
                            4) 'html' is interactive image in .html format
                            """)
    else:
        raise ValueError("Currently only Matplotlib and Plotly are supported")        
    
