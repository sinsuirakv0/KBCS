# 00bab8dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bab8dc",
  "name": "_ZNSt6__ndk114__split_bufferINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEERNS_9allocatorIS6_EEE9push_backEOS6_",
  "size": 696,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b82ee4374b4a8df2df81cb57bc53ee6ec8e387aa799b012a657bad02d1d566f3",
  "source_text_sha256": "b82ee4374b4a8df2df81cb57bc53ee6ec8e387aa799b012a657bad02d1d566f3"
}
~~~

## 呼び出し元

- [00c5dc10](../00c5d/00c5dc10.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)

## 疑似コード / UTF-8 6404 bytes

~~~c

void _ZNSt6__ndk114__split_bufferINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEERNS_9allocatorIS6_EEE9push_backEOS6_
               (ulong *param_1,undefined8 *param_2)

{
  long lVar1;
  ulong uVar2;
  long lVar3;
  long lVar4;
  ulong uVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  undefined8 *puVar10;
  byte *pbVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  
                    /* try { // try from 00bab8ec to 00cab8f7 has its CatchHandler @ 00bacf14 */
  puVar10 = (undefined8 *)param_1[2];
                    /* try { // try from 00bab8f8 to 00cab917 has its CatchHandler @ 00bad0c4 */
  if (puVar10 == (undefined8 *)param_1[3]) {
    puVar6 = (undefined8 *)*param_1;
    puVar9 = (undefined8 *)param_1[1];
    if (puVar9 < puVar6 || (long)puVar9 - (long)puVar6 == 0) {
                    /* try { // try from 00bab9e8 to 00cab9f3 has its CatchHandler @ 00bacfb0 */
      lVar4 = (long)param_1[3] - (long)puVar6;
      uVar5 = (lVar4 >> 3) * 0x1c71c71c71c71c72;
      if (lVar4 == 0) {
        uVar5 = 1;
      }
                    /* try { // try from 00baba14 to 00caba1f has its CatchHandler @ 00bacf70 */
      if (0x38e38e38e38e38e < uVar5) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      uVar2 = _Znwm(uVar5 * 0x48);
      lVar4 = (long)puVar10 - (long)puVar9;
      puVar7 = (undefined8 *)(uVar2 + (uVar5 >> 2) * 0x48);
                    /* try { // try from 00baba38 to 00caba43 has its CatchHandler @ 00bacf60 */
      puVar8 = puVar7;
      if (lVar4 != 0) {
        lVar3 = 0;
                    /* try { // try from 00baba64 to 00caba6f has its CatchHandler @ 00bacf20 */
        puVar10 = puVar7;
        do {
          puVar6 = (undefined8 *)((long)puVar9 + lVar3);
          uVar12 = *puVar6;
          uVar14 = puVar6[3];
          uVar13 = puVar6[2];
          lVar1 = uVar2 + (uVar5 >> 2) * 0x48 + lVar3;
          lVar3 = lVar3 + 0x48;
                    /* try { // try from 00baba88 to 00caba93 has its CatchHandler @ 00bacf10 */
          puVar10[1] = puVar6[1];
          *puVar10 = uVar12;
          puVar10[3] = uVar14;
          puVar10[2] = uVar13;
          uVar13 = puVar6[5];
          uVar12 = puVar6[4];
                    /* try { // try from 00baba94 to 00cabab3 has its CatchHandler @ 00bad0c0 */
          *(undefined8 *)(lVar1 + 0x30) = puVar6[6];
          *(undefined8 *)(lVar1 + 0x28) = uVar13;
          *(undefined8 *)(lVar1 + 0x20) = uVar12;
          puVar6[5] = 0;
          puVar6[6] = 0;
          puVar6[4] = 0;
          *(undefined2 *)(lVar1 + 0x38) = *(undefined2 *)(puVar6 + 7);
          *(undefined8 *)(lVar1 + 0x40) = puVar6[8];
                    /* try { // try from 00babab4 to 00cabaeb has its CatchHandler @ 00bad130 */
          puVar10 = (undefined8 *)(lVar1 + 0x48);
        } while ((lVar4 >> 3) * 8 - lVar3 != 0);
        puVar6 = (undefined8 *)*param_1;
        puVar9 = (undefined8 *)param_1[1];
        puVar10 = (undefined8 *)param_1[2];
        puVar8 = (undefined8 *)((long)puVar7 + lVar4);
      }
      *param_1 = uVar2;
      param_1[1] = (ulong)puVar7;
      param_1[2] = (ulong)puVar8;
      param_1[3] = uVar2 + uVar5 * 0x48;
      while (puVar8 = puVar10, puVar8 != puVar9) {
        puVar10 = puVar8 + -9;
        if ((*(byte *)(puVar8 + -5) & 1) != 0) {
          _ZdlPv((void *)puVar8[-3]);
        }
      }
      if (puVar6 != (undefined8 *)0x0) {
        _ZdlPv(puVar6);
      }
    }
    else {
                    /* try { // try from 00bab918 to 00cab94f has its CatchHandler @ 00bad134 */
      lVar3 = ((long)puVar9 - (long)puVar6 >> 3) * -0x71c71c71c71c71c7;
      lVar4 = lVar3 + 2;
      if (-1 < lVar3 + 1) {
        lVar4 = lVar3 + 1;
      }
      lVar4 = lVar4 >> 1;
      if (puVar9 == puVar10) {
        puVar6 = puVar9 + lVar4 * -9;
      }
      else {
        do {
          uVar12 = *(undefined8 *)((long)puVar9 + 10);
          uVar14 = puVar9[1];
          uVar13 = *puVar9;
          puVar6 = puVar9 + lVar4 * -9;
                    /* try { // try from 00bab9a8 to 00cab9ab has its CatchHandler @ 00bad000 */
          *(undefined8 *)((long)puVar6 + 0x12) = *(undefined8 *)((long)puVar9 + 0x12);
          *(undefined8 *)((long)puVar6 + 10) = uVar12;
          puVar6[1] = uVar14;
          *puVar6 = uVar13;
          pbVar11 = (byte *)(puVar6 + 4);
          if ((*pbVar11 & 1) == 0) {
            *(undefined1 *)((long)puVar6 + 0x21) = 0;
            *pbVar11 = 0;
          }
          else {
            *(undefined1 *)puVar6[6] = 0;
            puVar6[5] = 0;
                    /* try { // try from 00bab9c8 to 00cab9d3 has its CatchHandler @ 00bacfc0 */
            if ((*pbVar11 & 1) != 0) {
              _ZdlPv((void *)puVar6[6]);
              puVar9[lVar4 * -9 + 4] = 0;
            }
          }
          uVar13 = puVar9[5];
          uVar12 = puVar9[4];
          puVar6[6] = puVar9[6];
                    /* try { // try from 00bab970 to 00cab97b has its CatchHandler @ 00bad070 */
          puVar6[5] = uVar13;
          *(undefined8 *)pbVar11 = uVar12;
          puVar9[5] = 0;
          puVar9[6] = 0;
          puVar9[4] = 0;
          *(undefined2 *)(puVar9 + lVar4 * -9 + 7) = *(undefined2 *)(puVar9 + 7);
          puVar6 = puVar9 + 9;
          puVar9[lVar4 * -9 + 8] = puVar9[8];
          puVar9 = puVar6;
                    /* try { // try from 00bab994 to 00cab99f has its CatchHandler @ 00bad060 */
        } while (puVar10 != puVar6);
        puVar10 = (undefined8 *)param_1[1];
        puVar6 = puVar6 + lVar4 * -9;
      }
      param_1[1] = (ulong)(puVar10 + lVar4 * -9);
      param_1[2] = (ulong)puVar6;
    }
  }
  puVar10 = (undefined8 *)param_1[2];
  uVar12 = *param_2;
  uVar14 = param_2[3];
  uVar13 = param_2[2];
  puVar10[1] = param_2[1];
  *puVar10 = uVar12;
  puVar10[3] = uVar14;
  puVar10[2] = uVar13;
  uVar13 = param_2[5];
  uVar12 = param_2[4];
                    /* try { // try from 00babb28 to 00cabb2b has its CatchHandler @ 00bace2c */
  puVar10[6] = param_2[6];
  puVar10[5] = uVar13;
  puVar10[4] = uVar12;
  param_2[5] = 0;
  param_2[6] = 0;
  param_2[4] = 0;
  *(undefined2 *)(puVar10 + 7) = *(undefined2 *)(param_2 + 7);
  puVar10[8] = param_2[8];
  param_1[2] = param_1[2] + 0x48;
                    /* try { // try from 00babb68 to 00cabb7b has its CatchHandler @ 00bacb48 */
  return;
}

~~~
