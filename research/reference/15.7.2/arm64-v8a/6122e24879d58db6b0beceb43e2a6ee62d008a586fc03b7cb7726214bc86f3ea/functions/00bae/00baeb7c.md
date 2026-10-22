# 00baeb7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baeb7c.md)

## 関数情報

~~~json
{
  "address": "00baeb7c",
  "name": "std::__ndk1::__codecvt_utf8_utf16<wchar_t>::do_length",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df2558e1217e8870d8a2ee9bc197616142a663e0431271073677b20459ce9edd",
  "source_text_sha256": "df2558e1217e8870d8a2ee9bc197616142a663e0431271073677b20459ce9edd"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bac2fc](../00bac/00bac2fc.md)

## 疑似コード 1/1 / UTF-8 541 bytes

~~~c

/* std::__ndk1::__codecvt_utf8_utf16<wchar_t>::do_length(mbstate_t&, char const*, char const*,
   unsigned long) const */

void __thiscall
std::__ndk1::__codecvt_utf8_utf16<wchar_t>::do_length
          (__codecvt_utf8_utf16<wchar_t> *this,mbstate_t *param_1,char *param_2,char *param_3,
          ulong param_4)

{
                    /* try { // try from 00baeb80 to 00caebd7 has its CatchHandler @ 00baeab8 */
  FUN_00bac2fc(param_2,param_3,param_4,*(undefined8 *)(this + 0x18),*(undefined4 *)(this + 0x20));
  return;
}

~~~
