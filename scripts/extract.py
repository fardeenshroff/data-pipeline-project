import pandas as pd  # Importing pandas library

def extract_data(csv_file):
    """Extract data from a CSV file."""
    try:
        df = pd.read_csv(csv_file)  # Reading the CSV file into a DataFrame
        print("✅ Data extracted successfully!")
        return df
    except Exception as e:
        print(f"❌ Error extracting data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    print("Script is running...")  # Debug print
    df = extract_data("../data/sample_data.csv")  # Update the path to the CSV file
    if df is not None:
        print(df.head())  # Print the first 5 rows of the DataFrame
    else:
        print("No data to display.")