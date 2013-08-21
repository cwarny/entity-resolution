# -*- coding: utf-8 -*-

###############################################################################
#
# ListCountryCodes
# Returns a complete list of ISO-3166 standard country and subdivision codes.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListCountryCodes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListCountryCodes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Lists/ListCountryCodes')


    def new_input_set(self):
        return ListCountryCodesInputSet()

    def _make_result_set(self, result, path):
        return ListCountryCodesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListCountryCodesChoreographyExecution(session, exec_id, path)

class ListCountryCodesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListCountryCodes
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

class ListCountryCodesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListCountryCodes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class ListCountryCodesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListCountryCodesResultSet(response, path)
