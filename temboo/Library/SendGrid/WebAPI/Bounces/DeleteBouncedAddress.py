# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteBouncedAddress
# Delete an address from the bounced email list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteBouncedAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteBouncedAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Bounces/DeleteBouncedAddress')


    def new_input_set(self):
        return DeleteBouncedAddressInputSet()

    def _make_result_set(self, result, path):
        return DeleteBouncedAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteBouncedAddressChoreographyExecution(session, exec_id, path)

class DeleteBouncedAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteBouncedAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        InputSet._set_input(self, 'APIUser', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((optional, string) The valid email address to be deleted from your block list.)
        """
        InputSet._set_input(self, 'EmailAddress', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) The end of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) The start of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format, and must be earlier than the EndDate variable value.)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of bounce to search for. Choices include: hard, or soft.)
        """
        InputSet._set_input(self, 'Type', value)


class DeleteBouncedAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteBouncedAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class DeleteBouncedAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteBouncedAddressResultSet(response, path)
