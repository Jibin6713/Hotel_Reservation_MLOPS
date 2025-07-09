from src.data_ingestion import DataIngestion
from src.data_processing import Data_Processor
from src.model_training import ModelTraining
from utils.common_function import read_yaml
from config.paths_config import *



if __name__=="__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    ### 2. Data Processing

    processor = Data_Processor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)
    processor.process()

    ### 3. Model Training

    trainer = ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUTPUT_PATH)
    trainer.run()

