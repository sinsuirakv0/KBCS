# 00b7edec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b7edec",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE9pubsetbufEPcl",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f444a1a5e475a91a7e37d15151e190ef68c0c3899630207cad78c77a3c43d5a4",
  "source_text_sha256": "f444a1a5e475a91a7e37d15151e190ef68c0c3899630207cad78c77a3c43d5a4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 302 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE9pubsetbufEPcl(long *param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00b7edf8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0x18))();
  return;
}

~~~
