"""
Welcome to a Data Anlytics Project Using Python
This is a Python Project of data analysis, where we take a dataset of a flight, by which we have to find some insights and solutions of the problem that occure in the flight. To expain Every point line by line I am going to visualize the data by which i gonna get some insights from it.

Let's Get Started......
First we have to load the dataset on which we are going to perform that action, the data is available on kaggle so I am going to fetch it from there and load in my google colab.

Link of the dataset : https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction
"""

# Importing the python modules for performing the different task on dataset
import pandas as pd
import matplotlib.pyplot as plt

# After loading the modules of python, I am going to load the dataset to perform the EDA Task means Exploratory Data
# Analysis, but for EDA first we have to clean the dataset.

# Loading the data set in google colab
flight_df = pd.read_csv("data//Clean_Dataset.csv")

# Now first we check the top 5 values of dataset
flight_df.head()

# According to head method we get the top 5 data of dataset, now first I need to analyse the data and explain about
# all the columns that are present in the given dataset.

# Let me find the columns name separately
print(flight_df.columns)

# We have total 12 columns and some of them are not important so we have to remove some column from it.

# Now we have to find the summary of the dataset.
print(flight_df.info())

"""According to the info method, I analyse that their is no null values in dataset, and all the columns are of object type except days_left and price.
In the dataset, duration, days_left, and price are not important column, so I am going to remove it."""
print(flight_df.drop(["duration", "days_left", "price"], axis=1))

# Next I am describing the dataset for the statical analysis
print(flight_df.describe(include="all"))

# Next I am going to find the category and its value count from airline column
print(flight_df["airline"].value_counts())

"""According to the value_count method, I get that Vistara airlines are used so much by peoples, and spiceJet airline is used very less.
For Making this analysis more easy, I am going to plot a bar graph to represent these flights in visual form."""

plt.figure(figsize=(10, 7))
flight_name = ["Vistara", "Air_India", "Indigo", "Go_First", "AirAsia", "SpiceJet"]
flight_count = flight_df["airline"].value_counts()
plt.bar(flight_name, flight_count, color="pink")
plt.xlabel("Airlines Name")
plt.ylabel("Counts")
plt.show()

# Now we have to count the total counts of the city form where the flight is board.
print(flight_df["departure_time"].value_counts())

"""According to count function, I analyse that maximum passengers are taking their flight in Morning, and very less passengers taking their flight in late night.
Now to make the analysis more easy , i am going to plat a bar chart to represent the departure time."""

plt.figure(figsize=(10, 7))
departure_count = flight_df["departure_time"].value_counts()
plt.title('Departure_Time Count')
plt.pie(departure_count, autopct='%.2f', labels=departure_count.index)
plt.show()

# Now I am going to find the flight count value according to departure time.

# Evening departure flight Count
evening = flight_df[flight_df["departure_time"] == "Evening"]
print(evening["airline"].value_counts())

plt.figure(figsize=(12, 6))
plt.title("Flight count for Evening")
plt.plot(evening["airline"].value_counts(), label="Evening")
plt.xlabel("Airlines")
plt.ylabel("Flight Count")
plt.legend()
plt.show()

# Morning departure Flight Count
morning = flight_df[flight_df["departure_time"] == "Morning"]
print(morning["airline"].value_counts())

plt.figure(figsize=(12, 6))
plt.title("Flight count for Morning")
plt.plot(morning["airline"].value_counts(), label="Morning", color="orange")
plt.xlabel("Airlines")
plt.ylabel("Flight Count")
plt.legend()
plt.show()

# Early Morning departure flight count
early_morning = flight_df[flight_df["departure_time"] == "Early_Morning"]
print(early_morning["airline"].value_counts())

plt.figure(figsize=(12, 6))
plt.title("Flight count for Early Morning")
plt.plot(early_morning["airline"].value_counts(), color="pink", label="Evening")
plt.xlabel("Airlines")
plt.ylabel("Flight Count")
plt.legend()
plt.show()

# Afternoon departure flight count.
afternoon = flight_df[flight_df["departure_time"] == "Afternoon"]
print(afternoon["airline"].value_counts())

plt.figure(figsize=(12, 6))
plt.title("Flight count for afternoon")
plt.plot(afternoon["airline"].value_counts(), color="green", label="Evening")
plt.xlabel("Airlines")
plt.ylabel("Flight Count")
plt.legend()
plt.show()

# Night departure flight count
night = flight_df[flight_df["departure_time"] == "Night"]
print(night["airline"].value_counts())

plt.figure(figsize=(12, 6))
plt.title("flight count for Night")
plt.plot(night["airline"].value_counts(), color="gray", label="Night")
plt.xlabel("Airlines")
plt.ylabel("Flight Count")
plt.legend()
plt.show()

# Late Night departure flight count
late_night = flight_df[flight_df["departure_time"] == "Late_Night"]
print(late_night["airline"].value_counts())

plt.figure(figsize=(12, 6))
plt.title("Flight count for Night")
plt.plot(late_night["airline"].value_counts(), color="red", label="Light Night")
plt.xlabel("Airline")
plt.ylabel("Flight Count")
plt.legend()
plt.show()

