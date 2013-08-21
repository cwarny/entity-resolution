# -*- coding: utf-8 -*-

###############################################################################
#
# LogGlucose
# Creates log entry for a blood glucose measurement and/or HbA1c measurement.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class LogGlucose(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LogGlucose Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/Glucose/LogGlucose')


    def new_input_set(self):
        return LogGlucoseInputSet()

    def _make_result_set(self, result, path):
        return LogGlucoseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LogGlucoseChoreographyExecution(session, exec_id, path)

class LogGlucoseInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LogGlucose
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, date) The date that corresponds with the log entry (in the format yyyy-MM-dd).)
        """
        InputSet._set_input(self, 'Date', value)
    def set_Glucose(self, value):
        """
        Set the value of the Glucose input for this Choreo. ((conditional, integer) Glucose measurement; in the format X.X, required with tracker parameter, otherwise optional.)
        """
        InputSet._set_input(self, 'Glucose', value)
    def set_HBA1C(self, value):
        """
        Set the value of the HBA1C input for this Choreo. ((conditional, decimal) HbA1c measurement; in the format X.X, either hba1c or tracker should be provided (or both).)
        """
        InputSet._set_input(self, 'HBA1C', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Time(self, value):
        """
        Set the value of the Time input for this Choreo. ((optional, string) Time of the measurement; hours and minutes in the format HH:mm.)
        """
        InputSet._set_input(self, 'Time', value)
    def set_Tracker(self, value):
        """
        Set the value of the Tracker input for this Choreo. ((conditional, string) Glucose tracker name; predefined or custom tracker name (matches tracker name on the website, e.g. "Afternoon").)
        """
        InputSet._set_input(self, 'Tracker', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        InputSet._set_input(self, 'UserID', value)

class LogGlucoseResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LogGlucose Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class LogGlucoseChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LogGlucoseResultSet(response, path)
