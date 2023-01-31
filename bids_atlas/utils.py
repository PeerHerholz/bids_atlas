import os
import numpy as np
import nibabel as nb
import pathlib
from nilearn.image import resample_to_img
from shutil import copyfile
import importlib_resources


# define function to check output path
def check_output_path(path, atlas):
    """
    Check if the desired path to save the atlas exists and if not,
    create it.

    Parameters
    ----------
    path : string
        Path where the atlas will be saved. If None, the file will be saved
        in the current working directory.
    atlas : string
        Name of the atlas that should be obtained.
    
    Returns
    -------
    path : PosixPath
        A PosixPath indicating the path to the atlas.

    Examples
    --------
    Check if the indicated directory exists in the current directory, for
    example, concerning the AAL atlas.

    >>> check_output_path(os.curdir, 'AAL')

    Check if the indicated directory exists in the user's Desktop, for
    example, concerning the AAL atlas.

    >>> check_output_path('/home/user/Desktop', 'AAL')
    """

    # generate full path to atlas based on indicated output directory and atlas name
    atlas_path = os.path.join(os.path.abspath(path), 'bids_atlas_datasets', atlas)

    # check if the path exists and if not create it
    if os.path.isdir(atlas_path) is False:

        # create the path if it doesn't exist
        os.makedirs(atlas_path)
        
        # print an informative message where the atlas will be provided
        print('Atlas will be saved to %s' % atlas_path)

    return atlas_path


# define function to resample atlas to indicated resolution
def resample_atlas_target(atlas, target):
    """
    Check if the atlas is in the desired resolution and if not resample it.

    Parameters
    ----------
    atlas : string or NiftiImage
        Name of the atlas that should be evaluated concerning its resolution.
    target : string, Path or NiftiImage
        Name of the template with the target resolution.
    
    Returns
    -------
    atlas : NiftiImage
        The atlas, either in resampled or original form.

    Examples
    --------
    Check if the indicated atlas' resolution fits with that of a target image.
    Here, the AAL atlas and 1mm resolution.

    >>> resample_atlas_target('/home/user/AAL.nii',
                              '/home/user/tpl-MNI152NLin6Asym_res-01_desc-brain_T1w.nii.gz')
    """

    # check if atlas is a string, if so load it
    if type(atlas) is str:
        atlas = nb.load(atlas)

    # check if target template is a string or path, if so load it
    if type(target) is str or isinstance(target, pathlib.Path):
        target = nb.load(target)

    # print an informative message
    print('checking if atlas needs to be resampled')

    # check if the respective image properties are equal
    # if so, return the atlas
    # if not resample atlas and then return it
    if np.array_equal(atlas.header['dim'], target.header['dim']) and np.array_equal(atlas.header['pixdim'], target.header['pixdim']):

        # print an informative message
        print('no resampling needed, all good!')

        return atlas

    else:

        # print an informative message
        print('atlas will be resampled to target')

        # resample the atlas to the target template
        atlas_resampled = resample_to_img(atlas, target, interpolation='nearest')

        return atlas_resampled


def generate_json_sidecar_file(atlas_name, filename):
    """
    Create .json file for the obtained atlas.

    Parameters
    ----------
    atlas_name : str
        The name of the atlas.
    filename : str
        The file naming pattern of the atlas.

    Returns
    -------
    Generated atlas.json file in the specified directory.

    Examples
    --------
    Create dataset_description.json for the AAL atlas.

    >>>generate_json_sidecar_file('AAL', '/home/user/bids_atlas_datasets/AAL/atlas-AAL_res-2_dseg.nii.gz')
    """
    
    # check which atlas was provided and copy the respective metadata template to the corresponding directory
    if atlas_name == 'AAL':

        # get metadata for atlas
        json_metadata = importlib_resources.files(__name__).joinpath('data/atlas_metadata/atlas-AAL_desg.json')

        # copy the atlas to the required directory
        copyfile(json_metadata, filename)
