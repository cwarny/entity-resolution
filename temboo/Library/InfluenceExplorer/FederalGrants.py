# -*- coding: utf-8 -*-

###############################################################################
#
# FederalGrants
# Returns information about federal grants awarded.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FederalGrants(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FederalGrants Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/FederalGrants')


    def new_input_set(self):
        return FederalGrantsInputSet()

    def _make_result_set(self, result, path):
        return FederalGrantsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FederalGrantsChoreographyExecution(session, exec_id, path)

class FederalGrantsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FederalGrants
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AgencyName(self, value):
        """
        Set the value of the AgencyName input for this Choreo. ((optional, string) Full-text search on the reported name of the federal agency awarding the grant.)
        """
        InputSet._set_input(self, 'AgencyName', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((optional, string) The grant amount. Valid formats include: 500 (exactly $500); >|500 (greater than, or equal to 500); <|500 (less than or equal to 500).)
        """
        InputSet._set_input(self, 'Amount', value)
    def set_AssistanceType(self, value):
        """
        Set the value of the AssistanceType input for this Choreo. ((optional, integer) A numeric code for the type of grant awarded. See documentation for more details for this parameter.)
        """
        InputSet._set_input(self, 'AssistanceType', value)
    def set_FiscalYear(self, value):
        """
        Set the value of the FiscalYear input for this Choreo. ((optional, date) The year in which the grant was awarded. A YYYY formatted year. You can also specify a range by separating years with a pipe (i.e. 2008|2012).)
        """
        InputSet._set_input(self, 'FiscalYear', value)
    def set_RecipientName(self, value):
        """
        Set the value of the RecipientName input for this Choreo. ((optional, string) Full-text search on the reported name of the grant recipient.)
        """
        InputSet._set_input(self, 'RecipientName', value)
    def set_RecipientState(self, value):
        """
        Set the value of the RecipientState input for this Choreo. ((optional, string) Two-letter abbreviation of the state in which the grant was awarded.)
        """
        InputSet._set_input(self, 'RecipientState', value)
    def set_RecipientType(self, value):
        """
        Set the value of the RecipientType input for this Choreo. ((optional, integer) The numeric code representing the type of entity that received the grant. See documentation for more details about this parameter.)
        """
        InputSet._set_input(self, 'RecipientType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Indicates the desired format for the response. Accepted values are: json (the default), csv, and xls. Note when specifying xls, restults are returned as Base64 encoded data.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class FederalGrantsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FederalGrants Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Influence Explorer. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class FederalGrantsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FederalGrantsResultSet(response, path)
