def busytask_print(a) :
        print('<오늘의 할 일>')
        sa = ''
        for i in a :
            if( i in busy ) :
                sa += i + '     **급합!!** ' + '\n'
        return sa


def taskforP_print(a) :
        sa = ''
        for i in a :
            if( i in task ) :
                sa += i + '\n'
        return sa


def taskforJ_print(a) :
        print('<오늘의 할 일>')
        for i in range(len(a)) :
            for j in range(len(a[i])) :
                print(a[i][j], end = '')
            print('\n')


    

#MBTI 맞춤 스케쥴러

mbti = input('MBTI를 대문자로 입력해주세요.  ')[3:4]

if(mbti == 'P') :
    task = []
    busy = []

    sum = 0
    flag = 0

    time = 24 - int(input('평균 수면 시간을 입력해주세요.   '))



    #할 일 입력받기
    while(1) :      
        a = input('할 일을 입력해주세요.  ')
        b = int(input('예상 소요 시간을 시간 단위로 입력해주세요.  '))
        c = input('급한 일인가요? 예, 아니오로 답해주세요.   ')
        if(c != '예' and c != '아니오') :
            print('입력 오류입니다. 처음부터 다시 입력해주세요.')
            continue

        if(flag == 0) :
            sum += b
            if(sum > time) :
                answer = input('이 일을 추가하면 수면 시간이 줄어듭니다. 수면 시간을 줄이시겠습니까? 예, 아니오로 답해주세요.   ')
                if(answer == '아니오') :
                    print('스케줄 조정 후, 해당 스케줄부터 다시 입력해주세요.')
            
                    print(busytask_print(busy))
                    print(taskforP_print(task))
                    
                    continue
                else :
                    print('수면 시간을 고려하지 않는 모드로 전환됩니다.')
                    flag = 1
                    
        if(c == '예') :
            busy.append(a)
            
        else :
            task.append(a)

        add = input('스케줄을 더 추가하시겠습니까? 예, 아니오로 답해주세요.  ')
        if(add == '아니오') :
            break
        else :
            continue
    
                
    #할 일 출력하기
    
    print(busytask_print(busy))
    print(taskforP_print(task))
    



#J 스케줄러
if(mbti == 'J') :
        
    task = [ ['0시 ', ''],
            ['1시 ', ''],
            ['2시 ', ''],
            ['3시 ', ''],
            ['4시 ', ''],
            ['5시 ', ''],
            ['6시 ', ''],
            ['7시 ', ''],
            ['8시 ', ''],
            ['9시 ', ''],
            ['10시 ', ''],
            ['11시 ', ''],
            ['12시 ', ''],
            ['13시 ', ''],
            ['14시 ', ''],
            ['15시 ', ''],
            ['16시 ', ''],
            ['17시 ', ''],
            ['18시 ', ''],
            ['19시 ', ''],
            ['20시 ', ''],
            ['21시 ', ''],
            ['22시 ', ''],
            ['23시 ', ''] ]

    
    #할 일 입력받기
    while(1) :      
        a = input('할 일을 입력해주세요.  ')
        b = int(input('시작 시간을 입력해주세요.   '))
        c = int(input('예상 소요 시간을 시간 단위로 입력해주세요.  '))
        
        found = 0
        for i in range (b, b + c) :
            if(task[i][1] != '') :
                found = 1
                break
            

        if(found == 0) :
            for i in range (b, b + c) :
                task[i][1] = a


        else :
            print('이미 계획된 스케줄이 있습니다. 스케줄 조정 후, 해당 스케줄부터 다시 입력해주세요.')
            print(taskforJ_print(task))
            continue

        add = input('스케줄을 더 추가하시겠습니까? 예, 아니오로 답해주세요.  ')
        if(add == '아니오') :
                break
                
        else :
            continue


        #할 일 출력하기
    print(taskforJ_print(task))

    

            
        
