# Wolt integration project
This project helps upload items and inventory updates to online shopping platform Wolt, using Wolt API

Class WoltAPIHook has only one method patch_data, which calls PATCH request to necessary endpoint

In Main.py main logic is implemented:
1. Read data from files
2. Initialize WoltAPIHook instance and call patch_data method

For correct work you need config.py file with following content:
* DATA_PATH = '' - path where data files are located
* API_URL = 'https://pos-integration-service.development.dev.woltapi.com' - Wolt API url
* TOKEN = '' - authorization token
* ENDPOINTS = {
    'items': 'items',
    'inventory': 'items/inventory'} - API endpoints dictionary