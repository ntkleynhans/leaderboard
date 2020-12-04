from collections import defaultdict
from functools import cmp_to_key

class Table(object):
    def __init__(self, config):
        self.table = defaultdict(int)
        self.config = config
    
    def collect(self, feed):
        """
            Collect results and process the team scores

            Parameters:
            feed (generator): returns a processed result in nested array format

            Returns:
            None
        """
        for teams, scores in feed:
            if scores.count(scores[0]) != 2:
                team = teams[scores.index(max(scores))]
                self.table[team] += self.config['WIN_PTS']
            else:
                for team in teams:
                    self.table[team] += self.config['DRAW_PTS']

    @staticmethod
    def compare(a, b):
        if a[-1] != b[-1]:
            return b[-1] - a[-1]
        else:
            if a[0] < b[0]:
                return -1
            elif a[0] > b[0]:
                return 1
            return 0

    def present(self):
        """
            Returns a formatted leaderboard

            Teams are racked by totals then by name (given the same totals)
        """
        entries = list(self.table.items())
        entries.sort(key=cmp_to_key(Table.compare))
        for team, score in entries:
           yield f"{team}, {score} pts\n" 
