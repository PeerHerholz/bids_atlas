import os
import pandas as pd
import nibabel as nb
import pytest
from ..datasets import get_AAL, get_Destrieux, get_HarvardOxford, get_Talairach, get_Juelich, get_Schaefer2018


@pytest.fixture
def atlas_validator():
    """Fixture providing common atlas validation functions."""
    
    class AtlasValidator:
        @staticmethod
        def validate_basic_structure(atlas_dict, atlas_name):
            """Validate basic atlas dictionary structure."""
            assert isinstance(atlas_dict, dict)
            required_keys = ['AtlasImage', 'AtlasTSV', 'AtlasJson']
            for key in required_keys:
                assert key in atlas_dict, f"Missing key {key} in {atlas_name} result"
                assert os.path.exists(atlas_dict[key]), f"{key} file does not exist for {atlas_name}"
        
        @staticmethod
        def validate_tsv_structure(tsv_path, expected_rows, expected_columns=None):
            """Validate TSV file structure and content."""
            if expected_columns is None:
                expected_columns = ['Index', 'Label', 'Hemisphere']
            
            tsv_df = pd.read_csv(tsv_path, sep='\t', keep_default_na=False)
            
            # Check row count
            assert len(tsv_df) == expected_rows, f"Expected {expected_rows} rows, got {len(tsv_df)}"
            
            # Check columns
            actual_columns = list(tsv_df.columns)
            assert actual_columns == expected_columns, f"Expected columns {expected_columns}, got {actual_columns}"
            
            # Check data types
            assert tsv_df['Index'].dtype in ['int64', 'int32'], f"Index column should be integer, got {tsv_df['Index'].dtype}"
            assert tsv_df['Label'].dtype == 'object', f"Label column should be string/object, got {tsv_df['Label'].dtype}"
            
            return tsv_df
        
        @staticmethod
        def validate_resolution(nii_path, expected_resolution=(1.0, 1.0, 1.0)):
            """Validate NIfTI file resolution (with tolerance for floating point differences)."""
            img = nb.load(nii_path)
            actual_resolution = img.header.get_zooms()[:3]
            # Allow small floating point differences
            assert all(abs(actual - expected) < 0.01 for actual, expected in zip(actual_resolution, expected_resolution)), \
                f"Expected resolution {expected_resolution}, got {actual_resolution}"
    
    return AtlasValidator()


def test_download_AAL(atlas_validator):
    """Test AAL atlas download."""
    
    AAL_atlas = get_AAL()
    
    # Use validator for basic structure checks
    atlas_validator.validate_basic_structure(AAL_atlas, 'AAL')
    
    # Check filename patterns
    assert 'AAL' in AAL_atlas['AtlasImage']
    assert 'MNIColin27' in AAL_atlas['AtlasImage']
    
    # Check file extensions
    assert AAL_atlas['AtlasImage'].endswith('.nii.gz')
    assert AAL_atlas['AtlasTSV'].endswith('.tsv')
    assert AAL_atlas['AtlasJson'].endswith('.json')
    
    # Check that template file exists in the same directory as atlas
    atlas_dir = os.path.dirname(AAL_atlas['AtlasImage'])
    template_file = os.path.join(atlas_dir, 'tpl-MNIColin27_T1w.nii.gz')
    assert os.path.exists(template_file)
    
    # Check that template metadata JSON exists in the same directory
    template_json = os.path.join(atlas_dir, 'tpl-MNIColin27.json')
    assert os.path.exists(template_json)
    
    # Check that atlas description JSON exists in the parent directory
    atlas_parent_dir = os.path.dirname(os.path.dirname(atlas_dir))
    atlas_description_json = os.path.join(atlas_parent_dir, 'atlas-AAL_description.json')
    assert os.path.exists(atlas_description_json)
    
    # Use validator for resolution checks
    atlas_validator.validate_resolution(AAL_atlas['AtlasImage'])
    atlas_validator.validate_resolution(template_file)
    
    # Use validator for TSV structure validation
    tsv_df = atlas_validator.validate_tsv_structure(AAL_atlas['AtlasTSV'], expected_rows=167)
    
    # Check hemisphere values (specific to AAL)
    hemisphere_values = set(tsv_df['Hemisphere'].unique())
    hemisphere_values_clean = {val for val in hemisphere_values if pd.notna(val)}
    expected_hemispheres = {'L', 'R', 'NA'}  # AAL includes 'NA' values
    
    assert hemisphere_values_clean.issubset(expected_hemispheres), f"Unexpected hemisphere values: {hemisphere_values_clean - expected_hemispheres}"


