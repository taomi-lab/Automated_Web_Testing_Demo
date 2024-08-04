# 使用说明
使用前，需要配置data文件夹内的各种json文件。
	1. common/driver.py封装了web基本操作，如元素定位、元素点击、多表单（窗口）切换等方法
	2. common/logger.py封装了log对象
	3. pages文件夹内封装了多个页面对象，将登录/火车票查询等页面各自封装为单独页面对象
	4. actions文件夹内封装了每个页面的操作
