#coding=UTF-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkr_kvstore.request.v20150101.DescribeInstancesRequest import DescribeInstancesRequest
import json

"""
pip install aliyun-python-sdk-r-kvstore
"""

ID = '<ID>'
Secret = '<Secret>'
RegionId = 'cn-beijing'

clt = AcsClient(ID,Secret,RegionId)

DBInstanceIdList = []
DBInstanceIdDict = {}
ZabbixDataDict = {}

def GetMongoList():
    MongoRequest = DescribeInstancesRequest()
    MongoRequest.set_accept_format('json')
    RedisInfo = clt.do_action_with_exception(MongoRequest)
    for RedisInfoJson in json.loads(RedisInfo)['Instances']['KVStoreInstance']:
        DBInstanceIdDict = {}
        try:
            DBInstanceIdDict["{#DBINSTANCEID}"] = RedisInfoJson['InstanceId']
            DBInstanceIdDict["{#DBINSTANCEDESCRIPTION}"] = RedisInfoJson['InstanceName']
            DBInstanceIdList.append(DBInstanceIdDict)
        except Exception, e:
            print Exception, ":", e
            print "Please check the Mongodb alias !Alias must not be the same as DBInstanceId！！！"

GetMongoList()
ZabbixDataDict['data'] = DBInstanceIdList
print json.dumps(ZabbixDataDict)