import argparse
import os
from pathlib import Path
from bids_atlas.datasets import get_AAL, get_Destrieux, get_HarvardOxford


# define parser to collect required inputs
def get_parser():

    __version__ = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                    '_version.py')).read()

    parser = argparse.ArgumentParser(description='a CLI for accessing commonly used publicly available atlases in a BIDS-Atlas compliant form')
    parser.add_argument('bids_atlas_dir', action='store', type=Path, help='The directory where the atlas should be stored.')
    parser.add_argument('atlas', help='Atlas to download in a BIDS-Atlas compliant form.',
                        choices=['AAL', 'Destrieux', 'HarvardOxford', 'Schaefer100'])
    parser.add_argument('--target_space',
                        help='Target space the atlas should be provided in.'
                        'Currently, only MNI152NLin6Asym is available.',
                        choices=['MNI152NLin6Asym'])
    parser.add_argument('--resolution', help='Resolution the atlas should be provided in.',
                        choices=['1', '2'])
    parser.add_argument('--type', help='Type the atlas should be provided in. (Only for Harvard-Oxford)',
                        choices=['pseg', 'dseg'])
    parser.add_argument('--threshold', help='Threshold the atlas should be provided in. (Only for Harvard-Oxford)',
                        choices=['25', '50'])
    parser.add_argument('-v', '--version', action='version',
                        version='BIDS-Atlas version {}'.format(__version__))

    return parser


# define the CLI
def run_bids_atlas():

    # get arguments from parser
    args = get_parser().parse_args()

    # special variable set in the container
    if os.getenv('IS_DOCKER'):
        exec_env = 'singularity'
        cgroup = Path('/proc/1/cgroup')
        if cgroup.exists() and 'docker' in cgroup.read_text():
            exec_env = 'docker'
    else:
        exec_env = 'local'

    # check which atlas should be downloaded and run the respective function
    if args.atlas == 'AAL':

        # download the AAL atlas and set user-defined input
        get_AAL(target_space='MNI152NLin6Asym', resolution=args.resolution, path=args.bids_atlas_dir)

    elif args.atlas == 'Destrieux':

        # download the Destrieux atlas and set user-defined input
        get_Destrieux(target_space='MNI152NLin6Asym', resolution=args.resolution, path=args.bids_atlas_dir)

    elif args.atlas == 'HarvardOxford':

        # download the Harvard-Oxford atlas and set user-defined input
        get_HarvardOxford(target_space='MNI152NLin6Asym', type=args.type, threshold=args.threshold,
                          resolution=args.resolution, path=args.bids_atlas_dir)


# run the CLI
if __name__ == "__main__":

    run_bids_atlas()
