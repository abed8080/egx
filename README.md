# egx

[![PyPI](https://img.shields.io/pypi/v/egx)](https://pypi.org/project/egx/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/egx)](https://pypi.org/project/egx/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


An unofficial API wrapper for the Egyptian Exchange that lets you fetch historical and intraday index data.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install egx.

```bash
pip install egx
```

## Usage

```python
import egx

# List all available indices
print(egx.get_supported_indices())
# {'EGX30_CAP', 'EGXVolatility', 'EGX30_TR', 'EGX100_EWI', 'EGX30', 'EGX70_EWI', 'EGX_33_Shariah'}

# Fetch EGX30 data for the current day
df = egx.get_index_data("EGX30")
print(df.head())

# Fetch EGX30 data for the last year
df_1y = egx.get_index_data("EGX30", period=365)
print(df_1y.head())
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
