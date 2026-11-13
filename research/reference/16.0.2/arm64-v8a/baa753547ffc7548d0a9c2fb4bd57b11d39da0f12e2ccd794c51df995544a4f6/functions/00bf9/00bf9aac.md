# 00bf9aac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bf9aac",
  "name": "_ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5cac8a2745ea7a00e46c3c8060bca9e60be786e48a4e49c1f283941c0870eb0",
  "source_text_sha256": "e5cac8a2745ea7a00e46c3c8060bca9e60be786e48a4e49c1f283941c0870eb0"
}
~~~

## 呼び出し元

- [00c58570](../00c58/00c58570.md)

## 呼び出し先

- [00c581c0](../00c58/00c581c0.md)
- [00c581f0](../00c58/00c581f0.md)
- [00c58550](../00c58/00c58550.md)

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
                    /* WARNING: Could not recover jumptable at 0x00bf9b28. Too many branches */
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
