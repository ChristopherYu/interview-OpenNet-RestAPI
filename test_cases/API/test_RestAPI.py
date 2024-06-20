import os
import json
import requests
from pathlib import Path


class TestRestAPI:

    @staticmethod
    def _get_current_test_data_path():
        """
        Gets the current test data path.
        :return:
        """
        path = Path(os.path.abspath(os.getcwd()))
        return path.parent.parent.absolute()

    def test_poetry_author(self, api_default_data: dict):
        """
        test given field: [author], and then return author listing
        :param api_default_data: dict of default datas
        :return None:
        """
        file_path = Path(self._get_current_test_data_path(), "Interview", "interview-OpenNet", "test_data",
                         "authors.json")
        print(file_path)
        try:
            with open(file_path, "r") as file:
                expected_result = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError
        except json.decoder.JSONDecodeError:
            raise json.decoder.JSONDecodeError

        url = api_default_data['url'] + "/author"

        response = requests.get(url, headers=api_default_data["headers"])
        assert response.status_code == 200
        assert response.json() == expected_result

    def test_poetry_spec_author(self, api_default_data: dict):
        """
        test given specification author, and then get correct data
        :param api_default_data: dict of default data
        :return None:
        """

        file_path = Path(self._get_current_test_data_path(), "Interview", "interview-OpenNet", "test_data",
                         "authors_Thomas.json")
        try:
            with open(file_path, "r") as file:
                expected_result = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError
        except json.decoder.JSONDecodeError:
            raise json.decoder.JSONDecodeError

        url = api_default_data['url'] + "/author/Thomas Gray"

        response = requests.get(url, headers=api_default_data["headers"])
        assert response.status_code == 200
        assert response.json() == expected_result
