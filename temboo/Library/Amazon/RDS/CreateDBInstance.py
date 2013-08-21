# -*- coding: utf-8 -*-

###############################################################################
#
# CreateDBInstance
# Creates a new database instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateDBInstance(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateDBInstance Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/CreateDBInstance')


    def new_input_set(self):
        return CreateDBInstanceInputSet()

    def _make_result_set(self, result, path):
        return CreateDBInstanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDBInstanceChoreographyExecution(session, exec_id, path)

class CreateDBInstanceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateDBInstance
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
        Set the value of the AllocatedStorage input for this Choreo. ((required, integer) Storage amount (in gigabytes) to be configured for the DB. Use 5 to 1024 for MySQL , 10 to 1024 for Oracle, or 200 to 1024 for SQLServer.)
        """
        InputSet._set_input(self, 'AllocatedStorage', value)
    def set_AutoMinorVersionUpgrade(self, value):
        """
        Set the value of the AutoMinorVersionUpgrade input for this Choreo. ((optional, boolean) Indicates that minor engine upgrades will be applied to the DB Instance automatically during the maintenance window.)
        """
        InputSet._set_input(self, 'AutoMinorVersionUpgrade', value)
    def set_AvailabilityZone(self, value):
        """
        Set the value of the AvailabilityZone input for this Choreo. ((optional, string) The EC2 Availability Zone that the database instance will be created in (e.g. us-east-1a, us-east-1b, us-east-1c).)
        """
        InputSet._set_input(self, 'AvailabilityZone', value)
    def set_BackupRetentionPeriod(self, value):
        """
        Set the value of the BackupRetentionPeriod input for this Choreo. ((optional, integer) The number of days for which automated backups are retained. When set to a positive number, backups are enabled. Set to 0 to disable automated backups.)
        """
        InputSet._set_input(self, 'BackupRetentionPeriod', value)
    def set_CharacterSetName(self, value):
        """
        Set the value of the CharacterSetName input for this Choreo. ((optional, string) Indicates that the DB Instance should be associated with the specified CharacterSet.)
        """
        InputSet._set_input(self, 'CharacterSetName', value)
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
    def set_DBName(self, value):
        """
        Set the value of the DBName input for this Choreo. ((conditional, string) For MySQL, this is the name of the db that is created on the instance. For Oracle, it refers to the SID. Must be null for SQLServer.)
        """
        InputSet._set_input(self, 'DBName', value)
    def set_DBParameterGroupName(self, value):
        """
        Set the value of the DBParameterGroupName input for this Choreo. ((optional, string) The name of the DB Parameter Group to associate with this DB instance. If this argument is omitted, the default DBParameterGroup for the specified engine will be used.)
        """
        InputSet._set_input(self, 'DBParameterGroupName', value)
    def set_DBSecurityGroups(self, value):
        """
        Set the value of the DBSecurityGroups input for this Choreo. ((optional, string) A comma separated list of up to 10 DB Security Groups to associate with this DB Instance.)
        """
        InputSet._set_input(self, 'DBSecurityGroups', value)
    def set_DBSubnetGroupName(self, value):
        """
        Set the value of the DBSubnetGroupName input for this Choreo. ((optional, string) A DB Subnet Group to associate with this DB Instance. When not specified, it indicates that this is a non-VPC DB instance.)
        """
        InputSet._set_input(self, 'DBSubnetGroupName', value)
    def set_EngineVersion(self, value):
        """
        Set the value of the EngineVersion input for this Choreo. ((optional, string) The version number of the database engine to use.)
        """
        InputSet._set_input(self, 'EngineVersion', value)
    def set_Engine(self, value):
        """
        Set the value of the Engine input for this Choreo. ((required, string) The name of the database engine to use for the instance. Options are: MySQL, oracle-se1, oracle-se, oracle-ee, sqlserver-ee, sqlserver-se, sqlserver-ex, sqlserver-web.)
        """
        InputSet._set_input(self, 'Engine', value)
    def set_Iops(self, value):
        """
        Set the value of the Iops input for this Choreo. ((optional, string) The amount of provisioned input/output operations per second to be initially allocated for the DB Instance.)
        """
        InputSet._set_input(self, 'Iops', value)
    def set_LicenseModel(self, value):
        """
        Set the value of the LicenseModel input for this Choreo. ((optional, string) License model information for this DB Instance. Valid values are: license-included, bring-your-own-license, general-public-license.)
        """
        InputSet._set_input(self, 'LicenseModel', value)
    def set_MasterUserPassword(self, value):
        """
        Set the value of the MasterUserPassword input for this Choreo. ((required, string) The master password for the DB instance.)
        """
        InputSet._set_input(self, 'MasterUserPassword', value)
    def set_MasterUsername(self, value):
        """
        Set the value of the MasterUsername input for this Choreo. ((required, string) The master username for the DB instance.)
        """
        InputSet._set_input(self, 'MasterUsername', value)
    def set_MultiAZ(self, value):
        """
        Set the value of the MultiAZ input for this Choreo. ((optional, boolean) Specifies if the DB Instance is a Multi-AZ deployment. You cannot set the AvailabilityZone parameter if the MultiAZ parameter is set to true.)
        """
        InputSet._set_input(self, 'MultiAZ', value)
    def set_OptionGroupName(self, value):
        """
        Set the value of the OptionGroupName input for this Choreo. ((optional, string) Indicates that the DB Instance should be associated with the specified option group.)
        """
        InputSet._set_input(self, 'OptionGroupName', value)
    def set_Port(self, value):
        """
        Set the value of the Port input for this Choreo. ((optional, integer) The port number on which the database accepts connections. Valid range for MySQL is 1150-65535. Valid range for Oracle is 1150-65535. Valid range for SQLServer is 1150-65535 except for 1434 and 3389.)
        """
        InputSet._set_input(self, 'Port', value)
    def set_PreferredBackupWindow(self, value):
        """
        Set the value of the PreferredBackupWindow input for this Choreo. ((optional, string) The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter. Must be in the format hh24:mi-hh24:mi (in UTC).)
        """
        InputSet._set_input(self, 'PreferredBackupWindow', value)
    def set_PreferredMaintenanceWindow(self, value):
        """
        Set the value of the PreferredMaintenanceWindow input for this Choreo. ((optional, string) The weekly time range (in UTC) during which system maintenance can occur. Format: ddd:hh24:mi-ddd:hh24:mi.)
        """
        InputSet._set_input(self, 'PreferredMaintenanceWindow', value)
    def set_PubliclyAccessible(self, value):
        """
        Set the value of the PubliclyAccessible input for this Choreo. ((optional, boolean) Specifies the accessibility options for the DB Instance. The default behavior varies depending on whether a VPC has been requested or not.)
        """
        InputSet._set_input(self, 'PubliclyAccessible', value)
    def set_VpcSecurityGroupIds(self, value):
        """
        Set the value of the VpcSecurityGroupIds input for this Choreo. ((optional, string) A comma separated list of up to 10 EC2 VPC Security Groups to associate with this DB Instance.)
        """
        InputSet._set_input(self, 'VpcSecurityGroupIds', value)

class CreateDBInstanceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateDBInstance Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateDBInstanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateDBInstanceResultSet(response, path)
