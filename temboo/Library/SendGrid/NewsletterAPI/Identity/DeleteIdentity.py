# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteIdentity
# Delete an Identity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteIdentity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteIdentity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/Identity/DeleteIdentity')


    def new_input_set(self):
        return DeleteIdentityInputSet()

    def _make_result_set(self, result, path):
        return DeleteIdentityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteIdentityChoreographyExecution(session, exec_id, path)

class DeleteIdentityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteIdentity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Response(self, value):
        """
        Set the value of the Response input for this Choreo. ((required, any) The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        InputSet._set_input(self, 'Response', value)
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
    def set_Identity(self, value):
        """
        Set the value of the Identity input for this Choreo. ((required, string) The identity to be removed from your account.)
        """
        InputSet._set_input(self, 'Identity', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid. Specify json, or xml.  Default is set to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)


class DeleteIdentityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteIdentity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    pass

class DeleteIdentityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteIdentityResultSet(response, path)
