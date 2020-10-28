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


class DetectResponse(object):
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
        'code': 'FaceRecognitionResultCode',
        'results': 'DetectResult'
    }

    attribute_map = {
        'code': 'code',
        'results': 'results'
    }

    def __init__(self, code=None, results=None, local_vars_configuration=None):  # noqa: E501
        """DetectResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._results = None
        self.discriminator = None

        self.code = code
        self.results = results

    @property
    def code(self):
        """Gets the code of this DetectResponse.  # noqa: E501


        :return: The code of this DetectResponse.  # noqa: E501
        :rtype: FaceRecognitionResultCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DetectResponse.


        :param code: The code of this DetectResponse.  # noqa: E501
        :type code: FaceRecognitionResultCode
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def results(self):
        """Gets the results of this DetectResponse.  # noqa: E501


        :return: The results of this DetectResponse.  # noqa: E501
        :rtype: DetectResult
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this DetectResponse.


        :param results: The results of this DetectResponse.  # noqa: E501
        :type results: DetectResult
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

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
        if not isinstance(other, DetectResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetectResponse):
            return True

        return self.to_dict() != other.to_dict()
