# 00befff8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00befff8",
  "name": "_ZNSt6__ndk114__shared_countD0Ev",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d71f2a8a8a70d2a3eb28624ed9179837b0d7ac3f151a5c182405f628e3e24ab6",
  "source_text_sha256": "d71f2a8a8a70d2a3eb28624ed9179837b0d7ac3f151a5c182405f628e3e24ab6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 187 bytes

~~~c

void _ZNSt6__ndk114__shared_countD0Ev(void)

{
  code *pcVar1;
  
                    /* WARNING: Does not return */
  pcVar1 = (code *)SoftwareBreakpoint(1,0xbf0000);
  (*pcVar1)();
}

~~~
