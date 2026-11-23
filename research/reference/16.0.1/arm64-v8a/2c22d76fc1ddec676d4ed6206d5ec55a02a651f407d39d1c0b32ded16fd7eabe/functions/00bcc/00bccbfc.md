# 00bccbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc7d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc7d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0010.md#compare-cd583bd2b3cdd95ccfeb4e94f236c043)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0090.md#compare-1b630de1dbf1878e9399e260b9255282)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccbfc",
  "name": "_ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a1986486adf9931b89021e7cdba390b8b2614e2f7fae751946c5cf176c97a209",
  "source_text_sha256": "a1986486adf9931b89021e7cdba390b8b2614e2f7fae751946c5cf176c97a209"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 309 bytes

~~~c

undefined8 _ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
                    /* try { // try from 00bccc30 to 00cccc3b has its CatchHandler @ 00bce900 */
  return (&DAT_01126800)[param_1];
}

~~~