def test_download_Destrieux():
    """Test Destrieux atlas download with default parameters."""
    
    Destrieux_atlas = get_Destrieux()
    
    # Check that the function returns a dictionary with expected keys
    assert isinstance(Destrieux_atlas, dict)
    assert 'AtlasImage' in Destrieux_atlas
    assert 'AtlasTSV' in Destrieux_atlas
    assert 'AtlasJson' in Destrieux_atlas
    
    # Check that files exist and are correctly named
    assert os.path.exists(Destrieux_atlas['AtlasImage'])
    assert os.path.exists(Destrieux_atlas['AtlasTSV'])
    assert os.path.exists(Destrieux_atlas['AtlasJson'])
    
    # Check filename patterns
    assert 'Destrieux' in Destrieux_atlas['AtlasImage']
    assert 'fsaverage' in Destrieux_atlas['AtlasImage']
    assert Destrieux_atlas['AtlasImage'].endswith('.nii.gz')
    assert Destrieux_atlas['AtlasTSV'].endswith('.tsv')
    assert Destrieux_atlas['AtlasJson'].endswith('.json')
    
    # Check that template file exists in the same directory as atlas
    atlas_dir = os.path.dirname(Destrieux_atlas['AtlasImage'])
    template_file = os.path.join(atlas_dir, 'tpl-fsaverage_res-01_T1w.nii.gz')
    assert os.path.exists(template_file)
    
    # Check that template metadata JSON exists in the same directory
    template_json = os.path.join(atlas_dir, 'tpl-fsaverage.json')
    assert os.path.exists(template_json)
    
    # Check that atlas description JSON exists in the parent directory
    atlas_parent_dir = os.path.dirname(os.path.dirname(atlas_dir))
    atlas_description_json = os.path.join(atlas_parent_dir, 'atlas-Destrieux_description.json')
    assert os.path.exists(atlas_description_json)
    
    # Check atlas NIfTI file resolution (should be approximately 1mm)
    atlas_img = nb.load(Destrieux_atlas['AtlasImage'])
    atlas_resolution = atlas_img.header.get_zooms()[:3]  # Get x,y,z resolution
    expected_resolution = (1.0, 1.0, 1.0)
    # Allow small floating point differences
    assert all(abs(actual - expected) < 0.01 for actual, expected in zip(atlas_resolution, expected_resolution)), \
        f"Expected resolution {expected_resolution}, got {atlas_resolution}"
    
    # Check template NIfTI file resolution (should be approximately 1mm)
    template_img = nb.load(template_file)
    template_resolution = template_img.header.get_zooms()[:3]
    # Allow small floating point differences
    assert all(abs(actual - expected) < 0.01 for actual, expected in zip(template_resolution, expected_resolution)), \
        f"Expected template resolution {expected_resolution}, got {template_resolution}"
    
    # Check TSV file structure
    tsv_df = pd.read_csv(Destrieux_atlas['AtlasTSV'], sep='\t', keep_default_na=False)
    
    # Check that TSV has the expected number of rows (Destrieux has 151 regions when lateralized)
    assert len(tsv_df) == 151, f"Expected 151 rows in TSV file, got {len(tsv_df)}"
    
    # Check that TSV has the correct columns
    expected_columns = ['Index', 'Label', 'Hemisphere']
    actual_columns = list(tsv_df.columns)
    assert actual_columns == expected_columns, f"Expected columns {expected_columns}, got {actual_columns}"
    
    # Check that Index column contains integers
    assert tsv_df['Index'].dtype in ['int64', 'int32'], f"Index column should be integer, got {tsv_df['Index'].dtype}"
    
    # Check that Label column contains strings
    assert tsv_df['Label'].dtype == 'object', f"Label column should be string/object, got {tsv_df['Label'].dtype}"
    
    # Check that Hemisphere column contains expected values (L and R for lateralized version)
    hemisphere_values = set(tsv_df['Hemisphere'].unique())
    expected_hemispheres = {'L', 'R', 'NA'}
    assert hemisphere_values.issubset(expected_hemispheres), f"Unexpected hemisphere values: {hemisphere_values - expected_hemispheres}"


