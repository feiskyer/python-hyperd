# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import types_pb2 as types__pb2


class PublicAPIStub(object):
  """PublicAPI defines the public APIs which are handled over TCP sockets.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PodList = channel.unary_unary(
        '/types.PublicAPI/PodList',
        request_serializer=types__pb2.PodListRequest.SerializeToString,
        response_deserializer=types__pb2.PodListResponse.FromString,
        )
    self.PodCreate = channel.unary_unary(
        '/types.PublicAPI/PodCreate',
        request_serializer=types__pb2.PodCreateRequest.SerializeToString,
        response_deserializer=types__pb2.PodCreateResponse.FromString,
        )
    self.PodInfo = channel.unary_unary(
        '/types.PublicAPI/PodInfo',
        request_serializer=types__pb2.PodInfoRequest.SerializeToString,
        response_deserializer=types__pb2.PodInfoResponse.FromString,
        )
    self.PodRemove = channel.unary_unary(
        '/types.PublicAPI/PodRemove',
        request_serializer=types__pb2.PodRemoveRequest.SerializeToString,
        response_deserializer=types__pb2.PodRemoveResponse.FromString,
        )
    self.PodStart = channel.unary_unary(
        '/types.PublicAPI/PodStart',
        request_serializer=types__pb2.PodStartRequest.SerializeToString,
        response_deserializer=types__pb2.PodStartResponse.FromString,
        )
    self.PodStop = channel.unary_unary(
        '/types.PublicAPI/PodStop',
        request_serializer=types__pb2.PodStopRequest.SerializeToString,
        response_deserializer=types__pb2.PodStopResponse.FromString,
        )
    self.PodSignal = channel.unary_unary(
        '/types.PublicAPI/PodSignal',
        request_serializer=types__pb2.PodSignalRequest.SerializeToString,
        response_deserializer=types__pb2.PodSignalResponse.FromString,
        )
    self.PodPause = channel.unary_unary(
        '/types.PublicAPI/PodPause',
        request_serializer=types__pb2.PodPauseRequest.SerializeToString,
        response_deserializer=types__pb2.PodPauseResponse.FromString,
        )
    self.PodUnpause = channel.unary_unary(
        '/types.PublicAPI/PodUnpause',
        request_serializer=types__pb2.PodUnpauseRequest.SerializeToString,
        response_deserializer=types__pb2.PodUnpauseResponse.FromString,
        )
    self.ExecVM = channel.stream_stream(
        '/types.PublicAPI/ExecVM',
        request_serializer=types__pb2.ExecVMRequest.SerializeToString,
        response_deserializer=types__pb2.ExecVMResponse.FromString,
        )
    self.ContainerList = channel.unary_unary(
        '/types.PublicAPI/ContainerList',
        request_serializer=types__pb2.ContainerListRequest.SerializeToString,
        response_deserializer=types__pb2.ContainerListResponse.FromString,
        )
    self.ContainerInfo = channel.unary_unary(
        '/types.PublicAPI/ContainerInfo',
        request_serializer=types__pb2.ContainerInfoRequest.SerializeToString,
        response_deserializer=types__pb2.ContainerInfoResponse.FromString,
        )
    self.ImageList = channel.unary_unary(
        '/types.PublicAPI/ImageList',
        request_serializer=types__pb2.ImageListRequest.SerializeToString,
        response_deserializer=types__pb2.ImageListResponse.FromString,
        )
    self.VMList = channel.unary_unary(
        '/types.PublicAPI/VMList',
        request_serializer=types__pb2.VMListRequest.SerializeToString,
        response_deserializer=types__pb2.VMListResponse.FromString,
        )
    self.SetPodLabels = channel.unary_unary(
        '/types.PublicAPI/SetPodLabels',
        request_serializer=types__pb2.PodLabelsRequest.SerializeToString,
        response_deserializer=types__pb2.PodLabelsResponse.FromString,
        )
    self.PodStats = channel.unary_unary(
        '/types.PublicAPI/PodStats',
        request_serializer=types__pb2.PodStatsRequest.SerializeToString,
        response_deserializer=types__pb2.PodStatsResponse.FromString,
        )
    self.ContainerLogs = channel.unary_stream(
        '/types.PublicAPI/ContainerLogs',
        request_serializer=types__pb2.ContainerLogsRequest.SerializeToString,
        response_deserializer=types__pb2.ContainerLogsResponse.FromString,
        )
    self.ContainerCreate = channel.unary_unary(
        '/types.PublicAPI/ContainerCreate',
        request_serializer=types__pb2.ContainerCreateRequest.SerializeToString,
        response_deserializer=types__pb2.ContainerCreateResponse.FromString,
        )
    self.ContainerStart = channel.unary_unary(
        '/types.PublicAPI/ContainerStart',
        request_serializer=types__pb2.ContainerStartRequest.SerializeToString,
        response_deserializer=types__pb2.ContainerStartResponse.FromString,
        )
    self.ContainerRename = channel.unary_unary(
        '/types.PublicAPI/ContainerRename',
        request_serializer=types__pb2.ContainerRenameRequest.SerializeToString,
        response_deserializer=types__pb2.ContainerRenameResponse.FromString,
        )
    self.ContainerSignal = channel.unary_unary(
        '/types.PublicAPI/ContainerSignal',
        request_serializer=types__pb2.ContainerSignalRequest.SerializeToString,
        response_deserializer=types__pb2.ContainerSignalResponse.FromString,
        )
    self.ContainerStop = channel.unary_unary(
        '/types.PublicAPI/ContainerStop',
        request_serializer=types__pb2.ContainerStopRequest.SerializeToString,
        response_deserializer=types__pb2.ContainerStopResponse.FromString,
        )
    self.ContainerRemove = channel.unary_unary(
        '/types.PublicAPI/ContainerRemove',
        request_serializer=types__pb2.ContainerRemoveRequest.SerializeToString,
        response_deserializer=types__pb2.ContainerRemoveResponse.FromString,
        )
    self.ExecCreate = channel.unary_unary(
        '/types.PublicAPI/ExecCreate',
        request_serializer=types__pb2.ExecCreateRequest.SerializeToString,
        response_deserializer=types__pb2.ExecCreateResponse.FromString,
        )
    self.ExecStart = channel.stream_stream(
        '/types.PublicAPI/ExecStart',
        request_serializer=types__pb2.ExecStartRequest.SerializeToString,
        response_deserializer=types__pb2.ExecStartResponse.FromString,
        )
    self.ExecSignal = channel.unary_unary(
        '/types.PublicAPI/ExecSignal',
        request_serializer=types__pb2.ExecSignalRequest.SerializeToString,
        response_deserializer=types__pb2.ExecSignalResponse.FromString,
        )
    self.Attach = channel.stream_stream(
        '/types.PublicAPI/Attach',
        request_serializer=types__pb2.AttachMessage.SerializeToString,
        response_deserializer=types__pb2.AttachMessage.FromString,
        )
    self.Wait = channel.unary_unary(
        '/types.PublicAPI/Wait',
        request_serializer=types__pb2.WaitRequest.SerializeToString,
        response_deserializer=types__pb2.WaitResponse.FromString,
        )
    self.TTYResize = channel.unary_unary(
        '/types.PublicAPI/TTYResize',
        request_serializer=types__pb2.TTYResizeRequest.SerializeToString,
        response_deserializer=types__pb2.TTYResizeResponse.FromString,
        )
    self.ServiceList = channel.unary_unary(
        '/types.PublicAPI/ServiceList',
        request_serializer=types__pb2.ServiceListRequest.SerializeToString,
        response_deserializer=types__pb2.ServiceListResponse.FromString,
        )
    self.ServiceAdd = channel.unary_unary(
        '/types.PublicAPI/ServiceAdd',
        request_serializer=types__pb2.ServiceAddRequest.SerializeToString,
        response_deserializer=types__pb2.ServiceAddResponse.FromString,
        )
    self.ServiceDelete = channel.unary_unary(
        '/types.PublicAPI/ServiceDelete',
        request_serializer=types__pb2.ServiceDelRequest.SerializeToString,
        response_deserializer=types__pb2.ServiceDelResponse.FromString,
        )
    self.ServiceUpdate = channel.unary_unary(
        '/types.PublicAPI/ServiceUpdate',
        request_serializer=types__pb2.ServiceUpdateRequest.SerializeToString,
        response_deserializer=types__pb2.ServiceUpdateResponse.FromString,
        )
    self.ImagePull = channel.unary_stream(
        '/types.PublicAPI/ImagePull',
        request_serializer=types__pb2.ImagePullRequest.SerializeToString,
        response_deserializer=types__pb2.ImagePullResponse.FromString,
        )
    self.ImagePush = channel.unary_stream(
        '/types.PublicAPI/ImagePush',
        request_serializer=types__pb2.ImagePushRequest.SerializeToString,
        response_deserializer=types__pb2.ImagePushResponse.FromString,
        )
    self.ImageRemove = channel.unary_unary(
        '/types.PublicAPI/ImageRemove',
        request_serializer=types__pb2.ImageRemoveRequest.SerializeToString,
        response_deserializer=types__pb2.ImageRemoveResponse.FromString,
        )
    self.Ping = channel.unary_unary(
        '/types.PublicAPI/Ping',
        request_serializer=types__pb2.PingRequest.SerializeToString,
        response_deserializer=types__pb2.PingResponse.FromString,
        )
    self.Info = channel.unary_unary(
        '/types.PublicAPI/Info',
        request_serializer=types__pb2.InfoRequest.SerializeToString,
        response_deserializer=types__pb2.InfoResponse.FromString,
        )
    self.Version = channel.unary_unary(
        '/types.PublicAPI/Version',
        request_serializer=types__pb2.VersionRequest.SerializeToString,
        response_deserializer=types__pb2.VersionResponse.FromString,
        )


class PublicAPIServicer(object):
  """PublicAPI defines the public APIs which are handled over TCP sockets.
  """

  def PodList(self, request, context):
    """PodList gets a list of pods
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PodCreate(self, request, context):
    """PodCreate creates a pod according to UserPod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PodInfo(self, request, context):
    """PodInfo gets pod's info by podID
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PodRemove(self, request, context):
    """PodRemove deletes a pod by podID
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PodStart(self, request, context):
    """PodStart starts a pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PodStop(self, request, context):
    """PodStop stops a pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PodSignal(self, request, context):
    """PodSignal sends a signal to all containers of specified pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PodPause(self, request, context):
    """PodPause pauses a pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PodUnpause(self, request, context):
    """PodUnpause unpauses a pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecVM(self, request_iterator, context):
    """ExecVM executes a command outside of any containers.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContainerList(self, request, context):
    """ContainerList gets a list of containers
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContainerInfo(self, request, context):
    """ContainerInfo gets container's info by container's id or name
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ImageList(self, request, context):
    """ImageList gets a list of images by filters
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VMList(self, request, context):
    """VMList gets a list of HyperVMs
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetPodLabels(self, request, context):
    """SetPodLabels sets labels of given pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PodStats(self, request, context):
    """PodStats gets pod stats of a given pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContainerLogs(self, request, context):
    """ContainerLogs gets the log of specified container
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContainerCreate(self, request, context):
    """ContainerCreate creates a container in specified pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContainerStart(self, request, context):
    """ContainerStart starts a container in a specified pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContainerRename(self, request, context):
    """ContainerRename renames a container
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContainerSignal(self, request, context):
    """TODO: ContainerCommit commits the changes of the specified container
    ContainerSignal sends a signal to specified container
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContainerStop(self, request, context):
    """TODO: ContainerLabels updates labels of the specified container
    ContainerStop stops the specified container
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ContainerRemove(self, request, context):
    """ContainerRemove removes a container from a specified pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecCreate(self, request, context):
    """ExecCreate creates exec in specified container
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecStart(self, request_iterator, context):
    """ExecStart starts exec
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecSignal(self, request, context):
    """ExecSignal sends a signal to specified exec in specified container
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Attach(self, request_iterator, context):
    """Attach attaches to the specified container
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Wait(self, request, context):
    """Wait gets the exit code of the specified container
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TTYResize(self, request, context):
    """TTYResize resizes the tty of the specified container
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServiceList(self, request, context):
    """ServiceList gets a list of services
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServiceAdd(self, request, context):
    """ServiceAdd add a service to a pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServiceDelete(self, request, context):
    """ServiceDelete delete a service from a pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServiceUpdate(self, request, context):
    """ServiceUpdate updates an existing service of a pod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ImagePull(self, request, context):
    """ImagePull pulls a image from registry
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ImagePush(self, request, context):
    """ImagePush pushes a local image to registry
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ImageRemove(self, request, context):
    """ImageRemove deletes a image from hyperd
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Ping(self, request, context):
    """Ping checks if hyperd is running (returns 'OK' on success)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Info(self, request, context):
    """Info gets the info of hyperd
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Version(self, request, context):
    """Version gets the version and apiVersion of hyperd
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PublicAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PodList': grpc.unary_unary_rpc_method_handler(
          servicer.PodList,
          request_deserializer=types__pb2.PodListRequest.FromString,
          response_serializer=types__pb2.PodListResponse.SerializeToString,
      ),
      'PodCreate': grpc.unary_unary_rpc_method_handler(
          servicer.PodCreate,
          request_deserializer=types__pb2.PodCreateRequest.FromString,
          response_serializer=types__pb2.PodCreateResponse.SerializeToString,
      ),
      'PodInfo': grpc.unary_unary_rpc_method_handler(
          servicer.PodInfo,
          request_deserializer=types__pb2.PodInfoRequest.FromString,
          response_serializer=types__pb2.PodInfoResponse.SerializeToString,
      ),
      'PodRemove': grpc.unary_unary_rpc_method_handler(
          servicer.PodRemove,
          request_deserializer=types__pb2.PodRemoveRequest.FromString,
          response_serializer=types__pb2.PodRemoveResponse.SerializeToString,
      ),
      'PodStart': grpc.unary_unary_rpc_method_handler(
          servicer.PodStart,
          request_deserializer=types__pb2.PodStartRequest.FromString,
          response_serializer=types__pb2.PodStartResponse.SerializeToString,
      ),
      'PodStop': grpc.unary_unary_rpc_method_handler(
          servicer.PodStop,
          request_deserializer=types__pb2.PodStopRequest.FromString,
          response_serializer=types__pb2.PodStopResponse.SerializeToString,
      ),
      'PodSignal': grpc.unary_unary_rpc_method_handler(
          servicer.PodSignal,
          request_deserializer=types__pb2.PodSignalRequest.FromString,
          response_serializer=types__pb2.PodSignalResponse.SerializeToString,
      ),
      'PodPause': grpc.unary_unary_rpc_method_handler(
          servicer.PodPause,
          request_deserializer=types__pb2.PodPauseRequest.FromString,
          response_serializer=types__pb2.PodPauseResponse.SerializeToString,
      ),
      'PodUnpause': grpc.unary_unary_rpc_method_handler(
          servicer.PodUnpause,
          request_deserializer=types__pb2.PodUnpauseRequest.FromString,
          response_serializer=types__pb2.PodUnpauseResponse.SerializeToString,
      ),
      'ExecVM': grpc.stream_stream_rpc_method_handler(
          servicer.ExecVM,
          request_deserializer=types__pb2.ExecVMRequest.FromString,
          response_serializer=types__pb2.ExecVMResponse.SerializeToString,
      ),
      'ContainerList': grpc.unary_unary_rpc_method_handler(
          servicer.ContainerList,
          request_deserializer=types__pb2.ContainerListRequest.FromString,
          response_serializer=types__pb2.ContainerListResponse.SerializeToString,
      ),
      'ContainerInfo': grpc.unary_unary_rpc_method_handler(
          servicer.ContainerInfo,
          request_deserializer=types__pb2.ContainerInfoRequest.FromString,
          response_serializer=types__pb2.ContainerInfoResponse.SerializeToString,
      ),
      'ImageList': grpc.unary_unary_rpc_method_handler(
          servicer.ImageList,
          request_deserializer=types__pb2.ImageListRequest.FromString,
          response_serializer=types__pb2.ImageListResponse.SerializeToString,
      ),
      'VMList': grpc.unary_unary_rpc_method_handler(
          servicer.VMList,
          request_deserializer=types__pb2.VMListRequest.FromString,
          response_serializer=types__pb2.VMListResponse.SerializeToString,
      ),
      'SetPodLabels': grpc.unary_unary_rpc_method_handler(
          servicer.SetPodLabels,
          request_deserializer=types__pb2.PodLabelsRequest.FromString,
          response_serializer=types__pb2.PodLabelsResponse.SerializeToString,
      ),
      'PodStats': grpc.unary_unary_rpc_method_handler(
          servicer.PodStats,
          request_deserializer=types__pb2.PodStatsRequest.FromString,
          response_serializer=types__pb2.PodStatsResponse.SerializeToString,
      ),
      'ContainerLogs': grpc.unary_stream_rpc_method_handler(
          servicer.ContainerLogs,
          request_deserializer=types__pb2.ContainerLogsRequest.FromString,
          response_serializer=types__pb2.ContainerLogsResponse.SerializeToString,
      ),
      'ContainerCreate': grpc.unary_unary_rpc_method_handler(
          servicer.ContainerCreate,
          request_deserializer=types__pb2.ContainerCreateRequest.FromString,
          response_serializer=types__pb2.ContainerCreateResponse.SerializeToString,
      ),
      'ContainerStart': grpc.unary_unary_rpc_method_handler(
          servicer.ContainerStart,
          request_deserializer=types__pb2.ContainerStartRequest.FromString,
          response_serializer=types__pb2.ContainerStartResponse.SerializeToString,
      ),
      'ContainerRename': grpc.unary_unary_rpc_method_handler(
          servicer.ContainerRename,
          request_deserializer=types__pb2.ContainerRenameRequest.FromString,
          response_serializer=types__pb2.ContainerRenameResponse.SerializeToString,
      ),
      'ContainerSignal': grpc.unary_unary_rpc_method_handler(
          servicer.ContainerSignal,
          request_deserializer=types__pb2.ContainerSignalRequest.FromString,
          response_serializer=types__pb2.ContainerSignalResponse.SerializeToString,
      ),
      'ContainerStop': grpc.unary_unary_rpc_method_handler(
          servicer.ContainerStop,
          request_deserializer=types__pb2.ContainerStopRequest.FromString,
          response_serializer=types__pb2.ContainerStopResponse.SerializeToString,
      ),
      'ContainerRemove': grpc.unary_unary_rpc_method_handler(
          servicer.ContainerRemove,
          request_deserializer=types__pb2.ContainerRemoveRequest.FromString,
          response_serializer=types__pb2.ContainerRemoveResponse.SerializeToString,
      ),
      'ExecCreate': grpc.unary_unary_rpc_method_handler(
          servicer.ExecCreate,
          request_deserializer=types__pb2.ExecCreateRequest.FromString,
          response_serializer=types__pb2.ExecCreateResponse.SerializeToString,
      ),
      'ExecStart': grpc.stream_stream_rpc_method_handler(
          servicer.ExecStart,
          request_deserializer=types__pb2.ExecStartRequest.FromString,
          response_serializer=types__pb2.ExecStartResponse.SerializeToString,
      ),
      'ExecSignal': grpc.unary_unary_rpc_method_handler(
          servicer.ExecSignal,
          request_deserializer=types__pb2.ExecSignalRequest.FromString,
          response_serializer=types__pb2.ExecSignalResponse.SerializeToString,
      ),
      'Attach': grpc.stream_stream_rpc_method_handler(
          servicer.Attach,
          request_deserializer=types__pb2.AttachMessage.FromString,
          response_serializer=types__pb2.AttachMessage.SerializeToString,
      ),
      'Wait': grpc.unary_unary_rpc_method_handler(
          servicer.Wait,
          request_deserializer=types__pb2.WaitRequest.FromString,
          response_serializer=types__pb2.WaitResponse.SerializeToString,
      ),
      'TTYResize': grpc.unary_unary_rpc_method_handler(
          servicer.TTYResize,
          request_deserializer=types__pb2.TTYResizeRequest.FromString,
          response_serializer=types__pb2.TTYResizeResponse.SerializeToString,
      ),
      'ServiceList': grpc.unary_unary_rpc_method_handler(
          servicer.ServiceList,
          request_deserializer=types__pb2.ServiceListRequest.FromString,
          response_serializer=types__pb2.ServiceListResponse.SerializeToString,
      ),
      'ServiceAdd': grpc.unary_unary_rpc_method_handler(
          servicer.ServiceAdd,
          request_deserializer=types__pb2.ServiceAddRequest.FromString,
          response_serializer=types__pb2.ServiceAddResponse.SerializeToString,
      ),
      'ServiceDelete': grpc.unary_unary_rpc_method_handler(
          servicer.ServiceDelete,
          request_deserializer=types__pb2.ServiceDelRequest.FromString,
          response_serializer=types__pb2.ServiceDelResponse.SerializeToString,
      ),
      'ServiceUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.ServiceUpdate,
          request_deserializer=types__pb2.ServiceUpdateRequest.FromString,
          response_serializer=types__pb2.ServiceUpdateResponse.SerializeToString,
      ),
      'ImagePull': grpc.unary_stream_rpc_method_handler(
          servicer.ImagePull,
          request_deserializer=types__pb2.ImagePullRequest.FromString,
          response_serializer=types__pb2.ImagePullResponse.SerializeToString,
      ),
      'ImagePush': grpc.unary_stream_rpc_method_handler(
          servicer.ImagePush,
          request_deserializer=types__pb2.ImagePushRequest.FromString,
          response_serializer=types__pb2.ImagePushResponse.SerializeToString,
      ),
      'ImageRemove': grpc.unary_unary_rpc_method_handler(
          servicer.ImageRemove,
          request_deserializer=types__pb2.ImageRemoveRequest.FromString,
          response_serializer=types__pb2.ImageRemoveResponse.SerializeToString,
      ),
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=types__pb2.PingRequest.FromString,
          response_serializer=types__pb2.PingResponse.SerializeToString,
      ),
      'Info': grpc.unary_unary_rpc_method_handler(
          servicer.Info,
          request_deserializer=types__pb2.InfoRequest.FromString,
          response_serializer=types__pb2.InfoResponse.SerializeToString,
      ),
      'Version': grpc.unary_unary_rpc_method_handler(
          servicer.Version,
          request_deserializer=types__pb2.VersionRequest.FromString,
          response_serializer=types__pb2.VersionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'types.PublicAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
