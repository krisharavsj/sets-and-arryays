list1=[1,2,3,4]
list2=['a','b','c','d']
list3=list(zip(list1,list2))
print(list3)
list4=[11,22,33,44]
list5=['aa','bb','cc','dd']
for x,y in zip(list4,list5[::-1]):
    print(x,y)
stocks=['reliance','infosys','techm']
prices=[2468,3746,2036]
dict={stocks:prices for stocks,prices in zip(stocks,prices)}
print(dict)