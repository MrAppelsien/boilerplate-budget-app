class Category:
    def __init__(self, category):
        self.category = category
        self.amount = 0
        self.ledger = []

    def deposit(self, amount, wat=''):
        self.amount += amount
        self.ledger.append({'description': wat, 'amount': self.amount})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        else:
            self.amount -= amount
            self.ledger.append({'amount':-amount, 'description': description})
            return True

    def check_funds(self, amount):
        if self.amount < amount:
            return False
        else:
            return True

    def get_balance(self):
        return self.amount

    def transfer(self, amount, transfer_category):
        if self.category != transfer_category.category:
            if not self.check_funds(amount):
                return False
            else:
                self.amount -= amount
                self.ledger.append({'amount': -amount, 'description': 'Transfer to ' + transfer_category.category})
                transfer_category.amount += amount
                transfer_category.ledger.append({'amount': transfer_category.amount, 'description': 'Transfer from ' + self.category})
                return True
        else:
            return False

    def __repr__(self):
        titel = f'{self.category:*^30}' + '\n'
        budgetoutput = ''
        totalbudget = 'Total: ' + f'{self.amount:.2f}'
        for i in range(len(self.ledger)):
            spaces = 29 - len(self.ledger[i]['description'][:23])
            amount = self.ledger[i]['amount']
            famount = f'{amount:>{spaces}.2f}'
            xdescription = self.ledger[i]['description'][:23]
            budgetoutput += xdescription + ' ' + famount + '\n'
        return str(titel + budgetoutput + totalbudget)


def create_spend_chart(categories):
    category_names = []
    spent = []
    spent_percentages = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total -= item['amount']
        spent.append(round(total, 2))
        category_names.append(category)

    for amount in spent:
        spent_percentages.append(round(amount / sum(spent), 2)*100)

    dotplot = "Percentage spent by category\n"

    labels = range(100, -10, -10)

    for label in labels:
        dotplot += str(label).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= label:
                dotplot += "o  "
            else:
                dotplot += "   "
        dotplot += "\n"

    dotplot += "    ----" + ("---" * (len(category_names) - 1))
    dotplot += "\n     "

    longest_name_length = 13
    names = ['Business', 'Food', 'Entertainment']



    for i in range(longest_name_length):
        for name in names:
            if len(name) > i:
                dotplot += name[i] + "  "
            else:
                dotplot += "   "
        if i < longest_name_length-1:
            dotplot += "\n     "

    return (dotplot)
