import csv


data = ['id','name','model','price']
#with open('step.csv','w') as File:
    #writer= csv.writer(File)
    #writer.writerows(data)
    
with open('dz.csv','w') as myfile:
    fieldNames = ['id','name','model','price']
    writer =csv.DictWriter(myfile,fieldnames=fieldNames)
    writer.writerows([{'id':'1','name':'Apple','model':'iPhone 11 128GB Black','price':'339 990 тг.'}])
    
    writer.writerows([{'id':'2','name':'Apple','model':'iPhone 13 256GB Midnight','price':'539 990 тг.'}])
    
    writer.writerows([{'id':'3','name':'Apple','model':'iPhone 12 64GB Black','price':'404 990 тг.'}])
    
    writer.writerows([{'id':'4','name':' Samsung','model':'Galaxy A32 128GB Black','price':'139 990 тг.'}])
    
    writer.writerows([{'id':'5','name':'Samsung','model':'Galaxy S20 FE 128GB Blue','price':'279 990 тг.'}])
    
    writer.writerows([{'id':'6','name':'Xiaomi','model':'Redmi 9A 32GB Grey','price':'48 990 тг.'}])
    
    writer.writerows([{'id':'7','name':'Xiaomi','model':'Redmi Note 10S 64GB Onyx Gray','price':'89 990 тг.'}])
    
    writer.writerows([{'id':'8','name':'HUAWEI','model':'P Smart 2021 128GB Green','price':'99 990 тг.'}])
    
    writer.writerows([{'id':'9','name':'HUAWEI','model':'nova 8i 128GB Звездное небо','price':'169 990 тг.'}])
    
    writer.writerows([{'id':'10','name':'HUAWEI','model':'Y5p 32GB Midnight Black','price':'49 990 тг.'}])