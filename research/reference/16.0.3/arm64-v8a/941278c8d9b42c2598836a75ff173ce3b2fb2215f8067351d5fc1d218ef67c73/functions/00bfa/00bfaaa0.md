# 00bfaaa0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfaaa0",
  "name": "_ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dbd1d9ab0bd02154146a73b796c31062cd3920d51f86cdc185027ab5c2ce3b67",
  "source_text_sha256": "dbd1d9ab0bd02154146a73b796c31062cd3920d51f86cdc185027ab5c2ce3b67"
}
~~~

## 呼び出し元

- [00c59540](../00c59/00c59540.md)

## 呼び出し先

- [00c59190](../00c59/00c59190.md)
- [00c591c0](../00c59/00c591c0.md)
- [00c59520](../00c59/00c59520.md)

## 関連文字列（未確認候補）

~~~text
"unique_lock::unlock: not locked"
~~~

## 疑似コード / UTF-8 1079 bytes

~~~c

void _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE
               (long *param_1,undefined8 *param_2)

{
  uint uVar1;
  byte bVar2;
  long lVar3;
  
  uVar1 = *(uint *)(param_1 + 0xe);
  if ((uVar1 >> 2 & 1) == 0) {
    if ((uVar1 >> 3 & 1) != 0) {
      bVar2 = *(byte *)(param_2 + 1);
      *(uint *)(param_1 + 0xe) = uVar1 & 0xfffffff3;
      if ((bVar2 & 1) != 0) {
        _ZNSt6__ndk15mutex6unlockEv(*param_2);
        lVar3 = *param_1;
        *(undefined1 *)(param_2 + 1) = 0;
                    /* WARNING: Could not recover jumptable at 0x00bfab1c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
        (**(code **)(lVar3 + 0x18))(param_1);
        return;
      }
                    /* WARNING: Subroutine does not return */
      _ZNSt6__ndk120__throw_system_errorEiPKc(1,"unique_lock::unlock: not locked");
    }
    do {
      _ZNSt6__ndk118condition_variable4waitERNS_11unique_lockINS_5mutexEEE(param_1 + 8,param_2);
    } while ((*(byte *)(param_1 + 0xe) >> 2 & 1) == 0);
  }
  return;
}

~~~
