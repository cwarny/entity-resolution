# -*- coding: utf-8 -*-

###############################################################################
#
# XMLToTSV
# Converts an XML file to TSV format (TAB-separated values).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class XMLToTSV(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the XMLToTSV Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/DataConversions/XMLToTSV')


    def new_input_set(self):
        return XMLToTSVInputSet()

    def _make_result_set(self, result, path):
        return XMLToTSVResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return XMLToTSVChoreographyExecution(session, exec_id, path)

class XMLToTSVInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the XMLToTSV
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_XML(self, value):
        """
        Set the value of the XML input for this Choreo. ((required, xml) The XML file to convert to TSV data.)
        """
        InputSet._set_input(self, 'XML', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((optional, string) If your XML is not in "/rowset/row/column_name" format, specify a path to the rows. See documentation for examples.)
        """
        InputSet._set_input(self, 'Path', value)

class XMLToTSVResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the XMLToTSV Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_TSV(self):
        """
        Retrieve the value for the "TSV" output from this Choreo execution. ((multiline) The tab-separated data generated from the XML input.)
        """
        return self._output.get('TSV', None)

class XMLToTSVChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return XMLToTSVResultSet(response, path)
