# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import argparse

from azureml.core import Dataset, Datastore
from utils import workspace

def register_dataset(ws, datastore, data_path, dataset_name):


    datastore = Datastore(ws, datastore)
    dataset = Dataset.Tabular.from_delimited_files(path=(datastore, data_path), separator=",", support_multi_line=True)
    dataset = dataset.register(workspace = ws,
                                name = dataset_name,
                                create_new_version=True)
    print(f"Register dataset {dataset_name}")

    return dataset


def main(dataset_name, datastore_name, data_path):
    
    ws =  workspace.retrieve_workspace()

    _ = dataset.register_dataset(
        ws, 
        datastore=datastore_name,
        data_path=data_path,
        dataset_name=dataset_name
    )


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str)
    parser.add_argument('--datastore', type=str)
    parser.add_argument('--path', type=str)
    return parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args()

    main(args.name, args.datastore, args.path)
