from jnius import autoclass, cast

class Flash:
    CameraManager = autoclass('android.hardware.camera2.CameraManager')
    Context=autoclass("android.content.Context")
    context=Context()
    camera_manager=cast("android.hardware.camera2.CameraManager",context.getSystemService(Context.CAMERA_SERVICE))
    cameraid = camera_manager.getCameraIdList()[0]
    @staticmethod
    def on():
        Flash.camera_manager.setTorchMode(Flash.cameraid, True)
    @staticmethod
    def off():
        Flash.camera_manager.setTorchMode(Flash.cameraid, False)