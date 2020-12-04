import sys
import argparse
import logging

from leaderboard.data import ResultsParser
from leaderboard.process import LeaderTable

logger = logging.getLogger('leaderBoard')

CONFIG = {
    'WIN_PTS': 3,
    'DRAW_PTS': 1
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?',
                        type=argparse.FileType('r'), default=sys.stdin,
                        help="input file containing results")
    parser.add_argument('outfile', nargs='?',
                        type=argparse.FileType('w'), default=sys.stdout,
                        help="ouput leader board")
    args = parser.parse_args()

    try:
        df = ResultsParser(args.infile)
        table = LeaderTable(CONFIG)

        table.collect(df)
        for team_entry in table.present():
            args.outfile.write(team_entry)
    except Exception as e:
        logger.error(str(e))
