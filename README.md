# Wolt integration project
This project helps upload items and inventory updates to online shopping platform Wolt, using Wolt API

Class WoltAPIHook has only one method patch_data, which call PATCH request to necessary endpoint

In Main.py main logic is implemented:
1. Read data from files
2. Initialize WoltAPIHook instance and call patch_data method
