# 00bc9fac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bc9fac",
  "name": "_ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc11d15c30ab1c3ca3836fa5312c9aabe5b9a32fdab81ccd5e18473ab0891829",
  "source_text_sha256": "bc11d15c30ab1c3ca3836fa5312c9aabe5b9a32fdab81ccd5e18473ab0891829"
}
~~~

## 呼び出し元

- [00c5d290](../00c5d/00c5d290.md)

## 呼び出し先

- [00b60d04](../00b60/00b60d04.md)

## 疑似コード / UTF-8 1104 bytes

~~~c

void _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev
               (long param_1)

{
  long *plVar1;
  code *UNRECOVERED_JUMPTABLE;
  
  if (*(char *)(param_1 + 0x40) == '\0') {
    *(undefined1 *)(param_1 + 0x40) = 1;
    if (*(long **)(param_1 + 0x30) == (long *)0x0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b60d04();
    }
    (**(code **)(**(long **)(param_1 + 0x30) + 0x30))();
  }
  plVar1 = *(long **)(param_1 + 0x30);
  if ((long *)(param_1 + 0x10) == plVar1) {
    UNRECOVERED_JUMPTABLE = *(code **)(*plVar1 + 0x20);
  }
  else {
                    /* catch() { ... } // from try @ 00bc9df8 with catch @ 00bc9ff0 */
    if (plVar1 == (long *)0x0) {
      return;
    }
                    /* catch() { ... } // from try @ 00bc9ef0 with catch @ 00bc9ff4 */
    UNRECOVERED_JUMPTABLE = *(code **)(*plVar1 + 0x28);
  }
                    /* WARNING: Could not recover jumptable at 0x00bca010. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (*UNRECOVERED_JUMPTABLE)();
  return;
}

~~~
