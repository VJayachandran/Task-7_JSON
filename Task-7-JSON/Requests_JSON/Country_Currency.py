import requests

#Functions to fetch country data and currency
class CountryCurrency:
    def __init__(self, api_url):
        self.api_url = api_url
        self.countries_data = self.fetch_country_data()

    def fetch_country_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch data from API")

    def display_currencies(self):
        for country in self.countries_data:
            country_name = country.get('name', {}).get('common', 'Unknown')
            currencies = country.get('currencies', {})

            if currencies:
                for currency_code, currency_info in currencies.items():
                    currency_name = currency_info.get('name', 'Unknown')
                    currency_symbol = currency_info.get('symbol', 'No symbol')
                    print(f"Country: {country_name}, Currency: {currency_name}, Symbol: {currency_symbol}")
            else:
                print(f"Country: {country_name}, Currency: No currencies listed")


# Usage
if __name__ == "__main__":
    api_url = "https://restcountries.com/v3.1/all"
    country_currency = CountryCurrency(api_url)
    country_currency.display_currencies()