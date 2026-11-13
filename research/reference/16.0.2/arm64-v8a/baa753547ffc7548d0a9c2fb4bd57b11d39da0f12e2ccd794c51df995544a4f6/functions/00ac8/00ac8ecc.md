# 00ac8ecc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00ac8ecc",
  "name": "FUN_00ac8ecc",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83026b603df259e896eab1b8f1abdf14fc30595c656444b6510032f78ab52cc3",
  "source_text_sha256": "83026b603df259e896eab1b8f1abdf14fc30595c656444b6510032f78ab52cc3"
}
~~~

## 呼び出し元

- [00657fcc](../00657/00657fcc.md)
- [0068aae0](../0068a/0068aae0.md)
- [006d3e94](../006d3/006d3e94.md)
- [007001b0](../00700/007001b0.md)
- [00769ddc](../00769/00769ddc.md)
- [00835794](../00835/00835794.md)
- [008c038c](../008c0/008c038c.md)
- [00a01544](../00a01/00a01544.md)

## 呼び出し先

- [00851550](../00851/00851550.md)
- [00859ba4](../00859/00859ba4.md)
- [0085b2fc](../0085b/0085b2fc.md)
- [0085b304](../0085b/0085b304.md)
- [0085b338](../0085b/0085b338.md)
- [00ac8ff0](../00ac8/00ac8ff0.md)

## 疑似コード / UTF-8 2005 bytes

~~~c

undefined8 FUN_00ac8ecc(long param_1)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  float fVar4;
  float fVar5;
  float fVar6;
  
  if (*(char *)(param_1 + 0x1d4) == '\0') {
    return 0;
  }
  FUN_00851550();
  uVar2 = FUN_00859ba4();
  if ((uVar2 & 1) == 0) {
    FUN_00851550();
    uVar2 = FUN_0085b338();
    if (((uVar2 & 1) == 0) && (lVar3 = FUN_00851550(), *(char *)(lVar3 + 0x3575) == '\0'))
    goto LAB_00ac8f8c;
  }
  FUN_00851550();
  uVar2 = FUN_0085b338();
  if ((uVar2 & 1) != 0) {
                    /* try { // try from 00ac8f20 to 00bc8f2b has its CatchHandler @ 00ac9384 */
    *(undefined4 *)(param_1 + 500) = *(undefined4 *)(param_1 + 0x1f0);
    return 1;
  }
                    /* try { // try from 00ac8f3c to 00bc8f4b has its CatchHandler @ 00ac935c */
  uVar2 = FUN_00ac8ff0(param_1);
  if ((uVar2 & 1) != 0) {
    fVar4 = *(float *)(param_1 + 0x1d8);
                    /* try { // try from 00ac8f4c to 00bc8f5b has its CatchHandler @ 00ac9358 */
    iVar1 = *(int *)(param_1 + 0x284);
    fVar5 = (fVar4 * *(float *)(param_1 + 0x1e0)) / *(float *)(param_1 + 0x1dc);
    if (fVar5 <= 14.0) {
      fVar5 = 14.0;
    }
    FUN_00851550();
    if (iVar1 == 0) {
      iVar1 = FUN_0085b2fc();
      fVar6 = *(float *)(param_1 + 0x1e4);
    }
    else {
      iVar1 = FUN_0085b304();
      fVar6 = *(float *)(param_1 + 0x1e8);
                    /* try { // try from 00ac8f88 to 00bc8f9b has its CatchHandler @ 00ac9350 */
    }
                    /* try { // try from 00ac8fbc to 00bc8fcf has its CatchHandler @ 00ac9370 */
    fVar4 = (float)NEON_fminnm((((float)iVar1 - fVar6) + -fVar5 * 0.5) / (float)(int)(fVar4 - fVar5)
                               ,0x3f800000);
                    /* try { // try from 00ac8fd4 to 00bc900b has its CatchHandler @ 00ac9390 */
    if (fVar4 <= 0.0) {
      fVar4 = 0.0;
    }
    *(float *)(param_1 + 0x1f0) = fVar4;
    return 1;
  }
LAB_00ac8f8c:
  *(undefined4 *)(param_1 + 500) = *(undefined4 *)(param_1 + 0x1f0);
  return 0;
}

~~~
