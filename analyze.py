#!/usr/bin/env python3
"""analyze behavioral experiment data."""

import os
import pandas as pd


def get_subject_data(subject_path="/data/Visual-assessment/Data/p101"):
    """get the the success rates for both days,
    compute the differences for both, and the overall difference"""
    names = ["day_1_pre", "day_1_post", "day_2_pre", "day_2_post"]
    suffixes = ["-1-1_results.csv",  "-1-2_results.csv", "-2-1_results.csv", "-2-2_results.csv"]
    # session_names = [(x, y) for x, y  list(zip(names, suffixes))]
    # base_path = "./data/Visual-assessment/Data"
    # subject_path = os.path.join(base_path, subject_id)
    subject_id = os.path.basename(subject_path)
    d_all_session_data = {name: pd.read_csv
                          (os.path.join(subject_path, subject_id + suffix),
                           skipinitialspace=True)
                          for name, suffix in zip(names, suffixes)}
    df_all_subjects = pd.concat([d_all_session_data[name]["response score"]
                                          for name, _ in zip(names, suffixes)], axis='columns')
    df_all_subjects.columns = names
    scores = pd.DataFrame(df_all_subjects.sum()/df_all_subjects.shape[0])
    return scores




all_subject_dirs = glob.glob(os.path.join(base_path, "p*"))
all_subject_names = [os.path.basename(dir) for dir in all_subject_dirs]
#TODO: check if all 4 files exist before trying to read the csv 
all_subject_results = pd.concat([get_subject_data(dir) for dir in all_subject_dirs], axis=1) 
