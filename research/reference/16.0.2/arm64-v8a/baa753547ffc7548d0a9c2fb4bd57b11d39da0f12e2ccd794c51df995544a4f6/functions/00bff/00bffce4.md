# 00bffce4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bffce4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sgetnEPwl",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83e4a0ea83a0c36edfa89a6d56dc29e760c12c9d64eee60109a084404c8e6a54",
  "source_text_sha256": "83e4a0ea83a0c36edfa89a6d56dc29e760c12c9d64eee60109a084404c8e6a54"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 298 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sgetnEPwl(long *param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bffcf0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0x40))();
  return;
}

~~~
