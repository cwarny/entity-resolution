# -*- coding: utf-8 -*-

###############################################################################
#
# NearbyContacts
# Retrieves nearby Dwolla spots within the range of the provided latitude and longitude.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class NearbyContacts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the NearbyContacts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Contacts/NearbyContacts')


    def new_input_set(self):
        return NearbyContactsInputSet()

    def _make_result_set(self, result, path):
        return NearbyContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return NearbyContactsChoreographyExecution(session, exec_id, path)

class NearbyContactsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the NearbyContacts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The Client ID provided by Dwolla (AKA the Consumer Key).)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The Client Secret provided by Dwolla (AKA the Consumer Secret).)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) Current latitude.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of spots to retrieve. Defaults to 10.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) Current longitude.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Range(self, value):
        """
        Set the value of the Range input for this Choreo. ((optional, integer) Range to retrieve spots for in miles.)
        """
        InputSet._set_input(self, 'Range', value)

class NearbyContactsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the NearbyContacts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class NearbyContactsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return NearbyContactsResultSet(response, path)
