s=str(input('Sirul este:'))
##a
print('numarul de aparitie ale caracterelor 'A' in sirul S', s.count('A')) 
##b
print('sirul obtinut prin substituirea caracterului 'A' in caracterul '*'', s.replace ('A','*'))
##c
s1=list(s)
s1.remove('B')
s1=''.join(s1)
print('radierea din 'S' a tuturor aparitiilor caracterelor 'B':' , 's1')
##d
print('numarul de aparitii ale silabei MA in sirul S', s.count('MA'))
##e
print('sirul obtinut prin substituirea tuturor aparitiilor in sirul S a silabei MA prin silaba TA's.replace('MA', 'TA'))
##f
s1=list(s)
s1.remove('TO'
s1=''.joim(s1)
print('sirul obtinut prin radierea din sirul 'S' a tuturor aparitiilor silabei 'TO':', 's1')
##g
print('scrierea inversa a sirului S', s[::-1])