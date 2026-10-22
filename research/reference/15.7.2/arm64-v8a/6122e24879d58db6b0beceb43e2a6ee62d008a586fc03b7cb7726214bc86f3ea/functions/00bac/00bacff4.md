# 00bacff4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bacff4.md)

## 関数情報

~~~json
{
  "address": "00bacff4",
  "name": "std::__ndk1::codecvt<char32_t,char8_t,mbstate_t>::do_length",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23b2fa342c39e716f200ece64786d41c6a7876c8b5c986c156d1ec36a3a844e4",
  "source_text_sha256": "23b2fa342c39e716f200ece64786d41c6a7876c8b5c986c156d1ec36a3a844e4"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bacc20](../00bac/00bacc20.md)

## 疑似コード 1/1 / UTF-8 512 bytes

~~~c

/* std::__ndk1::codecvt<char32_t, char8_t, mbstate_t>::do_length(mbstate_t&, char8_t const*, char8_t
   const*, unsigned long) const */

void __thiscall
std::__ndk1::codecvt<char32_t,char8_t,mbstate_t>::do_length
          (codecvt<char32_t,char8_t,mbstate_t> *this,mbstate_t *param_1,uchar *param_2,
          uchar *param_3,ulong param_4)

{
                    /* catch() { ... } // from try @ 00bace54 with catch @ 00bacff8 */
  FUN_00bacc20(param_2,param_3,param_4,0x10ffff,0);
  return;
}

~~~
