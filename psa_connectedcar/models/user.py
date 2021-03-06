# coding: utf-8

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class User(object):
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
        'created_at': 'datetime',
        'embedded': 'UserEmbedded',
        'links': 'UserLinks',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'embedded': '_embedded',
        'links': '_links',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName'
    }

    def __init__(self, created_at=None, embedded=None, links=None, email=None, first_name=None, last_name=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._embedded = None
        self._links = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if embedded is not None:
            self.embedded = embedded
        if links is not None:
            self.links = links
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501

        Date when the resource has been created.  # noqa: E501

        :return: The created_at of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.

        Date when the resource has been created.  # noqa: E501

        :param created_at: The created_at of this User.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def embedded(self):
        """Gets the embedded of this User.  # noqa: E501


        :return: The embedded of this User.  # noqa: E501
        :rtype: UserEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this User.


        :param embedded: The embedded of this User.  # noqa: E501
        :type: UserEmbedded
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this User.  # noqa: E501


        :return: The links of this User.  # noqa: E501
        :rtype: UserLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this User.


        :param links: The links of this User.  # noqa: E501
        :type: UserLinks
        """

        self._links = links

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        Mail of user  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        Mail of user  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501

        First name of user  # noqa: E501

        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

        First name of user  # noqa: E501

        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501

        Last name of user  # noqa: E501

        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

        Last name of user  # noqa: E501

        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
