# 00acadfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acadfc",
  "name": "FUN_00acadfc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53f3dc8895cb13b7e24f910de1d7b7ee38362f5f050877b1ab2bfe3e2a6170c4",
  "source_text_sha256": "53f3dc8895cb13b7e24f910de1d7b7ee38362f5f050877b1ab2bfe3e2a6170c4"
}
~~~

## 呼び出し元

- [00789da0](../00789/00789da0.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008feea4](../008fe/008feea4.md)
- [00a3e32c](../00a3e/00a3e32c.md)
- [00ac08a0](../00ac0/00ac08a0.md)

## 呼び出し先

- [007590d4](../00759/007590d4.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 444 bytes

~~~c

void FUN_00acadfc(long param_1)

{
  int iVar1;
  undefined8 uVar2;
  undefined4 uVar3;
  
  iVar1 = *(int *)(param_1 + 0x9c);
  if (iVar1 == 0) {
    uVar2 = FUN_008514b8();
    uVar3 = 0;
  }
  else {
    if ((iVar1 != 1) && (iVar1 != 2)) {
      return;
    }
    uVar2 = FUN_008514b8();
    FUN_008514b8();
    uVar3 = *(undefined4 *)(PTR_DAT_00c9b108 + (long)*(int *)(param_1 + 0x98) * 4);
  }
  FUN_007590d4(uVar2,uVar3,0);
  return;
}

~~~
