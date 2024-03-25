import requests
import zipfile
from utils import *
from pydantic import BaseModel


class DataIngestionConfigValidator(BaseModel):
    data_dir: Path
    url: str
    raw_zip_file: Path #Path #data_dir:
    target_dir: Path

class DataIngestion:
    def __init__(self, config_path):
        self.config_path = config_path

    def validate_data(self):
        configbox = read_yaml(Path(self.config_path))
        config = configbox.data_ingestion
        config = DataIngestionConfigValidator(**config)
        return config
        
    def download_file(self, config):
        """
        Url: str
        downloads data into a specified directory
        config (ConfigBox): yaml file that contains file path

        Returns None
        """
        create_directories([config.data_dir])
        
        if not os.path.exists(config.raw_zip_file):
            response = requests.get(config.url)
            
            with open(config.raw_zip_file, 'wb') as file:
                file.write(response.content)
                
        else:
            print(f"File already exists in {config.raw_zip_file}")
        
        
    def unzip_file(self, config):
        """
            zip_file_path: str
            Extracts the zip file into the data directory
            Function returns None
            """
        with zipfile.ZipFile(config.raw_zip_file, 'r') as files:
            files.extractall(config.target_dir)
