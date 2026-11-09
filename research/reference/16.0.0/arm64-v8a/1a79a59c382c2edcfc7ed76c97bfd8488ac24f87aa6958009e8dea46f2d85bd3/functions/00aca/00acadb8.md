# 00acadb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acadb8",
  "name": "FUN_00acadb8",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a60f5170e9dac47a6eb0cc814bc769e66b0fb1b5a816db1ef0bad79e88c8b99",
  "source_text_sha256": "4a60f5170e9dac47a6eb0cc814bc769e66b0fb1b5a816db1ef0bad79e88c8b99"
}
~~~

## 呼び出し元

- [00788c6c](../00788/00788c6c.md)
- [0082ede0](../0082e/0082ede0.md)
- [008fe848](../008fe/008fe848.md)
- [00a3dc60](../00a3d/00a3dc60.md)
- [00ac0258](../00ac0/00ac0258.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 307 bytes

~~~c

void FUN_00acadb8(long param_1,uint param_2)

{
  undefined4 uVar1;
  
  if ((param_2 & 1) == 0) {
    *(undefined4 *)(param_1 + 0x9c) = 2;
    FUN_008514b8();
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
