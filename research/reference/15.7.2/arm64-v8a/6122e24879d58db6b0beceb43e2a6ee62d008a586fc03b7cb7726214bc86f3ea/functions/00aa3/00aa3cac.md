# 00aa3cac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aa3cac.md)

## 関数情報

~~~json
{
  "address": "00aa3cac",
  "name": "FUN_00aa3cac",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35bb62d81d642aa74f7870c86a1d25c696999b1d549357615b74d5369fb1fb57",
  "source_text_sha256": "35bb62d81d642aa74f7870c86a1d25c696999b1d549357615b74d5369fb1fb57"
}
~~~
## 呼び出し元

- [006a0ab4](../006a0/006a0ab4.md)
- [006a4d58](../006a4/006a4d58.md)
- [009f1e64](../009f1/009f1e64.md)
- [00aa0f20](../00aa0/00aa0f20.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c2c](../00aa2/00aa2c2c.md)

## 疑似コード 1/1 / UTF-8 915 bytes

~~~c

undefined8 FUN_00aa3cac(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  undefined8 uVar3;
  
                    /* try { // try from 00aa3cc8 to 00ba3cd7 has its CatchHandler @ 00aa5998 */
  lVar1 = FUN_0081f580();
                    /* try { // try from 00aa3cd8 to 00ba3ceb has its CatchHandler @ 00aa5970 */
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar2 & 1) == 0) {
    uVar3 = 0;
  }
  else {
    lVar1 = FUN_0081f580();
    if (*(int *)(lVar1 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0x9feec) == 0) {
      uVar3 = FUN_00aa2c2c(lVar1,param_2,param_3,0x3f);
      return uVar3;
    }
    uVar3 = 1;
  }
                    /* try { // try from 00aa3d18 to 00ba3d1f has its CatchHandler @ 00aa5a58 */
                    /* try { // try from 00aa3d20 to 00ba3d5b has its CatchHandler @ 00aa5a70 */
  return uVar3;
}

~~~
