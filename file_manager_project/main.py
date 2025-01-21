from file_operations import rename_files

def main():
    # Пример использования функции
    rename_files(
        target_name="_processed", 
        digits_count=3, 
        source_extension=".txt", 
        target_extension=".csv", 
        name_range=(2, 5), 
        directory="./test_files"
    )

if __name__ == "__main__":
    main()
