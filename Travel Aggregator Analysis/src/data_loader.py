import pandas as pd

class DataLoader:
    def __init__(self, bookings_path: str, sessions_path: str):
        # Initialize with file paths
        self.bookings_path = bookings_path
        self.sessions_path = sessions_path
        self.bookings = None
        self.sessions = None
        self.merged_data = None

    def load_data(self):
        """Loads the bookings and sessions data from CSV"""
        self.bookings = pd.read_csv(self.bookings_path)
        self.sessions = pd.read_csv(self.sessions_path)

        print("Data loaded: Sessions and Bookings")

    def check_missing_values(self):
        """Checks and prints missing values in both datasets"""
        if self.bookings.isnull().values.any():
            print("Missing values in Bookings: ", self.bookings.isnull().sum())
        if self.sessions.isnull().values.any():
            print("Missing values in Sessions: ", self.sessions.isnull().sum())

    def convert_columns_to_datetime(self, column:str, date_format: str):
        """Converts specified columns in both datasets to datetime"""
        if column in self.bookings.columns:
            self.bookings[column] = pd.to_datetime(self.bookings[column], format=date_format, errors='coerce')
        if column in self.sessions.columns:
            self.sessions[column] = pd.to_datetime(self.sessions[column], format=date_format, errors='coerce')

    def merge_data(self):
        """Merge bookings and sessions datasets"""
        if ('booking_id' in self.bookings.columns) and ('booking_id' in self.sessions.columns):
            self.merge_data = pd.merge(self.bookings, self.sessions, on='booking_id', how='left')

            print('Data Merged Successfully')
        
        else:
            print("Error: 'booking_id' not found in one of the datasets.")

    def save_merged_data(self, output_path: str):
        """Saves the merged dataset to a CSV file"""
        if self.merge_data is not None:
            self.merge_data.to_csv(output_path, index=False)
            print(f"Merged data saved to {output_path}")
        else:
            print("Error: No merged data to save")
