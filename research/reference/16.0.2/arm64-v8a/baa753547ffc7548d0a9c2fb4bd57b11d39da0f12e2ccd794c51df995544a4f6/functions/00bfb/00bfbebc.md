# 00bfbebc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfbebc",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE7sungetcEv",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ccfd6d5436c691b2e9519442ddfd98d0e12000f38f1e017c2eb7a81f341a854",
  "source_text_sha256": "9ccfd6d5436c691b2e9519442ddfd98d0e12000f38f1e017c2eb7a81f341a854"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 488 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE7sungetcEv(long *param_1)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = param_1[3];
  if (param_1[2] != lVar1) {
    param_1[3] = lVar1 + -1;
    return (ulong)*(byte *)(lVar1 + -1);
  }
                    /* WARNING: Could not recover jumptable at 0x00bfbee8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x58))(param_1,0xffffffff);
  return uVar2;
}

~~~
