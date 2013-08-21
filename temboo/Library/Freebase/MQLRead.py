# -*- coding: utf-8 -*-

###############################################################################
#
# MQLRead
# Search the Freebase dataset using the Metaweb query language (MQL).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class MQLRead(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MQLRead Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Freebase/MQLRead')


    def new_input_set(self):
        return MQLReadInputSet()

    def _make_result_set(self, result, path):
        return MQLReadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MQLReadChoreographyExecution(session, exec_id, path)

class MQLReadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MQLRead
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Freebase.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AsOfTime(self, value):
        """
        Set the value of the AsOfTime input for this Choreo. ((optional, string) Run a query as it would have run at a specific point in time. Timestamps must be entered in the following format: 2007-01-09T22, or 2007-02.)
        """
        InputSet._set_input(self, 'AsOfTime', value)
    def set_Cost(self, value):
        """
        Set the value of the Cost input for this Choreo. ((optional, boolean) If cost is set to true, a key is returned in the results, indicating the computational cost incurred by lower levels of the service. Default value: false)
        """
        InputSet._set_input(self, 'Cost', value)
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, string) If set. results can be paged.  See examples at: http://wiki.freebase.com/wiki/MQL_Read_Service)
        """
        InputSet._set_input(self, 'Cursor', value)
    def set_EscapeHTMLResults(self, value):
        """
        Set the value of the EscapeHTMLResults input for this Choreo. ((optional, boolean) Specify whether html results are to be escaped or not.  Default is set to: true.)
        """
        InputSet._set_input(self, 'EscapeHTMLResults', value)
    def set_Indent(self, value):
        """
        Set the value of the Indent input for this Choreo. ((optional, boolean) Specify whether the JSON results should be indented, or not. Enter true, or false. Default: false. Range of values: 0-10.)
        """
        InputSet._set_input(self, 'Indent', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) Specify the language in which the searches will be performed.  Multiple languages can be specified. Default is: /lang/en)
        """
        InputSet._set_input(self, 'Language', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) Enter a search query  in a valid MQL JSON format.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_UniqenessFailure(self, value):
        """
        Set the value of the UniqenessFailure input for this Choreo. ((optional, string) Specify how MQL responds to uniqueness failures. Enter hard, or soft.  Default is set to: hard.)
        """
        InputSet._set_input(self, 'UniqenessFailure', value)

class MQLReadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MQLRead Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Freebase MQL Read API in JSON format.)
        """
        return self._output.get('Response', None)

class MQLReadChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MQLReadResultSet(response, path)
