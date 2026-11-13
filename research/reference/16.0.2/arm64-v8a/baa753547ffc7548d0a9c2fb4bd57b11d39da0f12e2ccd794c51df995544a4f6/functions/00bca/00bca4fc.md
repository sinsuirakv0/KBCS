# 00bca4fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bca4fc",
  "name": "_ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42dc68417f42122a5e1333b86d12283d26c0a14534288f0d5b3861bb373a807b",
  "source_text_sha256": "42dc68417f42122a5e1333b86d12283d26c0a14534288f0d5b3861bb373a807b"
}
~~~

## 呼び出し元

- [00c5d740](../00c5d/00c5d740.md)

## 呼び出し先

- [00b611c8](../00b61/00b611c8.md)

## 疑似コード / UTF-8 618 bytes

~~~c

void _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv
               (long param_1)

{
  long *plVar1;
  
  if (*(char *)(param_1 + 0x40) != '\0') {
    return;
  }
  plVar1 = *(long **)(param_1 + 0x30);
  *(undefined1 *)(param_1 + 0x40) = 1;
  if (plVar1 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00bca534. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*plVar1 + 0x30))(plVar1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00b611c8();
}

~~~
