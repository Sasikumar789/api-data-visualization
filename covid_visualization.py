import json
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data():
    with open("covid_data.json", "r") as f:
        data = json.load(f)
    return data

def process_data(data, country):
    countries = data['Countries']
    df = pd.DataFrame(countries)
    country_data = df[df['Country'].str.lower() == country.lower()]
    if not country_data.empty:
        return country_data.iloc[0]
    else:
        print("Country not found.")
        return None

def visualize_data(country_data):
    labels = ['Total Confirmed', 'Total Deaths', 'Total Recovered']
    values = [
        country_data['TotalConfirmed'],
        country_data['TotalDeaths'],
        country_data['TotalRecovered']
    ]
    
    plt.figure(figsize=(8,5))
    plt.bar(labels, values, color=['blue', 'red', 'green'])
    plt.title(f"COVID-19 Stats for {country_data['Country']}")
    plt.show()

def main():
    data = fetch_data()
    country = input("Enter the country name (e.g., India): ")
    country_data = process_data(data, country)
    if country_data is not None:
        print(f"\nShowing COVID-19 stats for {country_data['Country']}:")
        print(f"Total Confirmed Cases: {country_data['TotalConfirmed']}")
        print(f"Total Deaths: {country_data['TotalDeaths']}")
        print(f"Total Recovered: {country_data['TotalRecovered']}\n")
        visualize_data(country_data)

if __name__ == "__main__":
    main()
