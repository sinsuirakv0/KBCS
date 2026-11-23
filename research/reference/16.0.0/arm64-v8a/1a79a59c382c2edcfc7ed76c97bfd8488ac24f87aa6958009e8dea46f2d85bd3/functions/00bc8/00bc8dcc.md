# 00bc8dcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b598cc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b598cc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0066.md#compare-983a1feff210698847fbdefb8f0fcc1c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc8dcc",
  "name": "_ZN8firebase13remote_config8internal20RemoteConfigInternal25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17RemoteConfigErrorEEEE",
  "size": 576,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e5a3f66648fccafb2bc3ecd6385e96bc59f649be4162cf30bdb1462c1ba42c9",
  "source_text_sha256": "1e5a3f66648fccafb2bc3ecd6385e96bc59f649be4162cf30bdb1462c1ba42c9"
}
~~~

## 呼び出し元

- [00c5d390](../00c5d/00c5d390.md)

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [005896b4](../00589/005896b4.md)
- [00bc9ba8](../00bc9/00bc9ba8.md)
- [00bc9bac](../00bc9/00bc9bac.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a800](../00c5a/00c5a800.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5d260](../00c5d/00c5d260.md)
- [00c5d280](../00c5d/00c5d280.md)

## 関連文字列（未確認候補）

~~~text
"!util::CheckAndClearJniExceptions(env)"
~~~

## 疑似コード / UTF-8 3081 bytes

~~~c

void _ZN8firebase13remote_config8internal20RemoteConfigInternal25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17RemoteConfigErrorEEEE
               (undefined8 param_1,undefined8 *param_2,long *param_3)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  undefined8 uVar4;
  ulong uVar5;
  undefined8 uVar6;
  long *plVar7;
  code *pcVar8;
  undefined **local_b0;
  undefined8 uStack_a8;
  long *local_90;
  long local_80 [4];
  long *local_60;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_2);
  lVar3 = _Znwm(0x30);
  plVar7 = (long *)param_3[4];
  if (plVar7 == (long *)0x0) {
    local_60 = (long *)0x0;
    *(undefined8 *)(lVar3 + 0x20) = 0;
  }
  else {
    if (param_3 == plVar7) {
      local_60 = local_80;
      (**(code **)(*plVar7 + 0x18))(plVar7,local_80);
    }
    else {
      local_60 = (long *)(**(code **)(*plVar7 + 0x10))(plVar7);
    }
    if (local_60 == (long *)0x0) {
      *(undefined8 *)(lVar3 + 0x20) = 0;
    }
    else {
      if (local_80 == local_60) {
        *(long *)(lVar3 + 0x20) = lVar3;
        (**(code **)(*local_60 + 0x18))(local_60,lVar3);
      }
      else {
        uVar4 = (**(code **)(*local_60 + 0x10))();
        *(undefined8 *)(lVar3 + 0x20) = uVar4;
      }
      if (local_80 == local_60) {
        pcVar8 = *(code **)(*local_60 + 0x20);
      }
      else {
        if (local_60 == (long *)0x0) goto LAB_00bc8ed4;
        pcVar8 = *(code **)(*local_60 + 0x28);
      }
      (*pcVar8)();
    }
  }
LAB_00bc8ed4:
  uVar4 = FUN_005896b4(plVar2,DAT_01126258,DAT_01126268,lVar3);
  uVar5 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
  if ((uVar5 & 1) != 0) {
    _ZN8firebase9LogAssertEPKcz("!util::CheckAndClearJniExceptions(env)");
  }
  uVar4 = FUN_004977f4(plVar2,param_2[0x33],DAT_01126110,uVar4);
  uVar5 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
  if ((uVar5 & 1) != 0) {
    _ZN8firebase9LogAssertEPKcz("!util::CheckAndClearJniExceptions(env)");
  }
  uVar6 = (**(code **)(*plVar2 + 0xa8))(plVar2,uVar4);
  (**(code **)(*plVar2 + 0xb8))(plVar2,uVar4);
  uVar4 = _Znwm(0x50);
  local_b0 = &PTR_FUN_00c91428;
  uStack_a8 = uVar6;
  local_90 = (long *)&local_b0;
  _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalC2EPNS1_20RemoteConfigInternalENSt6__ndk18functionIFvvEEE
            (uVar4,param_2,&local_b0);
  if (&local_b0 == (undefined ***)local_90) {
    pcVar8 = *(code **)(*local_90 + 0x20);
  }
  else {
    if (local_90 == (long *)0x0) goto LAB_00bc8fc0;
    pcVar8 = *(code **)(*local_90 + 0x28);
  }
  (*pcVar8)();
LAB_00bc8fc0:
  _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E(param_2 + 0x27,uVar4,FUN_00bc9570);
  _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1EPNS0_8internal40ConfigUpdateListenerRegistrationInternalE
            (param_1,uVar4);
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
