# 00b0ecdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b0ecdc.md)

## 関数情報

~~~json
{
  "address": "00b0ecdc",
  "name": "_ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96cafc98461b2d9e58eda77306b8d3bc611b5a3f0735c90a4fed86aef0530462",
  "source_text_sha256": "96cafc98461b2d9e58eda77306b8d3bc611b5a3f0735c90a4fed86aef0530462"
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

## 疑似コード 1/1 / UTF-8 1329 bytes

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
                    /* catch() { ... } // from try @ 00b0ebec with catch @ 00b0ed58 */
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
