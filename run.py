import argparse
from fractions import Fraction

from experiment import Experiment

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--numerator',
        help='numerator of probability',
        action='store',
        required=True,
        type=int
    )
    parser.add_argument(
        '-d',
        '--denominator',
        help='denominator of probability',
        action='store',
        required=True,
        type=int
    )
    parser.add_argument(
        '-e',
        '--numepisodes',
        help='number of episodes to run',
        action='store',
        type=int,
        default=10000
    )
    args = parser.parse_args()

    experiment = Experiment(Fraction(args.numerator, args.denominator))
    result = experiment.run_experiment(num_episodes=args.numepisodes)
    print("Result: {0} from {1:,} episodes. Expected result is {2:.5f}".format(
        result, args.numepisodes, args.numerator / args.denominator))
