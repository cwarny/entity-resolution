# -*- coding: utf-8 -*-

###############################################################################
#
# ModifyDBInstance
# Modify settings for a DB Instance. You can change one or more database configuration parameters by specifying values for the Choreo inputs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ModifyDBInstance(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ModifyDBInstance Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/ModifyDBInstance')


    def new_input_set(self):
        return ModifyDBInstanceInputSet()

    def _make_result_set(self, result, path):
        return ModifyDBInstanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ModifyDBInstanceChoreographyExecution(session, exec_id, path)

class ModifyDBInstanceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ModifyDBInstance
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
    def set_AllocatedStorage(self, value):
        """
        Set the value of the AllocatedStorage input for this Choreo. ((required, integer) Storage amount (in gigabytes) to be configured for the DB. Use 5 to 1024 for MySQL or 10 to 1024 for Oracle. Value supplied must be at least 10% greater than the current value)
        """
        InputSet._set_input(self, 'AllocatedStorage', value)
    def set_AllowMajorVersionUpgrade(self, value):
        """
        Set the value of the AllowMajorVersionUpgrade input for this Choreo. ((optional, boolean) Indicates that major version upgrades are allowed. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'AllowMajorVersionUpgrade', value)
    def set_ApplyImmediately(self, value):
        """
        Set the value of the ApplyImmediately input for this Choreo. ((optional, boolean) Specifies whether or not the modifications applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the DB Instance. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'ApplyImmediately', value)
    def set_AutoMinorVersionUpgrade(self, value):
        """
        Set the value of the AutoMinorVersionUpgrade input for this Choreo. ((optional, boolean) Indicates that minor version upgrades will be applied automatically to the DB Instance during the maintenance window. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'AutoMinorVersionUpgrade', value)
    def set_BackupRetentionPeriod(self, value):
        """
        Set the value of the BackupRetentionPeriod input for this Choreo. ((optional, integer) Number of days to retain automated backups. Setting to a positive number enables backups. Setting to 0 disables automated backups. Must be a value from 0 to 8. Defaults to 0 (disabled).)
        """
        InputSet._set_input(self, 'BackupRetentionPeriod', value)
    def set_DBInstanceClass(self, value):
        """
        Set the value of the DBInstanceClass input for this Choreo. ((required, string) Capacity for the DB instance.  (db.m1.small, db.m1.large, db.m1.xlarge, db.m2.xlarge, db.m2.2xlarge, or db.m2.4xlarge).)
        """
        InputSet._set_input(self, 'DBInstanceClass', value)
    def set_DBInstanceIdentifier(self, value):
        """
        Set the value of the DBInstanceIdentifier input for this Choreo. ((required, string) The DB Instance identifier. Should be in all lowercase.)
        """
        InputSet._set_input(self, 'DBInstanceIdentifier', value)
    def set_DBParameterGroupName(self, value):
        """
        Set the value of the DBParameterGroupName input for this Choreo. ((optional, string) The name of the DB Parameter Group to apply to this DB Instance.)
        """
        InputSet._set_input(self, 'DBParameterGroupName', value)
    def set_DBSecurityGroup(self, value):
        """
        Set the value of the DBSecurityGroup input for this Choreo. ((optional, string) A DB Security Groups to authorize on this DB Instance.)
        """
        InputSet._set_input(self, 'DBSecurityGroup', value)
    def set_EngineVersion(self, value):
        """
        Set the value of the EngineVersion input for this Choreo. ((optional, string) The version number of the database engine to upgrade to.)
        """
        InputSet._set_input(self, 'EngineVersion', value)
    def set_MasterUserPassword(self, value):
        """
        Set the value of the MasterUserPassword input for this Choreo. ((required, string) The new password for the DB Instance master user.)
        """
        InputSet._set_input(self, 'MasterUserPassword', value)
    def set_MultiAZ(self, value):
        """
        Set the value of the MultiAZ input for this Choreo. ((optional, boolean) Specifies if the DB Instance is a Multi-AZ deployment.)
        """
        InputSet._set_input(self, 'MultiAZ', value)
    def set_PreferredBackupWindow(self, value):
        """
        Set the value of the PreferredBackupWindow input for this Choreo. ((optional, string) The daily time range during which automated backups are created. Format: hh24:mi-hh24:mi (in UTC). Must be at least 30 minutes. Can not conflict with PreferredMaintenanceWindow setting.)
        """
        InputSet._set_input(self, 'PreferredBackupWindow', value)
    def set_PreferredMaintenanceWindow(self, value):
        """
        Set the value of the PreferredMaintenanceWindow input for this Choreo. ((optional, string) The weekly time range (in UTC) during which system maintenance can occur, which may result in an outage. Format: ddd:hh24:mi-ddd:hh24:mi. Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun.)
        """
        InputSet._set_input(self, 'PreferredMaintenanceWindow', value)

class ModifyDBInstanceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ModifyDBInstance Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class ModifyDBInstanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ModifyDBInstanceResultSet(response, path)
