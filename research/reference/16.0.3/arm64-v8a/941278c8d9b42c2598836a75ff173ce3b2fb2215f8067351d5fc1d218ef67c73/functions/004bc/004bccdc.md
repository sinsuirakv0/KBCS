# 004bccdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "004bccdc",
  "name": "_ZNK5Botan8CBC_Mode18update_granularityEv",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "76f24c7cbcd62af4ec09681f545ee6d7abf47867ec726159413eb5eeb66f86a3",
  "source_text_sha256": "76f24c7cbcd62af4ec09681f545ee6d7abf47867ec726159413eb5eeb66f86a3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 277 bytes

~~~c

long _ZNK5Botan8CBC_Mode18update_granularityEv(long param_1)

{
  long lVar1;
  long lVar2;
  long *plVar3;
  
  plVar3 = *(long **)(param_1 + 8);
  lVar1 = (**(code **)(*plVar3 + 0x38))(plVar3);
  lVar2 = (**(code **)(*plVar3 + 0x30))(plVar3);
  return lVar1 * lVar2 * 4;
}

~~~
