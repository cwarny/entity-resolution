# -*- coding: utf-8 -*-

###############################################################################
#
# EditIdentity
# Edit a newsletter identity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class EditIdentity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EditIdentity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/Identity/EditIdentity')


    def new_input_set(self):
        return EditIdentityInputSet()

    def _make_result_set(self, result, path):
        return EditIdentityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EditIdentityChoreographyExecution(session, exec_id, path)

class EditIdentityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EditIdentity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid. )
        """
        InputSet._set_input(self, 'APIUser', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((required, string) The new physical address to be used for this Identity.)
        """
        InputSet._set_input(self, 'Address', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) The new city for this Identity.)
        """
        InputSet._set_input(self, 'City', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((required, string) The new country to be associated with this Identity.)
        """
        InputSet._set_input(self, 'Country', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) An email address to be used for this identity.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Identity(self, value):
        """
        Set the value of the Identity input for this Choreo. ((required, string) The identity that is to be edited.)
        """
        InputSet._set_input(self, 'Identity', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The new name to be associated with this identity.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_NewIdentity(self, value):
        """
        Set the value of the NewIdentity input for this Choreo. ((optional, string) The new name for this identity.)
        """
        InputSet._set_input(self, 'NewIdentity', value)
    def set_ReplyTo(self, value):
        """
        Set the value of the ReplyTo input for this Choreo. ((required, string) An email address to be used in the Reply-To field.)
        """
        InputSet._set_input(self, 'ReplyTo', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid: Soecify json, or xml.  Default is set to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((required, string) The state to be associated with this Identity.)
        """
        InputSet._set_input(self, 'State', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, integer) The new zip code associated with this Identity.)
        """
        InputSet._set_input(self, 'Zip', value)


class EditIdentityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EditIdentity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class EditIdentityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EditIdentityResultSet(response, path)
