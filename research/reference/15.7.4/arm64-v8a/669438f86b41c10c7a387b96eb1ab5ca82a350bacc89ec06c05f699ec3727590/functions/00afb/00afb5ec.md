# 00afb5ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afb5a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb5a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0008.md#compare-f29ca06f9be7f6ca5e853fd75979c761)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb5ec",
  "name": "_ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "249303df8d695d249fe860e2ad2c86c58b79d88d9de964987ccc208df50de769",
  "source_text_sha256": "249303df8d695d249fe860e2ad2c86c58b79d88d9de964987ccc208df50de769"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb090](../00bdb/00bdb090.md)

## 疑似コード / UTF-8 1201 bytes

~~~c

void _ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list
               (long *param_1,int param_2,undefined8 param_3,undefined8 *param_4)

{
  long lVar1;
  int iVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 uStack_50;
  undefined8 uStack_48;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar6 = param_4[1];
  uVar5 = *param_4;
                    /* try { // try from 00afb618 to 00bfb61f has its CatchHandler @ 00aff4c0 */
  uVar4 = param_4[3];
  uVar3 = param_4[2];
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 <= param_2) {
                    /* try { // try from 00afb648 to 00bfb65f has its CatchHandler @ 00aff4bc */
    local_60 = uVar5;
    uStack_58 = uVar6;
    uStack_50 = uVar3;
    uStack_48 = uVar4;
    (**(code **)(*param_1 + 0x20))(param_1,param_2,param_3,&local_60);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00afb670 to 00bfb677 has its CatchHandler @ 00aff4b8 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
