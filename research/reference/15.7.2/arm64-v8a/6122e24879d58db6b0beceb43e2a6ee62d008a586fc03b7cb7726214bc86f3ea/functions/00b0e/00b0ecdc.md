# 00b0ecdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b0ecdc.md)

## 関数情報

~~~json
{
  "address": "00b0ecdc",
  "name": "std::__ndk1::operator+",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0b13a75ff25c625dcb912dbd5ec3382437d76fba30e8b3dec1e98f89220f4c0d",
  "source_text_sha256": "0b13a75ff25c625dcb912dbd5ec3382437d76fba30e8b3dec1e98f89220f4c0d"
}
~~~
## 呼び出し元

- [00bdb160](../00bdb/00bdb160.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 疑似コード 1/1 / UTF-8 1953 bytes

~~~c

/* std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >
   std::__ndk1::TEMPNAMEPLACEHOLDERVALUE(char const*, std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> > const&) */

void __thiscall std::__ndk1::operator+(__ndk1 *this,char *param_1,basic_string *param_2)

{
  ulong uVar1;
  byte bVar2;
  size_t __n;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *in_x8;
  char *pcVar3;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *__dest;
  ulong uVar4;
  
  *(undefined8 *)in_x8 = 0;
  *(undefined8 *)(in_x8 + 8) = 0;
  *(undefined8 *)(in_x8 + 0x10) = 0;
  __n = strlen((char *)this);
  bVar2 = *param_1;
  uVar1 = (ulong)(bVar2 >> 1);
  if ((bVar2 & 1) != 0) {
    uVar1 = *(ulong *)(param_1 + 8);
  }
  uVar4 = uVar1 + __n;
  if (uVar4 < 0xfffffffffffffff0) {
    if (uVar4 < 0x17) {
      __dest = in_x8 + 1;
      *in_x8 = SUB41((int)__n << 1,0);
    }
    else {
      uVar4 = uVar4 + 0x10 & 0xfffffffffffffff0;
                    /* catch() { ... } // from try @ 00b0ebec with catch @ 00b0ed58 */
      __dest = operator_new(uVar4);
      *(size_t *)(in_x8 + 8) = __n;
      *(basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> **)
       (in_x8 + 0x10) = __dest;
      *(ulong *)in_x8 = uVar4 | 1;
    }
    if (__n != 0) {
      memcpy(__dest,this,__n);
    }
    __dest[__n] = (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>)
                  0x0;
    pcVar3 = *(char **)(param_1 + 0x10);
    if ((bVar2 & 1) == 0) {
      pcVar3 = param_1 + 1;
    }
    basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::append
              (in_x8,pcVar3,uVar1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~
