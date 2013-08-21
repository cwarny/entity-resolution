# -*- coding: utf-8 -*-

###############################################################################
#
# GetNewsletterScheduleTime
# Get the scheduled delivery time of a specified Newsletter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetNewsletterScheduleTime(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNewsletterScheduleTime Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/Schedule/GetNewsletterScheduleTime')


    def new_input_set(self):
        return GetNewsletterScheduleTimeInputSet()

    def _make_result_set(self, result, path):
        return GetNewsletterScheduleTimeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNewsletterScheduleTimeChoreographyExecution(session, exec_id, path)

class GetNewsletterScheduleTimeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNewsletterScheduleTime
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
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the newsletter for which delivery schedule information will be retrieved.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)


class GetNewsletterScheduleTimeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNewsletterScheduleTime Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class GetNewsletterScheduleTimeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetNewsletterScheduleTimeResultSet(response, path)
