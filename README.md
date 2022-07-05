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

-   데이터셋 uid를 이용하여 다운로드 하기 (data 폴더에 저장됩니다)

```python
import coredotdata as cdd
cdd.download_dataset("181I3nDWv0")
```

-   특정 디렉토리 이름을 지정하여 다운받을 수 있습니다 `target_directory`

```python
import coredotdata as cdd
cdd.download_dataset("181I3nDWv0", target_directory="./AAA")
```


## Contributors
<a href="https://github.com/coredottoday/coredotdata/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=coredottoday/coredotdata" />
</a>


## LICENSE
`coredotdata` is licensed under the terms of the Apache License 2.0.
