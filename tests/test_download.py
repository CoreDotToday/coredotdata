from coredotdata import get_dataset_file_url, get_dataset_file_list, download_dataset
from coredotdata.download import download_dataset
import os


def test_get_dataset_file_url():
    result = get_dataset_file_url("15Dif81I")
    assert result[0]['url'][:24] == "https://file.core.today/"

    result = get_dataset_file_url("15Dif81I", ['AgeDataset-V1.csv.zip'])
    assert result[0]['url'][:24] == "https://file.core.today/"


def test_get_dataset_file_list():
    result = get_dataset_file_list("15Dif81I")
    assert result[0] == 'AgeDataset-V1.csv.zip'


def test_download_dataset():
    download_dataset("15Dif81I", target_directory="/tmp")
    assert os.path.exists("/tmp/AgeDataset-V1.csv.zip")

    download_dataset("15Dif81I",
        target_directory="/tmp/cdd_test1",
        target_file_list=get_dataset_file_list("15Dif81I")
    )
    assert os.path.exists("/tmp/cdd_test1/AgeDataset-V1.csv.zip")
