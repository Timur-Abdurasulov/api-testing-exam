import pytest
from utils.api_client import ApiClient


@pytest.fixture(scope="class")
def api_client(request):
    url = getattr(request.cls, "url", "")
    return ApiClient(url)
