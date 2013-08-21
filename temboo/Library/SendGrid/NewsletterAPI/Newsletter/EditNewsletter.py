# -*- coding: utf-8 -*-

###############################################################################
#
# EditNewsletter
# Edit an existing newsletter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class EditNewsletter(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EditNewsletter Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/Newsletter/EditNewsletter')


    def new_input_set(self):
        return EditNewsletterInputSet()

    def _make_result_set(self, result, path):
        return EditNewsletterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EditNewsletterChoreographyExecution(session, exec_id, path)

class EditNewsletterInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EditNewsletter
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
    def set_HTML(self, value):
        """
        Set the value of the HTML input for this Choreo. ((required, string) The html portion of the newsletter.)
        """
        InputSet._set_input(self, 'HTML', value)
    def set_Identity(self, value):
        """
        Set the value of the Identity input for this Choreo. ((required, string) The new identity Identiy for the newsletter that is being edited.)
        """
        InputSet._set_input(self, 'Identity', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the newsletter that is being edited.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_NewName(self, value):
        """
        Set the value of the NewName input for this Choreo. ((required, string) The new name of the newsletter that is being edited.)
        """
        InputSet._set_input(self, 'NewName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((required, string) The new subject for the edited newsletter.)
        """
        InputSet._set_input(self, 'Subject', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text portion of the newsletter.)
        """
        InputSet._set_input(self, 'Text', value)


class EditNewsletterResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EditNewsletter Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class EditNewsletterChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EditNewsletterResultSet(response, path)
