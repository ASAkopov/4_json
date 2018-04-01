
# Prettify JSON

The code prints data from JSON-formatted file into standard output in a user-friendly way.

# Quickstart

Example of script launch on Linux, Python 3.5:

test.json can be found on GitHub: https://github.com/ASAkopov/test_files

```bash

$ python pprint_json.py test.json

{
    "Cells": {
        "Address": "улица Академика Павлова, дом 10",
        "AdmArea": "Западный административный округ",
        "District": "район Кунцево",
        "IsNetObject": "да",
        "Name": "Ароматный Мир",
        "OperatingCompany": "Ароматный Мир",
        "TypeService": "реализация продовольственных товаров",
        "WorkingHours": [
            {
                "DayOfWeek": "понедельник",
                "Hours": "09:30-22:30"
            },
            {
                "DayOfWeek": "воскресенье",
                "Hours": "09:30-22:30"
            }
        ],
        "global_id": 14371450
    },
    "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
    "Number": 1
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
