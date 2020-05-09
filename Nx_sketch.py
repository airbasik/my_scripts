import os
import time

packfile = os.listdir() #чтение всех файлов в папке

for i in packfile:     #цикл по файлам в папке

    astr = str(i)      
    time.sleep(0.001)      #ибо слишком быстро, а так норм
    if '.txt' in astr:    #учитывает расширение файла
        one_file = open(astr, 'r+')                            #открыть файл .txt
        astr2 = astr.replace('.txt', '.dat')                   #изменить расширение
        two_file = open(astr2, 'w')                        #открыть файл .dat
        
        for j in one_file:                                   #читает строку из файла
            alist = str(j)                                  #перевод элемента в строку
            alist = alist.strip('\n') + '0' + '\n'       #составленеи новой строки(координат)
            two_file.write(alist)                   #запись в .dat файл
            
            
        one_file.close()    
        two_file.close()  
        
    else:
        pass
print('!!!ВЫПОЛНЕНО!!!')
    
        
        
        
        
        



            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

    
    