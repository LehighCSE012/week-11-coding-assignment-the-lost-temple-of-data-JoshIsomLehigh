import pandas as pd
import re

def load_artifact_data(excel_filepath):
    """
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.

    Args:
        excel_filepath (str): The path to the artifacts Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the artifact data.
    """
    # Hint: Use pd.read_excel, specify sheet_name and skiprows
    # Replace 'pass' with your code
    df = pd.read_excel(excel_filepath, sheet_name='Main Chamber', skiprows=3)
    return df

def load_location_notes(tsv_filepath):
    """
    Reads location data from a Tab-Separated Value (TSV) file.

    Args:
        tsv_filepath (str): The path to the locations TSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the location data.
    """
    # Hint: Use pd.read_csv, specify the separator for tabs ('\t')
    # Replace 'pass' with your code
    df= pd.read_csv(tsv_filepath, sep='\t')
    return df
def extract_journal_dates(journal_text):
    """
    Extracts all dates in MM/DD/YYYY format from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of date strings found in the text.
    """
    # Hint: Use re.findall with a raw string pattern for MM/DD/YYYY format.
    # Pattern idea: r"\d{2}/\d{2}/\d{4}"
    # Replace 'pass' with your code
    regex_pattern = r"\d{2}/\d{2}/\d{4}"
    dates = re.findall(regex_pattern, journal_text)
    return dates
    # return the list of found dates

def extract_secret_codes(journal_text):
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of secret code strings found in the text.
    """
    # Hint: Use re.findall with a raw string pattern for AZMAR- followed by 3 digits.
    # Pattern idea: r"AZMAR-\d{3}"
    # Replace 'pass' with your code
    regex_pattern = r"AZMAR-\d{3}"
    codes = re.findall(regex_pattern, journal_text)
    return codes
    # return the list of found codes


# --- Optional: Main execution block for your own testing ---
if __name__ == '__main__':
    # Define file paths (adjust if your files are located elsewhere)
    EXCEL_FILE = 'artifacts.xlsx' # Renamed
    TSV_FILE = 'locations.tsv'   # Renamed
    JOURNAL_FILE = 'journal.txt' # Renamed

    print(f"--- Loading Artifact Data from {EXCEL_FILE} ---") # Updated
    try:
        artifacts_df = load_artifact_data(EXCEL_FILE) # Updated
        if artifacts_df is not None:
            print("Successfully loaded DataFrame. First 5 rows:")
            print(artifacts_df.head())
            print("\nDataFrame Info:")
            artifacts_df.info()
        else:
            print("Error: load_artifact_data returned None.")
    except FileNotFoundError:
        print(f"Error: File not found at {EXCEL_FILE}") # Updated
    except Exception as e:
        print(f"An error occurred loading artifact data: {e}")

    print(f"\n--- Loading Location Notes from {TSV_FILE} ---") # Updated
    try:
        locations_df = load_location_notes(TSV_FILE) # Updated
        if locations_df is not None:
            print("Successfully loaded DataFrame. First 5 rows:")
            print(locations_df.head())
            print("\nDataFrame Info:")
            locations_df.info()
        else:
            print("Error: load_location_notes returned None.")
    except FileNotFoundError:
        print(f"Error: File not found at {TSV_FILE}") # Updated
    except Exception as e:
        print(f"An error occurred loading location data: {e}")

    print(f"\n--- Processing Journal from {JOURNAL_FILE} ---") # Updated
    try:
        with open(JOURNAL_FILE, 'r', encoding='utf-8') as f: # Updated
            journal_content = f.read()

        print("\nExtracting Dates...")
        journal_dates = extract_journal_dates(journal_content) # Renamed variable
        print(f"Found dates: {journal_dates}") # Updated

        print("\nExtracting Secret Codes...")
        secret_codes = extract_secret_codes(journal_content) # Renamed variable
        print(f"Found codes: {secret_codes}") # Updated

    except FileNotFoundError:
        print(f"Error: File not found at {JOURNAL_FILE}") # Updated
    except Exception as e:
        print(f"An error occurred processing the journal: {e}")
    except Exception as e:
        print(f"An error occurred processing the journal: {e}")
