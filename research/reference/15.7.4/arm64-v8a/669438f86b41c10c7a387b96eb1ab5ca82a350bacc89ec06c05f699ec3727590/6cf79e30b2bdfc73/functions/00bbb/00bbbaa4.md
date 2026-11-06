# 00bbbaa4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bbbaa4.md)

## 関数情報

~~~json
{
  "address": "00bbbaa4",
  "name": "FUN_00bbbaa4",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56a60a2436559fdbfca3f0fc0abb78b208725c1c07588ba6df78f60c5fdd81c4",
  "source_text_sha256": "56a60a2436559fdbfca3f0fc0abb78b208725c1c07588ba6df78f60c5fdd81c4"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb7c0](../00bdb/00bdb7c0.md)
- [00bde9d0](../00bde/00bde9d0.md)

## 疑似コード 1/1 / UTF-8 658 bytes

~~~c

bool FUN_00bbbaa4(long param_1,long param_2)

{
  int iVar1;
  long lVar2;
  
  if ((*(byte *)(param_1 + 0x10) & 0x18) == 0) {
    if (param_2 == 0) {
      return false;
    }
    lVar2 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048,
                           PTR__ZTIN10__cxxabiv117__pbase_type_infoE_00c1c058,0);
    if (lVar2 == 0) {
      return false;
    }
    if ((*(byte *)(lVar2 + 0x10) & 0x18) == 0) {
      return *(long *)(param_1 + 8) == *(long *)(param_2 + 8);
    }
  }
  if (param_1 != param_2) {
    iVar1 = strcmp(*(char **)(param_1 + 8),*(char **)(param_2 + 8));
    return iVar1 == 0;
  }
  return true;
}

~~~
