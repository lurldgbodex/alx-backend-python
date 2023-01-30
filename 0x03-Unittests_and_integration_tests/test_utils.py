#!/usr/bin/env python3
'''test module for utils'''

import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''access_nested_map test class'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        '''test access_nested_map output'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a', ), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str],
                                         exception: Exception) -> None:
        '''Tests acces_nested_map exception'''
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Test class for get_json'''
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        '''Tests get_json output'''
        attri = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**attri)) as get_request:
            self.assertEqual(get_json(test_url), test_payload)
            get_request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''Memoize test class'''
    def test_memoize(self):
        '''Test memoize'''

        class TestClass:
            """ Test Class for wrapping with memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
