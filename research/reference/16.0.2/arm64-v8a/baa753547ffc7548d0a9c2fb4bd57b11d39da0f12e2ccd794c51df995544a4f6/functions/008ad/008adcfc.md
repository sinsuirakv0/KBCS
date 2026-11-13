# 008adcfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "008adcfc",
  "name": "FUN_008adcfc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "345df020bc030b8ab885af8bd77b9106d7af12cfb4e0724872318798bbffc7c3",
  "source_text_sha256": "345df020bc030b8ab885af8bd77b9106d7af12cfb4e0724872318798bbffc7c3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b91d0](../008b9/008b91d0.md)

## 疑似コード / UTF-8 242 bytes

~~~c

void FUN_008adcfc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
                    /* catch() { ... } // from try @ 008adb3c with catch @ 008add00 */
  if (*param_3 == 2) {
    FUN_008b91d0(*param_2);
    return;
  }
  return;
}

~~~
