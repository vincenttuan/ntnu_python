class Account:
    money = 0
    def setName(self, name): # 戶名
        self.name = name
    def getName(self):
        return self.name
    def setMoney(self, money):
        self.money = self.money + money
    def getMoney(self):
        return self.money

a = Account()
a.setName('Vincent')
a.setMoney(100)
a.setMoney(500)

b = Account()
b.setName('Anita')
b.setMoney(600)
b.setMoney(-200)

print(a.getName(), a.getMoney())
print(b.getName(), b.getMoney())

list_account = [a, b]
for x in list_account:
    print(x.getName(), x.getMoney())