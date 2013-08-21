# -*- coding: utf-8 -*-

###############################################################################
#
# Image
# Generates a thumbnail for an image from the content database to the requested size. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Image(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Image Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Freebase/Image')


    def new_input_set(self):
        return ImageInputSet()

    def _make_result_set(self, result, path):
        return ImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ImageChoreographyExecution(session, exec_id, path)

class ImageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Image
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Freebase.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_FallbackID(self, value):
        """
        Set the value of the FallbackID input for this Choreo. ((optional, string) Use this second (fallback) image ID, if the primary ID is not available.)
        """
        InputSet._set_input(self, 'FallbackID', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) Enter the ID of the entity for which description information will be retrieved. IDs and MIDs can be obtained by running the Search Choreo in this bundle. Example input: /en/bob_dylan)
        """
        InputSet._set_input(self, 'ID', value)
    def set_MaximumHeight(self, value):
        """
        Set the value of the MaximumHeight input for this Choreo. ((optional, integer) Enter the desired maximum image height in pixels. Integers must be in the following range: (0 --> 4,096))
        """
        InputSet._set_input(self, 'MaximumHeight', value)
    def set_MaximumWidth(self, value):
        """
        Set the value of the MaximumWidth input for this Choreo. ((optional, integer) Enter the desired maximum image width in pixels. Integers must be in the following range: (0 --> 4,096))
        """
        InputSet._set_input(self, 'MaximumWidth', value)
    def set_Mode(self, value):
        """
        Set the value of the Mode input for this Choreo. ((optional, string) Specify the method used to crop or scale images.  Available methods include: fill, fillcrop, fillcropmid, fit.)
        """
        InputSet._set_input(self, 'Mode', value)
    def set_Pad(self, value):
        """
        Set the value of the Pad input for this Choreo. ((optional, boolean) Enter 0, or 1 to specify whether the provided image should be padded to the requested dimensions.)
        """
        InputSet._set_input(self, 'Pad', value)

class ImageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Image Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from the Freebase Image API returns the thumbnail in base 64-encoded  format.)
        """
        return self._output.get('Response', None)

class ImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ImageResultSet(response, path)
