# 00ba4ffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ba4ffc.md)

## 関数情報

~~~json
{
  "address": "00ba4ffc",
  "name": "FUN_00ba4ffc",
  "size": 676,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd05d4fe176091ce781c2c94e43476a4d9673e1da50f3553b0ea707e626bd970",
  "source_text_sha256": "fd05d4fe176091ce781c2c94e43476a4d9673e1da50f3553b0ea707e626bd970"
}
~~~
## 呼び出し元

- [00ba82ec](../00ba8/00ba82ec.md)

## 呼び出し先

- [00ba05e4](../00ba0/00ba05e4.md)
- [00ba5360](../00ba5/00ba5360.md)
- [00ba54a4](../00ba5/00ba54a4.md)
- [00ba55e8](../00ba5/00ba55e8.md)
- [00ba572c](../00ba5/00ba572c.md)
- [00ba5870](../00ba5/00ba5870.md)
- [00ba59b4](../00ba5/00ba59b4.md)
- [00ba5af8](../00ba5/00ba5af8.md)
- [00ba5c3c](../00ba5/00ba5c3c.md)
- [00ba5d80](../00ba5/00ba5d80.md)
- [00ba5ec4](../00ba5/00ba5ec4.md)
- [00ba6008](../00ba6/00ba6008.md)
- [00ba614c](../00ba6/00ba614c.md)
- [00ba6290](../00ba6/00ba6290.md)
- [00ba63d4](../00ba6/00ba63d4.md)
- [00ba6518](../00ba6/00ba6518.md)
- [00ba665c](../00ba6/00ba665c.md)
- [00ba67a0](../00ba6/00ba67a0.md)
- [00ba68e4](../00ba6/00ba68e4.md)
- [00ba6a28](../00ba6/00ba6a28.md)
- [00ba6b6c](../00ba6/00ba6b6c.md)
- [00ba6cb0](../00ba6/00ba6cb0.md)
- [00ba6df4](../00ba6/00ba6df4.md)
- [00ba6f38](../00ba6/00ba6f38.md)
- [00ba707c](../00ba7/00ba707c.md)
- [00ba71c0](../00ba7/00ba71c0.md)
- [00ba7304](../00ba7/00ba7304.md)
- [00ba7448](../00ba7/00ba7448.md)
- [00ba758c](../00ba7/00ba758c.md)
- [00ba76d0](../00ba7/00ba76d0.md)
- [00ba7814](../00ba7/00ba7814.md)
- [00bb896c](../00bb8/00bb896c.md)
- [00bd6d60](../00bd6/00bd6d60.md)

## 疑似コード 1/1 / UTF-8 3370 bytes

~~~c

void FUN_00ba4ffc(undefined8 *param_1,undefined8 *param_2,long param_3,uint param_4)

{
  bool bVar1;
  long lVar2;
  long lVar3;
  long lVar4;
  ulong uVar6;
  ulong uVar5;
  
  *param_1 = &PTR_FUN_00c13818;
  param_1[1] = 0xffffffffffffffff;
  *(undefined1 *)(param_1 + 0x23) = 1;
  param_1[6] = 0;
  param_1[5] = 0;
  param_1[2] = param_1 + 5;
  param_1[8] = 0;
  param_1[7] = 0;
  param_1[10] = 0;
  param_1[9] = 0;
  param_1[0xc] = 0;
  param_1[0xb] = 0;
  param_1[0xe] = 0;
  param_1[0xd] = 0;
  param_1[0x10] = 0;
  param_1[0xf] = 0;
  param_1[0x12] = 0;
  param_1[0x11] = 0;
  param_1[0x14] = 0;
  param_1[0x13] = 0;
  param_1[0x16] = 0;
  param_1[0x15] = 0;
  param_1[0x18] = 0;
  param_1[0x17] = 0;
  param_1[0x1a] = 0;
  param_1[0x19] = 0;
  param_1[0x1c] = 0;
  param_1[0x1b] = 0;
  param_1[0x1e] = 0;
  param_1[0x1d] = 0;
  param_1[0x20] = 0;
  param_1[0x1f] = 0;
  param_1[0x22] = 0;
  param_1[0x21] = 0;
  param_1[3] = param_1 + 0x23;
  param_1[4] = param_1 + 0x23;
  FUN_00ba05e4(param_1 + 0x24,param_2 + 0x24,param_3 + 0x120,param_4);
  if (param_1 != param_2) {
    FUN_00bb896c(param_1 + 2,param_2[2],param_2[3],(long)(param_2[3] - param_2[2]) >> 3);
  }
  lVar3 = param_1[2];
  lVar2 = param_1[3];
  if (lVar2 != lVar3) {
    uVar5 = 0;
    uVar6 = 1;
    do {
      lVar4 = *(long *)(lVar3 + uVar5 * 8);
      if (lVar4 != 0) {
        FUN_00bd6d60(1,lVar4 + 8);
        lVar3 = param_1[2];
        lVar2 = param_1[3];
      }
      bVar1 = uVar6 < (ulong)(lVar2 - lVar3 >> 3);
      uVar5 = uVar6;
      uVar6 = (ulong)((int)uVar6 + 1);
    } while (bVar1);
  }
  if ((param_4 >> 3 & 1) != 0) {
    FUN_00ba5360(param_1,param_3);
                    /* try { // try from 00ba511c to 00ca517b has its CatchHandler @ 00ba5534 */
    FUN_00ba54a4(param_1,param_3);
  }
  if ((param_4 & 1) != 0) {
    FUN_00ba55e8(param_1,param_3);
    FUN_00ba572c(param_1,param_3);
    FUN_00ba5870(param_1,param_3);
    FUN_00ba59b4(param_1,param_3);
    FUN_00ba5af8(param_1,param_3);
    FUN_00ba5c3c(param_1,param_3);
    FUN_00ba5d80(param_1,param_3);
    FUN_00ba5ec4(param_1,param_3);
  }
  if ((param_4 >> 4 & 1) != 0) {
                    /* try { // try from 00ba5190 to 00ca51df has its CatchHandler @ 00ba5540 */
    FUN_00ba6008(param_1,param_3);
    FUN_00ba614c(param_1,param_3);
    FUN_00ba6290(param_1,param_3);
    FUN_00ba63d4(param_1,param_3);
    FUN_00ba6518(param_1,param_3);
    FUN_00ba665c(param_1,param_3);
    FUN_00ba67a0(param_1,param_3);
                    /* try { // try from 00ba51e0 to 00ca524b has its CatchHandler @ 00ba4fb0 */
    FUN_00ba68e4(param_1,param_3);
  }
  if ((param_4 >> 1 & 1) != 0) {
    FUN_00ba6a28(param_1,param_3);
    FUN_00ba6b6c(param_1,param_3);
    FUN_00ba6cb0(param_1,param_3);
    FUN_00ba6df4(param_1,param_3);
    FUN_00ba6f38(param_1,param_3);
    FUN_00ba707c(param_1,param_3);
  }
  if ((param_4 >> 2 & 1) != 0) {
    FUN_00ba71c0(param_1,param_3);
                    /* try { // try from 00ba524c to 00ca529b has its CatchHandler @ 00ba5540 */
    FUN_00ba7304(param_1,param_3);
    FUN_00ba7448(param_1,param_3);
    FUN_00ba758c(param_1,param_3);
  }
  if ((param_4 >> 5 & 1) != 0) {
    FUN_00ba76d0(param_1,param_3);
    FUN_00ba7814(param_1,param_3);
  }
  return;
}

~~~
