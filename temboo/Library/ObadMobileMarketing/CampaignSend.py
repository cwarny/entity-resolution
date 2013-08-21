# -*- coding: utf-8 -*-

###############################################################################
#
# CampaignSend
# Generate a CSV file for sending a campaign.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CampaignSend(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CampaignSend Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/CampaignSend')


    def new_input_set(self):
        return CampaignSendInputSet()

    def _make_result_set(self, result, path):
        return CampaignSendResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CampaignSendChoreographyExecution(session, exec_id, path)

class CampaignSendInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CampaignSend
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Private Key for 1 unique distributor - provided by Obad Mobile Marketing)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CampaignID(self, value):
        """
        Set the value of the CampaignID input for this Choreo. ((integer) The ID for the campaign you want to send)
        """
        InputSet._set_input(self, 'CampaignID', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((integer) Private Key for 1 unique customer to connect with - provided by Obad Mobile Marketing)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of campaign you're sending.  Can be sms, mail, or smsmail. Defaults to sms.)
        """
        InputSet._set_input(self, 'Type', value)

class CampaignSendResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CampaignSend Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Obad)
        """
        return self._output.get('Response', None)

class CampaignSendChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CampaignSendResultSet(response, path)
