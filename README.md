# One_Time_Pad_Helper
 
Helper tool to help decode messages encoded using a 'one time pad', where the one time pad is used more than once to encode messages. 
Initially used to help decode a COMP6441 module activity given then following encoded messages

```
LpaGbbfctNiPvwdbjnPuqolhhtygWhEuafjlirfPxxl

WdafvnbcDymxeeulWOtpoofnilwngLhblUfecvqAxs

UijMltDjeumxUnbiKstvdrVhcoDasUlrvDypegublg

LpaAlrhGmjikgjdmLlcsnnYmIsoPcglaGtKeQcemiu

LpaDohqcOzVbglebjPdTnoTzbyRbuwGftflTliPiqp

```
Commands avaliable: 

\+ <letter 1> <letter 2> : adds two letter together (plaintext + key = cipher text)

\- <letter 1> <letter 2> : subtracts letter 2 from letter 1 (cipher text - plain text = key)

add <letter> : adds letter to overall key and computes plaintext for all given messages
 
print : prints current state of key (the one time pad)
