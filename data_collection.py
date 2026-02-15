import csv
import logging
from typing import Dict, List, Optional
import requests
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='data_collection.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataCollector:
    def __init__(self):
        self.data = []
        self.headers: Optional[List[str]] = None
        
    def _log_error(self, message: str) -> None:
        """Log errors with timestamp."""
        logging.error(f"ERROR: {message}")
        
    def _validate_headers(self, headers: List[str]) -> bool:
        """Validate that required headers are present."""
        required_headers = ['id', 'partner_name', 'affiliate_link']
        return all(h in headers for h in required_headers)
        
    def collect_from_csv(self, file_path: str) -> None:
        """Collect data from CSV file."""
        try:
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                self.headers = next(reader)
                if not self._validate_headers(self.headers):
                    raise ValueError("Invalid headers in CSV file")
                for row in reader:
                    self.data.append(row)
                    logging.info(f"Collected data: {row}")
        except FileNotFoundError:
            self._log_error(f"File {file_path} not found.")
        except csv.Error as e:
            self._log_error(f"CSV error: {e}")

    def collect_from_api(self, endpoint: str) -> None:
        """Collect data from API endpoint."""
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                data = response.json()
                for item in data['items']:
                    self.data.append(item)
                    logging.info(f"Collected data from API: {item}")
            else:
                self._log_error(f"API request failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            self._log_error(f"Request exception: {e}")

    def save_data(self, file_path: str) -> None:
        """Save collected data to a CSV file."""
        try:
            with open(file_path, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(self.headers)
                writer.writerows(self.data)
            logging.info(f"Data saved to {file_path}")
        except Exception as e:
            self._log_error(f"Error saving data: {e}")

# Example usage
if __name__ == "__main__":
    collector = DataCollector()
    collector.collect_from_csv('partners.csv')
    collector.collect_from_api('https://api.affiliatehub.com/partners')
    collector.save_data('collected_partners.csv')