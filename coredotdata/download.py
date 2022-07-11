import requests
import os
from tqdm import tqdm


def get_dataset_file_list(content_uid):
    """Get specific dataset file list using `content_uid`

    Parameters
    ----------
    content_uid : str
        content unique id

    Returns
    -------
    list
        dict information for download and file writing
    """
    r = requests.post(
        "https://tool.core.today/lib/cdd/dataset", json={"uid": content_uid})
    list_download_url = r.json()
    return list_download_url


def generate_directory(list_download_url, target_directory=""):
    """Make directory for download file

    Parameters
    ----------
    list_download_url : list
        [{"key": "", "url": ""}]
    """
    if type(list_download_url) == dict:
        raise Exception(list_download_url['detail'])

    # if list_download_url == []:
    #     raise Exception("Empty dataset list")

    for i in [i['key'] for i in list_download_url]:
        dir_path = '/'.join(i.split("/")[:-1])
        if dir_path:
            os.makedirs(
                target_directory+dir_path,
                exist_ok=True
            )


def write_files(list_download_url, target_directory=""):
    """Download Files

    Parameters
    ----------
    list_download_url : list
        dict information for download and file writing
    """
    for file in tqdm(list_download_url):
        result = requests.get(file['url'])
        with open(target_directory+file['key'], "wb") as f:
            f.write(result.content)


def download_dataset(uid, target_directory="./dataset/"):
    """Download dataset file list from Core.Today

    Parameters
    ----------
    uid : str
        Content Unique Id
    target_directory : str, optional
        Target directory for file download, by default "./dataset/"
    """
    if target_directory[-1] != '/':
        target_directory = target_directory + '/'
    list_download_url = get_dataset_file_list(uid)
    generate_directory(list_download_url, target_directory)
    write_files(list_download_url, target_directory)
