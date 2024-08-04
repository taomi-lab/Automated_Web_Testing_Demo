# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : page_login.py
# @author   : TaoMi
# @Time     : 2024/7/29 下午3:18

import pages
from pages.basepage import BasePage


class PageLogin(BasePage):

    # 切换到登录界面
    def page_click_please_login(self):
        # ele_info = {"name": "登录", "type": "linktext", "value": "登录", "timeout": 5}
        ele_info = {"name": "切换到登录界面",
                    "type": pages.login_please_login[0],
                    "value": pages.login_please_login[1]}
        self.operate.click(ele_info)

    #  切换主窗口到登录界面
    def page_change_window(self):
        self.operate.switch_to_window()

    # 点击登录按钮
    def page_click_login(self):
        ele_info = {"name": "点击登录按钮",
                    "type": pages.login_login[0],
                    "value": pages.login_login[1]}
        self.operate.click(ele_info)

    # 点击密码登录
    def page_click_pwd_login(self):
        ele_info = {"name": "点击密码登录",
                    "type": pages.login_click_pwd_login[0],
                    "value": pages.login_click_pwd_login[1]}
        self.operate.click(ele_info)

    # 输入账号
    def page_input_account(self, username):
        ele_info = {"name": "输入账号",
                    "type": pages.login_input_account[0],
                    "value": pages.login_input_account[1]}
        self.operate.send_keys(ele_info, username)

    # 输入密码
    def page_input_password(self, password):
        ele_info = {"name": "输入密码",
                    "type": pages.login_input_password[0],
                    "value": pages.login_input_password[1]}
        self.operate.send_keys(ele_info, password)

    # 点击协议
    def page_click_protocol(self):
        ele_info = {"name": "点击协议",
                    "type": pages.login_click_protocol[0],
                    "value": pages.login_click_protocol[1]}
        self.operate.click(ele_info)

    # 登录
    def page_click_login_button(self):
        ele_info = {"name": "执行登录",
                    "type": pages.login_click_login_button[0],
                    "value": pages.login_click_login_button[1]}
        self.operate.click(ele_info)

    # 判断是否登录成功
    def page_is_login_success(self):
        ele_info = {"name": "判断是否登录成功: 退出按钮",
                    "type": pages.login_logout[0],
                    "value": pages.login_logout[1]}
        return self.operate.is_element_exist(ele_info)

    # 判断是否退出成功
    def page_is_logout_success(self):
        ele_info = {"name": "判断是否退出成功: 登录按钮",
                    "type": pages.login_login[0],
                    "value": pages.login_login[1]}
        return self.operate.is_element_exist(ele_info)

    # 安全退出
    def page_click_logout(self):
        ele_info = {"name": "安全退出",
                    "type": pages.login_logout[0],
                    "value": pages.login_logout[1]}
        self.operate.click(ele_info)

    # 在登陆前获取异常信息
    def page_get_error_info_before(self):
        # 判断是否输入输入用户名
        if self.operate.is_input({"name": "用户名",
                                  "type": pages.login_input_account[0],
                                  "value": pages.login_input_account[1]}):
            # 返回用户名为空
            return " "

        # 判断是否输入密码
        elif self.operate.is_input({"name": "用户名",
                                    "type": pages.login_input_password[0],
                                    "value": pages.login_input_password[1]}):
            # 返回密码为空
            return " "

        # 判断协议是否勾选
        elif self.operate.is_checkbox_checked({"name": "协议复选框",
                                               "type": pages.login_click_protocol[0],
                                               "value": pages.login_click_protocol[1]}):
            # 返回协议未勾选
            return self.operate.get_text({"name": "请协议复选框",
                                          "type": pages.login_protocol_fail[0],
                                          "value": pages.login_protocol_fail[1]})
        # 否则就是账号 或者密码格式不对 或者是账号不对 密码不对等等

    # 获取异常提示信息
    def page_get_error_info(self):
        return self.operate.get_text({"name": "获取异常提示信息(账号密码错误)",
                                      "type": pages.login_account_or_pwd_error[0],
                                      "value": pages.login_account_or_pwd_error[1]})

    def page_get_error_info1(self):
        return self.operate.get_text({"name": "获取异常提示信息(登录失败)",
                                      "type": pages.login_login_fail[0],
                                      "value": pages.login_login_fail[1]})

    # 移动滑块
    def page_moving_verify_code(self):
        ele_info1 = {"name": "滑块起始位置",
                     "type": pages.login_moving_btn[0],
                     "value": pages.login_moving_btn[1]}
        ele_info2 = {"name": "滑块结束位置",
                     "type": pages.login_moving_area[0],
                     "value": pages.login_moving_area[1]}

        self.operate.move(ele_info1, ele_info2)
