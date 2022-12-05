# coding: utf-8

"""
    Container Security API

    # Authentication You must authenticate to the Qualys Cloud Platform using Qualys account credentials (user name and password) and get the JSON Web Token (JWT) before you can start using the Container Security APIs. Use the Qualys Authentication API to get the JWT.  **Example Authentication Curl Request**:  curl -X POST https://gateway/auth -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=value1&password=passwordValue&token=true' where - gateway is the base URL to the Qualys API server where your account is located. - **username** and **password** are the credentials of the user account for which you want to fetch Container Security data. - **token** should be **true** - **Content-Type** should be **application/x-www-form-urlencoded**   # noqa: E501

    OpenAPI spec version: v1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import QualysAPI
from QualysAPI.api.container_api import ContainerApi  # noqa: E501
from QualysAPI.rest import ApiException


class TestContainerApi(unittest.TestCase):
    """ContainerApi unit test stubs"""

    def setUp(self):
        self.api = ContainerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_cs_containers(self):
        """Test case for delete_cs_containers

        Delete containers in your account  # noqa: E501
        """
        pass

    def test_get_container_details_using_get(self):
        """Test case for get_container_details_using_get

        show details of a container  # noqa: E501
        """
        pass

    def test_get_container_list_with_details(self):
        """Test case for get_container_list_with_details

        Containers Bulk API  # noqa: E501
        """
        pass

    def test_get_container_policy_compliance_details_using_get(self):
        """Test case for get_container_policy_compliance_details_using_get

        show policy compliance details of a container  # noqa: E501
        """
        pass

    def test_get_container_software_using_get(self):
        """Test case for get_container_software_using_get

        Show software installed on a container  # noqa: E501
        """
        pass

    def test_get_container_vuln_count_using_get(self):
        """Test case for get_container_vuln_count_using_get

        Show vulnerability count for a container  # noqa: E501
        """
        pass

    def test_get_container_vuln_using_get(self):
        """Test case for get_container_vuln_using_get

        Show vulnerability details for a container  # noqa: E501
        """
        pass

    def test_get_cs_containers_data_using_get(self):
        """Test case for get_cs_containers_data_using_get

        Show a list of containers in your account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()