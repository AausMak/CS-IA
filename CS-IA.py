# CREATING REVOLUTIONARY APP FOR ACCOUNTING IN THE BUSINESS WORLD

# To find the compound intrest as a bascic calculation for the program

def ci () :
    p=int(input("Value of PRINCIPAL:",p))
    r=int(input("Value of RATE:",r))
    t=int(input("Value of TIME PERIOD:",t))
    
    a=p*(1+(r/100))**t

    ci=a-p

    print(ci)

    return ci()

ci(p,r,t)


# To find the net income of an individual or an organization

def NetIncome ():
    Income=int(input("Income:",Income))
    Expences=int(input("Expences:",Expences))

    NetIncome=Income-Expences

    print(NetIncome)

    return NetIncome()

NetIncome=(Income,Expences)


# To find if the balance sheet of a company is balanced i.e finding Assets of individual or company

def AccountingEquation () :
    Liabilities=int(input("Liabilities:",Liabilities))
    Equity=int(input("Equity:",Equity))

    AccountingEquation=Equity+Liabilities

    print(AccountingEquation)

    return(AccountingEquation)

AccountingEquation=(Liabilities,Assets)

# COGS formula Cost Of Goods Sold

def cogs () :
    BI=int(input("Beginning Inventory:",BI))
    PDP=int(input("Purchases Durning The Period",PDP))
    EI=int(input("Ending Inventory: ",EI))

    cogs=BI+PDP-EI

    print(cogs)

    return(cogs)

cogs=(BI,PDP,EI)


# Break Even Point formula when there is no profit no loss in a business. It determines the amount of products to be sold to break even point

def bep ():
    FC=int(input("Fixed Cost:",FC))
    SPPU=int(input("Sales Price Per Unit:",SPPU))
    VCPU=int(input("Variable Cost Per Unit:",VCPU))

    bep=FC/SPPU-VCPU

    print(bep)

    return(bep)

bep=(FC,SPPU,VCPU)

# To find the percentage of Return On Investment

def ROI () :
    Ig=int(input("Investment Gain:",Ig))
    Coi=int(input("Cost Of Investment:",Coi))

    ROI=((Ig-Coi)/Coi)*100

    print(ROI)

    return(ROI)

ROI=(Ig,Coi)

# Profit Margine

def ProfitM () :
    NetIncome=int(input("Net Income:",NetIncome))
    Revenue=int(input("Revenue:",Revenue))

    ProfitM=(NetIncome/Revenue)*100

    print(ProfitM)

    return(ProfitM)

ProfitM=(NetIncome,Revenue)

# Current Ratio is to find if you have more assets or liabilites

def CurrentRatio () :
    currentAssets=int(input("Current Assets:",currentAssets))
    currentLiabilites=int(input("Current Liabilites:",currentLiabilites))

    CurrentRatio=currentAssets/currentLiabilites

    print(CurrentRatio)

    return(CurrentRatio)

CurrentRatio=(currentLiabilites,currentAssets)

# Markup Formula

def MarkupFormula () :
    Revenue=int(input("Revenue:",Revenue))
    COGS=int(input("COGS:",COGS))

    MarkupFormula=((Revenue-COGS)/COGS)*100

    print(MarkupFormula)
    
    return(MarkupFormula)

MarkupFormula=(Revenue,COGS)

# Inventory Shrinkage Formula

def ISF () :
    RecordedInventor=int(input("Recored Inventory",RecordedInventor))
    ActualInventory=int(input("Actual Inventory",ActualInventory))

    ISF=((RecordedInventor-ActualInventory)/RecordedInventor)*100

    print(ISF)

    return(ISF)

ISF=(RecordedInventor,ActualInventory)

# SOURCCE OF INFORMATION :- https://www.patriotsoftware.com/blog/accounting/small-business-formulas/