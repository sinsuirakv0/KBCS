# 004bfcdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "004bfcdc",
  "name": "_ZN5Botan14ECB_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm",
  "size": 580,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce0d5f745fa1c09427f52e70dd65c55b8c0ae4f3111b2cd0b59b4f299b9a719f",
  "source_text_sha256": "ce0d5f745fa1c09427f52e70dd65c55b8c0ae4f3111b2cd0b59b4f299b9a719f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0054084c](../00540/0054084c.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c58f90](../00c58/00c58f90.md)
- [00c58fb0](../00c58/00c58fb0.md)
- [00c59010](../00c59/00c59010.md)
- [00c596f0](../00c59/00c596f0.md)
- [00c597f0](../00c59/00c597f0.md)
- [00c59e60](../00c59/00c59e60.md)

## 関連文字列（未確認候補）

~~~text
"/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.3/Source/android_cpp/app/src/main/cpp/botan/botan_all.cpp"
"/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.3/Source/android_cpp/app/src/main/cpp/botan/botan_all.h"
": Ciphertext not a multiple of block size"
"Offset is sane"
"Offset ok"
"buffer.size() >= offset"
"finish"
"update"
~~~

## 疑似コード / UTF-8 3739 bytes

~~~c

void _ZN5Botan14ECB_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm
               (long *param_1,long *param_2,ulong param_3)

{
  long lVar1;
  ulong uVar2;
  long lVar3;
  long lVar4;
  undefined8 uVar5;
  undefined8 *puVar6;
  ulong uVar7;
  ulong uVar8;
  undefined1 auStack_78 [24];
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  lVar4 = *param_2;
  lVar3 = param_2[1];
  if ((ulong)(lVar3 - lVar4) < param_3) {
    if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
      _ZN5Botan17assertion_failureEPKcS1_S1_S1_i
                ("buffer.size() >= offset","Offset is sane","finish",
                 "/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.3/Source/android_cpp/app/src/main/cpp/botan/botan_all.cpp"
                 ,0x18a8);
    }
  }
  else {
    uVar2 = (**(code **)(*(long *)param_1[1] + 0x30))();
    uVar7 = (lVar3 - lVar4) - param_3;
    if (uVar7 != 0) {
      uVar8 = 0;
      if (uVar2 != 0) {
        uVar8 = uVar7 / uVar2;
      }
      if (uVar7 == uVar8 * uVar2) {
        uVar7 = param_2[1] - *param_2;
        if (uVar7 < param_3) {
          if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
            _ZN5Botan17assertion_failureEPKcS1_S1_S1_i
                      ("buffer.size() >= offset","Offset ok","update",
                       "/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.3/Source/android_cpp/app/src/main/cpp/botan/botan_all.h"
                       ,0x15e7);
          }
        }
        else {
          lVar3 = (**(code **)(*param_1 + 0x18))(param_1,*param_2 + param_3,uVar7 - param_3);
          lVar4 = param_2[1];
          param_3 = lVar3 + param_3;
          uVar7 = lVar4 - *param_2;
          if (param_3 < uVar7 || param_3 - uVar7 == 0) {
            if (param_3 < uVar7) {
              lVar4 = *param_2 + param_3;
              param_2[1] = lVar4;
            }
          }
          else {
            FUN_0054084c(param_2,param_3 - uVar7);
            lVar4 = param_2[1];
          }
          lVar4 = (**(code **)(*(long *)param_1[2] + 8))((long *)param_1[2],lVar4 - uVar2,uVar2);
          uVar8 = param_2[1] - *param_2;
          uVar7 = uVar8 + (lVar4 - uVar2);
          if (uVar8 < uVar7) {
            if (*(long *)(lVar1 + 0x28) == local_48) {
              FUN_0054084c(param_2);
              return;
            }
          }
          else {
            if (uVar8 != uVar7) {
              param_2[1] = *param_2 + uVar7;
            }
            if (*(long *)(lVar1 + 0x28) == local_48) {
              return;
            }
          }
        }
        goto LAB_004bff8c;
      }
    }
    uVar5 = __cxa_allocate_exception(0x20);
    _ZNK5Botan8ECB_Mode4nameEv(auStack_78,param_1);
    puVar6 = (undefined8 *)
             _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
                       (auStack_78,": Ciphertext not a multiple of block size");
    local_50 = puVar6[2];
    uStack_58 = puVar6[1];
    local_60 = *puVar6;
    puVar6[1] = 0;
    puVar6[2] = 0;
    *puVar6 = 0;
    _ZN5Botan14Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar5,&local_60);
    if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar5,PTR__ZTIN5Botan14Decoding_ErrorE_00c9bdf0,FUN_00535bc8);
    }
  }
LAB_004bff8c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
