class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        carry=0
        alen=len(a)
        blen=len(b)
        ans=""
        i=0
        while(alen<i or blen>i or carry!=0):
            x=0
            y=0
            if(alen>i and a[alen-i-1]=='1'):
                x=1
            if(blen>i and b[blen-i-1]=='1'):
                y=1
            ans=str((x+y+carry)%2) +ans
            carry=(x+y+carry)//2
            i+=1
        return ans
        #Time limit exceed  ;(
        """
        
        ans=''
        carry=0
        a=a[::-1]
        b=b[::-1]
        for i in range(max(len(a),len(b))):
            if i<len(a):
                digitA=ord(a[i])-ord("0") 
            else:
                digitA=0
            if i<len(b):
                digitB=ord(b[i])-ord("0") 
            else:
                digitB=0
            total=digitA+digitB+carry
            char=str(total%2)
            ans=char+ans
            carry=total//2
        if carry:
            ans="1"+ans
        return ans