# From the above analysis and visualization Vistara is the only flight who board by passangers.

# Source City Analysis
print(flight_df["source_city"].value_counts())

# According to above analysis Delhi is the source city, from where the maximum passengers board their flight,
# and Chennai is the source city from where the passengers board less flight.

# Now I just create a visual presentation for better presentation
source_city_count = flight_df["source_city"].value_counts()
print(source_city_count)

plt.figure(figsize=(10, 7))
plt.title('Source City Count')
plt.pie(source_city_count, autopct='%.2f', labels=source_city_count.index)
plt.show()

# According to this analysis, I know that in delhi city maximum people use the flight.

# Checking the departure time in different city
mumbai = flight_df[flight_df["source_city"] == "Mumbai"]
delhi = flight_df[flight_df["source_city"] == "Delhi"]
banglore = flight_df[flight_df["source_city"] == "Banglore"]
kolkata = flight_df[flight_df["source_city"] == "Kolkata"]
hyderabad = flight_df[flight_df["source_city"] == "Hyderabad"]
chennai = flight_df[flight_df["source_city"] == "Chennnai"]

plt.figure(figsize=(12, 6))
plt.title("Departure time count in different city")
plt.plot(mumbai["departure_time"].value_counts(), color="red", label="Mumbai")
plt.plot(delhi["departure_time"].value_counts(), color="blue", label="Delhi")
plt.plot(banglore["departure_time"].value_counts(), color="green", label="Banglore")
plt.plot(kolkata["departure_time"].value_counts(), color="purple", label="Kolkata")
plt.plot(hyderabad["departure_time"].value_counts(), color="yellow", label="Hyderabad")
plt.plot(chennai["departure_time"].value_counts(), color="grey", label="Chennai")
plt.xlabel("Cities")
plt.ylabel("Passengers Count")
plt.legend()
plt.show()

# Now we have to count the total counts of arrival time form where the flight is land.
print(flight_df["arrival_time"].value_counts())

# Now to make the analysis more easy , I am going to plat a bar chart to represent the arrival time.
plt.figure(figsize=(10, 7))
arrival_count = flight_df["arrival_time"].value_counts()
plt.title('Arrival Count')
plt.pie(arrival_count, autopct='%.2f', labels=arrival_count.index)
plt.show()


print(flight_df["destination_city"].value_counts())

# Now I just create a visual presentation for better presentation.
destination_count = flight_df["destination_city"].value_counts()
print(destination_count)

plt.figure(figsize=(10, 7))
plt.title('Destination City Count')
plt.pie(destination_count, autopct='%.2f', labels=destination_count.index)
plt.show()

# Maximum stopage analysis
print(flight_df["stops"].value_counts())

# Visual representation of above data
stops_count = flight_df["stops"].value_counts()
print(stops_count)

plt.figure(figsize=(10, 7))
plt.title('Stops Count')
plt.pie(stops_count, autopct='%.2f', labels=stops_count.index)
plt.show()

# Analysis said that count of one stop is maximum as compare to others.

# Flight_count that takes one stop
one = flight_df[flight_df["stops"] == "one"]
print(one["airline"].value_counts())

plt.figure(figsize=(12, 6))
plt.title("Flight count that take on stops")
plt.plot(one["airline"].value_counts(), label="One_Stop", color="red")
plt.xlabel("Airlines")
plt.ylabel("Flight Count")
plt.legend()
plt.show()

# In One stop Vistara is the top flight.

# Flight classes

# Counting of passengers class
print(flight_df["class"].value_counts())

plt.figure(figsize=(10, 7))
flight_name = ["Economy", "Business"]
flight_count = flight_df["class"].value_counts()
plt.bar(flight_name, flight_count, color="pink")
plt.xlabel("Flight Class")
plt.ylabel("Counts")
plt.show()

# Maximum Passengers who board their flight are taking economy class.

# Flight Count for max booking in economy
economy = flight_df[flight_df["class"] == "Economy"]
print(economy["airline"].value_counts())

plt.figure(figsize=(12, 6))
plt.title("Flight count")
plt.plot(economy["airline"].value_counts(), label="Economy", color="red")
plt.xlabel("Airlines")
plt.ylabel("Count")
plt.legend()
plt.show()

# Vistara is the airline in which maximum economy clases are booked.

# Flight Count for max booking in Business
business = flight_df[flight_df["class"] == "Business"]
print(business["airline"].value_counts())

plt.figure(figsize=(12, 6))
plt.title("Flight count")
plt.plot(business["airline"].value_counts(), label="Business", color="brown")
plt.xlabel("Airlines")
plt.ylabel("Count")
plt.legend()
plt.show()

"""Vistara is the airline in which passengers book their flight in business class.

Insights

Vistara is the only flight who is comes in top in every analysis.

In this flight analysis we see that vistara do something good by which he is on the top, So we have to improve the other flights by adopting some changes from vistara.

For improving the other flight first we have to decrease the prices of morning flight, by this we overcome from two thing one is pasangers attract to the flight and also the average passengers prefer morning time so no. of passengers.

Also we have to manage the departure time, means scheduling of flights."""
