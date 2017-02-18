# -*- coding: utf-8 -*-

"""
    healthoslib.models.search_food_restaurants_response
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 02/18/2017
"""
import healthoslib.models.base_model

class SearchFoodRestaurantsResponse(healthoslib.models.base_model.BaseModel):

    """Implementation of the 'Search Food RestaurantsResponse' model.

    TODO: type model description here.

    Attributes:
        logo (string): TODO: type description here.
        name (string): TODO: type description here.
        food_restaurant_id (string): TODO: type description here.
        search_score (float): TODO: type description here.

    """

    def __init__(self, 
                 logo = None,
                 name = None,
                 food_restaurant_id = None,
                 search_score = None):
        """Constructor for the SearchFoodRestaurantsResponse class"""
        
        # Initialize members of the class
        self.logo = logo
        self.name = name
        self.food_restaurant_id = food_restaurant_id
        self.search_score = search_score

        # Create a mapping from Model property names to API property names
        self.names = {
            "logo" : "logo",
            "name" : "name",
            "food_restaurant_id" : "food_restaurant_id",
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
            logo = dictionary.get("logo")
            name = dictionary.get("name")
            food_restaurant_id = dictionary.get("food_restaurant_id")
            search_score = dictionary.get("search_score")
            # Return an object of this model
            return cls(logo,
                       name,
                       food_restaurant_id,
                       search_score)


