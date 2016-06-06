#!/usr/bin/python
#_*_ coding: UTF-8 _*_
###################
#冒泡排序
###################
def bubbleSort(numbers):                   #冒泡排序  子函数
	for j in range(len(numbers)-1,-1,-1):  #j 从序号最大开始的，即为倒序   目的在于将最大的数放到最后
		for i in range(j):
			if numbers[i]>=numbers[i+1]:
				numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
	print numbers
def main():                                #主函数
	numbers=[12,4,25,1,6,10]
	bubbleSort(numbers)
if __name__=="__main__":
	main()