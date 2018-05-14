# xoshiro256-seed
PRNG xoshiro256**, solve for seed  (http://xoshiro.di.unimi.it/)
```
> xo256.py ** 0xf198480 0xe39be180 0x1e29e004cb80 0x3fa1c745120a3807
#1 = sat  
seed = 0x0000000000000abc,000000000000abcd,00000000000abcde,0000000000abcdef  
0xf198480  
0xe39be180  
0x1e29e004cb80  
0x3fa1c745120a3807  
0x7ce99007a771c4a6  
0x12e5858634f12c53  
0x355d5c17b876cf1f  
0x3733339a76a24607  
0x5f4cf0739cc63df0  
0xdb5d6a756eee2d16    
  
#2 = unsat    
```
Doing the same with xoshiro256+  
Solving xoshiro256+ seed is MUCH HARDER  
And you can forget about proving UNIQUENESS ...
```
> xo256.py + 0xabd8ab 0x6cc4400000ab6cb3 0xb07b8d9888a17125 0x685d5610c943f25c  
#1 = sat  
seed = 0x0000000000000abc,000000000000abcd,00000000000abcde,0000000000abcdef  
0xabd8ab  
0x6cc4400000ab6cb3  
0xb07b8d9888a17125  
0x685d5610c943f25c  
0x464ab080cee33b63  
0x42ec9394c0da357  
0xb6cbc08f369e6cca  
0x9fc736b52f27617f  
0x6e305107082e9556  
0xf8d1bf5f35e6d3d3    
```
