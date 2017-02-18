# -*- coding: utf-8 -*-

"""
    healthoslib.models.medicine_interactions_response
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 02/18/2017
"""
import healthoslib.models.interaction
import healthoslib.models.base_model

class MedicineInteractionsResponse(healthoslib.models.base_model.BaseModel):

    """Implementation of the 'Medicine InteractionsResponse' model.

    TODO: type model description here.

    Attributes:
        generic (string): TODO: type description here.
        interactions (list of Interaction): TODO: type description here.

    """

    def __init__(self, 
                 generic = None,
                 interactions = None):
        """Constructor for the MedicineInteractionsResponse class"""
        
        # Initialize members of the class
        self.generic = generic
        self.interactions = interactions

        # Create a mapping from Model property names to API property names
        self.names = {
            "generic" : "generic",
            "interactions" : "interactions",
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
            generic = dictionary.get("generic")
            interactions = None
            if dictionary.get("interactions") != None:
                interactions = list()
                for structure in dictionary.get("interactions"):
                    interactions.append(healthoslib.models.interaction.Interaction.from_dictionary(structure))
            # Return an object of this model
            return cls(generic,
                       interactions)


