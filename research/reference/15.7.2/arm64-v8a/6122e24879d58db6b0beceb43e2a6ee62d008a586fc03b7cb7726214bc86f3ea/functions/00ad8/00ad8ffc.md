# 00ad8ffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00ad8ffc",
  "name": "FUN_00ad8ffc",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e8a547b3e8d0b5a35523059cf181e00686e452911e4c530dd12428d2f3d5c482",
  "source_text_sha256": "e8a547b3e8d0b5a35523059cf181e00686e452911e4c530dd12428d2f3d5c482"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00adb010](../00adb/00adb010.md)

## 疑似コード / UTF-8 103 bytes

~~~c

void FUN_00ad8ffc(long param_1)

{
  FUN_00adb010(param_1,*(undefined8 *)(param_1 + 8));
  return;
}

~~~
