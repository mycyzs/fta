# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa
#
# Poll alarm from message queue for run solution

import signal
import time

from fta import settings
from fta.solution.process import Solution
from fta.utils import hooks, logging, send_notice

hook = hooks.HookManager("solution")
Solution = hook.get_by_argv("Solution", Solution)

logger = logging.getLogger("solution")

SHUTDOWN = False


def onsignal(signum, frame):
    """handle quit signal"""
    logger.info("solution shutdown")
    global SHUTDOWN
    SHUTDOWN = True


def main():
    signal.signal(signal.SIGTERM, onsignal)
    signal.signal(signal.SIGINT, onsignal)
    while not SHUTDOWN:
        try:
            solution = Solution()
            solution.start()
        except Exception as e:
            logger.exception(e)
            send_notice.exception(e)
            logger.info('exception occur, will retrying in %s(s).' % settings.EXCEPTION_RETRY_INTERVAL)
            time.sleep(settings.EXCEPTION_RETRY_INTERVAL)


if __name__ == "__main__":
    main()
