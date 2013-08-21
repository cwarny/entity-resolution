# -*- coding: utf-8 -*-

###############################################################################
#
# AddCSVData
# Transfer a csv file to add records to a specified group.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddCSVData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddCSVData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/AddCSVData')


    def new_input_set(self):
        return AddCSVDataInputSet()

    def _make_result_set(self, result, path):
        return AddCSVDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddCSVDataChoreographyExecution(session, exec_id, path)

class AddCSVDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddCSVData
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Private Key for 1 unique distributor - provided by Obad Mobile Marketing)
        """
        InputSet._set_input(self, 'APIKey', value)
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
    def set_GroupID(self, value):
        """
        Set the value of the GroupID input for this Choreo. ((integer) Unique ID for the group you want to update)
        """
        InputSet._set_input(self, 'GroupID', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((string) Specify the desired item list (i.e. camp, coupon, usergroup, shopgroup, or coupongroup). Defaults to 'shopgroup'.)
        """
        InputSet._set_input(self, 'Type', value)
    def set_URLSource(self, value):
        """
        Set the value of the URLSource input for this Choreo. ((string) The URL where you are hosting the CSV data (i.e. http://mybucket.s3.amazonaws.com/my_new_users.csv))
        """
        InputSet._set_input(self, 'URLSource', value)

class AddCSVDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddCSVData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Obad)
        """
        return self._output.get('Response', None)

class AddCSVDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddCSVDataResultSet(response, path)
