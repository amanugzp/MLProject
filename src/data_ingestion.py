import os
import sys

# Get the absolute path of the project's root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import your modules
from src.exception import CustomException
from src.logger import logging

import pandas as pd    
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # FIXED: Use raw string or forward slashes
            df = pd.read_csv(r'notebook\data\stud.csv')  # OR 'notebook/data/stud.csv'
            logging.info("Data ingestion completed")

            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)  # Missing line

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path  # FIXED: Typo
            )

        except Exception as e:
            raise CustomException(e, sys)  # FIXED: Ensure exception handling works properly

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
