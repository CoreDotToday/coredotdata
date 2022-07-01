=========== coredotdata ===========

.. image:: https://img.shields.io/pypi/v/coredotdata.svg :target:
https://pypi.python.org/pypi/coredotdata

.. image:: https://img.shields.io/travis/CoreDotToday/coredotdata.svg :target:
https://travis-ci.com/CoreDotToday/coredotdata

.. image:: https://readthedocs.org/projects/coredotdata/badge/?version=latest :target:
https://coredotdata.readthedocs.io/en/latest/?version=latest :alt: Documentation Status

.. image:: https://pyup.io/repos/github/CoreDotToday/coredotdata/shield.svg :target:
https://pyup.io/repos/github/CoreDotToday/coredotdata/ :alt: Updates

Core.Today Dataset Management Library

-   Free software: Apache Software License 2.0
-   Documentation: https://coredotdata.readthedocs.io.

## Installation

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
