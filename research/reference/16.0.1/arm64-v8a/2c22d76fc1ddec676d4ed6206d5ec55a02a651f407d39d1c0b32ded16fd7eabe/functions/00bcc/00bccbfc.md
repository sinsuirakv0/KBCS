# 00bccbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

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
