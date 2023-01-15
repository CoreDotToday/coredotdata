# coredotdata
### 코어닷투데이의 데이터셋을 원하는 곳에 다운로드할 수 있습니다.
[![PyPI version](https://badge.fury.io/py/coredotdata.svg)](https://badge.fury.io/py/coredotdata)
[![GitHup issues](https://img.shields.io/github/issues/CoreDotToday/coredotdata)](https://github.com/CoreDotToday/coredotdata/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/CoreDotToday/coredotdata)](https://github.com/CoreDotToday/coredotdata/pulls)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
----------------------------

-   Free software: Apache Software License 2.0

## Installation

```
pip install coredotdata
```

```
pip install git+https://github.com/CoreDotToday/coredotdata
```

```
pip uninstall coredotdata -y
```

## Features

- 데이터셋 uid를 이용하여 다운로드 하기 (data 폴더에 저장됩니다)

```python
import coredotdata as cdd
cdd.download_dataset("181I3nDWv0")
```

- 특정 디렉토리 이름을 지정하여 다운받을 수 있습니다 `target_directory`

```python
import coredotdata as cdd
cdd.download_dataset("181I3nDWv0", target_directory="./AAA")
```

- 콘텐츠에 담긴 파일 목록을 조회할 수 있습니다

```python
import coredotdata as cdd
cdd.get_dataset_file_list("15Dif81I")
```


- 원하는 파일만 선택하여 다운로드할 수 있습니다 `target_file_list`

```python
import coredotdata as cdd
cdd.download_dataset("15Dif81I", "./data", ['AgeDataset-V1.csv.zip'])
# cdd.download_dataset("15Dif81I", target_file_list=['AgeDataset-V1.csv.zip'])
# cdd.download_dataset("15Dif81I", target_directory="./data", target_file_list=['AgeDataset-V1.csv.zip'])
```


- 다운로드 폴더의 파일 목록을 조회합니다

```python
cdd.listdir()  # "./dataset" 폴더 안의 파일 목록을 반환합니다
# cdd.listdir(target_directory="./data")  # 목록 조회할 폴더를 지정합니다
# cdd.listdir(show_size=1)  # 파일 크기도 같이 반환합니다
```

## Contributors
<a href="https://github.com/coredottoday/coredotdata/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=coredottoday/coredotdata" />
</a>


## LICENSE
`coredotdata` is licensed under the terms of the Apache License 2.0.


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=CoreDotToday/coredotdata&type=Timeline)](https://star-history.com/#CoreDotToday/coredotdata&Timeline)
