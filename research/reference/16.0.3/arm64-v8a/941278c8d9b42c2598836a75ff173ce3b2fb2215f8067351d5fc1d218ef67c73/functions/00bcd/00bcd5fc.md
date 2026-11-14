# 00bcd5fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcd5fc",
  "name": "_ZN8firebase4auth4auth11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a5983696bb4e8680ac2b075f1a03802ad7733ff143fef46bc64d4c9b42f41657",
  "source_text_sha256": "a5983696bb4e8680ac2b075f1a03802ad7733ff143fef46bc64d4c9b42f41657"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5c0a0](../00c5c/00c5c0a0.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 2404 bytes

~~~c

undefined8 _ZN8firebase4auth4auth11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0x11 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
                    /* try { // try from 00bcd634 to 00ccd79b has its CatchHandler @ 00bcd634
                       catch() { ... } // from try @ 00bcd634 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcd7c0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcd828 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcd904 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcd9d0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdaa0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdb6c with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdc38 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdca0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdd7c with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcde48 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdf0c with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdfdc with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce0f8 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce1d0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce3a0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce468 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce5c8 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce97c with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcec20 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcef18 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcf024 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcf124 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcf234 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcf2a0 with catch @ 00bcd634 */
  return (&DAT_011277f8)[param_1];
}

~~~
