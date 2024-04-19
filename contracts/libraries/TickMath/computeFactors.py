from decimal import *
getcontext().prec = 1000
# Source: https://www.geeksforgeeks.org/divide-large-number-represented-string/#

# Python3 program to implement division
# with large number
# This code is contributed by mits

import math

# A function to perform division of
# large numbers
def longDivision(number, divisor):

    # As result can be very large
    # store it in string
    ans = "";

    # Find prefix of number that
    # is larger than divisor.
    idx = 0;
    temp = ord(number[idx]) - ord('0');
    while (temp < divisor):
        temp = (temp * 10 + ord(number[idx + 1]) -
                            ord('0'));
        idx += 1;

    idx +=1;

    # Repeatedly divide divisor with temp.
    # After every division, update temp to
    # include one more digit.
    while ((len(number)) > idx):

        # Store result in answer i.e. temp / divisor
        ans += chr(math.floor(temp // divisor) + ord('0'));

        # Take next digit of number
        temp = ((temp % divisor) * 10 + ord(number[idx]) -
                                        ord('0'));
        idx += 1;

    ans += chr(math.floor(temp // divisor) + ord('0'));

    # If divisor is greater than number
    if (len(ans) == 0):
        return "0";

    # else return ans
    return ans;

# Base constants

sqrtBaseX256 = int(Decimal(10001).sqrt()*10**254) 
X256 = '0'*256
baseX256 = int('10001'+X256[:-4])

# sqrt(1.0001) ticks:

for i in range(21):
    A = str(int(2**128))
    for j in range(2**(i)):
        A = longDivision(A+X256, sqrtBaseX256)
    print(i, hex(int(A)))

'''
0 0xfffcb933bd6fad37aa2d162d1a594001
1 0xfff97272373d413259a46990580e2139
2 0xfff2e50f5f656932ef12357cf3c7fdca
3 0xffe5caca7e10e4e61c3624eaa0941ccd
4 0xffcb9843d60f6159c9db58835c92663e
5 0xff973b41fa98c081472e6896dfb254b2
6 0xff2ea16466c96a3843ec78b326b52843
7 0xfe5dee046a99a2a811c461f1969c301a
8 0xfcbe86c7900a88aedcffc83b479aa32d
9 0xf987a7253ac413176f2b074cf7815d68
10 0xf3392b0822b70005940c7a398e4b6f07
11 0xe7159475a2c29b7443b29c7fa6e8860a
12 0xd097f3bdfd2022b8845ad8f792aa50e7
13 0xa9f746462d870fdf8a65dc1f90e054d5
14 0x70d869a156d2a1b890bb3df62baf1d1c
15 0x31be135f97d08fd981231505542fb012
16 0x9aa508b5b7a84e1c677de54f3e97624
17 0x5d6af8dedb81196699c329225ebeee
18 0x2216e584f5fa1ea926041bedd7b2
19 0x48a170391f7dc42444e68d9
20 0x149b34ee7a9b73
'''


# 1.0001 base ticks:

for i in range(21):
    A = str(int(2**128))
    for j in range(2**(i)):
        A = longDivision(A+X256, baseX256)
    print(i, hex(int(A)))

'''
0 0xfff97272373d413259a46990580e2139
1 0xfff2e50f5f656932ef12357cf3c7fdca
2 0xffe5caca7e10e4e61c3624eaa0941ccd
3 0xffcb9843d60f6159c9db58835c92663e
4 0xff973b41fa98c081472e6896dfb254b6
5 0xff2ea16466c96a3843ec78b326b5284f
6 0xfe5dee046a99a2a811c461f1969c3032
7 0xfcbe86c7900a88aedcffc83b479aa363
8 0xf987a7253ac413176f2b074cf7815dd0
9 0xf3392b0822b70005940c7a398e4b6ff1
10 0xe7159475a2c29b7443b29c7fa6e887f2
11 0xd097f3bdfd2022b8845ad8f792aa548c
12 0xa9f746462d870fdf8a65dc1f90e05b52
13 0x70d869a156d2a1b890bb3df62baf27ff
14 0x31be135f97d08fd981231505542fbfe8
15 0x9aa508b5b7a84e1c677de54f3e988fe
16 0x5d6af8dedb81196699c329225ed28d
17 0x2216e584f5fa1ea926041bedeaf4
18 0x48a170391f7dc42444e7be7
19 0x149b34ee7aaee0
'''


