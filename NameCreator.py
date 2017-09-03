#导入时间、系统、随机模块
import time,os,random
#导入翻译模块
from translate import Translator

#确定文字库
local=os.getcwd()+r'\words\\'

#定义 读取字库
def ReadWord(Location):
        origin=open(local+Location) #打开文件
        odata=origin.read() #读入数据
        fdata=odata.split() #分割
        origin.close()#关闭文件
        maxnum=len(fdata)#取得字符数
        return fdata,maxnum

#读入中文字库
FSTNAMES_CN = ReadWord(r'NAME_CN\Fstnames.txt')
WORDSb_CN = ReadWord(r'NAME_CN\word_b.txt')
WORDSg_CN = ReadWord(r'NAME_CN\word_g.txt')

#读入英文字库
FAMNAME_EN = ReadWord(r'NAME_EN\FamilyNames.txt')
GIVNAMEb_EN = ReadWord(r'NAME_EN\Givenname_b.txt')
GIVNAMEg_EN = ReadWord(r'NAME_EN\Givenname_g.txt')
NAMEb_EN = ReadWord(r'NAME_EN\Names_b.txt')
NAMEg_EN = ReadWord(r'NAME_EN\Names_g.txt')

#测试输出
a='''
--------------------------
NameMaker byRed_Cell

Test Output:

'''

b='''
--------------------------
'''

print(a)
print('CN:')
print(FSTNAMES_CN[0])
print(WORDSg_CN[0])
print(WORDSb_CN[0])

print(FSTNAMES_CN[1])
print(WORDSg_CN[1])
print(WORDSb_CN[1])

print('EN:')
print(FAMNAME_EN[0])
print(GIVNAMEb_EN[0])
print(GIVNAMEg_EN[0])
print(NAMEb_EN[0])
print(NAMEg_EN[0])

print(FAMNAME_EN[1])
print(GIVNAMEb_EN[1])
print(GIVNAMEg_EN[1])
print(NAMEg_EN[1])
print(NAMEg_EN[1])

print(b)
ver='''

目前版本 0.4
更新：
优化代码
增加英文字库

'''
print(ver)

input('按下回车键继续')

#开始主循环
while True:
        os.system('cls')
        #用户输入
        welcome='''
------------------------------
姓名随机生产器 byRed_Cell
一般是拿来写东西用的~ 原理纯随机
出来的名字可能有点怪=w=
------------------------------

        '''
        print(welcome)

        def CNname ():
                onamew=input('输入你要多少字的名字：')
                namew=int(int(onamew))
        
                FM=input('输入你需要的性别(F/M)：')

                FstName=input('输入你需要的姓氏(输入false使用随机姓氏)：')
                if FM=='F' or 'f':
                        words_fi=WORDSg_CN[0]
                        maxnum=WORDSg_CN[1]
                elif FM=='M' or 'm':
                        words_fi=WORDSb_CN[0]
                        maxnum=WORDSb_CN[1]
                
                print('生成中，请稍候...')

                if FstName=='false':
                        #确定姓氏
                        var=namew-1
                        fnn=random.randint(0,FSTNAMES_CN[1])
                        name=FSTNAMES_CN[0][fnn]
                
                else:
                        name=FstName
                        var=namew-1

                #确定名字
                while var>0:
                        num=random.randint(0,maxnum)
                        now=words_fi[num]
                        name+=now
                        var-=1
                else:
                        global tran
                        tran="无"
                        return name
                

        def ENname():
                FAMw=FAMNAME_EN[0]
                FAMmn=FAMNAME_EN[1]

                FM=input('输入你需要的性别(F/M)：')

                if FM=='F' or 'f':
                        words=NAMEg_EN[0]
                        wordmn=NAMEg_EN[1]

                        givw=GIVNAMEg_EN[0]
                        givmn=GIVNAMEg_EN[1]

                elif FM=='M' or 'm':
                        words=NAMEb_EN[0]
                        wordmn=NAMEb_EN[1]

                        givw=GIVNAMEb_EN[0]
                        givmn=GIVNAMEb_EN[1]
                
                

                NameEN=''

                print('生成中，请稍候...')

                #确定教名
                num=random.randint(0,givmn)
                NameEN+=givw[num]+' '
                #确定自取名
                num=random.randint(0,wordmn)
                NameEN+=words[num]+' '
                #确定姓
                num=random.randint(0,FAMmn)
                NameEN+=FAMw[num]
                global tran
                translator=Translator(to_lang="zh")
                tran=translator.translate(NameEN)
                return NameEN

        kind=input('输入你要生成名字的类型(CN/EN):')
        
        if kind=='CN':
                
                name=CNname()
        elif kind=='EN':
                
                name=ENname()
        

        #输出
        os.system('cls')
        print('结果是: '+name+'\n')
        print('翻译（参考）：'+tran+'\n')
        if input('是否退出(y/n)：')=='y' or 'Y':
                break
        else:
                pass

