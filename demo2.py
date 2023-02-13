#if(0.3 == 0.1 +0.2):
#   print('yes');
#else:
#    print('no');

import decimal

a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
c = decimal.Decimal('0.3')
if(a +b ==c):
    print('yes');
else:
   print('no');

print("终于上传成功")