import pandas as pd
import numpy as np

from typing import List, Dict 


def unique_counts(data: pd.DataFrame, columns: List[str]) -> Dict[str, int]:
    """
    Retrieve the unique counts for specified columns in a DataFrame.
    """
    # check if input is a DataFrame 
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    # validate all the columns exist in the DataFrame
    for col in columns:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' does not exist in the DataFrame.")
        
    # calculate the unique counts for each column 
    unique_counts = {col: data[col].nunique() for col in columns}

    return unique_counts

def group_count_and_filter(data: pd.DataFrame, group_by: List[str], count_column: str, threshold: int) -> pd.Series:
    """ 
    Group a DataFrame by specified columns, count occurrences, and filter rows exceeding a threshold
    """

    # check if DataFrame 
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")
    
    # validate group by columns
    for col in group_by:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' does not exist in the DataFrame")
        
    # validate count columns
    if count_column not in data.columns:
        raise ValueError(f"Column '{count_column}' does not exist in the DataFrame")
    
    # group by specified columns and count occurrences
    grouped_data = data.groupby(group_by)[count_column].count().sort_values(ascending=False)

    # filter rows where the count exceeds the threshold
    filtered_data = grouped_data[grouped_data > threshold]

    return filtered_data
    
def bookings_by_day(data: pd.DataFrame, datetime_column: str) -> Dict[str, int]:
    """ 
    Count bookings by day of the week from a Datetime column.
    """
    # check if input DataFrame 
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a DataFrame.")
    # check if the datetime columns does exist
    if datetime_column not in data.columns:
        raise ValueError(f"Column '{datetime_column}' does not exist in the DataFrame.")
    # check if the column is in datetime format 
    if not pd.api.types.is_datetime64_any_dtype(data[datetime_column]):
        raise ValueError(f"Column '{datetime_column}' must be in datetime fortmat.")
    
    # Extract the day of the week and count bookings 
    day_counts = data[datetime_column].dt.day_name().value_counts().to_dict()

    return day_counts

def aggregate_bookings(data: pd.DataFrame, group_by: List[str], agg_columns: Dict[str, tuple]) -> pd.DataFrame:
    """ 
    Aggregate booking data by grouping and calcultaing specific metrics
    """
    # check if data is dataframe 
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    # check if the group by columns exist
    for col in group_by:
        if col not in data.columns:
            raise ValueError(f"Grouping column '{col}' does not exist in the DataFrame")
        
    # check if all aggregation columns exist
    for col, _ in agg_columns.values():
        if col not in data.columns:
            raise ValueError(f"Aggregation column '{col}' does not exist in the DataFrame")
        
    # perform group aggregation 
    aggregated_data = data.groupby(group_by).agg(**agg_columns).reset_index()

    return aggregated_data

def get_customer_with_multiple_bookings(data: pd.DataFrame, customer_column: str, booking_column:str, threshold: int) -> pd.Index:
    """ 
    Identify customers with more than one booking.
    """
    # check if data is DataFrame
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")
    # check if columns are in DataFrame
    if (customer_column not in data.columns):
        raise ValueError(f"Customer column '{customer_column}' does not exist in the DataFrame")
    elif (booking_column not in data.columns):
        raise ValueError(f"Booking column '{booking_column}' does not exist in the DataFrame")
    
    # group by customers and count their bookings
    customer_booking_counts = data.groupby(customer_column)[booking_column].count()

    # filter customers with more than threshold
    return customer_booking_counts[customer_booking_counts > threshold].index

def get_most_booked_route(data: pd.DataFrame, customer_column: str, from_column: str, to_column: str, booking_column: str, threshold: int) -> pd.Series:
    """ 
    Find the most booked routes for customers with a certain threshold of bookings.
    """
    # check if input is DataFrame 
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be DataFrame")
    # validate columns 
    columns = [customer_column, from_column, to_column, booking_column]

    for col in columns:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' does not exist in the DataFrame")
    
    # filter customers with more than threshold bookings
    multi_booking_customers = get_customer_with_multiple_bookings(data, customer_column, booking_column, threshold)

    # filter data for these customers 
    filtered_data = data[data[customer_column].isin(multi_booking_customers)]

    # group by routes and count bookings 
    most_booked_routes = filtered_data.groupby([from_column, to_column]).agg(Bookings_Count = (booking_column, "count")).sort_values(by="Bookings_Count", ascending=False)

    return most_booked_routes

