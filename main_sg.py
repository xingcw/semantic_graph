from utils import tab_printer
from sg_net import SGTrainer
from parser_sg import sgpr_args
import sys


def main():
    """
    Parsing command line parameters, reading data, fitting and scoring a SimGNN model.
    """
    args = sgpr_args()
    if len(sys.argv) > 1:
        args.load(sys.argv[1])
    else:
        args.load('./config/config.yml')
    tab_printer(args)
    trainer = SGTrainer(args, True)
    trainer.fit()
    trainer.score()


if __name__ == "__main__":
    main()
