import os
import seedir as sd
from templateflow import api as tflow

from bids_atlas.utils import check_output_path, resample_atlas_target, generate_json_sidecar_file

import pandas as pd

import nibabel as nb
from nilearn import datasets


# define function to get the AAL atlas
def get_AAL(target_space=None, resolution=None, path=None):
    """
    Download the AAL atlas in specified target space and resolution,
    providing it in a BIDS-Atlas compliant manner.

    Parameters
    ----------
    target_space : string
        Target space the atlas should be provided in. If None, the atlas
        will be provided in MNI152NLin6Asym. Default = None.
    resolution : string
        Resolution the atlas should be provided in. If None, the atlas
        will be provided in 2mm resolution. Default = None.
    path : string
        Path where the atlas will be saved. If None, the file will be saved
        in the current working directory. Default = None.

    Returns
    -------
    dict : Dictionary
        A Dictionary containing the paths to the atlas image, tsv and json files.

    Examples
    --------
    Download the AAL atlas to the current directory.

    >>> get_AAL()

    Download the atlas to a specific path, e.g. the user's Desktop
    and indicate a resolution.

    >>> get_AAL(resolution=1, path='/home/user/Desktop')
    """

    # check input arguments and if not provided assign default
    # target_space will be actively supported soon
    if target_space is None:
        target_space = 'MNI152NLin6Asym'
    else:
        print('Spatial transformations of atlases will soon be supported.')
        print('At the moment only MNI152NLin6Asym is available.')
        target_space = 'MNI152NLin6Asym'
    if resolution is None:
        resolution = 2
    if path is None:
        path = os.curdir

    # get the AAL atlas as provided by nilearn
    aal_atlas = datasets.fetch_atlas_aal(version='SPM12')

    # get the target/reference as provided by templateflow
    target = tflow.get(target_space, desc='brain', resolution=resolution, suffix='T1w',
                       extension='nii.gz')

    # resample the atlas to the indicated resolution if needed
    aal_atlas_nii = resample_atlas_target(aal_atlas.maps, target)

    # generate the output path
    outpath = check_output_path(path, atlas='AAL')

    # generate the filename pattern
    atlas_file_name = 'atlas-AAL_res-%s_dseg.nii.gz' % resolution

    # save the atlas at the indicated path with the generated filename
    nb.save(aal_atlas_nii, os.path.join(outpath, atlas_file_name))

    # create the atlas .tsv file
    aal_df = pd.DataFrame({'Index': aal_atlas.indices,
                           'Label': aal_atlas.labels,
                           'Hemisphere': ['L' if '_L' in label else 'R' if "_R" in label else 'NA' for label in aal_atlas.labels]
                           })
    
    # save the atlas .tsv file
    aal_df.to_csv(os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.tsv')),
                  index=False)

    # generate the atlas json sidecar file
    generate_json_sidecar_file('AAL',
                               os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json')))

    # print a message indicating what files were downloaded where
    print('The following files were downloaded at %s' % outpath)
    sd.seedir(outpath)

    aal_atlas_dict = {'AtlasImage': os.path.join(outpath, atlas_file_name),
                      'AtlasTSV': os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.tsv')),
                      'AtlasJson': os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json'))}

    return aal_atlas_dict


# define function to get the Destrieux atlas
def get_Destrieux(target_space=None, resolution=None, path=None):
    """
    Download the Destrieux atlas in specified target space and resolution,
    providing it in a BIDS-Atlas compliant manner.

    Parameters
    ----------
    target_space : string
        Target space the atlas should be provided in. If None, the atlas
        will be provided in MNI152NLin6Asym. Default = None.
    resolution : string
        Resolution the atlas should be provided in. If None, the atlas
        will be provided in 2mm resolution. Default = None.
    path : string
        Path where the atlas will be saved. If None, the file will be saved
        in the current working directory. Default = None.

    Returns
    -------
    dict : Dictionary
        A Dictionary containing the paths to the atlas image, tsv and json files.

    Examples
    --------
    Download the Destrieux atlas to the current directory.

    >>> get_Destrieux()

    Download the atlas to a specific path, e.g. the user's Desktop
    and indicate a resolution.

    >>> get_Destrieux(resolution=1, path='/home/user/Desktop')
    """

    # check input arguments and if not provided assign default
    # target_space will be actively supported soon
    if target_space is None:
        target_space = 'MNI152NLin6Asym'
    else:
        print('Spatial transformations of atlases will soon be supported.')
        print('At the moment only MNI152NLin6Asym is available.')
        target_space = 'MNI152NLin6Asym'
    if resolution is None:
        resolution = 2
    if path is None:
        path = os.curdir

    # get the Destrieux atlas as provided by nilearn
    destrieux_atlas = datasets.fetch_atlas_destrieux_2009()

    # get the target/reference as provided by templateflow
    target = tflow.get(target_space, desc='brain', resolution=resolution, suffix='T1w',
                       extension='nii.gz')

    # resample the atlas to the indicated resolution if needed
    destrieux_atlas_nii = resample_atlas_target(destrieux_atlas.maps, target)

    # generate the output path
    outpath = check_output_path(path, atlas='Destrieux')

    # generate the filename pattern
    atlas_file_name = 'atlas-Destrieux_res-%s_dseg.nii.gz' % resolution

    # save the atlas at the indicated path with the generated filename
    nb.save(destrieux_atlas_nii, os.path.join(outpath, atlas_file_name))

    # create the atlas .tsv file
    destrieux_df = pd.DataFrame({'Index': [ind[0] for ind in destrieux_atlas.labels],
                                 'Label': [ind[1] for ind in destrieux_atlas.labels],
                                 'Hemisphere': ['L' if 'L' in label[1] else 'R' if "R" in label[1] else 'NA' for label in destrieux_atlas.labels]
                                 })
    
    # save the atlas .tsv file
    destrieux_df.to_csv(os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.tsv')),
                        index=False)

    # generate the atlas json sidecar file
    generate_json_sidecar_file('Destrieux',
                               os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json')))

    # print a message indicating what files were downloaded where
    print('The following files were downloaded at %s' % outpath)
    sd.seedir(outpath)

    destrieux_atlas_dict = {'AtlasImage': os.path.join(outpath, atlas_file_name),
                            'AtlasTSV': os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.tsv')),
                            'AtlasJson': os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json'))}

    return destrieux_atlas_dict


# define function to get the Harvard-Oxford atlas
def get_HarvardOxford(target_space=None, resolution=None, type='dseg', threshold=None, path=None):
    """
    Download the Harvard-Oxford atlas in specified target space and resolution,
    providing it in a BIDS-Atlas compliant manner.

    Parameters
    ----------
    target_space : string
        Target space the atlas should be provided in. If None, the atlas
        will be provided in MNI152NLin6Asym. Default = None.
    resolution : string
        Resolution the atlas should be provided in. If None, the atlas
        will be provided in 2mm resolution. Default = None.
    type : string
        Type the atlas should be provided in. If None, the atlas
        will be provided as dseg. Default = 'dseg'.
    threshold : string
        Threshold the atlas should be provided in. If None, the threshold
        will be set as 25. Default = '25'.
    path : string
        Path where the atlas will be saved. If None, the file will be saved
        in the current working directory. Default = None.

    Returns
    -------
    dict : Dictionary
        A Dictionary containing the paths to the atlas image, tsv and json files.

    Examples
    --------
    Download the Harvard-Oxford atlas to the current directory.

    >>> get_HarvardOxford()

    Download the atlas to a specific path, e.g. the user's Desktop
    and indicate a resolution.

    >>> get_HarvardOxford(resolution=1, path='/home/user/Desktop')
    """

    # check input arguments and if not provided assign default
    # target_space will be actively supported soon
    if target_space is None:
        target_space = 'MNI152NLin6Asym'
    else:
        print('Spatial transformations of atlases will soon be supported.')
        print('At the moment only MNI152NLin6Asym is available.')
        target_space = 'MNI152NLin6Asym'
    if resolution is None:
        resolution = 2
    if threshold is None:
        threshold = '25'
    if path is None:
        path = os.curdir

    # generate the output path
    outpath = check_output_path(path, atlas='HarvardOxford')

    if type == 'dseg':
        # get the Harvard-Oxford atlas as provided by nilearn, deterministic version
        harvardoxford_atlas = datasets.fetch_atlas_harvard_oxford(atlas_name='cort-maxprob-thr%s-%smm' % (threshold, resolution),
                                                                  symmetric_split=True)
        # generate the filename pattern
        atlas_file_name = 'atlas-HarvardOxford_res-%s_desc-thr%s_dseg.nii.gz' % (resolution, threshold)

        # generate the atlas json sidecar file
        generate_json_sidecar_file('HarvardOxford',
                                   os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json')), version='dseg')
    else:
        # get the Harvard-Oxford atlas as provided by nilearn, probabilistic version
        harvardoxford_atlas = datasets.fetch_atlas_harvard_oxford(atlas_name='cort-prob-%smm' % resolution)
        # generate the filename pattern
        atlas_file_name = 'atlas-HarvardOxford_res-%s_pseg.nii.gz' % resolution

        # generate the atlas json sidecar file
        generate_json_sidecar_file('HarvardOxford',
                                   os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json')), version='pseg')

    # save the atlas at the indicated path with the generated filename
    nb.save(harvardoxford_atlas.maps, os.path.join(outpath, atlas_file_name))

    # create the atlas .tsv file
    ho_df = pd.DataFrame({'Index': [i for i, label in enumerate(harvardoxford_atlas.labels)],
                          'Label': [label for i, label in enumerate(harvardoxford_atlas.labels)],
                          'Hemisphere': ['L' if 'Left' in label[1] else 'R' if "Right" in label[1] else 'bilat' for label in enumerate(harvardoxford_atlas.labels)]
                          })
    
    # save the atlas .tsv file
    ho_df.to_csv(os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.tsv')),
                 index=False)

    # print a message indicating what files were downloaded where
    print('The following files were downloaded at %s' % outpath)
    sd.seedir(outpath)

    ho_atlas_dict = {'AtlasImage': os.path.join(outpath, atlas_file_name),
                     'AtlasTSV': os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.tsv')),
                     'AtlasJson': os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json'))}

    return ho_atlas_dict


# define function to get the Harvard-Oxford atlas
def get_Talairach(target_space=None, resolution=None, level='gyrus', path=None):
    """
    Download the Talairach atlas in specified target space and resolution,
    providing it in a BIDS-Atlas compliant manner.

    Parameters
    ----------
    target_space : string
        Target space the atlas should be provided in. If None, the atlas
        will be provided in MNI152NLin6Asym. Default = None.
    resolution : string
        Resolution the atlas should be provided in. If None, the atlas
        will be provided in 2mm resolution. Default = None.
    level : string
        Level the atlas should be provided in. If None, the atlas
        will be provided based on gyri. Default = 'gyrus'.
    path : string
        Path where the atlas will be saved. If None, the file will be saved
        in the current working directory. Default = None.

    Returns
    -------
    dict : Dictionary
        A Dictionary containing the paths to the atlas image, tsv and json files.

    Examples
    --------
    Download the Talairach atlas to the current directory.

    >>> get_Talairach()

    Download the atlas to a specific path, e.g. the user's Desktop
    and indicate a resolution.

    >>> get_Talairach(resolution=1, path='/home/user/Desktop')
    """

    # check input arguments and if not provided assign default
    # target_space will be actively supported soon
    if target_space is None:
        target_space = 'MNI152NLin6Asym'
    else:
        print('Spatial transformations of atlases will soon be supported.')
        print('At the moment only MNI152NLin6Asym is available.')
        target_space = 'MNI152NLin6Asym'
    if resolution is None:
        resolution = 2
    if path is None:
        path = os.curdir

    # generate the output path
    outpath = check_output_path(path, atlas='Talairach')

    if level == 'gyrus':
        # get the Talairach atlas as provided by nilearn, deterministic version
        talairach_atlas = datasets.fetch_atlas_talairach(level_name='gyrus')
        # generate the filename pattern
        atlas_file_name = 'atlas-Talairach_res-%s_desc-gyrus_dseg.nii.gz' % resolution

        # generate the atlas json sidecar file
        generate_json_sidecar_file('Talairach',
                                   os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json')), version='gyrus')
    elif level == 'hemisphere':
        # get the Talairach atlas as provided by nilearn, deterministic version
        talairach_atlas = datasets.fetch_atlas_talairach(level_name='hemisphere')
        # generate the filename pattern
        atlas_file_name = 'atlas-Talairach_res-%s_desc-hemisphere_dseg.nii.gz' % resolution

        # generate the atlas json sidecar file
        generate_json_sidecar_file('Talairach',
                                   os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json')), version='hemisphere')
    elif level == 'lobe':
        # get the Talairach atlas as provided by nilearn, deterministic version
        talairach_atlas = datasets.fetch_atlas_talairach(level_name='lobe')
        # generate the filename pattern
        atlas_file_name = 'atlas-Talairach_res-%s_desc-lobe_dseg.nii.gz' % resolution

        # generate the atlas json sidecar file
        generate_json_sidecar_file('Talairach',
                                   os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json')), version='lobe')
    elif level == 'tissue':
        # get the Talairach atlas as provided by nilearn, deterministic version
        talairach_atlas = datasets.fetch_atlas_talairach(level_name='tissue')
        # generate the filename pattern
        atlas_file_name = 'atlas-Talairach_res-%s_desc-tissue_dseg.nii.gz' % resolution

        # generate the atlas json sidecar file
        generate_json_sidecar_file('Talairach',
                                   os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json')), version='tissue')
    elif level == 'ba':
        # get the Talairach atlas as provided by nilearn, deterministic version
        talairach_atlas = datasets.fetch_atlas_talairach(level_name='ba')
        # generate the filename pattern
        atlas_file_name = 'atlas-Talairach_res-%s_desc-ba_dseg.nii.gz' % resolution

        # generate the atlas json sidecar file
        generate_json_sidecar_file('Talairach',
                                   os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json')), version='ba')

    # save the atlas at the indicated path with the generated filename
    nb.save(talairach_atlas.maps, os.path.join(outpath, atlas_file_name))

    # create the atlas .tsv file
    talairach_df = pd.DataFrame({'Index': [i for i, label in enumerate(talairach_atlas.labels)],
                                 'Label': [label for i, label in enumerate(talairach_atlas.labels)],
                                 'Hemisphere': 'bilat'
                                 })
    
    # save the atlas .tsv file
    talairach_df.to_csv(os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.tsv')),
                        index=False)

    # print a message indicating what files were downloaded where
    print('The following files were downloaded at %s' % outpath)
    sd.seedir(outpath)

    talairach_atlas_dict = {'AtlasImage': os.path.join(outpath, atlas_file_name),
                            'AtlasTSV': os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.tsv')),
                            'AtlasJson': os.path.join(outpath, atlas_file_name.replace('.nii.gz', '.json'))}

    return talairach_atlas_dict
