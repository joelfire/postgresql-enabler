#
# Copyright (c) 2013 TIBCO Software Inc. All Rights Reserved.
# 
# Use is subject to the terms of the TIBCO license terms accompanying the download of this code. 
# In most instances, the license terms are contained in a file named license.txt.
#

from com.datasynapse.fabric.admin.info import AllocationInfo
from com.datasynapse.fabric.util import GridlibUtils, ContainerUtils
from com.datasynapse.fabric.common import RuntimeContextVariable, ActivationInfo
import java.lang.System
from subprocess import call, Popen
import os
import platform
import time
import socket
import fnmatch

# writes the message in the engine log
def logInfo(msg):
  logger.info(msg)

def prepareWorkDirectory():
    proxy.prepareWorkDirectory()
  
def doInit(additionalVariables):
    logInfo("--------------------doInit------------------------------")
    datadir = runtimeContext.getVariable('PGSQL_DATA_DIR').getValue()
    basedir = runtimeContext.getVariable('PGSQL_BASE_DIR').getValue() 
    
    logInfo("/usr/sbin/useradd postgres")
    call(["/usr/sbin/useradd","postgres"])
    
    logInfo("chown dirs to postgres")
    call(['chown','-R','postgres', basedir]);
    
def doStart():
    logInfo("--------------------doStart------------------------------")
    basedir = runtimeContext.getVariable('PGSQL_BASE_DIR').getValue() 
    datadir = runtimeContext.getVariable('PGSQL_DATA_DIR').getValue()
    if (not os.path.exists(datadir)) :
        logInfo("Data dir does not exist, creating and initializing: " + datadir)
        os.makedirs(datadir)
        call(['chown','-R','postgres', datadir]);
        command = os.path.join(basedir, "bin")
        command = os.path.join(command, 'initdb')
        command = command + ' -D ' + datadir
        callAsUser(command)
    else : 
        logInfo("Data directory already exists: " + datadir);

    callPgCtl('start')
   
def doInstall(info):
    logInfo("--------------------doInstall------------------------------")

def doUninstall():
    logInfo("--------------------doUninstall------------------------------")
 
def doShutdown():
    logInfo("--------------------doShutdown------------------------------")
    callPgCtl('stop')
    
# running condition
def getContainerRunningConditionPollPeriod():
    return 5000

def isContainerRunning():
    status = callPgCtl('status')
    if status == 0:
        return True
    else:
        return False 
    
def getComponentRunningConditionErrorMessage():
    return "pg_ctl status returned nonzero"

def callPgCtl(cmd):
    basedir = runtimeContext.getVariable('PGSQL_BASE_DIR').getValue() 
    datadir = runtimeContext.getVariable('PGSQL_DATA_DIR').getValue()
    command = os.path.join(basedir, "bin")
    command = os.path.join(command, 'pg_ctl')
    command = command + ' -D ' + datadir + ' ' + cmd 
    return callAsUser(command)
    
    
def callAsUser(command):
    logInfo('Executing command: ' + command)
    return call(['su','-c',command,'postgres'])
    logInfo('Command finished')
    
    

