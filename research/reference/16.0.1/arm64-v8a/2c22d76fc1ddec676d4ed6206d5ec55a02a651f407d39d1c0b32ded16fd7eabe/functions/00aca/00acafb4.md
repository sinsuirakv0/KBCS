# 00acafb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00acafb4",
  "name": "FUN_00acafb4",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3038d08e80c19faeb132d5462da0ce2621e5bedaa8b0a794ab06fc10931c483",
  "source_text_sha256": "e3038d08e80c19faeb132d5462da0ce2621e5bedaa8b0a794ab06fc10931c483"
}
~~~

## 呼び出し元

- [00788cac](../00788/00788cac.md)
- [0082ee20](../0082e/0082ee20.md)
- [008fe9e4](../008fe/008fe9e4.md)
- [00a3de58](../00a3d/00a3de58.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 307 bytes

~~~c

void FUN_00acafb4(long param_1,uint param_2)

{
  undefined4 uVar1;
  
  if ((param_2 & 1) == 0) {
    *(undefined4 *)(param_1 + 0x9c) = 2;
    FUN_008514f8();
    uVar1 = 0xe;
  }
  else {
    uVar1 = 0;
    *(undefined4 *)(param_1 + 0x9c) = 3;
  }
  *(undefined4 *)(param_1 + 0x98) = uVar1;
  return;
}

~~~
