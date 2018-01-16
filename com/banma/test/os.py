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