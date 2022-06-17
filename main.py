import config


def get_files_for_processing(data_path: str) -> list:
    pass


def process_file(file_name: str) -> None:
    pass


if __name__ == '__main__':
    data_path = config.DATA_PATH

    processing_files = get_files_for_processing(data_path)

    for file_name in processing_files:
        process_file(file_name)
