import points
p1={ 'name' : 'Virat Kohli' , 'role' : 'bat' , 'runs' :112, '4' :10, '6' :0,
'balls' :119, 'field' :0}
p2={ 'name' : 'du Plessis' , 'role' : 'bat' , 'runs' :120, '4' :11, '6' :2,
'balls' :112, 'field' :0}
p3={ 'name' : 'Bhuvneshwar Kumar' , 'role' : 'bowl' , 'wkts' :1, 'overs' :10,
'runs' :71, 'field' :1}
p4={ 'name' : 'Yuzvendra Chahal' , 'role' : 'bowl' , 'wkts' :2, 'overs' :10,
'runs' :45, 'field' :0}
p5={ 'name' : 'Kuldeep Yadav' , 'role' : 'bowl' , 'wkts' :3, 'overs' :10, 'runs' :34,
'field' :0}
max=0
mom=''
for i in (p1,p2,p3,p4,p5):
    if i.get('role')=='bat':
        bat=points.batscore(i)
        if max<bat:
            max=bat
            mom=i.get('name')
        r={'name':i.get('name'),'batscore':bat}
        print(r)
    elif i.get('role')=='bowl':
        bowl=points.bowlscore(i)
        if max<bowl:
            max=bowl
            mom=i.get('name')
        r={'name':i.get('name'),'bowlscore':bowl}
        print(r)
    else:
        print('Incorrect data')
print('{} is Man of the Match with {} points'.format(mom,max))
