from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

Stage_name = "Data Ingestion stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {Stage_name} started")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>> stage {Stage_name} completed <<<<<<<<< \n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e

