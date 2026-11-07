# 00aad3ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00aad2e0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad2e0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00aad3ec",
  "name": "FUN_00aad3ec",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "245f1a3803a578e7f3d9d33cd046bf93a4682367694c353196e3e8655d58d7be",
  "source_text_sha256": "245f1a3803a578e7f3d9d33cd046bf93a4682367694c353196e3e8655d58d7be"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_00aad3ec(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c0f458;
  puVar1[1] = uVar2;
  return;
}

~~~
