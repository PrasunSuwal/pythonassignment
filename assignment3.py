data=[]

for i in range (0,5):
    dataValue={"Name":"","DOB":""}
    dataValue["Name"]=str(input("Enter the Name:"))
    dataValue["DOB"]=str(input("Enter the DOB in yyyy/mm/dd format:"))
    data.append(dataValue)
search=str(input("Enter the DOB in yyyy/mm/dd format to search for:"))
found=0;
index=[];
for i in data:
    if(i["DOB"]==search):
        found=1
        index.append(data.index(i));

if(found):
    print("The people with Birthday on %s are:\n" %(search))
    for i in index:
        print("Name: %s "%(data[i]["Name"]))

else:
    print("Any DOB doesn't match with one entered above.");