@pytest.mark.parametrize("lateralized,expected_rows,description", [
    (True, 151, "lateralized version should have 151 regions"),
    (False, 76, "non-lateralized version should have 76 regions")
])
def test_download_Destrieux_lateralized_parameter(lateralized, expected_rows, description):
    """Test Destrieux atlas download with different lateralized parameters."""
    
    Destrieux_atlas = get_Destrieux(lateralized=lateralized)
    
    # Check that files exist and are correctly named
    assert os.path.exists(Destrieux_atlas['AtlasImage'])
    assert os.path.exists(Destrieux_atlas['AtlasTSV'])
    assert os.path.exists(Destrieux_atlas['AtlasJson'])
    
    # Check filename patterns
    assert 'Destrieux' in Destrieux_atlas['AtlasImage']
    assert 'fsaverage' in Destrieux_atlas['AtlasImage']
    
    # Check TSV file structure
    tsv_df = pd.read_csv(Destrieux_atlas['AtlasTSV'], sep='\t', keep_default_na=False)
    
    # Check expected number of rows based on lateralization
    assert len(tsv_df) == expected_rows, f"Expected {expected_rows} rows ({description}), got {len(tsv_df)}"
    
    # Check that TSV has the correct columns
    expected_columns = ['Index', 'Label', 'Hemisphere']
    actual_columns = list(tsv_df.columns)
    assert actual_columns == expected_columns, f"Expected columns {expected_columns}, got {actual_columns}"
    
    # Check hemisphere values based on lateralization
    hemisphere_values = set(tsv_df['Hemisphere'].unique())
    if lateralized:
        # Lateralized version should have L and R regions
        expected_hemispheres = {'L', 'R', 'NA'}
        assert hemisphere_values.issubset(expected_hemispheres), f"Lateralized version should have L/R regions, got: {hemisphere_values}"
    else:
        # Non-lateralized version should not have distinct L/R regions
        assert 'L' not in hemisphere_values or 'R' not in hemisphere_values, f"Non-lateralized version should not have distinct L/R regions, got: {hemisphere_values}"


def test_download_Destrieux_custom_path(tmp_path):
    """Test Destrieux atlas download with custom path."""
    
    Destrieux_atlas = get_Destrieux(path=str(tmp_path))
    
    # Check that files are created in the specified directory
    assert os.path.exists(Destrieux_atlas['AtlasImage'])
    assert os.path.exists(Destrieux_atlas['AtlasTSV'])
    assert os.path.exists(Destrieux_atlas['AtlasJson'])
    
    # Check that the files are in the specified path
    assert str(tmp_path) in Destrieux_atlas['AtlasImage']
    assert str(tmp_path) in Destrieux_atlas['AtlasTSV']
    assert str(tmp_path) in Destrieux_atlas['AtlasJson']


@pytest.mark.parametrize("file_key,expected_extension", [
    ('AtlasImage', '.nii.gz'),
    ('AtlasTSV', '.tsv'),
    ('AtlasJson', '.json')
])
def test_download_Destrieux_file_extensions(file_key, expected_extension):
    """Test that Destrieux atlas files have correct extensions."""
    
    Destrieux_atlas = get_Destrieux()
    
    # Check that the file exists
    assert os.path.exists(Destrieux_atlas[file_key])
    
    # Check that the file has the expected extension
    assert Destrieux_atlas[file_key].endswith(expected_extension), \
        f"{file_key} should end with {expected_extension}, got {Destrieux_atlas[file_key]}"


