def removeWhite(s):
    s=s.replace(" ", "")
    s=s.replace("'", "")
    return s
def isPal(s):
 if len(s)>0: 
  if not s[0]==s[len(s)-1]:
   return False

 if len(s)<=1:
     return True;
 else:
     return isPal(s[1:-1]);

print isPal(removeWhite("x"))
print isPal(removeWhite("radar"))
print isPal(removeWhite("hello"))
print isPal(removeWhite(""))
print isPal(removeWhite("hannah"))
print isPal(removeWhite("madam i'm adam"))
