'''
Author: Aastha Saxena
Purpose: Handling exceptions and validation

Details:
Read CSV File and store data in the dictionary.
Each key in the dictionary should be a string, as read from the CSV file. The value of that key will be a Python list. 
You will use this dictionary for the next three modules.
Take input from the user 
Calculate worldwide statistics (min, max, average) for a user-entered year
Plot the emissions data from a user-selected country. 
Plot a comparison graph based on user input.
'''
import csv
from matplotlib import pyplot as plt 

def get_key(dict,n):
    for i,j in dict.items():
        if j==str(n):
            return i


def main():
    try:
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
        while True:
            input_year = input("Select a year to find statistics (1997 to 2010):")
            if not input_year.isdigit() or not 1997 <= int(input_year) <= 2010:
                print("Sorry the year is not valid year.")
                continue
            else:
                break

            try:
                for key,year_list in data_dict.items():
              
                    if key == 'CO2 per capita':
                        year_index = year_list.index(input_year)
                        print("year_index",year_index)
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

            except ValueError:
                print("Year not found!")
                return
        
        
        
        # ask user to select the country for which plot of emissions is required
        while True:
            country= input("Select the country to visualize:")
            if country in data_dict.keys():

            
                for k,l in data_dict.items():
                    if k=='CO2 per capita':
                    #x axis of the plot as years 
                        x=[int(y) for y in l]
                    if k.lower()==country.lower():
                    #y axis of the plot as emissions data from a user-selected country
                        y=[float(emission) for emission in l]
                # Function to plot 
                plt.title('Year vs Emissions in capita') 
                # naming of x-axis and y-axis 
                plt.xlabel('Year') 
                plt.ylabel('Emissions in '+country) 
                plt.plot(x,y) 
           
                # function to show the plot 
                plt.show()
                break
            else:
                print("Sorry that is not a valid country.")
                continue
         
        

        ##Compare two countries emission graphs
         
        while True:

            try:
                country_one, country_two = [x for x in input("Write two comma-seperated countries for which  you want to visualize data:").split(',')] 
                print("\nThe value of country_oneis {} and country_two  is {}".format(country_one, country_two)) 
            except ValueError:
                print("Incorrect Input entered, Please try again!!")
                continue
            if country_one not in data_dict.keys() or country_two not in data_dict.keys(): 
                print("Sorry that is not a valid Country.")
                continue
            else:
                x1=[]
                y1,y2=[],[]
                for k1,l1 in data_dict.items():
                    
                    if k1=='CO2 per capita':
                            #x axis of the plot as years 
                        x1=[int(y) for y in l1]
                    if k1.lower()==country_one.lower():
                            #y axis of the plot as emissions data from a user-selected country
                        y1=[float(emission) for emission in l1]
                    if k1.lower()==country_two.lower():
                        y2=[float(emission) for emission in l1]
                    

                plt.title('Year vs Emissions in capita') 
                    # naming of x-axis and y-axis        
                plt.xlabel('Year') 
                plt.ylabel('Emissions in '+country_one+" and "+country_two)     
                plt.plot(x1,y1,label=country_one)
                plt.plot(x1,y2,label=country_two)
                plt.show()
                break
            
        while True:
            try:    
                countries = [x for x in input("Write up to three comma-seperated countries for which you want to extract data:").split(',')] 

            except ValueError:
                print("Please enter again.")
                continue
            if len(countries)>3 or len(countries)<0:
                print("ERR: Sorry, at most 3 countries can be entered")
                continue
            
            else:
                
                row_list=[]
                for key, value in data_dict.items():
                    if key=='CO2 per capita':
                        
                        temp = [key]
                        for v in value:
                            temp.append(int(v))
                        row_list.append(temp)
                    if key.lower() == countries[0].lower() or key.lower() == countries[1].lower() or key.lower()== countries[2].lower():
                        temp = [key]
                        for v in value:
                            temp.append(float(v))
                        row_list.append(temp)   
                           
       
                with open('Emissions_subset.csv','w',newline='') as file:
                    writer = csv.writer(file,delimiter=',')
                    writer.writerows(row_list)
                print("Data successfully extracted for countries",countries[0], countries[1], countries[2])

                break
    except FileNotFoundError:
        print("File not found......")
    except IOError:
        print("Output filr can't be saved.")    
   
#driver code
if __name__=='__main__':
    main() 