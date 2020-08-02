'''
Author: Aastha Saxena

Details:
Read CSV File and store data in the dictionary.
Each key in the dictionary should be a string, as read from the CSV file. The value of that key will be a Python list. 
You will use this dictionary for the next three modules.
Take input from the user 
Calculate worldwide statistics (min, max, average) for a user-entered year
Plot the emissions data from a user-selected country. 
'''
import csv
from matplotlib import pyplot as plt 

def get_key(dict,n):
    for i,j in dict.items():
        if j==str(n):
            return i


def main():
    data_dict={}
    # reading the file and storing in a dictionary
    filename = 'Emissions.csv'
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data_dict[row[0]] = row[1:]
    output_file_writer = open("data_dict.txt","w+")
    output_file_writer.write(str(data_dict))
    output_file_writer.close()
    print("All data from Emissions.csv has been read into a dictionary.")
    print('\n')
    input_year = input("Select a year to find statistics (1997 to 2010):")
    for key,year_list in data_dict.items():
        try:
            if key == 'CO2 per capita':
                year_index = year_list.index(input_year)
                print("year_index",year_index)

        except ValueError:
            print("Year not found!")
            return
    
    # a dictionary for storing country: emissions record for the asked year
    value_year_dict={}
    for i,values_list in data_dict.items():
        value_year_dict[i]=values_list[year_index]
    del value_year_dict['CO2 per capita']  
    list_of_dict_values=[float(values) for values in value_year_dict.values()]
    #find the minimum maximum and average value
    max_value=max(list_of_dict_values)
    min_value=min(list_of_dict_values)
    average_value=sum(list_of_dict_values)/len(list_of_dict_values)
    min_value_countries=[get_key(value_year_dict,min_value)]
    max_value_countries=[get_key(value_year_dict,max_value)]
    
    
    print("In %s,countries with minimum and maximum CO2 emission levels were: %s and %s respectively. Average CO2 emissions in %s were %0.6f" %(input_year, min_value_countries,max_value_countries,input_year,average_value))  
    print("\n")
    # ask user to select the country for which plot of emissions is required
    country= input("Select the country to visualize:")
    if country not in data_dict.keys():
        print("Data for country %s not found!" %(country))
        return 
    for k,l in data_dict.items():
        if k=='CO2 per capita':
            #x axis of the plot as years 
            x=[int(y) for y in l]
        if k==country:
            #y axis of the plot as emissions data from a user-selected country
            y=[float(emission) for emission in l]
  
    # Function to plot 
    plt.plot(x,y) 
       
    # function to show the plot 
    plt.show() 

#driver code
if __name__=='__main__':
    main()