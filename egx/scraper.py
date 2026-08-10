import pandas as pd
import requests

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
    """Fetch data for a given EGX index.

    Args:
        index: The name of the index (e.g., 'EGX30').
        period: Number of calendar days to look back from. Only trading
            days within that window are returned, so the number of rows
            may be less than `period` (e.g. weekends/holidays are
            excluded). Defaults to 0, which returns intraday data for
            the latest trading day instead of historical daily data.

    Returns:
        A pandas DataFrame. When period=0, contains intraday
        observations for today, or an empty
        DataFrame if the market is closed today (e.g. weekend or
        holiday) or has not yet opened. When period > 0, contains one
        row per trading day.

    Raises:
        ValueError: If the provided index is not in the set of supported indices.
        requests.exceptions.RequestException: If the request fails.
    """
    # Validate index name
    if index not in INDICES:
        raise ValueError(
            f"Invalid index: {index}. See get_supported_indices() for valid options."
        )

    params = {"index": index, "period": period, "gtk": 0}

    response = requests.get(
        f"{BASE_URL}/getIndexChartData", params=params, headers=HEADERS
    )
    response.raise_for_status()

    data = response.json()
    if not data:
        return pd.DataFrame(columns=["datetime", "value"])

    df = pd.DataFrame(data)

    # Rename columns to more user-friendly names
    df = df.rename(columns={"CDAY": "datetime", "INDEX_VALUE": "value"})

    # Convert date to datetime objects
    df["datetime"] = pd.to_datetime(df["datetime"])

    # Ensure data is sorted by date ascending
    df = df.sort_values("datetime").reset_index(drop=True)

    return df
