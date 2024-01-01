# Flight Data Analysis Project ✈️📊

## Introduction

This project revolves around an in-depth analysis of flight data aiming to gain insights and identify potential areas for improvement. The dataset used for this analysis is sourced from Kaggle. [Dataset Link](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)

## Objective

The goal of this analysis is to explore the flight data, understand various parameters influencing passenger choices, and propose actionable insights to enhance the overall flight experience.

## Data Loading and Cleaning

The project begins by importing necessary Python modules, including pandas and matplotlib. The dataset is loaded into a Google Colab notebook from the provided CSV file ('Clean_Dataset.csv').

Data cleaning involves dropping unnecessary columns ('duration', 'days_left', 'price') to streamline the dataset for analysis purposes.

## Dataset Overview

- Displaying the top 5 rows of the dataset and listing column names.
- Summary of dataset information using `info()` and `describe()` methods.
- Analysis reveals no null values, and most columns are of object type, except for 'days_left' and 'price'.

## Exploratory Data Analysis (EDA)

### Airline Analysis

- Analyzing the frequency of various airlines in the dataset.
- Visualizing airline frequency using a bar graph to highlight passenger preferences.

### Departure Time Analysis

- Investigating departure time trends.
- Plotting departure time counts and respective airline distributions for different times of the day.

### Source City Analysis

- Exploring the departure time distribution across cities.
- Visualizing the distribution of departure times for various cities.

### Arrival Time and Destination Analysis

- Analyzing arrival time distributions and passenger trends.
- Visualizing the distribution of arrival times and top destination cities.

### Stops and Flight Class Analysis

- Investigating the frequency of flights with different numbers of stops.
- Analyzing passenger class preferences - Economy vs. Business.

## Insights and Recommendations

- **Vistara**: Identified as the dominant airline across various analyses.
- **Recommendations**:
  - Reducing morning flight prices to attract more passengers.
  - Optimizing flight schedules to accommodate passenger preferences.

## Conclusion

This analysis provides valuable insights into passenger behaviors and preferences, highlighting areas for improvement in the airline industry.

## Future Scope

- Implementing predictive modeling for demand forecasting.
- Incorporating customer feedback analysis for service enhancement.

## Credits

- **Dataset:** [Kaggle](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)