@pytest.mark.parametrize("atlas_func,atlas_name,expected_space", [
    (get_AAL, 'AAL', 'MNIColin27'),
    (get_Destrieux, 'Destrieux', 'fsaverage'),
    (get_HarvardOxford, 'HarvardOxford', 'MNI152NLin6Asym'),
    (get_Talairach, 'Talairach', 'MNI152NLin6Asym'),
    (get_Juelich, 'Juelich', 'MNI152NLin6Asym'),
    (get_Schaefer2018, 'Schaefer', 'MNI152NLin6Asym')
])
def test_atlas_basic_functionality(atlas_func, atlas_name, expected_space):
    """Test basic functionality across different atlas functions."""
    
    atlas_result = atlas_func()
    
    # Check that the function returns a dictionary with expected keys
    assert isinstance(atlas_result, dict)
    required_keys = ['AtlasImage', 'AtlasTSV', 'AtlasJson']
    for key in required_keys:
        assert key in atlas_result, f"Missing key {key} in {atlas_name} result"
    
    # Check that all files exist
    for key in required_keys:
        assert os.path.exists(atlas_result[key]), f"{key} file does not exist for {atlas_name}"
    
    # Check that atlas name and space are in the image filename
    assert atlas_name in atlas_result['AtlasImage'], f"Atlas name {atlas_name} not in filename"
    assert expected_space in atlas_result['AtlasImage'], f"Expected space {expected_space} not in filename"


# =============================================================================
# HarvardOxford Atlas Tests
# =============================================================================

def test_download_HarvardOxford():
    """Test HarvardOxford atlas download with default parameters."""
    
    HarvardOxford_atlas = get_HarvardOxford()
    
    # Check that the function returns a dictionary with expected keys
    assert isinstance(HarvardOxford_atlas, dict)
    assert 'AtlasImage' in HarvardOxford_atlas
    assert 'AtlasTSV' in HarvardOxford_atlas
    assert 'AtlasJson' in HarvardOxford_atlas
    
    # Check that files exist and are correctly named
    assert os.path.exists(HarvardOxford_atlas['AtlasImage'])
    assert os.path.exists(HarvardOxford_atlas['AtlasTSV'])
    assert os.path.exists(HarvardOxford_atlas['AtlasJson'])
    
    # Check filename patterns
    assert 'HarvardOxford' in HarvardOxford_atlas['AtlasImage']
    assert 'MNI152NLin6Asym' in HarvardOxford_atlas['AtlasImage']
    assert HarvardOxford_atlas['AtlasImage'].endswith('.nii.gz')
    assert HarvardOxford_atlas['AtlasTSV'].endswith('.tsv')
    assert HarvardOxford_atlas['AtlasJson'].endswith('.json')


@pytest.mark.parametrize("atlas_type,expected_suffix", [
    ('dseg', '_dseg.nii.gz'),
    ('probseg', '_probseg.nii.gz')
])
def test_download_HarvardOxford_type_parameter(atlas_type, expected_suffix):
    """Test HarvardOxford atlas download with different type parameters."""
    
    HarvardOxford_atlas = get_HarvardOxford(type=atlas_type)
    
    # Check that files exist and are correctly named
    assert os.path.exists(HarvardOxford_atlas['AtlasImage'])
    assert os.path.exists(HarvardOxford_atlas['AtlasTSV'])
    assert os.path.exists(HarvardOxford_atlas['AtlasJson'])
    
    # Check filename patterns based on type
    assert 'HarvardOxford' in HarvardOxford_atlas['AtlasImage']
    assert expected_suffix in HarvardOxford_atlas['AtlasImage']


def test_download_HarvardOxford_custom_path(tmp_path):
    """Test HarvardOxford atlas download with custom path."""
    
    HarvardOxford_atlas = get_HarvardOxford(path=str(tmp_path))
    
    # Check that files are created in the specified directory
    assert os.path.exists(HarvardOxford_atlas['AtlasImage'])
    assert os.path.exists(HarvardOxford_atlas['AtlasTSV'])
    assert os.path.exists(HarvardOxford_atlas['AtlasJson'])
    
    # Check that the files are in the specified path
    assert str(tmp_path) in HarvardOxford_atlas['AtlasImage']
    assert str(tmp_path) in HarvardOxford_atlas['AtlasTSV']
    assert str(tmp_path) in HarvardOxford_atlas['AtlasJson']


# =============================================================================
# Talairach Atlas Tests
# =============================================================================

