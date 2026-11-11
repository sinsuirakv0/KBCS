# 00aff2cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aff2cc",
  "name": "FUN_00aff2cc",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1da62d81b7a74850beead82b12910edde0c3a03a3dcbdd802905d46f91fa17fd",
  "source_text_sha256": "1da62d81b7a74850beead82b12910edde0c3a03a3dcbdd802905d46f91fa17fd"
}
~~~

## 呼び出し元

- [00685588](../00685/00685588.md)
- [006c52f8](../006c5/006c52f8.md)
- [00a4f3b4](../00a4f/00a4f3b4.md)
- [00af5a94](../00af5/00af5a94.md)
- [00b009dc](../00b00/00b009dc.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)
- [00b04c7c](../00b04/00b04c7c.md)

## 疑似コード / UTF-8 846 bytes

~~~c

ulong FUN_00aff2cc(int param_1,int param_2,int param_3,ulong param_4)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00aff2cc to 00bff2f7 has its CatchHandler @ 00aff258 */
                    /* catch() { ... } // from try @ 00aff2ac with catch @ 00aff2e4 */
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  lVar2 = FUN_008514f8();
  if ((uVar3 & 1) == 0) {
    uVar3 = (ulong)(*(int *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0x1840) != 0)
    ;
  }
  else {
    iVar1 = *(int *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f724);
    uVar3 = (ulong)(iVar1 != 0);
    if ((iVar1 == 0) && ((param_4 & 1) != 0)) {
      uVar3 = FUN_00b04c7c(param_1,param_2,param_3,0x20);
      return uVar3;
    }
  }
  return uVar3;
}

~~~
