# -*- coding: utf-8 -*-
# @Time    : 2024/11/6 11:46
# @Desc    : 测试多人助力逻辑

from account import uid_list
import os

class ThreeStar:
    def __init__(self, uid):
        self.uid = uid
        self.remain_assist_times = 3  # 为别人助力次数
        self.remain_assisted_times = 6  # 别人为我助力的次数

    def assist_jid(self, jid):
        if self.remain_assist_times > 0:
            self.remain_assist_times -= 1
            print(f"{self.uid} assist {jid}, assist_times remain {self.remain_assist_times}")
        else:
            print(f"{self.uid} has no more assist times left.")

    def can_be_assisted(self):
        return self.remain_assisted_times > 0

    def assisted(self):
        self.remain_assisted_times -= 1
        if self.remain_assisted_times == 0:
            print(f"{self.uid} has reached the maximum assisted times.")


if __name__ == '__main__':
    # 创建账号实例
    ts_accounts = [ThreeStar(uid) for uid in uid_list]

    # 模拟助力过程
    for i in range(len(ts_accounts)):
        for j in range(len(ts_accounts)):
            if i != j and ts_accounts[i].remain_assist_times > 0 and ts_accounts[j].can_be_assisted():
                ts_accounts[i].assist_jid(ts_accounts[j].uid)
                ts_accounts[j].assisted()

    # 打印每个账号的助力情况
    for ts in ts_accounts:
        print(f"{ts.uid} has {ts.remain_assist_times} assist times left and has been assisted {ts.remain_assisted_times} times.")

