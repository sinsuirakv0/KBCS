# 00bbd4fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bbd4fc",
  "name": "FUN_00bbd4fc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac5edd45d20957f33e04eb3fda0bc93f5ee7a911d2ea60af88b3df77e3f1fb3b",
  "source_text_sha256": "ac5edd45d20957f33e04eb3fda0bc93f5ee7a911d2ea60af88b3df77e3f1fb3b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ae70](../00c5a/00c5ae70.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5d340](../00c5d/00c5d340.md)

## 疑似コード / UTF-8 976 bytes

~~~c

void FUN_00bbd4fc(undefined8 param_1,undefined8 param_2,int param_3,undefined8 param_4,void *param_5
                 )

{
  long lVar1;
  undefined8 uVar2;
  undefined1 auStack_60 [16];
  undefined1 auStack_50 [8];
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  uVar2 = _ZN8firebase9messaging10FutureData3GetEv();
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_60,param_5);
                    /* try { // try from 00bbd554 to 00cbd59b has its CatchHandler @ 00bbd73c */
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
            (uVar2,auStack_60,(ulong)(param_3 != 0) << 2,param_4,auStack_50);
  _ZN8firebase12FutureHandleD2Ev(auStack_60);
  _ZN8firebase12FutureHandleD2Ev(param_5);
  _ZdlPv(param_5);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
