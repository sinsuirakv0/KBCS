# 00baecfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baecfc.md)

## 関数情報

~~~json
{
  "address": "00baecfc",
  "name": "std::__ndk1::__codecvt_utf8_utf16<char32_t>::do_out",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f027e9646a61c102d4bebb7bb1256636e84f553bb38561a2951a536829c3102",
  "source_text_sha256": "9f027e9646a61c102d4bebb7bb1256636e84f553bb38561a2951a536829c3102"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bae630](../00bae/00bae630.md)

## 疑似コード 1/1 / UTF-8 1070 bytes

~~~c

/* std::__ndk1::__codecvt_utf8_utf16<char32_t>::do_out(mbstate_t&, char32_t const*, char32_t const*,
   char32_t const*&, char*, char*, char*&) const */

void __thiscall
std::__ndk1::__codecvt_utf8_utf16<char32_t>::do_out
          (__codecvt_utf8_utf16<char32_t> *this,mbstate_t *param_1,wchar32 *param_2,wchar32 *param_3
          ,wchar32 **param_4,char *param_5,char *param_6,char **param_7)

{
  char *local_30;
  wchar32 *pwStack_28;
  
                    /* catch() { ... } // from try @ 00baec60 with catch @ 00baed18 */
                    /* catch() { ... } // from try @ 00baec54 with catch @ 00baed30 */
  local_30 = param_5;
  pwStack_28 = param_2;
                    /* catch() { ... } // from try @ 00baec28 with catch @ 00baed48 */
  FUN_00bae630(param_2,param_3,&pwStack_28,param_5,param_6,&local_30,*(undefined8 *)(this + 0x10),
               *(undefined4 *)(this + 0x18));
  *param_4 = pwStack_28;
  *param_7 = local_30;
                    /* catch() { ... } // from try @ 00baebfc with catch @ 00baed58 */
  return;
}

~~~
