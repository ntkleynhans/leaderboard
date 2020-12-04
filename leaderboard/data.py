class ResultsParser(object):
    def __init__(self, infile):
        self.infile = infile

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        text = self.infile.readline().strip()
        if not len(text):
            raise StopIteration()
        return self.parse(text)

    def parse(self, entry):
        """
            Parse a results file entry

            Entry format is Team_Name Score, Team_Name Score

            Parameters:
            entry (str): line of text in result entry format

            Returns:
            str: result in nested array
                ([[Team_name, Team_name], [Score, Score]])
        """
        result = [[], []]
        for team_pair in entry.split(','):
            name, score = self.team_data(team_pair)
            result[0].append(name)
            result[-1].append(score)
        return result

    def clean(self):
        """
            Clean a result entry
        """
        raise NotImplementedError()

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
