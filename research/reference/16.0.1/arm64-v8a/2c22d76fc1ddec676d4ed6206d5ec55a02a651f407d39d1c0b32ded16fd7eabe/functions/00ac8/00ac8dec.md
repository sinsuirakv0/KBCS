# 00ac8dec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00ac8dec",
  "name": "FUN_00ac8dec",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "30f8019ac84cc0bee76d0f4deaaaf02da004582d94e1f1944f6f7ca1b591c81c",
  "source_text_sha256": "30f8019ac84cc0bee76d0f4deaaaf02da004582d94e1f1944f6f7ca1b591c81c"
}
~~~

## 呼び出し元

- [00789de0](../00789/00789de0.md)
- [0082ac68](../0082a/0082ac68.md)
- [008c87f8](../008c8/008c87f8.md)
- [008c89fc](../008c8/008c89fc.md)
- [008c990c](../008c9/008c990c.md)
- [008c9da8](../008c9/008c9da8.md)
- [00a75dac](../00a75/00a75dac.md)
- [00a79c04](../00a79/00a79c04.md)
- [00ac0a9c](../00ac0/00ac0a9c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 184 bytes

~~~c

undefined4 FUN_00ac8dec(long param_1)

{
                    /* try { // try from 00ac8df0 to 00bc8ecb has its CatchHandler @ 00ac8bcc */
  return *(undefined4 *)(param_1 + 0x68);
}

~~~
