# -*- coding: utf-8 -*-

###############################################################################
#
# TipDetails
# Gives details about a tip, including which users (especially friends) have marked the tip to-do or done. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification
from temboo.outputs.Foursquare.FoursquareTipDetails import FoursquareTipDetails

import json

class TipDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TipDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Tips/TipDetails')


    def new_input_set(self):
        return TipDetailsInputSet()

    def _make_result_set(self, result, path):
        return TipDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TipDetailsChoreographyExecution(session, exec_id, path)

class TipDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TipDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) Your Foursquare API Oauth token string.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_TipID(self, value):
        """
        Set the value of the TipID input for this Choreo. ((required, string) ID of tip to retrieve)
        """
        InputSet._set_input(self, 'TipID', value)

class TipDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TipDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def getMeta(self):
        """
        Get the response status code
        """
        return FoursquareMeta(self.getJSONFromString(self._output.get('Response', [])).get("meta", []))
    def getNotifications(self):
        """
        Get the count of unread notifications for the authenticated user
        """
        return [FoursquareNotification(le) for le in self.getJSONFromString(self._output.get('Response', [])).get("notifications", [])]

    def getTipDetails(self):
        """
        Get details for this tip
        """
        return FoursquareTipDetails(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("tip", []))

class TipDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TipDetailsResultSet(response, path)
