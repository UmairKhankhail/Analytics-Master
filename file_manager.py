import base64
import os
import pandas as pd
import shutil

class FileManager:
    def __init__(self):
        self.uploaded_file_path = None

    def save_file_from_base64(self, base64_str, file_type):
        file_data = base64.b64decode(base64_str)

        if file_type == 'excel':
            file_extension = '.xlsx'
        elif file_type == 'csv':
            file_extension = '.csv'
        else:
            raise ValueError("Unsupported file type. Use 'excel' or 'csv'.")

        file_name = 'uploaded_file' + file_extension
        with open(file_name, 'wb') as file:
            file.write(file_data)
        
        return file_name

    def clean_file(self, file_name, file_type):
        try:
            # Pre-clean the file to remove leading empty rows
            if file_type == 'excel':
                df = pd.read_excel(file_name, engine='openpyxl', header=None)
            elif file_type == 'csv':
                df = pd.read_csv(file_name, header=None)
            else:
                raise ValueError("Unsupported file type. Use 'excel' or 'csv'.")

            # Remove leading empty rows
            df.dropna(how='all', inplace=True)

            # Determine if the first row is a header or not
            if df.iloc[0].isnull().sum() > (len(df.columns) // 2):
                # If more than half of the first row is null, treat it as data, not header
                df.columns = [f'Unnamed: {i}' for i in range(len(df.columns))]
            else:
                # Set the first row as header
                df.columns = df.iloc[0]
                df = df[1:].reset_index(drop=True)

            # Remove all null values and empty columns
            df.dropna(how='all', inplace=True)
            df.dropna(axis=1, how='all', inplace=True)

            # Save cleaned file
            if file_type == 'excel':
                df.to_excel(file_name, index=False, engine='openpyxl')
            elif file_type == 'csv':
                df.to_csv(file_name, index=False)

        except Exception as e:
            raise ValueError(e)

    def handle_file_upload(self, base64_str, file_type):
        # Remove the existing uploaded file if it exists
        if self.uploaded_file_path and os.path.exists(self.uploaded_file_path):
            os.remove(self.uploaded_file_path)
        
        # Save and clean the new file
        self.uploaded_file_path = self.save_file_from_base64(base64_str, file_type)
        #self.clean_file(self.uploaded_file_path, file_type)
        
        # Remove cache folder if it exists
 # Remove cache folder if it exists, ignoring errors
        cache_folder = 'cache'
        if os.path.exists(cache_folder) and os.path.isdir(cache_folder):
            shutil.rmtree(cache_folder, ignore_errors=True)

        return f"File uploaded, cleaned, and saved as {self.uploaded_file_path}"
