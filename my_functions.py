import os 
import csv
import pandas as pd

def assign_bunch_to_annotator(annotator_number, batch_dict):
    """Assigning batch number to annotators
    Params
    ------
    annotator_number: int
        Number that identifies the annotator
    batch_dict: dict
        A dictionary that contains all batch_n: [annotator_a, annotator_b]

    Return:
    -------
    batch:
    batch_dict:
    exception_ocurred:
    """
    exception_occurred = False  # Initialize flag

    for key, value in batch_dict.items():
        print(key, "len(value)", len(value))
        try:
            # max number of annotators per bunch is 2
            if len(value) < 2:
                batch = key # batch name
                if annotator_number not in value:
                    # check if can be assigned to that specific batch
                    value.append(annotator_number)
                    break
                else:
                    continue
        except:
            exception_occurred = True
    print("\ndef assign_bunch_to_annotator", batch_dict) # updated dictionary
    return batch, batch_dict, exception_occurred

def csv_batch_to_list(csv_file):
    """
    Params
    ------
    csv_file: .csv
        Receives a batch_files/csv_file
    
    Returns
    -------
    lst_dataframe: list
        A list of the video ids
    total_videos: int
        How many videos are in the batch
    """
    df = pd.read_csv(csv_file, header=None, encoding='ISO-8859-1')
    #df = pd.read_csv(csv_file, header=None)
    lst_dataframe = df[0].tolist()
    total_videos = len(lst_dataframe)

    return lst_dataframe, total_videos