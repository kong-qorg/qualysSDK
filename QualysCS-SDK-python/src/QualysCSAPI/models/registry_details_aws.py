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

class RegistryDetailsAws(object):
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
        'account_id': 'str',
        'arn': 'str',
        'description': 'str',
        'name': 'str',
        'region': 'str',
        'account_type': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'arn': 'arn',
        'description': 'description',
        'name': 'name',
        'region': 'region',
        'account_type': 'accountType'
    }

    def __init__(self, account_id=None, arn=None, description=None, name=None, region=None, account_type=None):  # noqa: E501
        """RegistryDetailsAws - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._arn = None
        self._description = None
        self._name = None
        self._region = None
        self._account_type = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if arn is not None:
            self.arn = arn
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if account_type is not None:
            self.account_type = account_type

    @property
    def account_id(self):
        """Gets the account_id of this RegistryDetailsAws.  # noqa: E501


        :return: The account_id of this RegistryDetailsAws.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RegistryDetailsAws.


        :param account_id: The account_id of this RegistryDetailsAws.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def arn(self):
        """Gets the arn of this RegistryDetailsAws.  # noqa: E501


        :return: The arn of this RegistryDetailsAws.  # noqa: E501
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, arn):
        """Sets the arn of this RegistryDetailsAws.


        :param arn: The arn of this RegistryDetailsAws.  # noqa: E501
        :type: str
        """

        self._arn = arn

    @property
    def description(self):
        """Gets the description of this RegistryDetailsAws.  # noqa: E501


        :return: The description of this RegistryDetailsAws.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RegistryDetailsAws.


        :param description: The description of this RegistryDetailsAws.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this RegistryDetailsAws.  # noqa: E501


        :return: The name of this RegistryDetailsAws.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegistryDetailsAws.


        :param name: The name of this RegistryDetailsAws.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this RegistryDetailsAws.  # noqa: E501


        :return: The region of this RegistryDetailsAws.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this RegistryDetailsAws.


        :param region: The region of this RegistryDetailsAws.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def account_type(self):
        """Gets the account_type of this RegistryDetailsAws.  # noqa: E501


        :return: The account_type of this RegistryDetailsAws.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this RegistryDetailsAws.


        :param account_type: The account_type of this RegistryDetailsAws.  # noqa: E501
        :type: str
        """

        self._account_type = account_type

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
        if issubclass(RegistryDetailsAws, dict):
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
        if not isinstance(other, RegistryDetailsAws):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
