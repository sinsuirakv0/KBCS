# 00bccab0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc688`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc688.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0010.md#compare-f898c60c92fca50b7187c14582ee65b3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0090.md#compare-a775bfa83135a0e75e33fba3769e691c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccab0",
  "name": "_ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aa4fe6ee52d09f6b77e21829b53d3ebe57246e852263bcd5067a03f062af32cb",
  "source_text_sha256": "aa4fe6ee52d09f6b77e21829b53d3ebe57246e852263bcd5067a03f062af32cb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af60](../00c5a/00c5af60.md)

## 疑似コード / UTF-8 681 bytes

~~~c

bool _ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_011267f8 == '\0') {
                    /* try { // try from 00bccaf0 to 00cccb07 has its CatchHandler @ 00bce908 */
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_011267f0,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_011267f8 = iVar2 == 0;
                    /* try { // try from 00bccb08 to 00cccbbb has its CatchHandler @ 00bcc5d0 */
    bVar1 = (bool)DAT_011267f8;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
