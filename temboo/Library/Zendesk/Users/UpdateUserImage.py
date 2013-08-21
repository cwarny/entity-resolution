# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUserImage
# Updates a user's profile image.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateUserImage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateUserImage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Users/UpdateUserImage')


    def new_input_set(self):
        return UpdateUserImageInputSet()

    def _make_result_set(self, result, path):
        return UpdateUserImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUserImageChoreographyExecution(session, exec_id, path)

class UpdateUserImageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateUserImage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Response(self, value):
        """
        Set the value of the Response input for this Choreo. ((required, json) The response from Zendesk.)
        """
        InputSet._set_input(self, 'Response', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_ImageURL(self, value):
        """
        Set the value of the ImageURL input for this Choreo. ((required, string) Set the URL of the image.)
        """
        InputSet._set_input(self, 'ImageURL', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (i.e. temboocare.zendesk.com).)
        """
        InputSet._set_input(self, 'Server', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, integer) The id of the user being updated.)
        """
        InputSet._set_input(self, 'UserID', value)

class UpdateUserImageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateUserImage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((required, json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class UpdateUserImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateUserImageResultSet(response, path)
