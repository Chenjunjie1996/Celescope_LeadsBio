import celescope.tools.utils as utils
from celescope.tools.star_mixin import Star_mixin, get_opts_star_mixin


class Star_virus(Star_mixin):
    """
    star virus class
    """

    def __init__(self, args, display_title=None):
        # before init
        args.genomeDir = args.virus_genomeDir

        super().__init__(args, add_prefix='virus', display_title=display_title)

    def run(self):
        self.run_star()


@utils.add_log
def star_virus(args):
    with Star_virus(args, display_title='Mapping') as runner:
        runner.run()


def get_opts_star_virus(parser, sub_program):
    get_opts_star_mixin(parser, sub_program)
    parser.add_argument('--virus_genomeDir', help='virus genome dir', required=True)
