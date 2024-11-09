import unittest
from unittest.mock import MagicMock, patch

from src.api_hh import HH


class TestHH(unittest.TestCase):
    @patch("requests.get")
    def test_load_vacancies(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "items": [
                {"name": "Менеджер по логистике и ВЭД", "salary": "120000"},
                {"name": "Диспетчер - логист", "salary": "100000"},
            ]
        }
        mock_get.return_value = mock_response
        hh = HH()
        hh.load_vacancies("Менеджер по логистике и ВЭД")
        self.assertGreater(len(hh.vacancies), 0)
        self.assertEqual(hh.vacancies[0]["name"], "Менеджер по логистике и ВЭД")
        mock_get.assert_called_with(
            "https://api.hh.ru/vacancies",
            headers={"User-Agent": "HH-User-Agent"},
            params={"text": "Менеджер по логистике и ВЭД", "page": 20, "per_page": 100},
        )


if __name__ == "__main__":
    unittest.main()
