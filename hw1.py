from random import uniform

class Portfolio():
	def __init__(self,cash=0):
		self.cash = float(cash)
		self.portfolio = {"Stocks": {}, "Mutual Funds":{}, "Bonds":{}} #dictionary of assets
		self.history = ["Transactions' history:",]

	def addCash(self, added_cash): #add cash to portfolio
		self.cash += added_cash #sum cash from portfolio and added cash
		self.history.append("\n cash: +$%s" % added_cash)
		
		
	def withdrawCash(self, wcash): #withdraw cash from portfolio
		self.cash -= wcash
		self.history.append("\n cash: -$%s" % wcash)
		
		

	def buy(self, share, asset): #generic method for buying assets
		self.share = share
		self.asset = asset
		self.cash -= self.asset.price*self.share
		if asset in self.portfolio[asset.assetType()]:
			self.portfolio[asset.assetType()][asset] += share
		else: self.portfolio[asset.assetType()][asset] = share
		self.history.append("\n Bought %s shares of %s, by $%s" % (self.share,self.asset.assetType(),(self.share*asset.price)))
		
	buyMutualFund = buy #Apply function buy to both mutual funds and bonds
	buyBond = buy
	
	def buyStock(self,share,asset): #whole units for stocks
		return self.buy(int(share),asset)
	
	
	def sell(self, share, asset): #generic method for selling assets
		self.portfolio[asset.assetType()][asset] -= share
		self.cash += share*asset.SellFor()
		self.history.append("\n Sold %s shares of %s, by $%s" % (share,asset.assetType(),(share*asset.SellFor())))
		
	sellMutualFund = sell #Apply function sell to both mutual funds and bonds
	sellBond = sell
	
	def sellStock(self,asset,share): #whole units for stocks
		return self.sell(int(share),asset)
	
	def history_log(self):
		return "\n".join(self.history)
		
	def __str__(self):	# Creating the normal print output
		portprint = "\nYour portfolio:\nCash:\t$%.2f \n" % self.cash
		for i in self.portfolio:
			portprint += "%s: \n" % i
			if not self.portfolio[i]: portprint += "\t None \n"
			for j in self.portfolio[i]: portprint += "\t" + str(self.portfolio[i][j]) + "\t" + str(j.symbol) + "\n"
		return portprint
	

class InvestType():
	def __init__(self,price,symbol):
		self.price=price
		self.symbol=symbol
	
###The sons of the class InvestType
			
class Stock(InvestType):
	def __init__(self,price,symbol):
		InvestType.__init__(self, price, symbol)
			
	def SellFor(self):
		return int(10.0*uniform(.5*self.price,1.5*self.price))/10.0
	
	def assetType(self):
		return "Stocks"

class MutualFund(InvestType):
	def __init__(self, symbol):
		InvestType.__init__(self, 1.0, symbol)
		
	def SellFor(self): # need to do the same for the other assets
		return int(10.0*uniform(.9*self.price,1.2*self.price))/10.0
		
	def assetType(self):
		return "Mutual Funds"

class Bond(InvestType):
	def __init__(self, price, symbol):
		InvestType.__init__(self)
		self.price=float(price)
		self.symbol=str(symbol)
	
	def SellFor(self):
		return int(10.0*uniform(self.price,1.3*self.price))/10.0 #no risk, for a change
		
	def assetType(self):
		return "Bonds"

#Two things that are not exactly as asked, unfortunately:
	# 1) the sell function requres the asset rather than the ticker;
	# 2) the history has to be printed.
		

portfolio=Portfolio()
#print portfolio
portfolio.addCash(1000)
#print portfolio
s = Stock(20,"HFH")
portfolio.buyStock(5,s)
#print portfolio
#print portfolio.history_log()
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3,mf1)
portfolio.buyMutualFund(2,mf2)
#print portfolio.history_log()
#print portfolio
portfolio.sellMutualFund(3, mf1)
#print portfolio
portfolio.withdrawCash(100)
portfolio.sellStock(s,1)
print portfolio.history_log()

