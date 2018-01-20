# import os
# dir = os.getcwd()
# print("The current directory is ",dir,".")
# files=[]
# for file in dir:
#     files.append(file)
# print("The current directory has files: ",files,".")
# files2 = os.listdir(dir)
# print(files2)
# import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# sum = sum(data)/len(data)
# print("Sum is ",sum,".")
# a=0;
# for x in data:
#     a=a+(x-sum)**2
# print("a = ",a,".")
# print(a/(len(data)-1))
# print(statistics.variance(data))

# from urllib.request import urlopen
# with urlopen('http://180.167.23.130:9091/getWebCarouse') as response:
#      for line in response:
#          line = line.decode('utf-8')
#          print(line)
#          if('EST' in line or 'EDT' in line):
#              print(line)

# import smtplib
# server = smtplib.SMTP('smtp.126.com')
# server.login("liuyangyang_2010@126.com","xxx")
# server.sendmail("liuyangyang_2010@126.com","liuyangyang_2010@126.com","To: jcaesar@example.org \
#                                                                 From: soothsayer@example.org \
#                                                                 Beware the Ides of March.")
# server.quit()

# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)
# #
# # import doctest
# # a=doctest.testmod()
# # print(a)
#
# import unittest
#
# class TestStatisticalFunctions(unittest.TestCase):
#
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)
#
# unittest.main()  # Calling from the command line invokes all tests

# import reprlib
# print(reprlib.repr(set('supercalifragilisticexpialidocious')))
# import textwrap
# doc = """The wrap() method is just like fill() except that it returns
# ... a list of strings instead of one big string with newlines to separate
# ... the wrapped lines."""
# print(textwrap.fill(doc, width=40))
# import locale
# locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# conv = locale.localeconv()
# x = 1234567.8
# a=locale.format("%d", x, grouping=True)
# b=locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'], x), grouping=True)
# print(a)
# print(b)
from string import Template
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

