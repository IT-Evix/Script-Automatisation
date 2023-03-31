import pandas as pd
import os

def concat_csv_files():
    extracted_folder = "Le dossier des fichiers extraits"
    csv_files = [f for f in os.listdir(extracted_folder) if f.endswith(".csv")]
    final_df = None
    for csv_file in csv_files:
        try:
            df = pd.read_csv(os.path.join(extracted_folder, csv_file), delimiter=';')
            if final_df is None:
                final_df = df
            else:
                final_df = pd.concat([final_df, df], axis=0, ignore_index=True)
        except:
            print(f"{csv_file} est vide.")
            continue
    if final_df is not None:
        final_df.to_csv("final_data.csv", index=False, sep=';')

concat_csv_files()

