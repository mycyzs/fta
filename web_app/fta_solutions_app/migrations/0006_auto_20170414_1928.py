# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fta_solutions_app', '0005_auto_20170412_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdviceFtaDef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('advice_def_id', models.IntegerField(db_index=True)),
                ('is_enabled', models.BooleanField(default=False, verbose_name='\u662f\u5426\u542f\u7528')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('cc_biz_id', models.IntegerField(verbose_name='\u4e1a\u52a1\u7f16\u7801', db_index=True)),
                ('module', models.TextField(default=b'', help_text='\u5197\u4f59\u5b57\u6bb5', verbose_name='Module ID', blank=True)),
                ('topo_set', models.TextField(default=b'', help_text='\u5197\u4f59\u5b57\u6bb5', verbose_name='Set ID', blank=True)),
                ('set_names', models.TextField(default=b'', verbose_name='Set\u540d\u79f0', blank=True)),
                ('module_names', models.TextField(default=b'', verbose_name='Module\u540d\u79f0', blank=True)),
                ('responsible', models.CharField(max_length=255, null=True, verbose_name='\u989d\u5916\u901a\u77e5\u4eba', blank=True)),
                ('title', models.CharField(max_length=128, null=True, verbose_name='\u5168\u540d', blank=True)),
                ('description', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('notify', models.TextField(default=b'{}', verbose_name='\u901a\u77e5\u914d\u7f6e')),
                ('solution_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('timeout', models.IntegerField(default=40, verbose_name='\u8d85\u65f6\u65f6\u957f')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.AlterField(
            model_name='alarminstance',
            name='alarm_type',
            field=models.CharField(db_index=True, max_length=128, verbose_name='\u544a\u8b66\u7c7b\u578b', choices=[(b'Faild_ping', 'ping\u4e0d\u53ef\u8fbe'), (b'Read_onlyDisk', '\u78c1\u76d8\u53ea\u8bfb'), (b'Agent_report_timeout', 'agent\u4e0a\u62a5\u8d85\u65f6'), (b'DiskUtilization', '\u78c1\u76d8\u5229\u7528\u7387'), (b'CPUUtilization', 'CPU\u5229\u7528\u7387'), (b'MemoryUtilization', '\u5185\u5b58\u4f7f\u7528\u91cf'), (b'Machine_restart', '\u673a\u5668\u91cd\u542f'), (b'PublicBandwidthHigh', '\u5916\u7f51\u5e26\u5bbd\u5360\u7528\u9ad8'), (b'DiskIOAwait', '\u78c1\u76d8IO\u7b49\u5f85'), (b'DiskReadTraffic', '\u78c1\u76d8\u8bfb\u6d41\u91cf'), (b'DiskWriteTraffic', '\u78c1\u76d8\u5199\u6d41\u91cf'), (b'PublicBandwidthIn', '\u5916\u7f51\u5165\u5e26\u5bbd'), (b'PublicBandwidthOut', '\u5916\u7f51\u51fa\u5e26\u5bbd'), (b'PublicPacketsIn', '\u5916\u7f51\u5165\u5305\u91cf'), (b'PublicPacketsOut', '\u5916\u7f51\u51fa\u5305\u91cf'), (b'PublicBandwidthUtilization', '\u5916\u7f51\u5e26\u5bbd\u4f7f\u7528\u7387'), (b'MemoryUtilization', '\u5185\u5b58\u5229\u7528\u7387'), (b'PrivateBandwidthIn', '\u5185\u7f51\u5165\u5e26\u5bbd'), (b'PrivateBandwidthOut', '\u5185\u7f51\u51fa\u5e26\u5bbd'), (b'PrivatePacketsIn', '\u5185\u7f51\u5165\u5305\u91cf'), (b'PrivatePacketsOut', '\u5185\u7f51\u51fa\u5305\u91cf'), (b'dockerCPUUtilization', 'docker\u96c6\u7fa4cpu\u5229\u7528\u7387'), (b'dockerMemoryUtilization', 'docker\u96c6\u7fa4\u5185\u5b58\u5229\u7528\u7387'), (b'cpu_3', '5\u5206\u949f\u5e73\u5747\u8d1f\u8f7d\uff08\u4e58\u4ee5100)'), (b'cpu_7', 'cpu\u603b\u4f7f\u7528\u7387'), (b'cpu_8', 'cpu\u5355\u6838\u4f7f\u7528\u7387'), (b'mem_98', '\u5e94\u7528\u7a0b\u5e8f\u4f7f\u7528\u5185\u5b58\u91cf'), (b'mem_64', '\u7269\u7406\u5185\u5b58\u4f7f\u7528\u7387'), (b'mem_97', '\u5df2\u7528\u7269\u7406\u5185\u5b58'), (b'net_10', '\u7f51\u5361\u5165\u6d41\u91cf'), (b'net_14', '\u7f51\u5361\u51fa\u6d41\u91cf'), (b'net_16', '\u7f51\u5361\u53d1\u5305\u91cf'), (b'net_20', '\u7f51\u5361\u6536\u5305\u91cf'), (b'disk_81', '\u5df2\u7528\u7a7a\u95f4\u5360\u6bd4'), (b'disk_86', '\u78c1\u76d8IO\u8bfb\u901f\u7387'), (b'disk_87', '\u78c1\u76d8IO\u5199\u901f\u7387'), (b'disk_96', '\u78c1\u76d8IO\u4f7f\u7528\u7387'), (b'BASE_ALARM_3', '\u78c1\u76d8\u53ea\u8bfb'), (b'BASE_ALARM_6', '\u78c1\u76d8\u5199\u6ee1'), (b'BASE_ALARM_7', 'Corefile\u4ea7\u751f'), (b'custom', '\u81ea\u5b9a\u4e49'), (b'agent.*', 'Agent\u72b6\u6001(agent.*)'), (b'system.cpu.*', 'CPU\u4f7f\u7528\u7387(system.cpu.*)'), (b'vm.memory.size', '\u5185\u5b58\u4f7f\u7528\u91cf(vm.memory.size)'), (b'system.swap.*', 'Swap\u4f7f\u7528\u91cf(system.swap.*)'), (b'kernel.*', '\u7cfb\u7edf\u5185\u6838\u72b6\u6001(kernel.*)'), (b'vfs.dev.*', '\u78c1\u76d8IO\u4f7f\u7528\u7387(vfs.dev.*)'), (b'vfs.fs.*', '\u78c1\u76d8\u5bb9\u91cf(vfs.fs.*)'), (b'proc.num', '\u8fdb\u7a0b\u6570\u91cf\u68c0\u67e5(proc.num)'), (b'icmping*', 'Ping\u68c0\u67e5(icmpping*)'), (b'net.tcp.*', 'TCP\u94fe\u63a5\u68c0\u67e5(net.tcp.*)'), (b'net.udp.*', 'UDP\u94fe\u63a5\u68c0\u67e5(net.udp.*)'), (b'vfs.file.*', '\u6587\u4ef6\u72b6\u6001\u68c0\u67e5(vfs.file.*)'), (b'zabbix.*', 'Zabbix\u5176\u4ed6'), (b'open-falon-agent.*', 'Agent\u72b6\u6001(agent.*)'), (b'open-falon-load.*', 'CPU\u4f7f\u7528\u7387(load.*)'), (b'open-falon-mem.*', '\u5185\u5b58\u4f7f\u7528\u91cf(mem.*)'), (b'open-falon-disk.io.*', '\u78c1\u76d8IO\u4f7f\u7528\u7387(disk.io.*)'), (b'open-falon-df.*', '\u78c1\u76d8\u5bb9\u91cf(df.*)'), (b'open-falon-net.if.*', '\u7f51\u5361\u6d41\u91cf(net.if.*)'), (b'open-falon-net.port.listen', '\u7aef\u53e3\u76d1\u63a7(net.port.listen)'), (b'open-falon-.*', 'Open-Falon\u5176\u4ed6'), (b'http', 'HTTP'), (b'cpu', 'CPU'), (b'mem', '\u5185\u5b58'), (b'net', '\u7f51\u7edc'), (b'fs', '\u6587\u4ef6\u7cfb\u7edf'), (b'proc', '\u8fdb\u7a0b'), (b'nagios', 'Nagios\u5176\u4ed6'), (b'api_default', 'REST\u9ed8\u8ba4\u5206\u7c7b'), (b'fta_advice', '\u9884\u8b66\u81ea\u6108')]),
        ),
        migrations.AlterField(
            model_name='alarminstance',
            name='source_type',
            field=models.CharField(max_length=32, null=True, verbose_name='\u544a\u8b66\u6e90', choices=[(b'ALERT', '\u84dd\u9cb8\u76d1\u63a7'), (b'QCLOUD', '\u817e\u8baf\u4e91\u76d1\u63a7'), (b'ZABBIX', 'Zabbix\u76d1\u63a7'), (b'OPEN-FALON', 'Open-Falon\u76d1\u63a7'), (b'NAGIOS', 'NAGIOS\u76d1\u63a7'), (b'REST-API', b'REST API'), (b'FTA', '\u6545\u969c\u81ea\u6108')]),
        ),
    ]
