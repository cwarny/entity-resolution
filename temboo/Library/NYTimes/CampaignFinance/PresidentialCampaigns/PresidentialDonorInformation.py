# -*- coding: utf-8 -*-

###############################################################################
#
# PresidentialDonorInformation
# Retrieve details about individual donors, or a summary of donors from a particular location to a presidential election campaign.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PresidentialDonorInformation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PresidentialDonorInformation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/CampaignFinance/PresidentialCampaigns/PresidentialDonorInformation')


    def new_input_set(self):
        return PresidentialDonorInformationInputSet()

    def _make_result_set(self, result, path):
        return PresidentialDonorInformationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PresidentialDonorInformationChoreographyExecution(session, exec_id, path)

class PresidentialDonorInformationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PresidentialDonorInformation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CampaignCycle(self, value):
        """
        Set the value of the CampaignCycle input for this Choreo. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year.)
        """
        InputSet._set_input(self, 'CampaignCycle', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) Enter the first name of a donor.  This parameter can be used together with LastName and/or Zip)
        """
        InputSet._set_input(self, 'FirstName', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) Enter the last name of an individual donor to be retrieved.)
        """
        InputSet._set_input(self, 'LastName', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Specify the starting point of the retrieved results, in multiples of 20.  By default, the first 20 results are returned.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Enter json or xml.  Default is json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, integer) Enter a zipcode for which donor information wil be retrieved.)
        """
        InputSet._set_input(self, 'Zip', value)

class PresidentialDonorInformationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PresidentialDonorInformation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        return self._output.get('Response', None)

class PresidentialDonorInformationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PresidentialDonorInformationResultSet(response, path)
