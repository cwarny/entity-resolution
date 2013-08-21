# -*- coding: utf-8 -*-

###############################################################################
#
# ToxinReleaseByFacility
# Retrieves a list of the annual release quantities of toxic chemicals at EPA-regulated facilities into air, water, on-site land, and underground wells.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ToxinReleaseByFacility(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ToxinReleaseByFacility Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/Toxins/ToxinReleaseByFacility')


    def new_input_set(self):
        return ToxinReleaseByFacilityInputSet()

    def _make_result_set(self, result, path):
        return ToxinReleaseByFacilityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ToxinReleaseByFacilityChoreographyExecution(session, exec_id, path)

class ToxinReleaseByFacilityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ToxinReleaseByFacility
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FacilityID(self, value):
        """
        Set the value of the FacilityID input for this Choreo. ((required, string) FacilityID for which a toxin release report is to be generated. Found by first running the FacilitiesSearch Choreo.)
        """
        InputSet._set_input(self, 'FacilityID', value)
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

class ToxinReleaseByFacilityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ToxinReleaseByFacility Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class ToxinReleaseByFacilityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ToxinReleaseByFacilityResultSet(response, path)
