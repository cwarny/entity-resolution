# -*- coding: utf-8 -*-

###############################################################################
#
# JSONToDB
# Performs a batch operation in PostgreSQL with a set of records in JSON format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class JSONToDB(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the JSONToDB Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/PostgreSQL/JSONToDB')


    def new_input_set(self):
        return JSONToDBInputSet()

    def _make_result_set(self, result, path):
        return JSONToDBResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return JSONToDBChoreographyExecution(session, exec_id, path)

class JSONToDBInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the JSONToDB
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BatchFile(self, value):
        """
        Set the value of the BatchFile input for this Choreo. ((required, json) The records to send to the database for the batch operation.)
        """
        InputSet._set_input(self, 'BatchFile', value)
    def set_BatchMode(self, value):
        """
        Set the value of the BatchMode input for this Choreo. ((optional, string) The type of batch operation to perform. Accepted values are: insert, update, or upsert.)
        """
        InputSet._set_input(self, 'BatchMode', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database to connect to.)
        """
        InputSet._set_input(self, 'DatabaseName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password for the database user.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Port(self, value):
        """
        Set the value of the Port input for this Choreo. ((optional, integer) The database port. Defaults to 5432.)
        """
        InputSet._set_input(self, 'Port', value)
    def set_RollbackOnError(self, value):
        """
        Set the value of the RollbackOnError input for this Choreo. ((optional, boolean) Rollback if error occurs. Set to 1 to enable. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'RollbackOnError', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) The name or IP address of the database server.)
        """
        InputSet._set_input(self, 'Server', value)
    def set_TableName(self, value):
        """
        Set the value of the TableName input for this Choreo. ((required, string) The database table that the batch operation is to be performed on.)
        """
        InputSet._set_input(self, 'TableName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The database username.)
        """
        InputSet._set_input(self, 'Username', value)
    def set_Version(self, value):
        """
        Set the value of the Version input for this Choreo. ((optional, decimal) The version of the Postgres database. Allowed values are 8 and 9 (the default).)
        """
        InputSet._set_input(self, 'Version', value)

class JSONToDBResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the JSONToDB Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Success(self):
        """
        Retrieve the value for the "Success" output from this Choreo execution. ((boolean) Indicates the result of the batch operation. The value will be "true" when the SQL transaction executes successfully.)
        """
        return self._output.get('Success', None)

class JSONToDBChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return JSONToDBResultSet(response, path)
