# Problem Set 4
# Name: Protik Bose Pranto
# Collaborators: Protik bose Pranto
# Time: 11.30 AM ( GMT +6)

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # TODO: Your code here.

    salary=abs(float(salary))
    save=abs(float(save))

    if save > 100: return "Save should be less than 100"
    if growthRate > 100: return "growth rate should be less than 100"

    lst=[]
    lst.append(salary * save * .01)  #first year fund

    for year in range(years-1):
      lst.append(lst[year] * (1 + .01 * growthRate) + salary * save * .01 )  #second to last year fund
    
    return lst

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.
    print(nestEggFixed(500000, 20, 5, 20))
    print(nestEggFixed(5000000, 30, 2, 40))
    print(nestEggFixed(400000, 130, 3, 5))
    print(nestEggFixed(5000000, 10, 3, 3))
    print(nestEggFixed(400000,5, 5, 36))

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    salary=abs(float(salary))
    save=abs(float(save))

    if save > 100: return "Save should be less than 100"
    #if growthRates > 100: return "growth rate should be less than 100"

    lst=[]
    lst.append(salary * save * .01)  #first year fund

    for year in range(1,len(growthRates)):
      lst.append(lst[year-1] * (1 + .01 * growthRates[year]) + salary * save * .01 )  #second to last year fund
    
    return lst


def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.
    print(nestEggVariable(500000, 20, growthRates))
    print(nestEggVariable(5000000, 30, growthRates))
    print(nestEggVariable(400000, 130, growthRates))
    print(nestEggVariable(5000000, 10, growthRates))
    print(nestEggVariable(400000,5, growthRates))
#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    savings=abs(float(savings))
    #save=abs(float(save))

    #if save > 100: return "Save should be less than 100"
    #if growthRates > 100: return "growth rate should be less than 100"

    lst=[]
    lst.append(savings * (1 + .01 * growthRates[0]) -expenses)  #first year fund

    for year in range(1,len(growthRates)):
      lst.append(lst[year-1] * (1 + .01 * growthRates[year]) -expenses )  #second to last year fund
    
    return lst

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.
    print(postRetirement(500000,growthRates,3000))
    print(postRetirement(5000000, growthRates,20000))
    print(postRetirement(400000, growthRates,10000))
    print(postRetirement(5000000, growthRates,4000))
    print(postRetirement(400000,growthRates,30000))

'''
#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
    '''

#testNestEggFixed()
#testNestEggVariable()
testPostRetirement()