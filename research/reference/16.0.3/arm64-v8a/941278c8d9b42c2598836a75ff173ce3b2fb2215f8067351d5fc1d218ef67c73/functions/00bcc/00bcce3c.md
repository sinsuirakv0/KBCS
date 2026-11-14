# 00bcce3c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcce3c",
  "name": "FUN_00bcce3c",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dcdcbc5712e9bd4d70955456f8732326787ed9bd573207f373a35c30a728c09b",
  "source_text_sha256": "dcdcbc5712e9bd4d70955456f8732326787ed9bd573207f373a35c30a728c09b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5be80](../00c5b/00c5be80.md)
- [00c5ead0](../00c5e/00c5ead0.md)

## 関連文字列（未確認候補）

~~~text
"Auth object 0x%08x should be deleted before the App 0x%08x it depends upon."
~~~

## 疑似コード / UTF-8 300 bytes

~~~c

void FUN_00bcce3c(undefined8 *param_1)

{
  _ZN8firebase10LogWarningEPKcz
            ("Auth object 0x%08x should be deleted before the App 0x%08x it depends upon.",
             (ulong)param_1 & 0xffffffff,*(undefined4 *)*param_1);
  _ZN8firebase4auth4Auth14DeleteInternalEv(param_1);
  return;
}

~~~
