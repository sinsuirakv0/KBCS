# 00bddc0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bddc0c",
  "name": "_ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2efb92e33579282c34bc66ba1cd1eaae7e9ea8d34db6d0702dfd1548ffc1bd5e",
  "source_text_sha256": "2efb92e33579282c34bc66ba1cd1eaae7e9ea8d34db6d0702dfd1548ffc1bd5e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5edc0](../00c5e/00c5edc0.md)
- [00c5ee60](../00c5e/00c5ee60.md)

## 疑似コード / UTF-8 1419 bytes

~~~c

void _ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               void *param_5)

{
  int iVar1;
  long lVar2;
  int iVar3;
  long lVar4;
  undefined8 local_78;
  undefined1 local_70;
  void *local_68;
  undefined1 auStack_60 [20];
  undefined1 local_4c;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  local_4c = 0;
  iVar3 = _ZN8firebase4auth34MapFutureCallbackResultToAuthErrorEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPb
                    ();
  lVar4 = *(long *)((long)param_5 + 0x10);
  iVar1 = 0x3b;
  if (iVar3 != 7) {
    iVar1 = iVar3;
  }
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_60,param_5);
  local_70 = local_4c;
  local_78 = param_2;
  local_68 = param_5;
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_
            (lVar4 + 0x10,auStack_60,iVar1,param_4,&local_78);
  _ZN8firebase12FutureHandleD2Ev(auStack_60);
  _ZN8firebase12FutureHandleD2Ev(param_5);
  _ZdlPv(param_5);
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
