"""
日历模块


"""
import calendar

#使用

#返回指定某年某月的日历
print(calendar.month(2017,7))
#返回指定年的ruling
print(calendar.calendar(2017))

#闰年返回ture，否则返回false
print(calendar.isleap(2017))
#返回某个月的weekday的第一天和这个月所有的天数
print(calendar.monthrange(2017,7))

#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2017,7))


















































