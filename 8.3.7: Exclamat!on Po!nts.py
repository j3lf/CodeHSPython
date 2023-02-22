# update this function so it replaces all lowercase 'i's in `text` with '!'

def exclamation(myStr):
   for i in range(len(myStr)):
       if myStr[i] == "i":
           s = list(myStr)
           s[i] = '!'
           myStr = "".join(s)
   return myStr
