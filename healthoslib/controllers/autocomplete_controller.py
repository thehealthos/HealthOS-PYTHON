# -*- coding: utf-8 -*-

"""
    healthoslib.controllers.autocomplete_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 02/18/2017
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2

class AutocompleteController(BaseController):

    """A Controller to access Endpoints in the healthoslib API."""
    

    def get_exercises(self,
                      exercise_query):
        """Does a GET request to /autocomplete/exercises/{exercise_query}.

        TODO: Add Description

        Args:
            exercise_query (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/autocomplete/exercises/{exercise_query}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'exercise_query': exercise_query
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_diseases(self,
                     disease_query):
        """Does a GET request to /autocomplete/diseases/{disease_query}.

        TODO: Add Description

        Args:
            disease_query (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/autocomplete/diseases/{disease_query}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'disease_query': disease_query
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_lab_tests(self,
                      lab_test_query):
        """Does a GET request to /autocomplete/lab_tests/{lab_test_query}.

        TODO: Add Description

        Args:
            lab_test_query (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/autocomplete/lab_tests/{lab_test_query}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'lab_test_query': lab_test_query
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_food_items(self,
                       food_item_query):
        """Does a GET request to /autocomplete/food/items/{food_item_query}.

        TODO: Add Description

        Args:
            food_item_query (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/autocomplete/food/items/{food_item_query}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'food_item_query': food_item_query
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_generics(self,
                     generic_query):
        """Does a GET request to /autocomplete/medicines/generics/{generic_query}.

        TODO: Add Description

        Args:
            generic_query (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/autocomplete/medicines/generics/{generic_query}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'generic_query': generic_query
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_medicines(self,
                      medicine_query):
        """Does a GET request to /autocomplete/medicines/brands/{medicine_query}.

        TODO: Add Description

        Args:
            medicine_query (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/autocomplete/medicines/brands/{medicine_query}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'medicine_query': medicine_query
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)
