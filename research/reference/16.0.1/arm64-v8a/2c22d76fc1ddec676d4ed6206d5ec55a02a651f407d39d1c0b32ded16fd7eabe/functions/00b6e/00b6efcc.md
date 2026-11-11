# 00b6efcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b6efcc",
  "name": "_ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e42bdacabc3da6933f4e5126fe43aa7b1ba20bbd3c7f038e5fba35d51fd2959",
  "source_text_sha256": "0e42bdacabc3da6933f4e5126fe43aa7b1ba20bbd3c7f038e5fba35d51fd2959"
}
~~~

## 呼び出し元

- [00c580b0](../00c58/00c580b0.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c58000](../00c58/00c58000.md)
- [00c5b140](../00c5b/00c5b140.md)

## 疑似コード / UTF-8 1242 bytes

~~~c

void _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
               (ulong *param_1,char *param_2,byte *param_3)

{
  ulong uVar1;
  byte bVar2;
  size_t __n;
  byte *pbVar3;
  void *__dest;
  ulong uVar4;
  
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  __n = strlen(param_2);
  bVar2 = *param_3;
  uVar1 = (ulong)(bVar2 >> 1);
  if ((bVar2 & 1) != 0) {
    uVar1 = *(ulong *)(param_3 + 8);
  }
  uVar4 = uVar1 + __n;
  if (uVar4 < 0xfffffffffffffff0) {
    if (uVar4 < 0x17) {
      __dest = (void *)((long)param_1 + 1);
      *(char *)param_1 = (char)((int)__n << 1);
    }
    else {
      uVar4 = uVar4 + 0x10 & 0xfffffffffffffff0;
      __dest = (void *)_Znwm(uVar4);
      param_1[1] = __n;
      param_1[2] = (ulong)__dest;
      *param_1 = uVar4 | 1;
    }
    if (__n != 0) {
      memcpy(__dest,param_2,__n);
    }
    *(undefined1 *)((long)__dest + __n) = 0;
    pbVar3 = *(byte **)(param_3 + 0x10);
    if ((bVar2 & 1) == 0) {
      pbVar3 = param_3 + 1;
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
              (param_1,pbVar3,uVar1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~
