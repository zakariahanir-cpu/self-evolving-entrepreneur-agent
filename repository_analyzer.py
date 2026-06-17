import os

def analyze_repository():
    # Define the directory to analyze
    directory = os.getcwd()

    # Define the files to delete
    files_to_delete = ["web_scraper.py", "data_manager.py", "nlp_processor.py", "infiltrator.py", "website_infiltrator.py", "vulnerability_analyzer.py"]
    temp_files_to_delete = [f for f in os.listdir(directory) if f.endswith(".txt") or f.endswith(".json")]

    # Delete the files
    for file in files_to_delete:
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted file: {file}")

    for file in temp_files_to_delete:
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted temporary file: {file}")

    print("Repository analysis and cleanup complete.")

# Run the repository analyzer
analyze_repository()