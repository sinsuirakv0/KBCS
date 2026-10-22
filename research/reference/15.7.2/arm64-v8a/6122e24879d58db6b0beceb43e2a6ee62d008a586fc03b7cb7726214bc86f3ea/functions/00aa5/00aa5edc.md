# 00aa5edc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aa5edc.md)

## 関数情報

~~~json
{
  "address": "00aa5edc",
  "name": "FUN_00aa5edc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "81780e61d37e49b0123f29bc47ee9284c151afe384db4c1131187801fef2c058",
  "source_text_sha256": "81780e61d37e49b0123f29bc47ee9284c151afe384db4c1131187801fef2c058"
}
~~~
## 呼び出し元

- [009f1e64](../009f1/009f1e64.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00a9f0e0](../00a9f/00a9f0e0.md)

## 疑似コード 1/1 / UTF-8 583 bytes

~~~c

int FUN_00aa5edc(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
  lVar3 = FUN_0081f580();
  uVar4 = FUN_005c2710(lVar3 + (long)param_1 * 0x1f0 + 0x2678);
  lVar3 = FUN_0081f580();
  if ((uVar4 & 1) == 0) {
    iVar2 = *(int *)((long)__DT_JMPREL + lVar3 + ((long)param_2 + 2) * 0x1c4 + 0xa520);
  }
  else {
    iVar1 = *(int *)(lVar3 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f054);
    iVar2 = FUN_00a9f0e0(param_1,param_2,param_3,0x43,2);
    iVar2 = iVar2 + iVar1;
  }
  return iVar2;
}

~~~
