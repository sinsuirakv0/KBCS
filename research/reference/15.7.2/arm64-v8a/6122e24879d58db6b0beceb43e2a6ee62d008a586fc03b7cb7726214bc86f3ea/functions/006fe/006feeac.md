# 006feeac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](006feeac.md)

## 関数情報

~~~json
{
  "address": "006feeac",
  "name": "FUN_006feeac",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ef2a3ac3109866e76f2bdba08120a8f41016beff7d54064386ec10d025ff15e",
  "source_text_sha256": "9ef2a3ac3109866e76f2bdba08120a8f41016beff7d54064386ec10d025ff15e"
}
~~~
## 呼び出し元

- [00734830](../00734/00734830.md)
- [0073496c](../00734/0073496c.md)
- [0073fa38](../0073f/0073fa38.md)
- [00749514](../00749/00749514.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 185 bytes

~~~c

undefined4 FUN_006feeac(int param_1)

{
  if (param_1 + 0x1aU < 0x1f) {
    return *(undefined4 *)(&DAT_002d02d8 + (ulong)(param_1 + 0x1aU) * 4);
  }
  return 0xffffffff;
}

~~~
