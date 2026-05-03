# Sean Summers Assignment 7.2 
#  Function to return a city, country value pair in this format: City, Country
def print_city(city, country, population=None, language=None):
    if population: # if population is provided, include it, otherwise, don't.
        if language: # if language is provided, include it, otherwise, don't.
            return f"{city.title()}, {country.title()} - population {population}, {language.title()}"
        else:
            return f"{city.title()}, {country.title()} - population {population}"
    else:
        if language: # if language is provided, include it, otherwise, don't.
            return f"{city.title()}, {country.title()}, {language.title()}"
        else:
            return f"{city.title()}, {country.title()}"

# Prompt the user for how many times they want the program to run.
num_times = int(input("How many times do you want to enter a city and country? "))

# Loop the function the number of times specified by the user, redefining the city and country each time. 
for _ in range(num_times):
    city = input("Enter the name of a city: ") # Define the city variable

    country = input("Enter the name of the corresponding country: ") # Define the country variable

    population = input("Enter the population of the city: ") # Define the population variable

    language = input("What is the language of this country? ") # Define the language variable

    results = print_city(city, country, population, language) # Call the function and store the result in a variable.
    print(results) # Print the result.
    print() # Blank line for readability