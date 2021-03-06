# coding: utf-8

"""
    katib

    swagger description for katib  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha3SuggestionSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'algorithm_name': 'str',
        'requests': 'int'
    }

    attribute_map = {
        'algorithm_name': 'algorithmName',
        'requests': 'requests'
    }

    def __init__(self, algorithm_name=None, requests=None):  # noqa: E501
        """V1alpha3SuggestionSpec - a model defined in Swagger"""  # noqa: E501

        self._algorithm_name = None
        self._requests = None
        self.discriminator = None

        self.algorithm_name = algorithm_name
        if requests is not None:
            self.requests = requests

    @property
    def algorithm_name(self):
        """Gets the algorithm_name of this V1alpha3SuggestionSpec.  # noqa: E501


        :return: The algorithm_name of this V1alpha3SuggestionSpec.  # noqa: E501
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        """Sets the algorithm_name of this V1alpha3SuggestionSpec.


        :param algorithm_name: The algorithm_name of this V1alpha3SuggestionSpec.  # noqa: E501
        :type: str
        """
        if algorithm_name is None:
            raise ValueError("Invalid value for `algorithm_name`, must not be `None`")  # noqa: E501

        self._algorithm_name = algorithm_name

    @property
    def requests(self):
        """Gets the requests of this V1alpha3SuggestionSpec.  # noqa: E501

        Number of suggestions requested  # noqa: E501

        :return: The requests of this V1alpha3SuggestionSpec.  # noqa: E501
        :rtype: int
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this V1alpha3SuggestionSpec.

        Number of suggestions requested  # noqa: E501

        :param requests: The requests of this V1alpha3SuggestionSpec.  # noqa: E501
        :type: int
        """

        self._requests = requests

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(V1alpha3SuggestionSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha3SuggestionSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
