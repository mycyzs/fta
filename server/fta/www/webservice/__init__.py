# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa

import os
import importlib

from flask import Blueprint

from fta.utils import logging


fta_simple_page = Blueprint('fta', __name__,
                            template_folder='templates')
__all__ = ["fta_simple_page"]
views = set()
logger = logging.getLogger(__name__)

for f in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    if f.startswith("_"):
        continue
    module_name, ext = os.path.splitext(f)
    if not ext.startswith(".py"):
        continue
    views.add(module_name)

for view in views:
    try:
        importlib.import_module("fta.www.webservice.%s" % view)
    except Exception as err:
        logger.error(err)
