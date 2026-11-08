# 00b4aacc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b4aacc",
  "name": "_ZN8firebase9messaging8ListenerD0Ev",
  "size": 4,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "94e4874a269b85fc633496f1807c826674f3cfb29102af0282fe7a1a26b9f9cc",
  "source_text_sha256": "94e4874a269b85fc633496f1807c826674f3cfb29102af0282fe7a1a26b9f9cc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 190 bytes

~~~c

void _ZN8firebase9messaging8ListenerD0Ev(void)

{
  code *pcVar1;
  
                    /* WARNING: Does not return */
  pcVar1 = (code *)SoftwareBreakpoint(1,0xb4aad0);
  (*pcVar1)();
}

~~~
