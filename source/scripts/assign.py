# *******************************************************************************************
# *******************************************************************************************
#
#		Name : 		assign.py
#		Purpose :	Test generator
#		Date :		22nd September 2022
#		Author : 	Paul Robson (paul@robsons.org.uk)
#
# *******************************************************************************************
# *******************************************************************************************

import os,sys,re,random
from tests import *

# *******************************************************************************************
#
#								Variable Classes
#
# *******************************************************************************************

class Variable:
	def __init__(self,index):
		self.name = "".join([ chr(random.randint(0,25)+97)+str(random.randint(0,9)) for x in range(1,random.randint(2,4))])+"_"+str(index)
		if index < 20 and random.randint(0,3) == 0:
			self.name = chr(index+65)
		self.value = 0

	def getName(self):
		return self.name 
	def getValue(self):
		return self.value 
	def updateValue(self):
		newValue = self.getNewValue()
		self.value = newValue 
		return self.getValue()

class IntegerVariable(Variable):
	def getNewValue(self):
		return str(random.randint(-444444444,444444444))

class FloatVariable(Variable):
	def getName(self):
		return Variable.getName(self)+"#"
	def getNewValue(self):
		return str(random.randint(-444444444,444444444)/1000)

# *******************************************************************************************
#
#						Repeated assignments generator
#
# *******************************************************************************************

class AssignOne(TestAssertion):
	def create(self,parent):
		v = parent.variables[random.randint(0,len(parent.variables)-1)]					# pick a variable
		return [v.getName(), v.updateValue()]
	def make(self,data):
		kwd = "let " if random.randint(0,1) == 0 else ""
		return "{2}{0} = {1}".format(data[0],data[1],kwd)

# *******************************************************************************************
#
#									Complete Test Set class
#
# *******************************************************************************************

class AssignTestSet(TestSet):

	def getFactoryList(self):
		return [ 			 															# list of test factory classes
			AssignOne()
		]

	def startup(self):
		self.variables = [] 															# create variables, all initially zero or ""
		varCount = max(2,self.count // 3)
		for i in range(0,varCount):
			if i%2 == 0:
				v = IntegerVariable(i)
			if i%2 == 1:
				v = FloatVariable(i)
			self.variables.append(v)
		return self

	def closedown(self):
		for v in self.variables:
			self.handle.write("{0} assert {1} = {2}\n".format(self.lineNumber,v.getName(),v.getValue()))
			self.lineNumber += self.step
		return self

if __name__ == "__main__":
	AssignTestSet().do(48).startup().create().closedown().terminate()

