# 00adb7ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adb7ac.md)

## 関数情報

~~~json
{
  "address": "00adb7ac",
  "name": "FUN_00adb7ac",
  "size": 356,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6319c43dee4443249ef844c7acf848427878d49162dbbeef958dbb97ff1246f2",
  "source_text_sha256": "6319c43dee4443249ef844c7acf848427878d49162dbbeef958dbb97ff1246f2"
}
~~~
## 呼び出し元

- [00ada4e4](../00ada/00ada4e4.md)
- [00ada6ac](../00ada/00ada6ac.md)

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 2646 bytes

~~~c

void FUN_00adb7ac(long *param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long local_60 [5];
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (param_2 != param_1) {
    plVar2 = (long *)param_1[4];
    plVar3 = (long *)param_2[4];
    if (plVar2 == param_1) {
      if (plVar3 == param_2) {
        (**(code **)(*param_1 + 0x18))(param_1,local_60);
                    /* catch() { ... } // from try @ 00adb00c with catch @ 00adb884 */
                    /* catch() { ... } // from try @ 00adb254 with catch @ 00adb88c */
        (**(code **)(*(long *)param_1[4] + 0x20))();
        param_1[4] = 0;
                    /* catch() { ... } // from try @ 00adb26c with catch @ 00adb894 */
        (**(code **)(*(long *)param_2[4] + 0x18))((long *)param_2[4],param_1);
        (**(code **)(*(long *)param_2[4] + 0x20))();
                    /* catch() { ... } // from try @ 00adb1d0 with catch @ 00adb8bc */
        param_2[4] = 0;
                    /* catch() { ... } // from try @ 00adb1b0 with catch @ 00adb8c0 */
        param_1[4] = (long)param_1;
                    /* catch() { ... } // from try @ 00adb188 with catch @ 00adb8c4 */
        (**(code **)(local_60[0] + 0x18))(local_60,param_2);
                    /* catch() { ... } // from try @ 00adb65c with catch @ 00adb8dc */
                    /* catch() { ... } // from try @ 00adb4f4 with catch @ 00adb8e0 */
        (**(code **)(local_60[0] + 0x20))(local_60);
      }
      else {
        (**(code **)(*param_1 + 0x18))(param_1,param_2);
        (**(code **)(*(long *)param_1[4] + 0x20))();
        param_1[4] = param_2[4];
      }
                    /* catch() { ... } // from try @ 00adb4c0 with catch @ 00adb8e4 */
      param_2[4] = (long)param_2;
    }
    else if (plVar3 == param_2) {
      (**(code **)(*param_2 + 0x18))(param_2,param_1);
      (**(code **)(*(long *)param_2[4] + 0x20))();
      param_2[4] = param_1[4];
      param_1[4] = (long)param_1;
    }
    else {
      param_1[4] = (long)plVar3;
      param_2[4] = (long)plVar2;
    }
  }
                    /* catch() { ... } // from try @ 00adb4b4 with catch @ 00adb8e8 */
                    /* catch() { ... } // from try @ 00adb0c4 with catch @ 00adb8ec */
                    /* catch() { ... } // from try @ 00adb0cc with catch @ 00adb8f4 */
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* catch() { ... } // from try @ 00adb0d8 with catch @ 00adb904 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
