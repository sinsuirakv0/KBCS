# 00adfa7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adfa7c.md)

## 関数情報

~~~json
{
  "address": "00adfa7c",
  "name": "FUN_00adfa7c",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "66f2203c7e7affaa7c1753946b7cd435dad11de5fe9a0bbe075ddaa0f86fd240",
  "source_text_sha256": "66f2203c7e7affaa7c1753946b7cd435dad11de5fe9a0bbe075ddaa0f86fd240"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)

## 疑似コード 1/1 / UTF-8 427 bytes

~~~c

void FUN_00adfa7c(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00adfa80 to 00bdfa87 has its CatchHandler @ 00adfc30 */
  puVar1 = operator_new(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00adfa98 to 00bdfa9f has its CatchHandler @ 00adfc14 */
  *puVar1 = &PTR_FUN_00c0f948;
  puVar1[1] = uVar2;
  return;
}

~~~
