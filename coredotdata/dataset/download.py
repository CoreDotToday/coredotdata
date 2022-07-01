import requests
import os
from tqdm import tqdm


def generate_directory(list_download_url):
    """Make directory for download file

    Parameters
    ----------
    list_download_url : list
        [{"key": "", "url": ""}]
    """
    for i in [i['key'] for i in list_download_url]:
        dir_path = '/'.join(i.split("/")[:-1])
        if dir_path:
            os.makedirs(
                dir_path,
                exist_ok=True
            )


def get_path_from_uid(uid):
    """Generate prefix path from Content `uid`

    Parameters
    ----------
    uid : str
        content unique id

    Returns
    -------
    str
        prefix path for dataset download
    """
    r = requests.post("https://tool.core.today/lib/cdd/path",
                      json={"uid": uid})
    return r.json()


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
    path = get_path_from_uid(content_uid)
    key = path+"/upload"
    r = requests.post(
        "https://tool.core.today/lib/cdd/dataset", json={"key": key})
    list_download_url = r.json()
    return list_download_url


def write_files(list_download_url):
    """Download Files

    Parameters
    ----------
    list_download_url : list
        dict information for download and file writing
    """
    for file in tqdm(list_download_url):
        result = requests.get(file['url'])
        with open(file['key'], "wb") as f:
            f.write(result.content)


def download_dataset(uid):
    list_download_url = get_dataset_file_list(uid)
    generate_directory(list_download_url)
    write_files(list_download_url)
