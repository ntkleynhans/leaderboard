from collections import defaultdict
from functools import cmp_to_key


class TeamPoints(object):
    def __init__(self, team_name, score):
        self._team_name = team_name
        self._score = score

    @property
    def team_name(self):
        return self._team_name

    @property
    def score(self):
        return self._score


class LeaderTable(object):
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
        for result in feed:
            if not result.draw():
                self.table[result.winning_team()] += self.config['WIN_PTS']
            else:
                for team in result.teams():
                    self.table[team] += self.config['DRAW_PTS']

    @staticmethod
    def compare(a, b):
        """
            Complex objective sort comparison function

            First sort team by scores,
            then by Team name if teams have equal points
        """
        if a.score != b.score:
            return b.score - a.score
        else:
            if a.team_name < b.team_name:
                return -1
            elif a.team_name > b.team_name:
                return 1
            return 0

    def present(self):
        """
            Returns a formatted leaderboard

            Teams are racked by totals then by name (given the same totals)
        """
        table_entries = [TeamPoints(team_name, score)
                         for team_name, score in self.table.items()]
        table_entries.sort(key=cmp_to_key(LeaderTable.compare))
        for entry in table_entries:
            yield f"{entry.team_name}, {entry.score} pts\n"
