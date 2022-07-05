# coredotdata

코어닷투데이의 데이터셋을 원하는 곳에 다운로드할 수 있습니다.

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
