# Travel Aggregator Analysis

## Overview
This project aims to analyze travel-related data to uncover patterns, insights and trends that can help improve the services offered by **MyNextBooking**. The data analysis focuses on customer behaviour, booking patterns, and platform performance metrics using two datasets: **Booking.csv** and **Sessions.csv**

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
    * `booking_id`: Booking associated with the session (if applicable).
