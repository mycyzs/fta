# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserActivityLog'
        db.create_table('user_activity_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('log_id', self.gf('django.db.models.fields.CharField')(max_length=32, db_index=True)),
            ('app_code', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('activity_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('activity_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('request_params', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('before_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('after_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('activity_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('remarks', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('user_activity_log', ['UserActivityLog'])


    def backwards(self, orm):
        # Deleting model 'UserActivityLog'
        db.delete_table('user_activity_log')


    models = {
        'user_activity_log.useractivitylog': {
            'Meta': {'object_name': 'UserActivityLog', 'db_table': "'user_activity_log'"},
            'activity_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'activity_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'activity_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'after_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'app_code': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'before_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'request_params': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['user_activity_log']