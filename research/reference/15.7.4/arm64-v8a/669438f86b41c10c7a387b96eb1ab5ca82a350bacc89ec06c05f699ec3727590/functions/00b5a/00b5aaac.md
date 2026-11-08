# 00b5aaac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00b5aaac",
  "name": "_ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "51bada066e8c19e9ff377a53625919d7f937b3306eeaad2de633beb3a567c73e",
  "source_text_sha256": "51bada066e8c19e9ff377a53625919d7f937b3306eeaad2de633beb3a567c73e"
}
~~~

## 呼び出し元

- [00be06b0](../00be0/00be06b0.md)

## 呼び出し先

- [00b010ec](../00b01/00b010ec.md)

## 疑似コード / UTF-8 1027 bytes

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
      FUN_00b010ec();
    }
    (**(code **)(**(long **)(param_1 + 0x30) + 0x30))();
  }
                    /* try { // try from 00b5aae0 to 00c5ac0b has its CatchHandler @ 00b5af44 */
  plVar1 = *(long **)(param_1 + 0x30);
  if ((long *)(param_1 + 0x10) == plVar1) {
    UNRECOVERED_JUMPTABLE = *(code **)(*plVar1 + 0x20);
  }
  else {
    if (plVar1 == (long *)0x0) {
      return;
    }
    UNRECOVERED_JUMPTABLE = *(code **)(*plVar1 + 0x28);
  }
                    /* WARNING: Could not recover jumptable at 0x00b5ab10. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (*UNRECOVERED_JUMPTABLE)();
  return;
}

~~~
