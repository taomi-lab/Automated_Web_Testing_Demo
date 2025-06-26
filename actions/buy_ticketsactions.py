# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : buy_ticketsactions.py
# @author   : TaoMi
# @Time     : 2024/7/31 下午3:20

import time
from pages.page_buy_tickets import BuyLogin
from actions.loginactions import LoginActions
global_var = 0


class BuyticketsActions:

    def Buytickets(self, start_station, arrive_station, date, name, board, phone):
        global global_var
        if global_var == 0:
            # 登录
            LoginActions().Longin("15135976034", "shs092121")
            global_var = 1
        page = BuyLogin()
        page.page_click_buy_tickets()
        page.page_input_start_station(start_station)
        page.page_input_arrive_station(arrive_station)
        page.page_input_time(date)
        time.sleep(10)

        page.page_click_find()
        page.page_click_buy_ticket()
        page.page_input_buy_ticket_name(name)
        page.page_input_buy_ticket_board(board)
        page.page_input_contact_name(name)
        page.page_input_contact_phone(phone)
        page.page_click_submit()
