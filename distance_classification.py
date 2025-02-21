import pandas as pd

# Load dataset
def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset Loaded Successfully!")
        print("First 5 rows:")
        print(df.head())
    except Exception as e:
        print(f"Error loading dataset: {e}")

# Example usage
if __name__ == "__main__":
    dataset_path = r"C:\Users\Lakshay Aggarwal\OneDrive\Desktop\MLPR\distance_classification\A.csv"  # Modify the path as needed
    load_dataset(dataset_path)
