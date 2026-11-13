# 00affeb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00affeb0",
  "name": "FUN_00affeb0",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8870f9559e2bc8678b18a241c8f8f44f364f0e236e1bcffc5fcedf2363682e87",
  "source_text_sha256": "8870f9559e2bc8678b18a241c8f8f44f364f0e236e1bcffc5fcedf2363682e87"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)
- [00afeb84](../00afe/00afeb84.md)

## 疑似コード / UTF-8 857 bytes

~~~c

int FUN_00affeb0(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
  lVar3 = FUN_00851550();
  uVar4 = FUN_005e7460(lVar3 + (long)param_1 * 0x1f0 + 0x2768);
  lVar3 = FUN_00851550();
                    /* try { // try from 00affef0 to 00bfff0b has its CatchHandler @ 00afff2c */
  if ((uVar4 & 1) == 0) {
    iVar1 = *(int *)((long)__DT_JMPREL + lVar3 + ((long)param_2 + 2) * 0x1c4 + 0x1808);
                    /* try { // try from 00afff0c to 00bfff3f has its CatchHandler @ 00affea8 */
  }
  else {
                    /* catch() { ... } // from try @ 00affef0 with catch @ 00afff2c */
    iVar1 = *(int *)(lVar3 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6e0);
    iVar2 = FUN_00afeb84(param_1,param_2,param_3,0x3d,0);
    iVar1 = ((100 - iVar2) * iVar1) / 100;
  }
  return iVar1;
}

~~~
