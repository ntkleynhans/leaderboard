import pytest

from leaderboard.process import LeaderTable


@pytest.fixture()
def resource():
    CONFIG = {
        'WIN_PTS': 3,
        'DRAW_PTS': 1
    }
    yield LeaderTable(CONFIG)


class TestLeaderTable:
    def test_collect(self, resource):
        data = [[['A', 'B'], [1, 0]], [['A', 'B'], [0, 0]]]
        resource.collect(data)
        assert resource.table['A'] == 4
        assert resource.table['B'] == 1

    def test_present(self, resource):
        resource.table = {'A': 4, 'B': 1, 'C': 3, 'D': 1}
        text = [line for line in resource.present()]
        assert text == ['A, 4 pts\n', 'C, 3 pts\n', 'B, 1 pts\n', 'D, 1 pts\n']
