from file_operations.directory_info import get_directory_info
from file_operations.save_data import save_to_json, save_to_csv, save_to_pickle

def main():
    directory = "./test_directory"  # Путь к директории для анализа
    output_json = "./output/directory_info.json"
    output_csv = "./output/directory_info.csv"
    output_pickle = "./output/directory_info.pkl"

    # Получаем информацию о директории
    data = get_directory_info(directory)

    # Сохраняем данные в разные форматы
    save_to_json(data, output_json)
    save_to_csv(data, output_csv)
    save_to_pickle(data, output_pickle)

    print(f"Обработка завершена. Данные сохранены в файлы:\n{output_json}\n{output_csv}\n{output_pickle}")

if __name__ == "__main__":
    main()
