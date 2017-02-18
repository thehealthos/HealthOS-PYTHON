# -*- coding: utf-8 -*-

"""
    healthoslib.models.lab_test_data_34
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 02/18/2017
"""
import healthoslib.models.base_model

class LabTestData34(healthoslib.models.base_model.BaseModel):

    """Implementation of the 'LabTestData34' model.

    TODO: type model description here.

    Attributes:
        ordering_information (string): TODO: type description here.
        laboratory (string): TODO: type description here.
        test_code (string): TODO: type description here.
        specimen_types (string): TODO: type description here.
        container_types (string): TODO: type description here.
        collection_instructions (string): TODO: type description here.
        frequency (string): TODO: type description here.

    """

    def __init__(self, 
                 ordering_information = None,
                 laboratory = None,
                 test_code = None,
                 specimen_types = None,
                 container_types = None,
                 collection_instructions = None,
                 frequency = None):
        """Constructor for the LabTestData34 class"""
        
        # Initialize members of the class
        self.ordering_information = ordering_information
        self.laboratory = laboratory
        self.test_code = test_code
        self.specimen_types = specimen_types
        self.container_types = container_types
        self.collection_instructions = collection_instructions
        self.frequency = frequency

        # Create a mapping from Model property names to API property names
        self.names = {
            "ordering_information" : "Ordering information",
            "laboratory" : "Laboratory",
            "test_code" : "Test Code",
            "specimen_types" : "Specimen types",
            "container_types" : "Container types",
            "collection_instructions" : "Collection Instructions",
            "frequency" : "Frequency",
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
            ordering_information = dictionary.get("Ordering information")
            laboratory = dictionary.get("Laboratory")
            test_code = dictionary.get("Test Code")
            specimen_types = dictionary.get("Specimen types")
            container_types = dictionary.get("Container types")
            collection_instructions = dictionary.get("Collection Instructions")
            frequency = dictionary.get("Frequency")
            # Return an object of this model
            return cls(ordering_information,
                       laboratory,
                       test_code,
                       specimen_types,
                       container_types,
                       collection_instructions,
                       frequency)


