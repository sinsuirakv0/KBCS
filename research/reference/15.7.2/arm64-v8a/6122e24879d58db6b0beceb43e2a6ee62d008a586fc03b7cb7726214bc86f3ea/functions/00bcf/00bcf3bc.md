# 00bcf3bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bcf3bc.md)

## 関数情報

~~~json
{
  "address": "00bcf3bc",
  "name": "FUN_00bcf3bc",
  "size": 440,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eea658ef7c87f14f5bb0b566bf4d59a38f6c150c535697edbe8bc8daf5d6fe8b",
  "source_text_sha256": "eea658ef7c87f14f5bb0b566bf4d59a38f6c150c535697edbe8bc8daf5d6fe8b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb090](../00bbb/00bbb090.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 関連文字列（未確認候補）

~~~text
"%s:%d: %s"
"basic_iostream"
"basic_istream"
"basic_ostream"
"basic_string"
"out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h"
~~~
## 疑似コード 1/1 / UTF-8 2445 bytes

~~~c

void FUN_00bcf3bc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  int iVar2;
  void *pvVar3;
  size_t __size;
  long lVar4;
  size_t sVar5;
  char *pcVar6;
  
                    /* catch() { ... } // from try @ 00bcf5a8 with catch @ 00bcf3cc */
  lVar4 = param_2[1];
  pvVar3 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar4 + 5U) {
    sVar5 = param_2[2] * 2;
    uVar1 = lVar4 + 0x3e5;
    if (sVar5 < uVar1 || sVar5 - uVar1 == 0) {
      sVar5 = uVar1;
    }
    param_2[2] = sVar5;
    pvVar3 = realloc(pvVar3,sVar5);
    *param_2 = pvVar3;
    if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar4 = param_2[1];
  }
  *(undefined1 *)((undefined4 *)((long)pvVar3 + lVar4) + 1) = 0x3a;
  *(undefined4 *)((long)pvVar3 + lVar4) = 0x3a647473;
  iVar2 = *(int *)(param_1 + 0xc);
  lVar4 = param_2[1] + 5;
  param_2[1] = lVar4;
  if (iVar2 < 3) {
    if (iVar2 == 0) {
      pcVar6 = "allocator";
      sVar5 = 9;
      goto LAB_00bcf4e4;
    }
    if (iVar2 == 1) {
      pcVar6 = "basic_string";
      sVar5 = 0xc;
      goto LAB_00bcf4e4;
    }
    pcVar6 = "basic_string";
    sVar5 = 6;
  }
  else if (iVar2 == 3) {
    pcVar6 = "basic_istream";
    sVar5 = 7;
  }
  else if (iVar2 == 4) {
    pcVar6 = "basic_ostream";
    sVar5 = 7;
  }
  else {
    pcVar6 = "basic_iostream";
    sVar5 = 8;
  }
  if (*(int *)pcVar6 != 0x69736162 || (short)*(int *)((long)pcVar6 + 4) != 0x5f63) {
                    /* WARNING: Subroutine does not return */
    FUN_00bbb090("%s:%d: %s","out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h",0x6a9,
                 &DAT_002967d9);
  }
  pcVar6 = (char *)((long)pcVar6 + 6);
LAB_00bcf4e4:
  pvVar3 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar4 + sVar5) {
    __size = param_2[2] * 2;
    uVar1 = lVar4 + sVar5 + 0x3e0;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    pvVar3 = realloc(pvVar3,__size);
    *param_2 = pvVar3;
    if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar4 = param_2[1];
  }
                    /* try { // try from 00bcf520 to 00ccf5a7 has its CatchHandler @ 00bcf68c */
  memcpy((void *)((long)pvVar3 + lVar4),pcVar6,sVar5);
  param_2[1] = param_2[1] + sVar5;
  return;
}

~~~
