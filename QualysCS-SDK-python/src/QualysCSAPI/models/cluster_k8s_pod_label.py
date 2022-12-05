# coding: utf-8

"""
    Container Security API

    # Authentication You must authenticate to the Qualys Cloud Platform using Qualys account credentials (user name and password) and get the JSON Web Token (JWT) before you can start using the Container Security APIs. Use the Qualys Authentication API to get the JWT.  **Example Authentication Curl Request**:  curl -X POST https://gateway/auth -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=value1&password=passwordValue&token=true' where - gateway is the base URL to the Qualys API server where your account is located. - **username** and **password** are the credentials of the user account for which you want to fetch Container Security data. - **token** should be **true** - **Content-Type** should be **application/x-www-form-urlencoded**   # noqa: E501

    OpenAPI spec version: v1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ClusterK8sPodLabel(object):
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
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):  # noqa: E501
        """ClusterK8sPodLabel - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._value = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def key(self):
        """Gets the key of this ClusterK8sPodLabel.  # noqa: E501


        :return: The key of this ClusterK8sPodLabel.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ClusterK8sPodLabel.


        :param key: The key of this ClusterK8sPodLabel.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this ClusterK8sPodLabel.  # noqa: E501


        :return: The value of this ClusterK8sPodLabel.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ClusterK8sPodLabel.


        :param value: The value of this ClusterK8sPodLabel.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(ClusterK8sPodLabel, dict):
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
        if not isinstance(other, ClusterK8sPodLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
