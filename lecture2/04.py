str1="JhonDipPeta"
str2="JaSonAy"
def mid_chars(str1,str2):
   length1,length2=len(str1),len(str2)
   mid1=length1//2
   mid2=length2//2
   mid_char1=str1[mid1-1:mid1+2]
   mid_char2=str2[mid2-1:mid2+2]
   return mid_char1,mid_char2
print("Результат для Case1,Case2:", mid_chars(str1,str2))