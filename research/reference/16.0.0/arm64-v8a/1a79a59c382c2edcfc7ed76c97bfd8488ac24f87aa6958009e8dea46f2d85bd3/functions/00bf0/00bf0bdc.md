# 00bf0bdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bf0bdc",
  "name": "FUN_00bf0bdc",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e2bc01d9c5124797aebb75c51676b5b72926918da20f3a041a0a40123b90cc1",
  "source_text_sha256": "9e2bc01d9c5124797aebb75c51676b5b72926918da20f3a041a0a40123b90cc1"
}
~~~

## 呼び出し元

- [00bf0ea4](../00bf0/00bf0ea4.md)

## 呼び出し先

- [0043b724](../0043b/0043b724.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57b40](../00c57/00c57b40.md)

## 疑似コード / UTF-8 1326 bytes

~~~c

void FUN_00bf0bdc(ulong *param_1,ulong param_2,ulong param_3,long param_4,size_t param_5,
                 long param_6,long param_7)

{
  ulong uVar1;
  size_t __n;
  void *__dest;
  byte *__src;
  ulong uVar2;
  
  if (param_3 <= -param_2 - 9) {
    __src = (byte *)param_1[2];
    if ((*param_1 & 1) == 0) {
      __src = (byte *)((long)param_1 + 1);
    }
    if (param_2 < 0x7ffffffffffffff3) {
      uVar1 = param_3 + param_2;
      if (param_3 + param_2 <= param_2 * 2) {
        uVar1 = param_2 * 2;
      }
      if (uVar1 < 0x17) {
        uVar2 = 0x17;
      }
      else {
        uVar2 = (uVar1 & 0xfffffffffffffff8) + 8;
        if ((uVar1 | 7) != 0x17) {
          uVar2 = uVar1 | 7;
        }
        uVar2 = uVar2 + 1;
      }
    }
    else {
      uVar2 = 0xfffffffffffffff7;
    }
    __dest = (void *)_Znwm(uVar2);
    if (param_5 != 0) {
      memmove(__dest,__src,param_5);
    }
    __n = param_4 - (param_6 + param_5);
    if (__n != 0) {
      memmove((void *)((long)__dest + param_7 + param_5),__src + param_6 + param_5,__n);
    }
    if (param_2 != 0x16) {
      _ZdlPv(__src);
    }
    *param_1 = uVar2 | 1;
    param_1[1] = (param_4 - param_6) + param_7;
    param_1[2] = (ulong)__dest;
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0043b724(param_1);
}

~~~
