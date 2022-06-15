long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""


list = long_text.split('\n');
print(list)
name = list[1];
lei =  list[2];

point = long_text.count('.')
#print(point)
point_next = long_text.find('.')
FUND = long_text.find('FUND')
#point5 = point1;
#point6 = point2;


title = []
isin = []
sub_fund = []
sub = []
SUB = []
fu = []

#title 数组
for i in range(point):
    title.append(i)
    title[i] = long_text[point_next+1:FUND]
    point_next = long_text.find('.',point_next+1)
    FUND = long_text.find('FUND',FUND+1)
print(title)

point_next = long_text.find('.')
point_next = long_text.find('.',point_next+1)
FUND = long_text.find('FUND')
print(FUND)
for i in range(point):
    isin.append(i)
    isin[i] = long_text[FUND+1:point_next+1]
    point_next = long_text.find('.',point_next+1)
    FUND = long_text.find('FUND',FUND+1)
print(isin)
    
