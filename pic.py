import web
import os
import sys
import web     
import json   
urls = (
    '/pic', 'pic',
    '/piclist','piclist',
    '/idselect','idselect',
    '/uploadimg','uploadimg'
)
app = web.application(urls, globals())
def pic_list():
    list1=[]
    id=0

    for filename in os.listdir(r'/usr/local/pictures'):
    # for filename in os.listdir(r'C:\Users\ceuilisa\Desktop\pic'):
    # for filename in os.listdir(r'/Users/leo/Desktop/xiaoluoli/'):
        # data={"id":str(id),"name":'C://Users//ceuilisa//Desktop//pic//'+filename}
        data={"id":str(id),"name":'http://104.129.180.80:8082/pic?id='+filename}
        print data
        id=id+1
        list1.append(data)
    return json.dumps(list1)

class uploadimg():
    def POST(self):
        x = web.input(myfile={})
        filename=x.myfile.filename
        print 'filename:',filename
        # print x.myfile.file.read()
        # filedir = '/Users/leo/Desktop/companydoc/leo' 
        filedir='/usr/local/pictures/'
        # if 'myfile' in x: 
            # filepath=x.myfile.filename.replace('\\','/') 
            # filename=filepath.split('/')[-1] 
        # filename=x.filename
        fout = open(filedir +'/'+ filename,'w') 
        fout.write(x.myfile.file.read()) 
        fout.close() 
        print 'bobi'
        return "upload success84"
        # else:
        #     return "failed"










# class idselect:
#     def GET(self):
#         list2=[]
#         try:
#             i=str(web.input().id.encode("utf-8"))
#         except:
#             return "please input id"
#         a=pic_list()
#         print(a)
#         for a1 in a:
#             print "a1",a1
            # if(a1.has_key(i)):
            #     print("yes")
            #     name='/Users/leo/Desktop/xiaoluoli/'+a1[int(i)]
            #     # name='/usr/local/pictures/'+a[i]
            #     # name='C:\Users\ceuilisa\Desktop\pic\'+a1[i]
            #     print(name)
            #     f= open(name,'rb')
            #     r=f.read()
            #     data={str(i):r}
            #     list2.append(data)
            #     return list2
            # else:
            #     print("no")
            #     return "do not exist pic"
        



def pic_1(k):
    d={}
    try:
        # name='C://Users//ceuilisa//Desktop//pic//'+str(k)+'.jpg'
        # name='/Users/leo/Desktop/xiaoluoli/'+str(k)+'.jpg'
        name='/usr/local/pictures/'+str(k)
        print(name)
        f= open(name,'rb')
        r=f.read()
        return r
    except:
        return "you input number has no pic return"

class pic:        
    def GET(self):
        try:
            i=str(web.input().id.encode("utf-8"))
        except:
            return "please input id"
        img=pic_1(i)
        return img

class piclist:        
    def GET(self):
        d=pic_list()
        print d
        return d
      


if __name__ == "__main__":
    app.run()