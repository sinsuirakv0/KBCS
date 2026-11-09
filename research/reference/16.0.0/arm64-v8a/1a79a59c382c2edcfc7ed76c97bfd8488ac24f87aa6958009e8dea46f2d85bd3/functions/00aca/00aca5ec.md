# 00aca5ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aca5ec",
  "name": "FUN_00aca5ec",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b4ca553e52312c8304e84a7039b242732cd95da5214a33d2ba3a0feefdb30d1",
  "source_text_sha256": "1b4ca553e52312c8304e84a7039b242732cd95da5214a33d2ba3a0feefdb30d1"
}
~~~

## 呼び出し元

- [00789da0](../00789/00789da0.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008cb4a8](../008cb/008cb4a8.md)
- [008feea4](../008fe/008feea4.md)
- [00a3e32c](../00a3e/00a3e32c.md)
- [00ac08a0](../00ac0/00ac08a0.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)
- [008b6d58](../008b6/008b6d58.md)
- [008b7984](../008b7/008b7984.md)

## 疑似コード / UTF-8 308 bytes

~~~c

void FUN_00aca5ec(long param_1)

{
  long lVar1;
  undefined8 uVar2;
  
  if ((*(int *)(param_1 + 4) != -1) && (*(char *)(param_1 + 0x14) == '\0')) {
    lVar1 = FUN_008514b8();
    uVar2 = FUN_008b7984(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 4));
    FUN_008b6d58(uVar2,0,0);
    return;
  }
  return;
}

~~~
