import click
import argparse
import random
import os

from datetime import timedelta, datetime
from dotenv import load_dotenv

from storage.storage import PickleFiles
from api import FetchRequest
from data_processor import IterateOverData


def main():
    load_dotenv()
    caching_file = os.getenv('caching_file')
    api_to_fetch = os.getenv('api_to_fetch')

    fetchreq = FetchRequest()
    
    with PickleFiles() as pklf:
        try:
            iterator_obj = IterateOverData(caching_file, file_handler=PickleFiles, open_mode="rb")
        except Exception as e:
            api_response = fetchreq.get(api_to_fetch=api_to_fetch)
            api_response_json = api_response.json()
            pklf.dump(to_be_written=api_response_json, file_path=caching_file, mode="wb")
            iterator_obj = IterateOverData(caching_file, file_handler=PickleFiles, open_mode="rb")

        else:
            crypto_list = [crypto for crypto in iterator_obj]
            last_updated_crypto_str = crypto_list[0]['last_updated'].replace("Z","")
            last_updated_crypto_date = datetime.fromisoformat(last_updated_crypto_str)

            time_of_now = datetime.now()
            time_difference = time_of_now - last_updated_crypto_date
            allowed_time_difference = timedelta(hours=1)

            if time_difference > allowed_time_difference:
                api_response = fetchreq.get(api_to_fetch=api_to_fetch)
                api_response_json = api_response.json()
                pklf.dump(to_be_written=api_response_json, file_path=caching_file, mode="wb")
                iterator_obj = IterateOverData(caching_file, file_handler=PickleFiles, open_mode="rb")
    crypto_list = [crypto for crypto in iterator_obj]

    parser = argparse.ArgumentParser(description="here you can check the price for crypto")
    parser.add_argument("name", nargs="?", type=str, help="name of the crypto")
    args = parser.parse_args()

    if not args.name:
        click.echo("Fetching cryptocurrency data...")
        click.echo(f"Data successfully saved ", nl = False)
        click.secho(f"in", fg = "red", nl = False)
        click.echo(f" {caching_file}")

        for _ in range(2):
            crypto = random.choice(crypto_list)
            click.secho(f"{crypto['name']}: ", fg='white', nl=False)
            click.secho(f"${str(crypto['current_price'])[0]}", bold=True, nl=False, fg="magenta")
            click.secho(f"{str(crypto['current_price'])[1:]}", fg='magenta')
        for _ in range(3):
            print(".")
    else:
        click.echo("Fetching cryptocurrency data...")
        click.echo(f"Data successfully saved ", nl = False)
        click.secho(f"in", fg = "red", nl = False)
        click.echo(f" {caching_file}")
        for crypto in crypto_list:
            if crypto["id"] == args.name:
                click.secho(f"{crypto['name']}: ", fg='white', nl=False)
                click.secho(f"${str(crypto['current_price'])[0]}", 
                            bold=True, nl=False, fg="magenta"
                            )
                click.secho(f"{str(crypto['current_price'])[1:]}", fg='magenta')

if __name__ == "__main__":
    main()