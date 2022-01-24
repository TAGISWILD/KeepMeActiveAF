from os import system
############################################################
f1=open("Num.txt","r")
currnum=f1.read()
curr_num=str(currnum)
nex_nUm=int(curr_num)+1
nex_num=str(nex_nUm)
text="# KeepMeActiveAF\nThis is commit no. "
f1.close()
############################################################
f2=open("Num.txt","w")
f3=open("README.md","w")
f4=open("hello.txt","w")
############################################################
f3.write(text+curr_num)
############################################################
f2.write(nex_num)
############################################################
f4.write(text+curr_num)
############################################################
############################################################
system("git add hello.txt")
system('git commit -m "This is commit no. '+curr_num+'"')
system("git push")

