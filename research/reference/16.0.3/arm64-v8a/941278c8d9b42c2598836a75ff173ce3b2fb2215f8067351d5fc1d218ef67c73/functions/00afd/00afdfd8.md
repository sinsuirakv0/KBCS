# 00afdfd8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afdfd8",
  "name": "FUN_00afdfd8",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42c601c718dd57051d674a770b0f43248453e48bdc378887b7b2c2ea8c632c4b",
  "source_text_sha256": "42c601c718dd57051d674a770b0f43248453e48bdc378887b7b2c2ea8c632c4b"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 395 bytes

~~~c

undefined4 FUN_00afdfd8(int param_1,int param_2)

{
  undefined4 uVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008524fc();
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    lVar2 = FUN_008524fc();
    uVar1 = *(undefined4 *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c);
  }
  else {
    uVar1 = 0;
  }
  return uVar1;
}

~~~
