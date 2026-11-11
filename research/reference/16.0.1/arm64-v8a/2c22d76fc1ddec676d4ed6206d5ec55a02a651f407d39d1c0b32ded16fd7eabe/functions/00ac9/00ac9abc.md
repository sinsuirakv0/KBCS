# 00ac9abc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00ac9abc",
  "name": "FUN_00ac9abc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b38ce4491f7fe27984be5fd0847ae052e798c9282b3a1b71e26f494066dfff83",
  "source_text_sha256": "b38ce4491f7fe27984be5fd0847ae052e798c9282b3a1b71e26f494066dfff83"
}
~~~

## 呼び出し元

- [00788cac](../00788/00788cac.md)
- [0082ee20](../0082e/0082ee20.md)
- [008fe9e4](../008fe/008fe9e4.md)
- [00a3de58](../00a3d/00a3de58.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 468 bytes

~~~c

void FUN_00ac9abc(long param_1,undefined8 param_2,undefined4 param_3,undefined8 param_4,
                 undefined4 param_5)

{
  *(undefined4 *)(param_1 + 0x1b0) = param_3;
  *(undefined8 *)(param_1 + 0x1a0) = param_2;
  *(undefined8 *)(param_1 + 0x1a8) = param_4;
                    /* try { // try from 00ac9ac8 to 00bc9acf has its CatchHandler @ 00ac9b60 */
  *(undefined4 *)(param_1 + 0x1b4) = param_5;
  *(undefined2 *)(param_1 + 0x1b8) = 0x101;
  return;
}

~~~
