#!/usr/bin/python3
#-*-coding:utf-8-*-
import sys

portl = {"21":"FTP",
      "22":"SSH",
      "23":"TELNET",
      "25":"SMTP",
      "53":"DNS",
      "80":"WEB SERVER",
      "110":"POP3",
      "115":"SFTP",
      "135":"RPC",
      "139":"NetBIOS",
      "143":"IMAP",
      "194":"IRC",
      "443":"SSL",
      "445":"SMB",
      "1433":"MSSQL",
      "3306":"MySQL",
      "3389":"Remote Desktop",
      "5632":"PCAnywhere",
      "5900":"VNC",
      "6112":"Warcraft III",
    }
d1 = sys.argv
list = []
for i in d1:
	list.append(i)
try:
	d2 = str(list[1])
	print(portl[d2])

except (IndexError, NameError, KeyError):
	print("kullanım:python3  ps.py 21")
