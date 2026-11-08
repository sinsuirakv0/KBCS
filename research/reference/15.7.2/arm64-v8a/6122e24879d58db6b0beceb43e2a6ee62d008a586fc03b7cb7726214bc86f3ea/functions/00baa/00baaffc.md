# 00baaffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00baaffc",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE8do_widenEPKcS3_Pw",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5ce9b6b7f60c7d13ae8ef74d181f690fca85bf61b872dbf43e6688bd2a43789",
  "source_text_sha256": "c5ce9b6b7f60c7d13ae8ef74d181f690fca85bf61b872dbf43e6688bd2a43789"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a00](../00be1/00be1a00.md)

## 疑似コード / UTF-8 566 bytes

~~~c

byte * _ZNKSt6__ndk112ctype_bynameIwE8do_widenEPKcS3_Pw
                 (long param_1,byte *param_2,byte *param_3,wint_t *param_4)

{
  byte bVar1;
  byte *pbVar2;
  wint_t wVar3;
  __locale_t __dataset;
  
  pbVar2 = param_2;
  for (; param_2 != param_3; param_2 = param_2 + 1) {
    bVar1 = *param_2;
    __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
    wVar3 = btowc((uint)bVar1);
    if (__dataset != (__locale_t)0x0) {
      uselocale(__dataset);
    }
    *param_4 = wVar3;
    pbVar2 = param_3;
    param_4 = param_4 + 1;
  }
  return pbVar2;
}

~~~
