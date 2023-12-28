import oidn
from PIL import Image
import numpy as np

img = np.array(Image.open("example.png"), dtype=np.float32) / 255.0

result = np.zeros_like(img, dtype=np.float32)

device = oidn.NewDevice()
oidn.CommitDevice(device)

filter = oidn.NewFilter(device, "RT")

oidn.SetSharedFilterImage(
    filter,             # filter handle
    "color",            # name 
    img,                # data
    oidn.FORMAT_FLOAT4, # format
    img.shape[1],       # width
    img.shape[0]        # height
)
oidn.SetSharedFilterImage(
    filter,             # filter handle
    "output",           # name 
    result,             # data
    oidn.FORMAT_FLOAT4, # format
    img.shape[1],       # width
    img.shape[0]        # height
)

oidn.CommitFilter(filter)
oidn.ExecuteFilter(filter)

result = np.array(np.clip(result * 255, 0, 255), dtype=np.uint8)
resultImage = Image.fromarray(result)
resultImage.save("result.png")

oidn.ReleaseFilter(filter)
oidn.ReleaseDevice(device)
