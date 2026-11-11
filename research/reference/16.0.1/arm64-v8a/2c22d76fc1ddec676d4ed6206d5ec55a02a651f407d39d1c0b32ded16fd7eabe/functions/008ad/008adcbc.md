# 008adcbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "008adcbc",
  "name": "FUN_008adcbc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "769df90688d74d78c2c5fe3e722ec92f619257940795aae03a4cb1f8423297a3",
  "source_text_sha256": "769df90688d74d78c2c5fe3e722ec92f619257940795aae03a4cb1f8423297a3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 616 bytes

~~~c

long FUN_008adcbc(long param_1,long param_2)

{
                    /* catch() { ... } // from try @ 008ada2c with catch @ 008adcbc */
                    /* catch() { ... } // from try @ 008ada24 with catch @ 008adcc4 */
  param_1 = param_1 + 8;
                    /* catch() { ... } // from try @ 008ada80 with catch @ 008adccc */
  if (*(char **)(param_2 + 8) !=
      "ZZN17MyUtilityListener22nekokanBrowserFunctionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEENK3$_1clEN10NyankoClub6ResultEiEUlP9NewDialog20NewDialogChangeStateiE0_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
