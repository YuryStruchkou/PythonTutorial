import csv

from userCategoryMapper import ResultingDataset


def save_dataset_to_csv(dataset: ResultingDataset, filename: str):
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=vars(dataset[0]).keys())
        writer.writeheader()
        for row in dataset:
            writer.writerow(vars(row))
