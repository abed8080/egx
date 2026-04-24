# egx

A Python library for fetching index data from the Egyptian Exchange (EGX).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install egx.

```bash
pip install egx
```

## Usage

```python
import egx

# List all available indices
print(egx.INDICES)
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
