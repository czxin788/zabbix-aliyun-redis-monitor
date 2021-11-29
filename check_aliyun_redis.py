#coding=UTF-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkr_kvstore.request.v20150101.DescribeHistoryMonitorValuesRequest import DescribeHistoryMonitorValuesRequest
import json,sys,datetime


ID = '<id>'
Secret = '<Secret>'
RegionId = 'cn-beijing'

clt = AcsClient(ID,Secret,RegionId)

Type = sys.argv[1]
DBInstanceId = sys.argv[2]
MasterKey = sys.argv[3]
SubKey =  sys.argv[4]

# 阿里云返回的数据为UTC时间，因此要转换为东八区时间。其他时区同理。
UTC_End = datetime.datetime.today() - datetime.timedelta(hours=8)
UTC_Start = UTC_End - datetime.timedelta(minutes=25)

StartTime = datetime.datetime.strftime(UTC_Start, '%Y-%m-%dT%H:%M:%SZ')
EndTime = datetime.datetime.strftime(UTC_End, '%Y-%m-%dT%H:%M:%SZ')

def GetResourceUsage(DBInstanceId,MasterKey,SubKey,StartTime,EndTime):
    Performance = DescribeHistoryMonitorValuesRequest()
    Performance.set_accept_format('json')
    Performance.set_InstanceId(DBInstanceId)
    Performance.set_IntervalForHistory("01m")
    Performance.set_MonitorKeys(MasterKey)
    Performance.set_StartTime(StartTime)
    Performance.set_EndTime(EndTime)
    PerformanceInfo = clt.do_action_with_exception(Performance)
    Info = json.loads(PerformanceInfo)
    Value = Info['MonitorHistory']
    #把字符串转为字典
    ValueDict = json.loads(Value)
    #获取字典中最后一个元素的值
    Value = ValueDict.get(sorted(ValueDict.keys())[-1])[SubKey]
    print(float(Value) * 1048576)

def GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime):
    Performance = DescribeHistoryMonitorValuesRequest()
    Performance.set_accept_format('json')
    Performance.set_InstanceId(DBInstanceId)
    Performance.set_IntervalForHistory("01m")
    Performance.set_MonitorKeys(MasterKey)
    Performance.set_StartTime(StartTime)
    Performance.set_EndTime(EndTime)
    PerformanceInfo = clt.do_action_with_exception(Performance)
    Info = json.loads(PerformanceInfo)
    Value = Info['MonitorHistory']
    #把字符串转为字典
    ValueDict = json.loads(Value)
    #获取字典中最后一个元素的值
    Value = ValueDict.get(sorted(ValueDict.keys())[-1])[SubKey]
    print(Value)

if (Type == 'Disk'):
    #内存使用量，包含数据和缓存部分,此部分没有使用，代码保留
    if (MasterKey == 'UsedMemory' and  SubKey == 'UsedMemory'):
        GetResourceUsage(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
elif (Type == 'Performance'):
    #命中率 %
    if (MasterKey == 'Hit_Rate_Monitor' and  SubKey == 'hit_rate'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #每秒命中的Key数量 Counts/s
    elif (MasterKey == 'Hit_Rate_Monitor' and  SubKey == 'hit'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #每秒未命中的key数量 Counts/s
    elif (MasterKey == 'Hit_Rate_Monitor' and  SubKey == 'miss'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #CPU使用率 %
    elif (MasterKey == 'CpuUsage' and  SubKey == 'CpuUsage'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    # #连接数使用率 %
    # elif (MasterKey == 'ConnectionUsage' and  SubKey == 'connectionUsage'):
        # GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #内存使用率 %
    elif (MasterKey == 'MemoryUsage' and  SubKey == 'memoryUsage'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #入流量速率 KBps
    elif (MasterKey == 'IntranetIn' and  SubKey == 'InFlow'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #出流量速率 KBps
    elif (MasterKey == 'IntranetOut' and  SubKey == 'OutFlow'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #平均时延，数据节点从接收命令到发出响应的时延平均值 us
    elif (MasterKey == 'Redis_Avg_Rt_Monitor' and  SubKey == 'AvgRt'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)      
    #Key总数量，即实例存储的一级Key总数 Counts
    elif (MasterKey == 'Redis_Basic_Monitor' and  SubKey == 'Keys'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #实例中设置了过期时间的键值对数量 Counts
    elif (MasterKey == 'Redis_Basic_Monitor' and  SubKey == 'Expires'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #历史累计因内存不足被驱逐的Key总数 Counts
    elif (MasterKey == 'Redis_Basic_Monitor' and  SubKey == 'EvictedKeys'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #历史累计因过期淘汰的Key总数 Counts
    elif (MasterKey == 'Redis_Basic_Monitor' and  SubKey == 'ExpiredKeys'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #每秒被淘汰的Key数量 Counts/s
    elif (MasterKey == 'Redis_Basic_Monitor' and  SubKey == 'ExpiredKeysPerSecond'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #每秒被驱逐的Key数量 Counts/s
    elif (MasterKey == 'Redis_Basic_Monitor' and  SubKey == 'EvictedKeysPerSecond'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #内存使用量，包含数据和缓存部分 Bytes
    elif (MasterKey == 'UsedMemory' and  SubKey == 'UsedMemory'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #每秒总请求数，包含读和写命令  Counts/s
    elif (MasterKey == 'UsedQPS' and  SubKey == 'TotalQps'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #每秒读命令请求数。 Counts/s
    elif (MasterKey == 'UsedQPS' and  SubKey == 'GetQps'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)
    #每秒写命令请求数  Counts/s
    elif (MasterKey == 'UsedQPS' and  SubKey == 'PutQps'):
        GetPerformance(DBInstanceId,MasterKey,SubKey,StartTime,EndTime)

   
    

