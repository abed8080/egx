import requests
import pandas as pd

BASE_URL = "https://www.egx.com.eg/WebService.asmx"

INDICES = {
    "EGX30",
    "EGX_33_Shariah",
    "EGXVolatility",
    "EGX100_EWI",
    "EGX70_EWI",
    "EGX30_CAP",
    "EGX30_TR",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com/",
}


def get_supported_indices() -> set:
    """Return the set of supported EGX indices."""
    return set(INDICES)


def get_index_data(index: str, period: int = 0) -> pd.DataFrame:
    """Fetch historical data for a given EGX index.

    Args:
        index: The name of the index (e.g., 'EGX30').
        period: Time period in days. Defaults to 0 (current day).

    Returns:
        A pandas DataFrame with 'date' and 'value' columns.

    Raises:
        ValueError: If the provided index is not in the set of supported indices.
        requests.exceptions.RequestException: If the request fails.
    """
    # Validate index name
    if index not in INDICES:
        raise ValueError(f"Invalid index: {index}. Choose from {INDICES}")

    params = {"index": index, "period": period, "gtk": 0}

    response = requests.get(
        f"{BASE_URL}/getIndexChartData", params=params, headers=HEADERS
    )
    response.raise_for_status()

    data = response.json()
    if not data:
        return pd.DataFrame(columns=["date", "value"])

    df = pd.DataFrame(data)

    # Rename columns to more user-friendly names
    df = df.rename(columns={"CDAY": "date", "INDEX_VALUE": "value"})

    # Convert date to datetime objects
    df["date"] = pd.to_datetime(df["date"])

    # Ensure data is sorted by date ascending
    df = df.sort_values("date").reset_index(drop=True)

    return df
