def matchesPattern(s, pattern):
       patttern = pattern.lower()
   s = s.lower()
   
   if len(s)==len(pattern):
      for i in range(len(pattern)):
         if s[i] != pattern[i] and pattern[i] != '?':
            return False
            
      return True
   return False