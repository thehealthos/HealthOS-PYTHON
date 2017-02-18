# -*- coding: utf-8 -*-

"""
    healthoslib.models.generics_response
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 02/18/2017
"""
import healthoslib.models.base_model

class GenericsResponse(healthoslib.models.base_model.BaseModel):

    """Implementation of the 'GenericsResponse' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        generic_id (string): TODO: type description here.
        therauptic_uses (list of string): TODO: type description here.
        search_score (float): TODO: type description here.

    """

    def __init__(self, 
                 name = None,
                 generic_id = None,
                 therauptic_uses = None,
                 search_score = None):
        """Constructor for the GenericsResponse class"""
        
        # Initialize members of the class
        self.name = name
        self.generic_id = generic_id
        self.therauptic_uses = therauptic_uses
        self.search_score = search_score

        # Create a mapping from Model property names to API property names
        self.names = {
            "name" : "name",
            "generic_id" : "generic_id",
            "therauptic_uses" : "therauptic_uses",
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
            name = dictionary.get("name")
            generic_id = dictionary.get("generic_id")
            therauptic_uses = dictionary.get("therauptic_uses")
            search_score = dictionary.get("search_score")
            # Return an object of this model
            return cls(name,
                       generic_id,
                       therauptic_uses,
                       search_score)


