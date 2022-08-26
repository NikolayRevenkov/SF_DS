import numpy as np
number=np.random.randint(1,100)
count = 0
while True:
    count+=1
    predict_number=int(input('Ygaday chislo not 1 do 100'))
    
    if predict_number > number:
        print('Chislo dolzhno byt menshe')
    elif predict_number < number:
        print('Chyslo dolzhno byt bolshe')
        
    else:
        print('Vy ugadali')
        break