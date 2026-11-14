# 00bc5fbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bc5fbc",
  "name": "_ZN8firebase13remote_config8internal25EnsureInitializedCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "daf4995367100d2be558fc84dabd8182e6ca13a2f8746310ad59684107cccd05",
  "source_text_sha256": "daf4995367100d2be558fc84dabd8182e6ca13a2f8746310ad59684107cccd05"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bc60ec](../00bc6/00bc60ec.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5e970](../00c5e/00c5e970.md)

## 疑似コード / UTF-8 2047 bytes

~~~c

void _ZN8firebase13remote_config8internal25EnsureInitializedCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv
               (undefined8 param_1,long param_2,int param_3,undefined8 param_4,undefined8 *param_5)

{
  byte bVar1;
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  undefined8 uVar6;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined1 auStack_70 [16];
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  if ((param_2 != 0) && (param_3 == 0)) {
                    /* try { // try from 00bc5ff4 to 00cc5fff has its CatchHandler @ 00bc6504 */
    FUN_00bc60ec(param_1,param_2,&local_88);
  }
                    /* try { // try from 00bc6000 to 00cc6553 has its CatchHandler @ 00bc4ce4 */
  uVar6 = *param_5;
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_70,param_5 + 1);
  uStack_58 = uStack_80;
  local_60 = local_88;
  local_50 = local_78;
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_13remote_config10ConfigInfoEZNS0_26CompleteWithResultInternalIS3_EEvRKNS_12FutureHandleEiPKcRKT_EUlPS3_E_EEvS7_iS9_RKT0_
            (uVar6,auStack_70,param_3 != 0,param_4,&local_60);
  _ZN8firebase12FutureHandleD2Ev(auStack_70);
  pbVar5 = (byte *)param_5[4];
  if (pbVar5 != (byte *)0x0) {
    pbVar4 = (byte *)param_5[5];
    pbVar3 = pbVar5;
    if (pbVar4 != pbVar5) {
      bVar1 = pbVar4[-0x18];
      pbVar3 = pbVar4 + -0x18;
      while( true ) {
        if ((bVar1 & 1) != 0) {
          _ZdlPv(*(void **)(pbVar4 + -8));
        }
        if (pbVar5 == pbVar3) break;
        bVar1 = pbVar3[-0x18];
        pbVar4 = pbVar3;
        pbVar3 = pbVar3 + -0x18;
      }
      pbVar3 = (byte *)param_5[4];
    }
    param_5[5] = pbVar5;
    _ZdlPv(pbVar3);
  }
  _ZN8firebase12FutureHandleD2Ev(param_5 + 1);
  _ZdlPv(param_5);
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
