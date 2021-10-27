#CTF RTV DEFCON 29

#medium crack - 10

#The password is ThreatSims# plus 4 random digits ex: 

#String : ThreatSims#1234 

#Claudia:$6$2N2VK97xK5o1tWUF$ysoka7.ubAPVM2NoauRR8mzgZ3wjGDekbmImb5AnNSUkomb0/Pl775LMyvyHEJSasXpt8koYUz0sOuvPRfllA

Salt = "$6$2N2VK97xK5o1tWUF$"
UserHash = "$6$2N2VK97xK5o1tWUF$ysoka7.ubAPVM2NoauRR8mzgZ3wjGDekbmImb5AnNSUkomb0/Pl775LMyvyHEJSasXpt8koYUz0sOuvPRfllA"

f = open('workfile', 'w')

import crypt

fix = "ThreatSims#"
i = 0

for i in range(1000,10000):
	tmp = fix + str(i)
	hash = crypt.crypt(tmp, "$6$2N2VK97xK5o1tWUF$")
	f.write(hash + '\n' + str(i) + '\n')
f.close()

# Claudias Password is : ThreatSims#5596