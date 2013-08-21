# -*- coding: utf-8 -*-

###############################################################################
#
# RestoreDBInstanceToPointInTime
# Restores a DB Instance to an specified point-in-time.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RestoreDBInstanceToPointInTime(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RestoreDBInstanceToPointInTime Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/RestoreDBInstanceToPointInTime')


    def new_input_set(self):
        return RestoreDBInstanceToPointInTimeInputSet()

    def _make_result_set(self, result, path):
        return RestoreDBInstanceToPointInTimeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RestoreDBInstanceToPointInTimeChoreographyExecution(session, exec_id, path)

class RestoreDBInstanceToPointInTimeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RestoreDBInstanceToPointInTime
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_AutoMinorVersionUpgrade(self, value):
        """
        Set the value of the AutoMinorVersionUpgrade input for this Choreo. ((optional, boolean) Indicates that minor version upgrades will be applied automatically to the DB Instance during the maintenance window. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'AutoMinorVersionUpgrade', value)
    def set_AvailabilityZone(self, value):
        """
        Set the value of the AvailabilityZone input for this Choreo. ((optional, string) The EC2 Availability Zone that the database instance will be created in. A random one is chose if not provided. Can not be specified if the MultiAZ parameter is set to 1 (true).)
        """
        InputSet._set_input(self, 'AvailabilityZone', value)
    def set_DBInstanceClass(self, value):
        """
        Set the value of the DBInstanceClass input for this Choreo. ((optional, string) The compute and memory capacity of the Amazon RDS DB instance. Valid Values: db.m1.small | db.m1.large | db.m1.xlarge | db.m2.2xlarge | db.m2.4xlarge.)
        """
        InputSet._set_input(self, 'DBInstanceClass', value)
    def set_DBName(self, value):
        """
        Set the value of the DBName input for this Choreo. ((optional, string) The database name for the restored DB Instance. Note that this parameter doesn't apply to the MySQL engine.)
        """
        InputSet._set_input(self, 'DBName', value)
    def set_Engine(self, value):
        """
        Set the value of the Engine input for this Choreo. ((optional, string) The database engine to use for the new instance. Valid Values: MySQL | oracle-se1 | oracle-se | oracle-ee.)
        """
        InputSet._set_input(self, 'Engine', value)
    def set_LicenseModel(self, value):
        """
        Set the value of the LicenseModel input for this Choreo. ((optional, string) License model information for the restored DB Instance. Valid values: license-included | bring-your-own-license | general-public-license.)
        """
        InputSet._set_input(self, 'LicenseModel', value)
    def set_MultiAZ(self, value):
        """
        Set the value of the MultiAZ input for this Choreo. ((optional, boolean) Specifies if the DB Instance is a Multi-AZ deployment. Do not specify the AvailabilityZone parameter if the MultiAZ parameter is set to 1 (true).)
        """
        InputSet._set_input(self, 'MultiAZ', value)
    def set_Port(self, value):
        """
        Set the value of the Port input for this Choreo. ((optional, integer) The port number on which the database accepts connections.)
        """
        InputSet._set_input(self, 'Port', value)
    def set_RestoreTime(self, value):
        """
        Set the value of the RestoreTime input for this Choreo. ((optional, date) The date and time to restore from in UTC. Cannot be specified if UseLatestRestorableTime parameter is set to 1. (format: 2009-09-07T23:45:00Z).)
        """
        InputSet._set_input(self, 'RestoreTime', value)
    def set_SourceDBInstanceIdentifier(self, value):
        """
        Set the value of the SourceDBInstanceIdentifier input for this Choreo. ((required, string) The identifier of the source DB Instance from which to restore.)
        """
        InputSet._set_input(self, 'SourceDBInstanceIdentifier', value)
    def set_TargetDBInstanceIdentifier(self, value):
        """
        Set the value of the TargetDBInstanceIdentifier input for this Choreo. ((required, string) The name of the new database instance to be created.)
        """
        InputSet._set_input(self, 'TargetDBInstanceIdentifier', value)
    def set_UseLatestRestorableTime(self, value):
        """
        Set the value of the UseLatestRestorableTime input for this Choreo. ((optional, boolean) Specifies whether or not the DB Instance is restored from the latest backup time. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'UseLatestRestorableTime', value)

class RestoreDBInstanceToPointInTimeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RestoreDBInstanceToPointInTime Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class RestoreDBInstanceToPointInTimeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RestoreDBInstanceToPointInTimeResultSet(response, path)
