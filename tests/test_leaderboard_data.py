import pytest

from leaderboard.data import ResultsParser


@pytest.fixture()
def resource():
    yield ResultsParser(None)


class TestResultsParser:
    def test_parse(self, resource):
        result = resource.parse('Team A 2, Team B 0')
        assert result == [['Team A', 'Team B'], [2, 0]]
        result = resource.parse('Team Name Long A 2, Team Name Long B 0')
        assert result == [['Team Name Long A', 'Team Name Long B'], [2, 0]]

    def test_team_data(self, resource):
        result = resource.team_data('Team Name 0')
        assert result == ('Team Name', 0)