def test_download_Talairach():
    """Test Talairach atlas download with default parameters."""
    
    Talairach_atlas = get_Talairach()
    
    # Check that the function returns a dictionary with expected keys
    assert isinstance(Talairach_atlas, dict)
    assert 'AtlasImage' in Talairach_atlas
    assert 'AtlasTSV' in Talairach_atlas
    assert 'AtlasJson' in Talairach_atlas
    
    # Check that files exist and are correctly named
    assert os.path.exists(Talairach_atlas['AtlasImage'])
    assert os.path.exists(Talairach_atlas['AtlasTSV'])
    assert os.path.exists(Talairach_atlas['AtlasJson'])
    
    # Check filename patterns
    assert 'Talairach' in Talairach_atlas['AtlasImage']
    assert 'MNI152NLin6Asym' in Talairach_atlas['AtlasImage']
    assert Talairach_atlas['AtlasImage'].endswith('.nii.gz')
    assert Talairach_atlas['AtlasTSV'].endswith('.tsv')
    assert Talairach_atlas['AtlasJson'].endswith('.json')


@pytest.mark.parametrize("level", ['hemisphere', 'lobe', 'gyrus', 'tissue', 'ba'])
def test_download_Talairach_level_parameter(level):
    """Test Talairach atlas download with different level parameters."""
    
    Talairach_atlas = get_Talairach(level=level)
    
    # Check that files exist and are correctly named
    assert os.path.exists(Talairach_atlas['AtlasImage'])
    assert os.path.exists(Talairach_atlas['AtlasTSV'])
    assert os.path.exists(Talairach_atlas['AtlasJson'])
    
    # Check filename patterns
    assert 'Talairach' in Talairach_atlas['AtlasImage']
    assert 'MNI152NLin6Asym' in Talairach_atlas['AtlasImage']


def test_download_Talairach_custom_path(tmp_path):
    """Test Talairach atlas download with custom path."""
    
    Talairach_atlas = get_Talairach(path=str(tmp_path))
    
    # Check that files are created in the specified directory
    assert os.path.exists(Talairach_atlas['AtlasImage'])
    assert os.path.exists(Talairach_atlas['AtlasTSV'])
    assert os.path.exists(Talairach_atlas['AtlasJson'])
    
    # Check that the files are in the specified path
    assert str(tmp_path) in Talairach_atlas['AtlasImage']
    assert str(tmp_path) in Talairach_atlas['AtlasTSV']
    assert str(tmp_path) in Talairach_atlas['AtlasJson']


# =============================================================================
# Juelich Atlas Tests
# =============================================================================

def test_download_Juelich():
    """Test Juelich atlas download with default parameters."""
    
    Juelich_atlas = get_Juelich()
    
    # Check that the function returns a dictionary with expected keys
    assert isinstance(Juelich_atlas, dict)
    assert 'AtlasImage' in Juelich_atlas
    assert 'AtlasTSV' in Juelich_atlas
    assert 'AtlasJson' in Juelich_atlas
    
    # Check that files exist and are correctly named
    assert os.path.exists(Juelich_atlas['AtlasImage'])
    assert os.path.exists(Juelich_atlas['AtlasTSV'])
    assert os.path.exists(Juelich_atlas['AtlasJson'])
    
    # Check filename patterns
    assert 'Juelich' in Juelich_atlas['AtlasImage']
    assert 'MNI152NLin6Asym' in Juelich_atlas['AtlasImage']
    assert Juelich_atlas['AtlasImage'].endswith('.nii.gz')
    assert Juelich_atlas['AtlasTSV'].endswith('.tsv')
    assert Juelich_atlas['AtlasJson'].endswith('.json')


@pytest.mark.parametrize("atlas_type,expected_suffix", [
    ('dseg', '_dseg.nii.gz'),
    ('probseg', '_probseg.nii.gz')
])
def test_download_Juelich_type_parameter(atlas_type, expected_suffix):
    """Test Juelich atlas download with different type parameters."""
    
    Juelich_atlas = get_Juelich(type=atlas_type)
    
    # Check that files exist and are correctly named
    assert os.path.exists(Juelich_atlas['AtlasImage'])
    assert os.path.exists(Juelich_atlas['AtlasTSV'])
    assert os.path.exists(Juelich_atlas['AtlasJson'])
    
    # Check filename patterns based on type
    assert 'Juelich' in Juelich_atlas['AtlasImage']
    assert expected_suffix in Juelich_atlas['AtlasImage']


