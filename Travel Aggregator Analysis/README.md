# Travel Aggregator Analysis

## Overview
This project aims to analyze travel-related data to uncover patterns, insights and trends that can help improve the services offered by **MyNextBooking**. The data analysis focuses on customer behaviour, booking patterns, and platform performance metrics using two datasets: [**Booking.csv**](Data/Bookings.csv) and [**Sessions.csv**](Data/Sessions.csv)

------
## Objectives 
The projects answers the following key questions:
1. Count the number of distinct **bookings**, **sessions** and **searches** from the provided datasets.
2. Identify how many sessions have more than one bookings. 
3. Determine which days of the week have the highest bookings and visualize the distribution using a pie chart.
4. For each **service name**, calculate the total bookings and the total gross booking value (gbv) in INR.
5. For customers with more than one booking, find the most booked route(`from_city` to `to_city`).
6. Identify the top 3 departure cities where customers book the most in advance, considering cities with at least 5 departures.
7. Generate a heatmap displaying correlation of numerical columns and report the pair with the maximum correlation.
8. Identify the most used device type for making bookings on the platform, grouped by service name.
9. Plot quartely trends for the number of bookings by each device type using a time series.
10. Compute and analyze the overall booking-to-search-ratio(oBSR): 
    * Calculate the average oBSR for each month
    * Calculate the average oBSR for each day of the week
    * Plot a time series of oBSR for all available dates.

------

## Data Description
The data consist of two csv files:
1. Bookings.csv
    * `customer_id`: Unique identifier for a customer.
    * `booking_id`: Unique identifier for a booking.
    * `from_city`: Departure city.
    * `from_country`: Departure country.
    * `to_city`: Destination city.
    * `to_country`: Destination country.
    * `booking_time`: Timestamp of booking.
    * `device_type_used`: Device type used for booking.
    * `INR_Amount`: Gross Booking Value (GBV) in INR.
    * `service_name`: Platform used for booking (e.g., Yatra, MMT, Goibibo).
    * `no_of_passengers`: Number of passengers in the booking.
    * `days_to_departure`: Days remaining until departure.
    * `distance_km`: Distance of the journey in kilometers.

2. Sessions.csv

    * `session_id`: Unique identifier for a session.
    * `search_id`: Unique identifier for a search.
    * `search_time`: Timestamp of search.
    * `session_starting_time`: Session start time.
    * `booking_id`: Booking associated with the session.

-------

## Installation
1. Clone the repository
```bash
git clone https://github.com/antonygatua/Data-Science-Projects.git
cd 'Travel Aggregator Analysis'
```
2. Install Dependecies
```bash
pip install -r requirements.txt
```
3. Prepare data 
Place the `Booking.csv` and `Sessions.csv` files in the `data/` directory.

-----

## Usage 

* **Data Preprocessing**: Run the preprocessing script to clean and merge the data.
```bash
python preprocess.py
```

* **Analysis Scripts**: Use the analysis scripts to answer specific questions.
```bash 
python analyze_bookings.py
python analyze_sessions.py
```

* **Visualizations**: Generate visualizations (e.g., pie chart, heatmaps, time series) by running:
```bash 
python visualize_data.py
```

* **Interactive reports**: Open Jupyter notebooks in the `notebooks/` directory for interactive analysis.

-----

## Project Test 
```plaintext
Travel Aggregator Analysis/
│
├── data/                     # Raw and processed datasets
├── notebooks/                # Jupyter Notebooks for exploratory analysis
├── src/                      # Source code for data preprocessing and analysis
│   ├── preprocess.py         # Data cleaning and merging script
│   ├── analyze_bookings.py   # Analysis for bookings-related questions
│   ├── analyze_sessions.py   # Analysis for sessions-related questions
│   ├── visualize_data.py     # Scripts for generating plots and visualizations
├── tests/                    # Unit tests for validation
├── requirements.txt          # Python dependencies
└── README.md                 # Project README
```

------

## Visualizations

* **Pie Chart**: Distribution of bookings by day of the week.
* **Heatmap**: Correlations of numerical columns in the bookings dataset.
* **Time Series**: Trends in quarterly bookings by device type.
* **oBSR Trends**: Time series of booking-to-search ratios by date.

------

## Contribution Guidelines

I welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Added feature-name"`).
4. Push the branch (`git push origin feature-name`).
5. Open a pull request.

-----

## Contact 

You can reach me at:

* **Email**: [mailto:antonnymuiko@gmail.com](mailto:antonnymuiko@gmail.com)
* **LinkedIn**: [Antonny Muiko](https://www.linkedin.com/in/antonny-muiko-1b5aaa162/)

-----