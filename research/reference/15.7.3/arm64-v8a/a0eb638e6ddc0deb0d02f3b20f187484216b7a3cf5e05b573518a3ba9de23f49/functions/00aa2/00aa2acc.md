# 00aa2acc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aa2acc",
  "name": "FUN_00aa2acc",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b02557b9d97fcd023433b35a326e667cbdbe0c364ceab8eecb4f39e7d7a290b6",
  "source_text_sha256": "b02557b9d97fcd023433b35a326e667cbdbe0c364ceab8eecb4f39e7d7a290b6"
}
~~~

## 呼び出し元

- [006a0ab4](../006a0/006a0ab4.md)
- [009f1e64](../009f1/009f1e64.md)
- [00aa0f20](../00aa0/00aa0f20.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c2c](../00aa2/00aa2c2c.md)

## 疑似コード / UTF-8 570 bytes

~~~c

ulong FUN_00aa2acc(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_0081f580();
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
  lVar1 = FUN_0081f580();
  if ((uVar2 & 1) == 0) {
    uVar2 = (ulong)(*(int *)((long)__DT_JMPREL + lVar1 + ((long)param_2 + 2) * 0x1c4 + 0xa514) != 0)
    ;
  }
  else {
    if (*(int *)(lVar1 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9efc4) == 0) {
      uVar2 = FUN_00aa2c2c(lVar1,param_2,param_3,0x1d);
      return uVar2;
    }
    uVar2 = 1;
  }
  return uVar2;
}

~~~
