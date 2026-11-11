# 00b2bbcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b2bbcc",
  "name": "FUN_00b2bbcc",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8c41251ed4f0e61202543efc59a7f011f3f41e739595dccc5e1bb5f529c7d1d",
  "source_text_sha256": "d8c41251ed4f0e61202543efc59a7f011f3f41e739595dccc5e1bb5f529c7d1d"
}
~~~

## 呼び出し元

- [0043b5a8](../0043b/0043b5a8.md)
- [0043b658](../0043b/0043b658.md)

## 呼び出し先

- [0046caa4](../0046c/0046caa4.md)
- [0046cabc](../0046c/0046cabc.md)
- [0046cac8](../0046c/0046cac8.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 679 bytes

~~~c

void FUN_00b2bbcc(undefined8 param_1,ulong param_2)

{
  long *plVar1;
  undefined4 uVar2;
  uint uVar3;
  long lVar4;
  
  uVar2 = FUN_008514f8();
  if ((param_2 & 1) == 0) {
    FUN_0046caa4(uVar2,0);
    lVar4 = 0x18;
  }
  else {
    uVar3 = FUN_0046cabc();
    if ((uVar3 & 1) != 0) {
      uVar2 = FUN_008514f8();
      FUN_0046cac8(uVar2,0);
    }
    uVar2 = FUN_008514f8();
    FUN_0046caa4(uVar2,1);
    lVar4 = 0x10;
  }
  plVar1 = (long *)FUN_008514f8();
                    /* WARNING: Could not recover jumptable at 0x00b2bc2c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + lVar4))();
  return;
}

~~~
