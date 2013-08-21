# -*- coding: utf-8 -*-

###############################################################################
#
# FacilitiesSearchByZip
# Retrieves a list of EPA-regulated facilities in the Toxins Release Inventory (TRI) database within a given area code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FacilitiesSearchByZip(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FacilitiesSearchByZip Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/Toxins/FacilitiesSearchByZip')


    def new_input_set(self):
        return FacilitiesSearchByZipInputSet()

    def _make_result_set(self, result, path):
        return FacilitiesSearchByZipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FacilitiesSearchByZipChoreographyExecution(session, exec_id, path)

class FacilitiesSearchByZipInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FacilitiesSearchByZip
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify the desired response format. Valid formats are: xml (the default) and csv.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_RowEnd(self, value):
        """
        Set the value of the RowEnd input for this Choreo. ((optional, integer) Number 1 or greater indicates the ending row number of the results displayed. Default is 4999 when RowStart is 0. Up to 5000 entries are returned in the output.)
        """
        InputSet._set_input(self, 'RowEnd', value)
    def set_RowStart(self, value):
        """
        Set the value of the RowStart input for this Choreo. ((optional, integer) Indicates the starting row number of the results displayed. Default is 0.)
        """
        InputSet._set_input(self, 'RowStart', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, string) Zip code to be searched.)
        """
        InputSet._set_input(self, 'Zip', value)

class FacilitiesSearchByZipResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FacilitiesSearchByZip Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class FacilitiesSearchByZipChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FacilitiesSearchByZipResultSet(response, path)
