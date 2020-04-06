import os

__dir__ = os.path.abspath(os.path.dirname(__file__))

ATLAS_DIR = os.path.join(__dir__, 'atlases')
TOPOLOGY_LUT_DIR = os.path.join(ATLAS_DIR, 'topology_lut')
DEFAULT_ATLAS = os.path.join(ATLAS_DIR, 'brain-segmentation-prior3.0',
                             'brain-atlas-3.0.3.txt')

DEFAULT_MASSP_ATLAS = os.path.join(ATLAS_DIR, 'massp-prior')
DEFAULT_MASSP_INTENSITY = os.path.join(DEFAULT_MASSP_ATLAS,'massp_19structures_mp2rageme_histograms.nii.gz')
DEFAULT_MASSP_SPATIAL_PROBA = os.path.join(DEFAULT_MASSP_ATLAS,'massp_19structures_spatial_proba.nii.gz')
DEFAULT_MASSP_SPATIAL_LABEL = os.path.join(DEFAULT_MASSP_ATLAS,'massp_19structures_spatial_label.nii.gz')
DEFAULT_MASSP_SKEL_PROBA = os.path.join(DEFAULT_MASSP_ATLAS,'massp_19structures_skeleton_proba.nii.gz')
DEFAULT_MASSP_SKEL_LABEL = os.path.join(DEFAULT_MASSP_ATLAS,'massp_19structures_skeleton_label.nii.gz')
