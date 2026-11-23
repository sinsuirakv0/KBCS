# 00b5aaac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b5aa68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aa68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0012.md#compare-a7120a3431571ef3302bae0d09bc8a33)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
