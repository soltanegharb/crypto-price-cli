# Crypto Price CLI

A simple command-line interface (CLI) application that allows you to check the latest price of your requested cryptocurrency.

## Features
- Get real-time cryptocurrency prices.
- Easy-to-use command-line interface.

## Installation

```sh
# Clone the repository
git clone https://github.com/soltanegharb/crypto-price-cli.git

# Navigate to the project directory
cd crypto-price-cli

# Install dependencies

# Clone the repository
git clone https://github.com/soltanegharb/crypto-price-cli.git

# Navigate to the project directory
cd crypto-price-cli

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

```

## Usage

```sh
python crypto_cli.py crypto_name
```

Example:

```sh
# for 2 random cryptos 
python crypto_cli.py
# for bitcoin
python crypto_cli.py bitcoin
# for mantle
python crypto_cli.py mantle
```

## Output
### for randomly generated
```sh
Data successfully saved in storage/crypto_data.pkl
USDC: $0.999964
Rocket Pool ETH: $2105.06
.
.
.
```
### for bitcoin
```sh
Fetching cryptocurrency data...
Data successfully saved in storage/crypto_data.pkl
Bitcoin: $82648
```
## Arguments
- positional crypto name: The name of the cryptocurrency you want to check (e.g., bitcoin, mantle, solana).


## Requirements
- install requirements.txt (using pip install -r requirements.txt)

## License
MIT License

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author
[Mohammad Hossein Soltani](https://github.com/soltanegharb)
