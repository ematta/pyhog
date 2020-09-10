# coding: utf-8

"""
    MailHog API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Messages(object):
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
        'total': 'float',
        'start': 'float',
        'count': 'float',
        'messages': 'list[Message]'
    }

    attribute_map = {
        'total': 'total',
        'start': 'start',
        'count': 'count',
        'messages': 'messages'
    }

    def __init__(self, total=None, start=None, count=None, messages=None, local_vars_configuration=None):  # noqa: E501
        """Messages - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._start = None
        self._count = None
        self._messages = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if start is not None:
            self.start = start
        if count is not None:
            self.count = count
        if messages is not None:
            self.messages = messages

    @property
    def total(self):
        """Gets the total of this Messages.  # noqa: E501

        Total number of stored messages  # noqa: E501

        :return: The total of this Messages.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Messages.

        Total number of stored messages  # noqa: E501

        :param total: The total of this Messages.  # noqa: E501
        :type total: float
        """

        self._total = total

    @property
    def start(self):
        """Gets the start of this Messages.  # noqa: E501

        Start index of first returned message  # noqa: E501

        :return: The start of this Messages.  # noqa: E501
        :rtype: float
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Messages.

        Start index of first returned message  # noqa: E501

        :param start: The start of this Messages.  # noqa: E501
        :type start: float
        """

        self._start = start

    @property
    def count(self):
        """Gets the count of this Messages.  # noqa: E501

        Number of returned messages  # noqa: E501

        :return: The count of this Messages.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Messages.

        Number of returned messages  # noqa: E501

        :param count: The count of this Messages.  # noqa: E501
        :type count: float
        """

        self._count = count

    @property
    def messages(self):
        """Gets the messages of this Messages.  # noqa: E501


        :return: The messages of this Messages.  # noqa: E501
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this Messages.


        :param messages: The messages of this Messages.  # noqa: E501
        :type messages: list[Message]
        """

        self._messages = messages

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
        if not isinstance(other, Messages):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Messages):
            return True

        return self.to_dict() != other.to_dict()
