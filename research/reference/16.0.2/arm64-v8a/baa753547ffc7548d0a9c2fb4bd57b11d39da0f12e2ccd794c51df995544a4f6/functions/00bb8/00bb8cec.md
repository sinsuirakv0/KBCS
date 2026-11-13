# 00bb8cec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bb8cec",
  "name": "_ZN8firebase9messaging8ListenerD0Ev",
  "size": 4,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "589a890eaed62444dd43a46aeff65739d37ad6355e0a17d6a978ce76582cbd40",
  "source_text_sha256": "589a890eaed62444dd43a46aeff65739d37ad6355e0a17d6a978ce76582cbd40"
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
  pcVar1 = (code *)SoftwareBreakpoint(1,0xbb8cf0);
  (*pcVar1)();
}

~~~
