#to check the string has same opening and closing bracket
#we match the similar brackets and remove it from the top of stack
Class solution:
  def isvalid(self,s):
    stack=[]
    #hash map to map closing with opening brackets
    closeToOpen={")":"(","}":"{","]":"["}
    #search over string->to build stack
    for char in s:
      #if the char in closing bracket
      if char in closeToOpen:
        #check stack is not empty and value of top is matching opening bracket
        if stack and stack[-1]==closeToOpen[c]:
          stack.pop()
        else:
          return False
     else:
      #append open parentesis
       stack.append(c)
        
  
  return True if not stack else false
    
