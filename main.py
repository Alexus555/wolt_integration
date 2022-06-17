import config
import logging
import os
import sys

def get_files_for_processing(data_path: str) -> list:
    pass


def process_file(file_name: str) -> None:
    pass


if __name__ == '__main__':

    logging.basicConfig(
        level=logging.INFO,
        format=u"%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(".\\script.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logging.info("Start script")

    data_path = config.DATA_PATH

    processing_files = get_files_for_processing(data_path)

    for file_name in processing_files:
        process_file(file_name)

    logging.info("Finish script")