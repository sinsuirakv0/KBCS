# 00baeb9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baeb9c.md)

## 関数情報

~~~json
{
  "address": "00baeb9c",
  "name": "std::__ndk1::__codecvt_utf8_utf16<wchar_t>::do_max_length",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9660b8844cf5fb5a8dfdd87cd657fdfa1361c672a288da2e8048595b21d0e158",
  "source_text_sha256": "9660b8844cf5fb5a8dfdd87cd657fdfa1361c672a288da2e8048595b21d0e158"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 321 bytes

~~~c

/* std::__ndk1::__codecvt_utf8_utf16<wchar_t>::do_max_length() const */

undefined4 __thiscall
std::__ndk1::__codecvt_utf8_utf16<wchar_t>::do_max_length(__codecvt_utf8_utf16<wchar_t> *this)

{
  undefined4 uVar1;
  
  uVar1 = 4;
  if (((byte)this[0x20] & 4) != 0) {
    uVar1 = 7;
  }
  return uVar1;
}

~~~
