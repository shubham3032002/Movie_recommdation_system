from Recommand_system.logging import logger
from Recommand_system.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME ="Data Ingestion Stage"
 
try:
        logger.info(f">>>>>>>>>>stage{STAGE_NAME}started <<<<<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>{STAGE_NAME}Completed <<<<<<<<<<<<<<<")
        
except Exception as e:
        logger.exception(e)
        raise e     