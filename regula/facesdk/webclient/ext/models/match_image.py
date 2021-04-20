from typing import Union

from regula.facesdk.webclient.ext.common import Base64String, bytes_to_base64
from regula.facesdk.webclient.gen import ApiValueError, MatchImage as GenMatchImage, ImageSource


class MatchImage(GenMatchImage):
    def __init__(self, index=None, type=None, data: Union[Base64String, bytes] = None, local_vars_configuration=None):
        if not data:
            raise ApiValueError(f"compare image {index} data: expected <not empty>")

        if not type:
            type = ImageSource.LIVE
        if isinstance(data, bytes):
            data = bytes_to_base64(data)

        super().__init__(index, type, data, local_vars_configuration)
