
import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # Annetaan StatisticsService-luokan oliolle stub-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        player = self.stats.search("Semenko")

        self.assertEqual(player.name, "Semenko")

    def test_search_finds_player_with_partial_name(self):
        player = self.stats.search("Gret")

        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none_if_player_not_found(self):
        player = self.stats.search("Messi")

        self.assertIsNone(player)

    def test_team_returns_players_of_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_returns_empty_list_if_team_not_found(self):
        players = self.stats.team("XXX")

        self.assertEqual(players, [])

    def test_top_returns_correct_number_of_players(self):
        players = self.stats.top(3)

        self.assertEqual(len(players), 3)

    def test_top_returns_players_in_points_order(self):
        players = self.stats.top(3)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman", "Lemieux"]
        )


if __name__ == "__main__":
    unittest.main()

