# 00adfa7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00adfb88`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfb88.md)
<!-- /kbcs-version-next -->

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
  "source_sha256": "991eb2ec41a54801d21e11a981c677893e3332db7b02e0317b3a4633c203f284",
  "source_text_sha256": "991eb2ec41a54801d21e11a981c677893e3332db7b02e0317b3a4633c203f284"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)

## 疑似コード / UTF-8 418 bytes

~~~c

void FUN_00adfa7c(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00adfa80 to 00bdfa87 has its CatchHandler @ 00adfc30 */
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00adfa98 to 00bdfa9f has its CatchHandler @ 00adfc14 */
  *puVar1 = &PTR_FUN_00c0f948;
  puVar1[1] = uVar2;
  return;
}

~~~
