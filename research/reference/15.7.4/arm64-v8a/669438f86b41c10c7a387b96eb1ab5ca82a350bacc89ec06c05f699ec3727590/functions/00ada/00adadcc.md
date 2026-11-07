# 00adadcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00adacc0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adacc0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00adadcc",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8420b36aab70911f79586e3351ded4690dee6ba398feb690ebfb737747fd4c1",
  "source_text_sha256": "d8420b36aab70911f79586e3351ded4690dee6ba398feb690ebfb737747fd4c1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adba20](../00adb/00adba20.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

## 疑似コード / UTF-8 944 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_68 [16];
  void *local_58;
  byte local_50 [16];
  void *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_50,param_1,param_3);
  FUN_00566a7c(local_68,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adba20(&DAT_0109ff38,local_50);
  if ((puVar2 != &DAT_0109ff40) && (plVar3 = (long *)puVar2[0x12], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_50,local_68);
  }
  if ((local_68[0] & 1) != 0) {
    _ZdlPv(local_58);
  }
  if ((local_50[0] & 1) != 0) {
    _ZdlPv(local_40);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
