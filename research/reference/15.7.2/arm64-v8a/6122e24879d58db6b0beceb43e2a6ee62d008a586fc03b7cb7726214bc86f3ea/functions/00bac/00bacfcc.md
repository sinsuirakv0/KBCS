# 00bacfcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bacfcc.md)

## 関数情報

~~~json
{
  "address": "00bacfcc",
  "name": "std::__ndk1::codecvt<char32_t,char8_t,mbstate_t>::do_unshift",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4366e9b0222de0642b42794fe63ca3411bf46c519541fcb553ab82d42298c38b",
  "source_text_sha256": "4366e9b0222de0642b42794fe63ca3411bf46c519541fcb553ab82d42298c38b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 390 bytes

~~~c

/* std::__ndk1::codecvt<char32_t, char8_t, mbstate_t>::do_unshift(mbstate_t&, char8_t*, char8_t*,
   char8_t*&) const */

undefined8 __thiscall
std::__ndk1::codecvt<char32_t,char8_t,mbstate_t>::do_unshift
          (codecvt<char32_t,char8_t,mbstate_t> *this,mbstate_t *param_1,uchar *param_2,
          uchar *param_3,uchar **param_4)

{
  *param_4 = param_2;
  return 3;
}

~~~
