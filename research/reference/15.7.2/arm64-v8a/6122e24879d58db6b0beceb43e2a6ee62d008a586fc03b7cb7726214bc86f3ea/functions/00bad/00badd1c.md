# 00badd1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00badd1c.md)

## 関数情報

~~~json
{
  "address": "00badd1c",
  "name": "std::__ndk1::__codecvt_utf16<wchar_t,true>::do_max_length",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "50775ef6bd913125ef19f4baa1c6dce74ce15366d2d2c4282d284d48e4a1231c",
  "source_text_sha256": "50775ef6bd913125ef19f4baa1c6dce74ce15366d2d2c4282d284d48e4a1231c"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 322 bytes

~~~c

/* std::__ndk1::__codecvt_utf16<wchar_t, true>::do_max_length() const */

undefined4 __thiscall
std::__ndk1::__codecvt_utf16<wchar_t,true>::do_max_length(__codecvt_utf16<wchar_t,true> *this)

{
  undefined4 uVar1;
  
  uVar1 = 4;
  if (((byte)this[0x20] & 4) != 0) {
    uVar1 = 6;
  }
  return uVar1;
}

~~~
