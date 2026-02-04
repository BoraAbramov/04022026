
age = 20

qustion: bool = age > 18 #מאחסן בתא זיכרון את התשובה
qustion: bool = age > 18 #eager

print(qustion)

age = 16
print(age > 20) #lazy
#נותן את התשובה בחישוב עכשיו ולא שומר אותה לפני כמו בeager
