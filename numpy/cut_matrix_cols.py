import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Cut matrix to desired number of cols and save')
parser.add_argument('-m', '--matrix', required=True, type=str,
                    help='Input Matrix path')
parser.add_argument('-o', '--out', required=True, type=str,
                    help='Output Matrix path')
parser.add_argument('-n', required=True, type=int,
                    help='Number of columns in output')

args = parser.parse_args()
A = np.loadtxt(args.matrix)
np.savetxt(args.out, A[:, :args.n], fmt="%d")

