from leaderboard.data import Result


class TestResults:
    def test_parse(self):
        result = Result('Team A 2, Team B 0')
        result.parse()

        assert result._teams == ['Team A', 'Team B']
        assert result._scores == [2, 0]

    def test_parse_long(self):
        result = Result('Team Name Long A 3, Team Name Long B 3')
        result.parse()

        assert result._teams == ['Team Name Long A', 'Team Name Long B']
        assert result._scores == [3, 3]

    def test_team_data(self):
        result = Result('A 0, B 1')
        response = result.team_data('Team Name 0')
        assert response == ('Team Name', 0)

    def test_draw(self):
        result = Result('A 0, B 0')
        result.parse()
        assert result.draw() is True

    def test_not_draw(self):
        result = Result('A 1, B 0')
        result.parse()
        assert result.draw() is False

    def test_winning_team(self):
        result = Result('A 1, B 0')
        result.parse()
        assert result.winning_team() == 'A'
