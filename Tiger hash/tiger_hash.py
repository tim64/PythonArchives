from sboxes import t1, t2, t3, t4

a = 0x0123456789ABCDEF
b = 0xFEDCBA9876543210
c = 0xF096A5B4C3B2E187

table = [0]*1024
t1 = table
t2 = table[0:256]
t3 = table[256:512]
t4 = table[512:1024]

print t4



def tiger_round(a,b,c,x,mul):
      c ^= x
      a -= t1_1 ^ t2_2 ^ t3_3 ^ t4_4
      b += t4_1 ^ t3_3 ^ t2[c_5] ^ t1[c_7]
      b *= mul

def tiger_key_schedule():
    x0 -= x7 ^ 0xA5A5A5A5A5A5A5A5
    x1 ^= x0
    x2 += x1
    x3 -= x2 ^ ((~x1)<<19)
    x4 ^= x3
    x5 += x4
    x6 -= x5 ^ ((~x4)>>23)
    x7 ^= x6
    x0 += x7
    x1 -= x0 ^ ((~x7)<<19)
    x2 ^= x1
    x3 += x2
    x4 -= x3 ^ ((~x2)>>23)
    x5 ^= x4
    x6 += x5
    x7 -= x6 ^ 0x0123456789ABCDEF

def tiger_pass(a,b,c,mul):
      tiger_round(a,b,c,x0,mul)
      tiger_round(b,c,a,x1,mul)
      tiger_round(c,a,b,x2,mul)
      tiger_round(a,b,c,x3,mul)
      tiger_round(b,c,a,x4,mul)
      tiger_round(c,a,b,x5,mul)
      tiger_round(a,b,c,x6,mul)
      tiger_round(b,c,a,x7,mul)


def tiger_feedforward():
     a ^= aa
     b -= bb
     c += cc

def tiger_save_abc():
    aa = a
    bb = b
    cc = c
'''
def tiger_compress():
    tiger_save_abc
    for(pass_no=0; pass_no<PASSES; pass_no++) { \
        if(pass_no != 0) {key_schedule} \
	pass(a,b,c,(pass_no==0?5:pass_no==1?7:9)); \
	tmpa=a; a=c; c=b; b=tmpa;} \
      feedforward
'''