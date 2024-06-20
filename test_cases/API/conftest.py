import pytest


@pytest.fixture(scope="session")
def api_default_data() -> dict:
    headers = {"Content-Type": "application/json"}
    url = "https://poetrydb.org"
    return {"url": url, "headers": headers}
