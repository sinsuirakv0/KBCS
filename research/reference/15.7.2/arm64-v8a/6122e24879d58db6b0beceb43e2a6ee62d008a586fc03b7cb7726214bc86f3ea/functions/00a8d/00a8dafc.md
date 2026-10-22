# 00a8dafc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a8dafc.md)

## 関数情報

~~~json
{
  "address": "00a8dafc",
  "name": "FUN_00a8dafc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f2e39fbfeb1af5010586925c499f7e330842512786e6df74994b2feb792265d6",
  "source_text_sha256": "f2e39fbfeb1af5010586925c499f7e330842512786e6df74994b2feb792265d6"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)

## 疑似コード 1/1 / UTF-8 231 bytes

~~~c

void FUN_00a8dafc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = operator_new(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c0df58;
  puVar1[1] = uVar2;
  return;
}

~~~
