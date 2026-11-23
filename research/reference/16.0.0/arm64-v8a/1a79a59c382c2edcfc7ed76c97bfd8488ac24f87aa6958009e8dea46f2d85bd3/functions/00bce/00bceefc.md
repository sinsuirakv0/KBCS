# 00bceefc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5f9fc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f9fc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0067.md#compare-a4686213eb7a61ab76b00497d6cae27c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bceefc",
  "name": "_ZN8firebase4auth4Auth17set_language_codeEPKc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cebe7eb3785ec2225abda950424c3a756037a2bc3d7d652dfbb633934c693884",
  "source_text_sha256": "cebe7eb3785ec2225abda950424c3a756037a2bc3d7d652dfbb633934c693884"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00574cac](../00574/00574cac.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)

## 疑似コード / UTF-8 1051 bytes

~~~c

void _ZN8firebase4auth4Auth17set_language_codeEPKc(long *param_1,long param_2)

{
  long *plVar1;
  long lVar2;
  
  if ((undefined8 *)*param_1 != (undefined8 *)0x0) {
    plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
    lVar2 = 0;
    if (param_2 != 0) {
      lVar2 = (**(code **)(*plVar1 + 0x538))(plVar1,param_2);
    }
    FUN_00574cac(plVar1,*(undefined8 *)(*param_1 + 0x1f8),DAT_01126350,lVar2);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
    if (lVar2 != 0) {
                    /* try { // try from 00bcef7c to 00ccef83 has its CatchHandler @ 00bcef84 */
                    /* catch() { ... } // from try @ 00bcef7c with catch @ 00bcef84
                       try { // try from 00bcef84 to 00ccefbb has its CatchHandler @ 00bcec24 */
                    /* WARNING: Could not recover jumptable at 0x00bcef88. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar1 + 0xb8))(plVar1,lVar2);
      return;
    }
  }
  return;
}

~~~
