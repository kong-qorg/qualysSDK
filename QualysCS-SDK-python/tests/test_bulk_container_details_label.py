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
from QualysAPI.models.bulk_container_details_label import BulkContainerDetailsLabel  # noqa: E501
from QualysAPI.rest import ApiException


class TestBulkContainerDetailsLabel(unittest.TestCase):
    """BulkContainerDetailsLabel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBulkContainerDetailsLabel(self):
        """Test BulkContainerDetailsLabel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QualysAPI.models.bulk_container_details_label.BulkContainerDetailsLabel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
