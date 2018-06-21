class Solution:
    arr = [" ","start","E","T","I","A","N","M","S","U","R","W","D","K","G","O","H","V","F","Ü","L"," ","P","J","B","X","C","Y","Z","Q","Ç","İ","5","4","$","3","?","_",".","2",",",":","+",";","*","%","#","1","6","=","/","Ş","ğ","ö","&","8","7","9","0"]
    str = ".-- .. - .... .-.- -- -.-- .-.- -... . ... - .-.- .-- .. ... .... . ... **/"
    strToWords = str.split(" ");
    
    curIndex = 1;
    word = []
 
    def morseToChars(arr,strToWords,curIndex,word):
        for i in range(0,len(strToWords)-1):
           #print (len(strToWords))
           for j in range(0,len(strToWords[i])):
                if(strToWords[i][j]== '.'):
                    curIndex = curIndex * 2;
                elif(strToWords[i][j]== '-'):
                    curIndex = (curIndex * 2 + 1);
                else:
                    print('Invalid Morse Code at the %d th position of the code array'%(i+1)*(j+1) 
           )
           word.append(arr[curIndex])
           
           curIndex = 1;
            

 
    morseToChars(arr,strToWords,curIndex,word)
    print(word)


 