import  pickle  #数据持久性模块

mylist = [1,2,3,4,5,"sunck is a good man"]
path = r"C:\Users\Zhangyadi\Desktop\56fil6.txt"
f = open(path,"wb")
       #写入--dump
pickle.dump(mylist,f)
f.close()

#读取

f1 = open(path,"rb")
templist=pickle.load(f1)
print(templist)
f1.close()


