"""
Wimbledon Champions Data Processor

Estimate Time : 50 minutes
Actual Time : 28 February 2025 (12:00 pm - 12:50 pm)

This program reads data from 'wimbledon.csv', process it to :
- Display each champion's name and the number of times they have won.
- Display the countries of the champions in alphabetical order
"""
import csv

FILENAME = "wimbledon.csv"

def main() :
    """Load Wimbledon data, process it, and display the champions and their countries"""
    champions, countries = load_data(FILENAME)
    display_champions(champions)
    display_countries(countries)

def load_data(filename) :
    """Read the Wimbledon data file and return processed information"""
    champions = {}
    countries = set()

    with open (filename, "r", encoding = "utf-8") as file :
        reader = csv.reader (file)
        next(reader) # Skip header row

        for row in reader :
            champion,country = row[2], row[1]

            #Count wins per champion
            champions[champion] = champions.get(champion,0) + 1

            #Collect unique countries
            countries.add (country)
        return champions, countries

def display_champions (champions) :
    """Display the champions and their number of wins"""
    print ("Wimbledon Champions: ")
    for champion, wins in sorted (champions.items()) :
        print(f"{champion} : {wins}")

def display_countries (countries) :
    """Display the countries of the champions in alphabetical order"""
    print("\nCountries of Champions: ")
    print(",".join(sorted(countries)))

main()