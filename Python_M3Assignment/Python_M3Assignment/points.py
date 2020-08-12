'''Module with functions for calculating batscore or bowlscore using dictionary object of performance of a single player'''
def batscore(p):
    if p.get('role')=='bat':
        r=int(p.get('runs'))
        s=r//2+(r//100)*10+((r%100)//50)*5
        sr=(r/int(p.get('balls')))*100
        if sr>=80 and sr<=100:
            s=s+2
        elif sr>100:
            s=s+4
        s=s+int(p.get('4'))+2*int(p.get('6'))
        return s
    else:
        print('not applicable for batscore')
def bowlscore(p):
    if p.get('role')=='bowl':
        w=int(p.get('wkts'))
        s=10*w
        if w>=5:
            s=s+10
        elif w>=3 and w<5:
            s=s+5
        er=int(p.get('runs'))/int(p.get('overs'))
        if er<2:
            s=s+10
        elif er>=2 and er<=3.5:
            s=s+7
        elif er>3.5 and er<=4.5:
            s=s+4
        s=s+10*int(p.get('field'))
        return s
    else:
        print('not applicable for bowlscore')
