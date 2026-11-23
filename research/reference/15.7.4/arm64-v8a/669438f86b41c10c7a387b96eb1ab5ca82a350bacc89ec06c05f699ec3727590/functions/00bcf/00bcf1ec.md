# 00bcf1ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcf1a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf1a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0018.md#compare-9ecf0d50d62fa741bbaeff774cf861d4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcf1ec",
  "name": "FUN_00bcf1ec",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17b59d3062aff8f6cf15e132823076dbc82d962ff73f13d0288683c51c407e24",
  "source_text_sha256": "17b59d3062aff8f6cf15e132823076dbc82d962ff73f13d0288683c51c407e24"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
"operator\"\" "
~~~

## 疑似コード / UTF-8 1908 bytes

~~~c

void FUN_00bcf1ec(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  char *pcVar2;
  void *__ptr;
  long lVar3;
  size_t __size;
  long *plVar4;
  
  lVar3 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 0xbU) {
    __size = param_2[2] * 2;
    uVar1 = lVar3 + 0x3eb;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
                    /* catch() { ... } // from try @ 00bcf01c with catch @ 00bcf248 */
                    /* catch() { ... } // from try @ 00bcf00c with catch @ 00bcf24c */
  pcVar2 = (char *)((long)__ptr + lVar3);
                    /* catch() { ... } // from try @ 00bcf000 with catch @ 00bcf250 */
                    /* catch() { ... } // from try @ 00bcefc8 with catch @ 00bcf254 */
                    /* catch() { ... } // from try @ 00bceeb0 with catch @ 00bcf258 */
  *(undefined8 *)pcVar2 = s_operator___002ab3aa._0_8_;
  pcVar2[7] = 'r';
  pcVar2[8] = '\"';
  pcVar2[9] = '\"';
  pcVar2[10] = ' ';
  plVar4 = *(long **)(param_1 + 0x10);
  lVar3 = *plVar4;
  param_2[1] = param_2[1] + 0xb;
  (**(code **)(lVar3 + 0x20))(plVar4,param_2);
                    /* catch() { ... } // from try @ 00bceea0 with catch @ 00bcf28c */
  if ((*(ushort *)((long)plVar4 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* catch() { ... } // from try @ 00bcee94 with catch @ 00bcf2ac */
                    /* catch() { ... } // from try @ 00bcedd4 with catch @ 00bcf2c0 */
                    /* WARNING: Could not recover jumptable at 0x00bcf2c4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar4 + 0x28))(plVar4,param_2);
  return;
}

~~~
