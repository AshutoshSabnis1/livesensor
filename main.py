from sensor.exception import SensorException
import os 
import sys
from sensor.logger import logging
import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

from sensor.utils import dump_csv_file_to_mongodb_collection




if __name__ == "__main__":
    file_path="aps_failure_training_set1.csv"
    database_name="database_sensor"
    collection_name ="sensor"
    dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)




  












    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)