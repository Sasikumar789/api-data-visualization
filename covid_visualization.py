import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# File paths (update if needed)
# -----------------------------
deaths_path = r"C:\Users\Sasik\OneDrive\coding folder\meetmux product devloper project\full_data.csv"
mortality_path = r"C:\Users\Sasik\OneDrive\coding folder\meetmux product devloper project\excess_mortality.csv"
vaccinations_path = r"C:\Users\Sasik\OneDrive\coding folder\meetmux product devloper project\vaccinations.csv"

# -----------------------------
# Load CSV files
# -----------------------------
deaths_df = pd.read_csv(deaths_path)
mortality_df = pd.read_csv(mortality_path)
vaccinations_df = pd.read_csv(vaccinations_path)

# -----------------------------
# Functions
# -----------------------------
def get_country_stats(country_name):
    country_cases = deaths_df[deaths_df['location'] == country_name]
    country_vax = vaccinations_df[vaccinations_df['location'] == country_name]
    country_mortality = mortality_df[mortality_df['location'] == country_name]

    total_deaths = country_cases['total_deaths'].max() if not country_cases.empty else 0
    total_vaccinations = country_vax['total_vaccinations'].max() if not country_vax.empty else 0
    excess_mortality = country_mortality['excess_mortality'].max() if not country_mortality.empty else 0

    return {
        "Country": country_name,
        "Total Deaths": total_deaths,
        "Total Vaccinations": total_vaccinations,
        "Excess Mortality": excess_mortality
    }

def visualize_country_stats(stats):
    labels = ['Total Deaths', 'Total Vaccinations', 'Excess Mortality']
    values = [stats['Total Deaths'], stats['Total Vaccinations'], stats['Excess Mortality']]

    plt.figure(figsize=(10,6))
    bars = plt.bar(labels, values, color=['blue', 'red', 'green'])
    
    # Log scale for better visibility of deaths
    plt.yscale('log')
    
    # Annotate bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f'{int(height):,}', 
                 ha='center', va='bottom', fontsize=10)
    
    plt.title(f"COVID-19 Stats for {stats['Country']}")
    plt.ylabel("Counts (log scale)")
    plt.show()

# -----------------------------
# Main program
# -----------------------------
def main():
    country_name = input("Enter country name: ").strip()
    stats = get_country_stats(country_name)
    
    if stats['Total Deaths'] == 0 and stats['Total Vaccinations'] == 0:
        print(f"No data found for {country_name}. Check spelling or CSV files.")
    else:
        print("\nCOVID-19 Stats:")
        for k, v in stats.items():
            if isinstance(v, (int, float)):
                print(f"{k}: {v:,}")
            else:
                print(f"{k}: {v}")
        visualize_country_stats(stats)


if __name__ == "__main__":
    main()
