# -*- coding: utf-8 -*-

"""
    healthoslib.models.search_lab_tests_response
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 02/18/2017
"""
import healthoslib.models.lab_test_data
import healthoslib.models.base_model

class SearchLabTestsResponse(healthoslib.models.base_model.BaseModel):

    """Implementation of the 'Search Lab TestsResponse' model.

    TODO: type model description here.

    Attributes:
        alternate_name (string): TODO: type description here.
        lab_test_data (LabTestData): TODO: type description here.
        lab_test_id (string): TODO: type description here.
        lab_test_name (string): TODO: type description here.
        id (string): TODO: type description here.
        search_score (float): TODO: type description here.

    """

    def __init__(self, 
                 alternate_name = None,
                 lab_test_data = None,
                 lab_test_id = None,
                 lab_test_name = None,
                 id = None,
                 search_score = None):
        """Constructor for the SearchLabTestsResponse class"""
        
        # Initialize members of the class
        self.alternate_name = alternate_name
        self.lab_test_data = lab_test_data
        self.lab_test_id = lab_test_id
        self.lab_test_name = lab_test_name
        self.id = id
        self.search_score = search_score

        # Create a mapping from Model property names to API property names
        self.names = {
            "alternate_name" : "alternate_name",
            "lab_test_data" : "lab_test_data",
            "lab_test_id" : "lab_test_id",
            "lab_test_name" : "lab_test_name",
            "id" : "id",
            "search_score" : "search_score",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            alternate_name = dictionary.get("alternate_name")
            lab_test_data = healthoslib.models.lab_test_data.LabTestData.from_dictionary(dictionary.get("lab_test_data")) if dictionary.get("lab_test_data") else None
            lab_test_id = dictionary.get("lab_test_id")
            lab_test_name = dictionary.get("lab_test_name")
            id = dictionary.get("id")
            search_score = dictionary.get("search_score")
            # Return an object of this model
            return cls(alternate_name,
                       lab_test_data,
                       lab_test_id,
                       lab_test_name,
                       id,
                       search_score)


