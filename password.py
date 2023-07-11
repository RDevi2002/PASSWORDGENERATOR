l, u, p, d = 0, 0, 0, 0
s = input("Enter your password: ")
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_#%^&*()[\]{}|;:></?"
digits="0123456789"
if (len(s) >= 8):
	for i in s: #tHink@567 i=7

		# counting lowercase alphabets
		if (i in smallalphabets): # 6 in 
			l+=1	#l=4	

		# counting uppercase alphabets
		elif (i in capitalalphabets): # 5 in 
			u+=1	 # u = 1

		# counting digits
		elif (i in digits): # 5 in
			d+=1	#d = 3	
		# counting the mentioned special characters
		elif(i in specialchar): # @ in
			p+=1 #p = 1	
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
	print("Valid Password")
	print("small alphabets are",l)
	print("capital alphabets are",u)
	print("digits are",d)
	print("special characters are",p)
else:
	print("Invalid Password")
