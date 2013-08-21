# -*- coding: utf-8 -*-

###############################################################################
#
# Picture
# Retrieves the current profile photo for any object in the Facebook graph, and returns the image as a Base64 encoded string.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Picture(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Picture Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Reading/Picture')


    def new_input_set(self):
        return PictureInputSet()

    def _make_result_set(self, result, path):
        return PictureResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PictureChoreographyExecution(session, exec_id, path)

class PictureInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Picture
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((required, string) The id of the profile to retrieve a profile picture for. Defaults to "me" indicating the authenticated user.)
        """
        InputSet._set_input(self, 'ProfileID', value)
    def set_ReturnSSLResources(self, value):
        """
        Set the value of the ReturnSSLResources input for this Choreo. ((optional, boolean) Set to 1 to return the picture over a secure connection. Defaults to 0.)
        """
        InputSet._set_input(self, 'ReturnSSLResources', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The size of the image to retrieve. Valid values: square (50x50), small (50 pixels wide, variable height), normal (100 pixels wide, variable height), and large (about 200 pixels wide, variable height))
        """
        InputSet._set_input(self, 'Type', value)

class PictureResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Picture Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) Contains the Base64 encoded value of the image retrieved from Facebook.)
        """
        return self._output.get('Response', None)

class PictureChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PictureResultSet(response, path)
