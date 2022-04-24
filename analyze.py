#!/usr/bin/env python3
import os
import pandas as pd


def get_subject_data(subject_id = "p33"):
    all_subjects = dict()
    session_names = zip(["day_1_pre" ,"day_1_post","day_2_pre" ,"day_2_post"],\
                        ["-1-1_results.csv",  "-1-2_results.csv",  "-2-1_results.csv",  "-2-2_results.csv"])
    base_path = "/home/jonathan/documents/code/behavioral-analysis/data/Visual-assessment/Data"
    subject_path = os.path.join(base_path, subject_id)
    session_data = {name: pd.read_csv(os.path.join(subject_path, subject_id + suffix), skipinitialspace=True) \
                    for name, suffix in session_names}
    all_subjects[subject_id] = pd.concat([session_data[name]["response score"] for name, _ in session_names], axis = 'columns')
