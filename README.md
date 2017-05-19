# python-hyperd

Python client for hyperd's grpc API.

## Install

```
pip install hyperd
```

## Examples

```python
import grpc
from hyperd import types_pb2 as api

channel = grpc.insecure_channel('127.0.0.1:22318')
stube=api.PublicAPIStub(channel)
stub=api.PublicAPIStub(channel)

# get version
print stub.Version(api.VersionRequest())

# get pod list
print stub.PodList(api.PodListRequest())

# get image list
print stub.ImageList(api.ImageListRequest())
```
