# 00acbcd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00acbcd0",
  "name": "FUN_00acbcd0",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9fb3503de6ea8e6319996223104deb850f8e32c1948d81fb86b005babff31e77",
  "source_text_sha256": "9fb3503de6ea8e6319996223104deb850f8e32c1948d81fb86b005babff31e77"
}
~~~

## 呼び出し元

- [00418a68](../00418/00418a68.md)
- [00418b18](../00418/00418b18.md)

## 呼び出し先

- [00449bcc](../00449/00449bcc.md)
- [00449be4](../00449/00449be4.md)
- [00449bf0](../00449/00449bf0.md)
- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 679 bytes

~~~c

void FUN_00acbcd0(undefined8 param_1,ulong param_2)

{
  long *plVar1;
  undefined4 uVar2;
  uint uVar3;
  long lVar4;
  
  uVar2 = FUN_0081f580();
  if ((param_2 & 1) == 0) {
    FUN_00449bcc(uVar2,0);
    lVar4 = 0x18;
  }
  else {
    uVar3 = FUN_00449be4();
    if ((uVar3 & 1) != 0) {
      uVar2 = FUN_0081f580();
      FUN_00449bf0(uVar2,0);
    }
    uVar2 = FUN_0081f580();
    FUN_00449bcc(uVar2,1);
    lVar4 = 0x10;
  }
  plVar1 = (long *)FUN_0081f580();
                    /* WARNING: Could not recover jumptable at 0x00acbd30. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + lVar4))();
  return;
}

~~~
