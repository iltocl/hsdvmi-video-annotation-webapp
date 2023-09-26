import os 
import csv
import pandas as pd

def assign_bunch_to_annotator(annotator_number, batch_dict):
    exception_occurred = False  # Initialize flag

    for key, value in batch_dict.items():
        print(key, len(value))
        # max number of annotators per bunch is 3
        try:
            if len(value) >= 0 and len(value) <3:
                batch = key
                if annotator_number not in value:
                    value.append(annotator_number)
                    break
                else:
                    continue
        except:
            exception_occurred = True
    print(batch_dict)
    return batch, batch_dict, exception_occurred

def csv_batch_to_list(csv_file):
    df = pd.read_csv(csv_file, header=None)
    dataframe_lst = df[0].tolist()
    total_videos = len(dataframe_lst)

    return dataframe_lst, total_videos