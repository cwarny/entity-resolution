# -*- coding: utf-8 -*-

###############################################################################
#
# CommitteeIndependentExpenditures
# Retrieve the 20 most recent independent expenditures by a given committee, also known as "Super PACs."
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CommitteeIndependentExpenditures(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CommitteeIndependentExpenditures Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/CampaignFinance/IndependentExpenditures/CommitteeIndependentExpenditures')


    def new_input_set(self):
        return CommitteeIndependentExpendituresInputSet()

    def _make_result_set(self, result, path):
        return CommitteeIndependentExpendituresResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CommitteeIndependentExpendituresChoreographyExecution(session, exec_id, path)

class CommitteeIndependentExpendituresInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CommitteeIndependentExpenditures
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
    def set_FECID(self, value):
        """
        Set the value of the FECID input for this Choreo. ((required, string) Enter the FEC ID for the committee.  ID can be obtained by first running the CommitteeSearch Choreo.)
        """
        InputSet._set_input(self, 'FECID', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The first 20 results are shown by default. To page through the results, set Offset to the appropriate value (e.g., Offset=40 displays results 41–60).)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Enter json or xml.  Default is json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class CommitteeIndependentExpendituresResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CommitteeIndependentExpenditures Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        return self._output.get('Response', None)

class CommitteeIndependentExpendituresChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CommitteeIndependentExpendituresResultSet(response, path)
