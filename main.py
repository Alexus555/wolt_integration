import config
import logging
import os
import sys
from api.wolt_api import WoltApiHook


def get_files_for_processing(data_path: str) -> list:
    files = os.listdir(data_path)

    json_files = [
        os.path.join(data_path, fn) for fn in filter(lambda x: x.endswith('.json'), files)]

    logging.info(f'{len(json_files)} file(s) were found in directory {data_path}')

    return json_files


def process_file(file_name: str) -> None:
    logging.info(f'Processing file {file_name}...')

    name = str(os.path.basename(file_name)).replace('.json', '').lower()
    file_params = name.split('_')
    endpoint = file_params[0]

    if endpoint not in config.ENDPOINTS:
        logging.warning(f"Can't extract endpoint name from file name. Skipped")
        return

    with open(file_name, 'r', encoding='utf-8') as f:
        payload = f.read()

    if payload == '':
        logging.warning(f'File is empty. Skipped')
        return

    venue_id = file_params[1]

    wolt_api = WoltApiHook(config.API_URL, venue_id, config.TOKEN)
    if wolt_api.patch_data(config.ENDPOINTS[endpoint], payload):
        logging.info('File was processed successfully')
        os.remove(file_name)
    else:
        logging.warning('An error has been occurred during processing')


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

    processing_files = get_files_for_processing(config.DATA_PATH)

    for file in processing_files:
        process_file(file)

    logging.info("Finish script")
