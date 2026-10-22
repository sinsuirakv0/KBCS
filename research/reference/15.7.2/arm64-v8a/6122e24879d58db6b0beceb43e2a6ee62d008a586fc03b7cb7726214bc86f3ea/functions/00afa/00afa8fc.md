# 00afa8fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afa8fc.md)

## 関数情報

~~~json
{
  "address": "00afa8fc",
  "name": "FUN_00afa8fc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b35c7df91a89d05cc066a6b5c0469ff7561e426e69315a40be8aaef65077871c",
  "source_text_sha256": "b35c7df91a89d05cc066a6b5c0469ff7561e426e69315a40be8aaef65077871c"
}
~~~
## 呼び出し元

- [00af9e20](../00af9/00af9e20.md)
- [00afd380](../00afd/00afd380.md)
- [00afd444](../00afd/00afd444.md)
- [00b115bc](../00b11/00b115bc.md)
- [00b12714](../00b12/00b12714.md)
- [00b15764](../00b15/00b15764.md)
- [00b1e2cc](../00b1e/00b1e2cc.md)
- [00b4c3b8](../00b4c/00b4c3b8.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 疑似コード 1/1 / UTF-8 1757 bytes

~~~c

void FUN_00afa8fc(basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>
                  *param_1,byte *param_2,char *param_3)

{
  size_t sVar1;
  size_t __n;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *__dest;
  ulong uVar2;
  
  *(undefined8 *)param_1 = 0;
  *(undefined8 *)(param_1 + 8) = 0;
  *(undefined8 *)(param_1 + 0x10) = 0;
  if ((*param_2 & 1) == 0) {
    __n = (size_t)(*param_2 >> 1);
    sVar1 = strlen(param_3);
    param_2 = param_2 + 1;
  }
  else {
    __n = *(size_t *)(param_2 + 8);
    sVar1 = strlen(param_3);
    param_2 = *(byte **)(param_2 + 0x10);
  }
  uVar2 = __n + sVar1;
  if (uVar2 < 0xfffffffffffffff0) {
    if (uVar2 < 0x17) {
      __dest = param_1 + 1;
      *param_1 = SUB41((int)__n << 1,0);
                    /* try { // try from 00afa97c to 00bfa983 has its CatchHandler @ 00aff530 */
    }
    else {
      uVar2 = uVar2 + 0x10 & 0xfffffffffffffff0;
      __dest = operator_new(uVar2);
      *(size_t *)(param_1 + 8) = __n;
      *(basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> **)
       (param_1 + 0x10) = __dest;
      *(ulong *)param_1 = uVar2 | 1;
    }
    if (__n != 0) {
                    /* try { // try from 00afa9ac to 00bfa9bf has its CatchHandler @ 00aff520 */
      memcpy(__dest,param_2,__n);
    }
    __dest[__n] = (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>)
                  0x0;
    std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
    append(param_1,param_3,sVar1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~
