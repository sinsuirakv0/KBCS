# 00bcbdac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bcbdac",
  "name": "FUN_00bcbdac",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6333242f5190f9f5b97284a83378a72a71de6e96678dfefc28f1ca4978042440",
  "source_text_sha256": "6333242f5190f9f5b97284a83378a72a71de6e96678dfefc28f1ca4978042440"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ade0](../00c5a/00c5ade0.md)
- [00c5da30](../00c5d/00c5da30.md)

## 関連文字列（未確認候補）

~~~text
"Auth object 0x%08x should be deleted before the App 0x%08x it depends upon."
~~~

## 疑似コード / UTF-8 300 bytes

~~~c

void FUN_00bcbdac(undefined8 *param_1)

{
  _ZN8firebase10LogWarningEPKcz
            ("Auth object 0x%08x should be deleted before the App 0x%08x it depends upon.",
             (ulong)param_1 & 0xffffffff,*(undefined4 *)*param_1);
  _ZN8firebase4auth4Auth14DeleteInternalEv(param_1);
  return;
}

~~~
