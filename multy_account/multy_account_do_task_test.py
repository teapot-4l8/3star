# -*- coding: utf-8 -*-
# @Time    : 2024/11/7 14:16
# @Desc    : 多账户同时挂机测试
import time
from account import uid_list

import asyncio
from account import uid_list

import asyncio
from account import uid_list


class ThreeStar:
    def __init__(self, uid):
        self.uid = uid

    async def start(self):
        for i in range(5):
            await asyncio.sleep(2)  # 使用 asyncio.sleep 代替 time.sleep
            print(f"{self.uid} is doing task ...")

        print(f"{self.uid} finished !!!")


async def start_task(uid, delay):
    await asyncio.sleep(delay)  # 等待指定的延迟时间
    ts = ThreeStar(uid)
    await ts.start()


async def main():
    total_time = 13  # 总时间（秒）
    num_uids = len(uid_list)  # uid的个数
    if num_uids == 0:
        print("No uids to process.")
        return

    interval = total_time / (num_uids - 1)  # 计算每个任务之间的间隔时间
    tasks = []
    for i, uid in enumerate(uid_list):
        delay = interval * i  # 计算每个任务的延迟时间
        task = start_task(uid, delay)
        tasks.append(task)

    # 并发运行所有任务
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
