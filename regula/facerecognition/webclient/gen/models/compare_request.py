# coding: utf-8

"""
    Regula Face Recognition Web API

    Regula Face Recognition Web API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facerecognition.webclient.gen.configuration import Configuration


class CompareRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'thumbnails': 'bool',
        'images': 'list[CompareImage]'
    }

    attribute_map = {
        'thumbnails': 'thumbnails',
        'images': 'images'
    }

    def __init__(self, thumbnails=False, images=None, local_vars_configuration=None):  # noqa: E501
        """CompareRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._thumbnails = None
        self._images = None
        self.discriminator = None

        if thumbnails is not None:
            self.thumbnails = thumbnails
        self.images = images

    @property
    def thumbnails(self):
        """Gets the thumbnails of this CompareRequest.  # noqa: E501


        :return: The thumbnails of this CompareRequest.  # noqa: E501
        :rtype: bool
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """Sets the thumbnails of this CompareRequest.


        :param thumbnails: The thumbnails of this CompareRequest.  # noqa: E501
        :type thumbnails: bool
        """

        self._thumbnails = thumbnails

    @property
    def images(self):
        """Gets the images of this CompareRequest.  # noqa: E501


        :return: The images of this CompareRequest.  # noqa: E501
        :rtype: list[CompareImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this CompareRequest.


        :param images: The images of this CompareRequest.  # noqa: E501
        :type images: list[CompareImage]
        """
        if self.local_vars_configuration.client_side_validation and images is None:  # noqa: E501
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CompareRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompareRequest):
            return True

        return self.to_dict() != other.to_dict()