@pytest.mark.parametrize("symmetric_split", [True, False])
def test_download_Juelich_symmetric_split_parameter(symmetric_split):
    """Test Juelich atlas download with different symmetric_split parameters."""
    
    Juelich_atlas = get_Juelich(symmetric_split=symmetric_split)
    
    # Check that files exist and are correctly named
    assert os.path.exists(Juelich_atlas['AtlasImage'])
    assert os.path.exists(Juelich_atlas['AtlasTSV'])
    assert os.path.exists(Juelich_atlas['AtlasJson'])
    
    # Check filename patterns
    assert 'Juelich' in Juelich_atlas['AtlasImage']


def test_download_Juelich_custom_path(tmp_path):
    """Test Juelich atlas download with custom path."""
    
    Juelich_atlas = get_Juelich(path=str(tmp_path))
    
    # Check that files are created in the specified directory
    assert os.path.exists(Juelich_atlas['AtlasImage'])
    assert os.path.exists(Juelich_atlas['AtlasTSV'])
    assert os.path.exists(Juelich_atlas['AtlasJson'])
    
    # Check that the files are in the specified path
    assert str(tmp_path) in Juelich_atlas['AtlasImage']
    assert str(tmp_path) in Juelich_atlas['AtlasTSV']
    assert str(tmp_path) in Juelich_atlas['AtlasJson']


# =============================================================================
# Schaefer2018 Atlas Tests
# =============================================================================

def test_download_Schaefer2018():
    """Test Schaefer2018 atlas download with default parameters."""
    
    Schaefer_atlas = get_Schaefer2018()
    
    # Check that the function returns a dictionary with expected keys
    assert isinstance(Schaefer_atlas, dict)
    assert 'AtlasImage' in Schaefer_atlas
    assert 'AtlasTSV' in Schaefer_atlas
    assert 'AtlasJson' in Schaefer_atlas
    
    # Check that files exist and are correctly named
    assert os.path.exists(Schaefer_atlas['AtlasImage'])
    assert os.path.exists(Schaefer_atlas['AtlasTSV'])
    assert os.path.exists(Schaefer_atlas['AtlasJson'])
    
    # Check filename patterns
    assert 'Schaefer' in Schaefer_atlas['AtlasImage']
    assert 'MNI152NLin6Asym' in Schaefer_atlas['AtlasImage']
    assert Schaefer_atlas['AtlasImage'].endswith('.nii.gz')
    assert Schaefer_atlas['AtlasTSV'].endswith('.tsv')
    assert Schaefer_atlas['AtlasJson'].endswith('.json')


@pytest.mark.parametrize("n_rois,roi_annotation", [
    ('100', '7'), ('200', '7'), ('400', '7'),
    ('100', '17'), ('200', '17'), ('400', '17')
])
def test_download_Schaefer2018_parameters(n_rois, roi_annotation):
    """Test Schaefer2018 atlas download with different parameter combinations."""
    
    Schaefer_atlas = get_Schaefer2018(n_rois=n_rois, roi_annotation=roi_annotation)
    
    # Check that files exist and are correctly named
    assert os.path.exists(Schaefer_atlas['AtlasImage'])
    assert os.path.exists(Schaefer_atlas['AtlasTSV'])
    assert os.path.exists(Schaefer_atlas['AtlasJson'])
    
    # Check filename patterns include the parameters
    assert 'Schaefer' in Schaefer_atlas['AtlasImage']
    assert n_rois in Schaefer_atlas['AtlasImage']
    assert roi_annotation in Schaefer_atlas['AtlasImage']


def test_download_Schaefer2018_custom_path(tmp_path):
    """Test Schaefer2018 atlas download with custom path."""
    
    Schaefer_atlas = get_Schaefer2018(path=str(tmp_path))
    
    # Check that files are created in the specified directory
    assert os.path.exists(Schaefer_atlas['AtlasImage'])
    assert os.path.exists(Schaefer_atlas['AtlasTSV'])
    assert os.path.exists(Schaefer_atlas['AtlasJson'])
    
    # Check that the files are in the specified path
    assert str(tmp_path) in Schaefer_atlas['AtlasImage']
    assert str(tmp_path) in Schaefer_atlas['AtlasTSV']
    assert str(tmp_path) in Schaefer_atlas['AtlasJson']
