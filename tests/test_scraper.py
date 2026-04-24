import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from egx import INDICES, get_index_data


@pytest.mark.parametrize("index_name", list(INDICES)[:2])
@patch("requests.get")
def test_get_index_data_success(mock_get, index_name):
    # Mock successful API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"CDAY": "2024-01-01", "INDEX_VALUE": 25000.5},
        {"CDAY": "2024-01-02", "INDEX_VALUE": 25100.2},
    ]
    mock_get.return_value = mock_response

    df = get_index_data(index_name)

    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["date", "value"]
    assert len(df) == 2
    assert pd.api.types.is_datetime64_any_dtype(df["date"])
    assert df["value"].iloc[0] == 25000.5


@patch("requests.get")
def test_get_index_data_empty_response(mock_get):
    # Mock empty API response
    mock_response = MagicMock()
    mock_response.json.return_value = []
    mock_get.return_value = mock_response

    df = get_index_data("EGX30")

    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert list(df.columns) == ["date", "value"]


def test_invalid_index_raises_error():
    with pytest.raises(ValueError, match="Invalid index:"):
        get_index_data("WRONG_INDEX")
