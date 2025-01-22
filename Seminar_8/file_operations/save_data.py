import os
import json
import csv
import pickle

def save_to_json(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Создать директорию, если её нет
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def save_to_csv(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Создать директорию, если её нет
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Type', 'Parent Directory', 'Size (bytes)'])
        for item in data:
            writer.writerow([item['name'], item['type'], item['parent'], item['size']])

def save_to_pickle(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Создать директорию, если её нет
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
