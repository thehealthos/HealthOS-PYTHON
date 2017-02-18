# -*- coding: utf-8 -*-

"""
    healthoslib.models.all_exercises_response
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 02/18/2017
"""
import healthoslib.models.base_model

class AllExercisesResponse(healthoslib.models.base_model.BaseModel):

    """Implementation of the 'All ExercisesResponse' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        calory_count (string): TODO: type description here.
        category (string): TODO: type description here.
        cardio_subcategory (string): TODO: type description here.
        primary_muscle_group (string): TODO: type description here.
        excercise_id (string): TODO: type description here.

    """

    def __init__(self, 
                 name = None,
                 calory_count = None,
                 category = None,
                 cardio_subcategory = None,
                 primary_muscle_group = None,
                 excercise_id = None):
        """Constructor for the AllExercisesResponse class"""
        
        # Initialize members of the class
        self.name = name
        self.calory_count = calory_count
        self.category = category
        self.cardio_subcategory = cardio_subcategory
        self.primary_muscle_group = primary_muscle_group
        self.excercise_id = excercise_id

        # Create a mapping from Model property names to API property names
        self.names = {
            "name" : "name",
            "calory_count" : "calory_count",
            "category" : "category",
            "cardio_subcategory" : "cardio_subcategory",
            "primary_muscle_group" : "primary_muscle_group",
            "excercise_id" : "excercise_id",
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
            calory_count = dictionary.get("calory_count")
            category = dictionary.get("category")
            cardio_subcategory = dictionary.get("cardio_subcategory")
            primary_muscle_group = dictionary.get("primary_muscle_group")
            excercise_id = dictionary.get("excercise_id")
            # Return an object of this model
            return cls(name,
                       calory_count,
                       category,
                       cardio_subcategory,
                       primary_muscle_group,
                       excercise_id)


