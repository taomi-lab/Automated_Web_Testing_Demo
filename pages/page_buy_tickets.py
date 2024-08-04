# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : page_buy_tickets.py
# @author   : TaoMi
# @Time     : 2024/7/29 下午3:15

import pages
from common.driver import DriverOperate
from pages.basepage import BasePage


class BuyLogin(BasePage):
    # 点击购买火车票
    def page_click_buy_tickets(self):
        ele_info = {"name": "点击购买火车票",
                    "type": pages.buy_click_tickets[0],
                    "value": pages.buy_click_tickets[1]}
        self.operate.click(ele_info)

    # 选择出发站
    def page_input_start_station(self, start_station):
        ele_info = {"name": "选择出发站",
                    "type": pages.buy_start_station[0],
                    "value": pages.buy_start_station[1]}
        self.operate.send_keys(ele_info, start_station)

    # 选择到达站
    def page_input_arrive_station(self, arrive_station):
        ele_info = {"name": "选择到达站",
                    "type": pages.buy_arrive_station[0],
                    "value": pages.buy_arrive_station[1]}
        self.operate.send_keys(ele_info, arrive_station)

    # 选择日期
    def page_input_time(self, time):
        ele_info = {"name": "查找日期",
                    "type": pages.buy_start_time[0],
                    "value": pages.buy_start_time[1]}
        date_input = self.operate.find_element(ele_info)
        DriverOperate.globalDriverOperate.driver.execute_script("arguments[0].value = arguments[1];", date_input, time)

    # 选择搜索
    def page_click_find(self):
        ele_info = {"name": "选择搜索",
                    "type": pages.buy_click_find[0],
                    "value": pages.buy_click_find[1]}
        self.operate.click(ele_info)

    # 点击购买
    def page_click_buy_ticket(self):
        ele_info = {"name": "点击购买",
                    "type": pages.but_click_buy_ticket[0],
                    "value": pages.but_click_buy_ticket[1]}
        self.operate.click(ele_info)

    # 输入购票人姓名
    def page_input_buy_ticket_name(self, name):
        ele_info = {"name": "输入购票人姓名",
                    "type": pages.buy_input_name[0],
                    "value": pages.buy_input_name[1]}
        self.operate.send_keys(ele_info, name)

    # 输入购票人身份证信息
    def page_input_buy_ticket_board(self, board):
        ele_info = {"name": "输入购票人身份证信息",
                    "type": pages.buy_input_boardcard[0],
                    "value": pages.buy_input_boardcard[1]}
        self.operate.send_keys(ele_info, board)

    # 输入取票人姓名
    def page_input_contact_name(self, name):
        ele_info = {"name": "输入取票人姓名",
                    "type": pages.buy_input_contact_name[0],
                    "value": pages.buy_input_contact_name[1]}
        self.operate.send_keys(ele_info, name)

    # 输入取票人电话
    def page_input_contact_phone(self, phone):
        ele_info = {"name": "输入取票人电话",
                    "type": pages.buy_input_contact_phone[0],
                    "value": pages.buy_input_contact_phone[1]}
        self.operate.send_keys(ele_info, phone)

    # 点击提交订单
    def page_click_submit(self):
        ele_info = {"name": "点击提交订单",
                    "type": pages.buy_click_submit[0],
                    "value": pages.buy_click_submit[1]}
        self.operate.click(ele_info)

    # 提交订单成功
    def page_submit_access(self):
        ele_info = {"name": "提交订单成功",
                    "type": pages.buy_submit_success[0],
                    "value": pages.buy_submit_success[1]}
        self.operate.is_element_exist(ele_info)

    # 获取异常提示信息
    def page_buy_get_error_info(self):
        ele_info = {"name": "获取异常提示信息",
                    "type": pages.buy_submit_fail_info[0],
                    "value": pages.buy_submit_fail_info[1]}
        return self.operate.get_text(ele_info)

    # 点击错误提示信息的确认框
    def page_buy_click_button_ok(self):
        ele_info = {"name": "点击错误提示信息的确认框",
                    "type": pages.buy_submit_click_OK[0],
                    "value": pages.buy_submit_click_OK[1]}
        self.operate.click(ele_info)

    # 退出成功
    def page_buy_is_logout_success(self):
        ele_info = {"name": "退出成功",
                    "type": pages.buy_click_tickets[0],
                    "value": pages.buy_click_tickets[1]}
        self.operate.is_element_exist(ele_info)

