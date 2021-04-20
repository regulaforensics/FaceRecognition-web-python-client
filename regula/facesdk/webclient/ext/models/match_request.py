from typing import List, Union

from regula.facesdk.webclient.ext.common import Base64String
from regula.facesdk.webclient.ext.models.match_image import MatchImage
from regula.facesdk.webclient.gen import MatchRequest as GenMatchRequest, ApiValueError


class MatchRequest(GenMatchRequest):
    def __init__(
            self, images: List[Union[MatchImage, Base64String, bytes]], thumbnails=False,
            local_vars_configuration=None
    ):
        if not images:
            raise ApiValueError(f"compare request images: expected size <more than 1>")

        input_images = []
        for index, item in enumerate(images):
            if isinstance(item, MatchImage):
                input_images.append(item)
            else:
                input_images.append(MatchImage(index, None, item, local_vars_configuration))

        super().__init__(
            images=input_images, local_vars_configuration=local_vars_configuration, thumbnails=thumbnails
        )