def top_depature_cities_advanced_bookings(
        data: pd.DataFrame, from_city: str, days_to_depature: str, booking_column: str, 
        advanced_threshold: int, min_depatures: int, top_n: int
) -> pd.DataFrame:
    """ 
    Identify the top depature cities where customers book mostly in advance
    """
    # check if input is DataFrame 
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")
    # validate columns
    columns = [from_city, days_to_depature, booking_column]
    for col in columns:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' does not exist in the DataFrame")
    # validate int parameters
    if not isinstance(advanced_threshold, int) or (advanced_threshold < 0):
        raise ValueError(f"{advanced_threshold} must be a positive interger")
    if not isinstance(min_depatures, int) or (min_depatures < 0):
        raise ValueError(f"{min_depatures} must be a positive interger")
    if not isinstance(top_n, int) or (top_n <= 0):
        raise ValueError(f"{top_n} must be a positive interger greater than 0")
    
    # filter rows where bookings are made in advance 
    advanced_bookings = data[data[days_to_depature] > advanced_threshold]

    # Group by departure city and count bookings 
    city_bookings_count = advanced_bookings.groupby(from_city).agg(Booking_Count=(booking_column, "count")).reset_index()

    # filter cities with at least the minimum number of departures 
    filtered_cities = city_bookings_count[city_bookings_count['Booking_Count'] >= min_depatures]

    # sort by booking count in descending order
    top_cities = filtered_cities.sort_values(by='Booking_Count', ascending=False).head(top_n)

    return top_cities.reset_index(drop=True)

def numerical_correlation(data: pd.DataFrame, numerical_cols: List[str]) -> pd.DataFrame:
    """ 
    Calculate the correlation matrix for specified numerical columns in a pandas DataFrame
    """
    # check if input is DataFrame
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")
    
    # validate numerical cols
    for col in numerical_cols:
        if (col not in data.columns):
            raise ValueError(f"Column '{col}' does not exist in the DataFrame")
        elif not pd.api.types.is_numeric_dtype(data[col]):
            raise TypeError(f"Column '{col}' must be of numeric data type")
    
    # calculate correlation 
    correlation_maxtrix = data[numerical_cols].corr()

    return correlation_maxtrix

def device_type_by_service(data: pd.DataFrame, service_column: str, device_column: str, booking_column: str) -> pd.DataFrame:
    """ 
    Identify the most common device type used for bookings for each service
    """
    # check if data is DataFrame
    if  not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")
    # validate the columns 
    columns = [service_column, device_column, booking_column]

    for col in columns:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' does not exist in the DataFrame")
    
    # group by service and device type, count bookings 
    grouped_data = data.groupby([service_column, device_column]).agg(Bookings_Count=(booking_column, "count")).reset_index()

    # find the most common device type for each service
    most_common_device = grouped_data.loc[
        grouped_data.groupby(service_column)['Bookings_Count'].idxmax()
    ].reset_index(drop=True)

    return most_common_device

def group_bookings_by_time_and_device(data: pd.DataFrame, date_time:str, device_column: str, booking_column: str) -> pd.DataFrame:
    """ 
    Group bookings by year, quarter, and device type, counting the number of bookings
    """
    # check if input is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")
    
    # validate the columns
    columns = [date_time, device_column, booking_column]
    for col in columns:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' does not exist in the DataFrame")
    
    # check if the column is in datetime format
    if not pd.api.types.is_datetime64_any_dtype(data[date_time]):
        raise TypeError(f"Column '{date_time}' must be in datetime format.")
    
    # extract the year and quarter
    data['year'] = data[date_time].dt.year
    data['quarter'] = data[date_time].dt.quarter

    # group by year, quarter, and device column, then count bookings
    grouped_data = data.groupby(['year', 'quarter', device_column]).agg(Bookings_Count=(booking_column, 'count')).reset_index()

    return grouped_data

def calculate_monthly_obsr(data: pd.DataFrame, date_column:str, booking_column:str, searches_column: str) -> pd.DataFrame:
    """ 
    Calculate the overall monthly booking to search ratio
    """
    # check if input is DataFrame 
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    # check if columns exist in the DataFrame 
    columns = [date_column, booking_column, searches_column]
    for col in columns:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' does not exist in the DataFrame.")
    # validate the date_column
    if not pd.api.types.is_datetime64_any_dtype(data[date_column]):
        raise TypeError(f"{date_column} must be in datetime format.")
    
    # extract the month column
    data['month'] = data[date_column].dt.month_name()

    # calculate monthly obsr
    monthly_obsr = data.groupby('month').agg(
        Total_Bookings=(booking_column, 'count'),
        Total_Searches=(searches_column, 'count')
    )

    monthly_obsr['oBSR'] = np.round((monthly_obsr['Total_Bookings'] / monthly_obsr['Total_Searches']), 4)

    return monthly_obsr

def calculate_daily_obsr(data: pd.DataFrame, date_column:str, booking_column:str, searches_column: str) -> pd.DataFrame:
    """ 
    Calculate the overall weekly booking to search ratio
    """
    # check if input is DataFrame 
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    # check if columns exist in the DataFrame 
    columns = [date_column, booking_column, searches_column]
    for col in columns:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' does not exist in the DataFrame.")
    # validate the date_column
    if not pd.api.types.is_datetime64_any_dtype(data[date_column]):
        raise TypeError(f"{date_column} must be in datetime format.")
    
    # extract the day of the week column
    data['day'] = data[date_column].dt.day_name()

    # calculate weekly obsr
    daily_obsr = data.groupby('day').agg(
        Total_Bookings=(booking_column, 'count'),
        Total_Searches=(searches_column, 'count')
    )

    daily_obsr['oBSR'] = np.round((daily_obsr['Total_Bookings'] / daily_obsr['Total_Searches']), 4)

    return daily_obsr