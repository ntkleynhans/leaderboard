class Result(object):
    def __init__(self, result):
        self._result = result
        self._teams = []
        self._scores = []

    def parse(self):
        """
            Parse a results file entry

            Result format is Team_Name Score, Team_Name Score

            Parameters:
            self.result (str): line of text in result entry format

            Returns:
            None
        """
        for team_pair in self._result.split(','):
            name, score = self.team_data(team_pair)
            self._teams.append(name)
            self._scores.append(score)

    def team_data(self, team_score):
        """
            Extract team name and score

            Parameters:
            team_score (str): text containing a team score pair
                (e.g. Team_Name Score)

            Returns:
            tuple: team_name, score
        """
        *name, score = team_score.split()
        return ' '.join(name), int(score)

    def draw(self):
        """
            Determine if match was a draw

            Returns:
            bool
        """
        return self._scores.count(self._scores[0]) == 2

    def winning_team(self):
        """
            Find winning team name

            Returns:
            str: winning team name
        """
        return self._teams[self._scores.index(max(self._scores))]

    def teams(self):
        """
            Return extracted team names

            Returns:
            list[str]: team names
        """
        return self._teams


class ResultsParser(object):
    def __init__(self, infile):
        self._infile = infile

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        text = self._infile.readline().strip()
        if not len(text):
            raise StopIteration()
        result = Result(text)
        result.parse()
        return result
