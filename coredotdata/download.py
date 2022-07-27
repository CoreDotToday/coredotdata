import requests
import os
from tqdm import tqdm
from pathlib import Path


def get_dataset_file_url(content_uid, target_filenames=None):
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
    data = {"uid": content_uid}
    if target_filenames:
        if type(target_filenames) == str:
            data['target_filenames'] = list(target_filenames)
        else:
            data['target_filenames'] = target_filenames

    r = requests.post(
        "https://tool.core.today/lib/cdd/dataset", json=data)
    list_download_url = r.json()
    return list_download_url


def get_dataset_file_list(content_uid):
    r = requests.post(
        "https://tool.core.today/lib/cdd/dataset", json={"uid": content_uid, "get_filename": True})
    list_files = r.json()
    return list_files


def generate_directory(list_download_url, target_directory=""):
    """Make directory for download file

    Parameters
    ----------
    list_download_url : list
        [{"key": "", "url": ""}]
    """
    if type(list_download_url) == dict:
        raise Exception(list_download_url['detail'])

    if not os.path.exists(target_directory):
        os.mkdir(target_directory)

    for i in [i['filename'] for i in list_download_url]:
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
        with open(target_directory+file['filename'], "wb") as f:
            f.write(result.content)


def download_dataset(uid, target_directory="./dataset/", target_file_list=[]):
    """Download dataset file list from Core.Today

    Parameters
    ----------
    uid : str
        Content Unique Id
    target_directory : str, optional
        Target directory for file download, by default "./dataset/"
    target_file_list : list, str, optional
        Target download file list, by default []
    """
    if target_directory[-1] != '/':
        target_directory = target_directory + '/'
    if target_file_list:
        if target_file_list == str:
            list_download_url = get_dataset_file_url(uid, [target_file_list])
        else:
            list_download_url = get_dataset_file_url(uid, target_file_list)
    else:
        list_download_url = get_dataset_file_url(uid)

    generate_directory(list_download_url, target_directory)
    write_files(list_download_url, target_directory)


def listdir(target_directory="./dataset/", show_size=0):
    # if os.path.exists(target_directory):
    if show_size:
        return [(f.name, f.stat().st_size) for f in Path(target_directory).glob('**/*') if f.is_file()]

    return os.listdir(target_directory)

