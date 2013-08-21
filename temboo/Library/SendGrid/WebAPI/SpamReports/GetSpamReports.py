# -*- coding: utf-8 -*-

###############################################################################
#
# GetSpamReports
# Obtain a list of spam reports, with email addresses, response codes, and dates.

#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetSpamReports(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSpamReports Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/SpamReports/GetSpamReports')


    def new_input_set(self):
        return GetSpamReportsInputSet()

    def _make_result_set(self, result, path):
        return GetSpamReportsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSpamReportsChoreographyExecution(session, exec_id, path)

class GetSpamReportsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSpamReports
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
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) The timestamp of the Block records. Enter 1 to return a date in a MySQL timestamp format - YYYY-MM-DD HH:MM:SS)
        """
        InputSet._set_input(self, 'Date', value)
    def set_Days(self, value):
        """
        Set the value of the Days input for this Choreo. ((optional, integer) The number of days (greater than 0) for which block data will be retrieved.)
        """
        InputSet._set_input(self, 'Days', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) A specific email address to search for.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) The end of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) A number to limit the number of results returned.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The beginning point in the list to retrieve bounces from.)
        """
        InputSet._set_input(self, 'Offset', value)
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


class GetSpamReportsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSpamReports Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class GetSpamReportsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSpamReportsResultSet(response, path)
