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
        
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]