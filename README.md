# 功能
  zabbix通过阿里云api自动发现阿里云redis的性能监控
# 使用方法
## 环境要求
 python2或者python3
## 模块安装
`pip install aliyun-python-sdk-core`

`pip install aliyun-python-sdk-r-kvstore`
## 使用方法
从阿里云控制台获取 AccessKey ,并修改两个脚本中的 ID 与 Secret
修改区域 RegionId
将两个脚本放置于以下目录

```
/etc/zabbix/scripts
chmod +x /etc/zabbix/scripts/*
```

修改zabbix-agentd.conf，添加以下内容
```
#aliyun redis monitor
UserParameter=aliyun.redis.discovery,python /etc/zabbix/scripts/discovery_redis.py
UserParameter=check.aliyun.redis[*],python /etc/zabbix/scripts/check_aliyun_redis.py $1 $2 $3 $4
```

重启zabbix-agent
zabbix控制台导入模板，并关联主机
## 效果图
![image](https://user-images.githubusercontent.com/13861904/143827184-dbd8e17d-044b-48ba-a726-d7b9852ffc44.png)

