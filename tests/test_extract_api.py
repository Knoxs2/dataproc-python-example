import json
from unittest.mock import patch
from src.extract_api import fetch_data

@patch("src.extract_api.requests.get")
def test_fetch_data(mock_get, tmp_path):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"id": 1, "title": "test"}]
    output_file = tmp_path / "data.json"
    
    data = fetch_data("http://mock.api", str(output_file))
    assert output_file.exists()
    with open(output_file) as f:
        saved = json.load(f)
    assert saved == [{"id": 1, "title": "test"}]
    assert data == saved
