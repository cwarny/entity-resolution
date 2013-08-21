# -*- coding: utf-8 -*-

###############################################################################
#
# ListIndustryCodes
# Returns a complete list of all Standard Industrial Classification (SIC) codes and sectors.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListIndustryCodes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListIndustryCodes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Lists/ListIndustryCodes')


    def new_input_set(self):
        return ListIndustryCodesInputSet()

    def _make_result_set(self, result, path):
        return ListIndustryCodesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListIndustryCodesChoreographyExecution(session, exec_id, path)

class ListIndustryCodesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListIndustryCodes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        InputSet._set_input(self, 'Index', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        InputSet._set_input(self, 'ResponseType', value)

class ListIndustryCodesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListIndustryCodes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class ListIndustryCodesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListIndustryCodesResultSet(response, path)
