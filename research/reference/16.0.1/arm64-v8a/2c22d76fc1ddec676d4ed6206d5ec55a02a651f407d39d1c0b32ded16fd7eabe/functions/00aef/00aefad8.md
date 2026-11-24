# 00aefad8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aef6b0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef6b0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-c06212ae1cb68d677cd5682bd74d35a4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aefb74`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefb74.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-390e2b51660a9a05a7d98a22cfe90e8d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefad8",
  "name": "FUN_00aefad8",
  "size": 784,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "791b1e10ac97121726d20bc572317b2e39b86d69919146ad815ca2174f0700d2",
  "source_text_sha256": "791b1e10ac97121726d20bc572317b2e39b86d69919146ad815ca2174f0700d2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefad8",
        "00aefde7"
      ]
    ],
    "bytes_sha256": "47397a0ad5da324278e7aa785967a5c3b1f4c8dd20c9fa0b23bd99b71e808986",
    "instruction_count": 196,
    "instruction_bytes": 784,
    "body_bytes": 784,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00467b60](../00467/00467b60.md)
- [00469c04](../00469/00469c04.md)
- [00489f4c](../00489/00489f4c.md)
- [008b6d9c](../008b6/008b6d9c.md)
- [008b79c8](../008b7/008b79c8.md)
- [008b9290](../008b9/008b9290.md)
- [008b92ec](../008b9/008b92ec.md)
- [008b9794](../008b9/008b9794.md)
- [008b980c](../008b9/008b980c.md)
- [00c58610](../00c58/00c58610.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6098 bytes

~~~c

void FUN_00aefad8(long param_1,undefined8 *param_2,undefined8 *param_3)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  long lVar7;
  ulong uVar8;
  long lVar9;
  int extraout_var;
  int extraout_var_00;
  int extraout_w1;
  int extraout_w1_00;
  int extraout_var_01;
  int extraout_var_02;
  undefined8 uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  long lVar13;
  
  uVar11 = *param_2;
  uVar10 = *param_3;
  lVar13 = *(long *)(param_1 + 8);
  iVar4 = FUN_008b9290(uVar11);
  if ((iVar4 != 1) && (iVar4 = FUN_008b9290(uVar11), iVar4 != 2)) {
    return;
  }
  if (DAT_00ca4978 == 0) {
    lVar7 = 0;
  }
  else {
    lVar7 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d950,0);
                    /* try { // try from 00aefb48 to 00befb4f has its CatchHandler @ 00aefda8 */
  }
                    /* try { // try from 00aefb50 to 00befbc7 has its CatchHandler @ 00aef8e0 */
  uVar8 = FUN_008b9794(uVar11,0);
  if ((uVar8 & 1) == 0) {
    FUN_00467b60(uVar10,0x7f,0x7f,0x7f,0xff);
  }
  iVar5 = FUN_008b980c(uVar11,0);
  uVar12 = *(undefined8 *)(lVar7 + 0x118);
  iVar6 = FUN_008b92ec(uVar11,0);
  FUN_008b92ec(uVar11,0);
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x80);
  iVar4 = extraout_w1 - *(int *)(lVar9 + 8);
                    /* try { // try from 00aefbc8 to 00befbcf has its CatchHandler @ 00aefda4 */
  if (extraout_w1 < *(int *)(lVar9 + 8)) {
    iVar4 = iVar4 + 1;
  }
  iVar1 = iVar5;
                    /* try { // try from 00aefbd0 to 00befc43 has its CatchHandler @ 00aef8e0 */
  if (iVar5 < 0) {
    iVar1 = iVar5 + 1;
  }
  FUN_008b92ec(uVar11,0);
  FUN_008b92ec(uVar11,0);
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x80);
  iVar3 = extraout_var_01 - *(int *)(lVar9 + 0xc);
  if (extraout_var_01 < *(int *)(lVar9 + 0xc)) {
    iVar3 = iVar3 + 1;
  }
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x80);
  iVar2 = *(int *)(lVar9 + 8);
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x80);
                    /* try { // try from 00aefc44 to 00befc4b has its CatchHandler @ 00aefda0 */
                    /* try { // try from 00aefc4c to 00befcb7 has its CatchHandler @ 00aef8e0 */
  FUN_00469c04(uVar10,uVar12,(iVar6 - (iVar1 >> 1)) + (iVar4 >> 1),
               (extraout_var - (iVar1 >> 1)) + (iVar3 >> 1),iVar2 + iVar5,
               *(int *)(lVar9 + 0xc) + iVar5,0x80);
  FUN_00467b60(uVar10,0xff,0xff,0xff,0xff);
  uVar8 = FUN_008b9794(uVar11,1);
  if ((uVar8 & 1) == 0) {
    FUN_00467b60(uVar10,0x7f,0x7f,0x7f,0xff);
  }
  iVar5 = FUN_008b980c(uVar11,1);
  uVar12 = *(undefined8 *)(lVar7 + 0x118);
                    /* try { // try from 00aefcb8 to 00befcbf has its CatchHandler @ 00aefd9c */
  iVar6 = FUN_008b92ec(uVar11,1);
  FUN_008b92ec(uVar11,1);
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x7f);
  iVar4 = extraout_w1_00 - *(int *)(lVar9 + 8);
  if (extraout_w1_00 < *(int *)(lVar9 + 8)) {
    iVar4 = iVar4 + 1;
  }
  iVar1 = iVar5;
  if (iVar5 < 0) {
    iVar1 = iVar5 + 1;
  }
  FUN_008b92ec(uVar11,1);
                    /* try { // try from 00aefd0c to 00befd0f has its CatchHandler @ 00aefdb8 */
  FUN_008b92ec(uVar11,1);
                    /* try { // try from 00aefd20 to 00befd23 has its CatchHandler @ 00aefdb4 */
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x7f);
                    /* try { // try from 00aefd34 to 00befd37 has its CatchHandler @ 00aefdb0 */
  iVar3 = extraout_var_02 - *(int *)(lVar9 + 0xc);
  if (extraout_var_02 < *(int *)(lVar9 + 0xc)) {
    iVar3 = iVar3 + 1;
  }
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x7f);
                    /* try { // try from 00aefd48 to 00befd4b has its CatchHandler @ 00aefdac */
  iVar2 = *(int *)(lVar9 + 8);
  lVar7 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x7f);
                    /* try { // try from 00aefd5c to 00befd5f has its CatchHandler @ 00aefda8 */
                    /* try { // try from 00aefd70 to 00befd73 has its CatchHandler @ 00aefda4 */
  FUN_00469c04(uVar10,uVar12,(iVar6 - (iVar1 >> 1)) + (iVar4 >> 1),
               (extraout_var_00 - (iVar1 >> 1)) + (iVar3 >> 1),iVar2 + iVar5,
               *(int *)(lVar7 + 0xc) + iVar5,0x7f);
                    /* try { // try from 00aefd84 to 00befd87 has its CatchHandler @ 00aefda0 */
  FUN_00467b60(uVar10,0xff,0xff,0xff,0xff);
                    /* try { // try from 00aefd98 to 00befd9b has its CatchHandler @ 00aefd9c */
                    /* catch() { ... } // from try @ 00aefcb8 with catch @ 00aefd9c
                       catch() { ... } // from try @ 00aefd98 with catch @ 00aefd9c
                       try { // try from 00aefd9c to 00befde7 has its CatchHandler @ 00aef8e0 */
                    /* catch() { ... } // from try @ 00aefc44 with catch @ 00aefda0
                       catch() { ... } // from try @ 00aefd84 with catch @ 00aefda0 */
                    /* catch() { ... } // from try @ 00aefbc8 with catch @ 00aefda4
                       catch() { ... } // from try @ 00aefd70 with catch @ 00aefda4 */
  uVar10 = FUN_008b79c8(lVar13 + 0x2f38,0x326);
                    /* catch() { ... } // from try @ 00aefb48 with catch @ 00aefda8
                       catch() { ... } // from try @ 00aefd5c with catch @ 00aefda8 */
                    /* catch() { ... } // from try @ 00aefac8 with catch @ 00aefdac
                       catch() { ... } // from try @ 00aefd48 with catch @ 00aefdac */
                    /* catch() { ... } // from try @ 00aefa50 with catch @ 00aefdb0
                       catch() { ... } // from try @ 00aefd34 with catch @ 00aefdb0 */
                    /* catch() { ... } // from try @ 00aef9d8 with catch @ 00aefdb4
                       catch() { ... } // from try @ 00aefd20 with catch @ 00aefdb4 */
                    /* catch() { ... } // from try @ 00aef960 with catch @ 00aefdb8
                       catch() { ... } // from try @ 00aefd0c with catch @ 00aefdb8 */
  FUN_008b6d9c(uVar10,0,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aefad8"></a> `00aefad8` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00aefadc"></a> `00aefadc` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefae0"></a> `00aefae0` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aefae4"></a> `00aefae4` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aefae8"></a> `00aefae8` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aefaec"></a> `00aefaec` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aefaf0"></a> `00aefaf0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aefaf4"></a> `00aefaf4` | `34 00 40 f9` | ldr x20,[x1] | `FALL_THROUGH`
<a id="insn-00aefaf8"></a> `00aefaf8` | `53 00 40 f9` | ldr x19,[x2] | `FALL_THROUGH`
<a id="insn-00aefafc"></a> `00aefafc` | `1a 04 40 f9` | ldr x26,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefb00"></a> `00aefb00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefb04"></a> `00aefb04` | `e3 25 f7 97` | bl 0x008b9290 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb08"></a> `00aefb08` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aefb0c"></a> `00aefb0c` | `a0 00 00 54` | b.eq 0x00aefb20 | `CONDITIONAL_JUMP`
<a id="insn-00aefb10"></a> `00aefb10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefb14"></a> `00aefb14` | `df 25 f7 97` | bl 0x008b9290 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb18"></a> `00aefb18` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00aefb1c"></a> `00aefb1c` | `81 15 00 54` | b.ne 0x00aefdcc | `CONDITIONAL_JUMP`
<a id="insn-00aefb20"></a> `00aefb20` | `a8 0d 00 b0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00aefb24"></a> `00aefb24` | `00 bd 44 f9` | ldr x0,[x8, #0x978] | `FALL_THROUGH`
<a id="insn-00aefb28"></a> `00aefb28` | `20 01 00 b4` | cbz x0,0x00aefb4c | `CONDITIONAL_JUMP`
<a id="insn-00aefb2c"></a> `00aefb2c` | `a1 0b 00 d0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00aefb30"></a> `00aefb30` | `21 60 39 91` | add x1,x1,#0xe58 | `FALL_THROUGH`
<a id="insn-00aefb34"></a> `00aefb34` | `e2 0c 00 d0` | adrp x2,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aefb38"></a> `00aefb38` | `42 40 25 91` | add x2,x2,#0x950 | `FALL_THROUGH`
<a id="insn-00aefb3c"></a> `00aefb3c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00aefb40"></a> `00aefb40` | `b4 a2 05 94` | bl 0x00c58610 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb44"></a> `00aefb44` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aefb48"></a> `00aefb48` | `02 00 00 14` | b 0x00aefb50 | `UNCONDITIONAL_JUMP`
<a id="insn-00aefb4c"></a> `00aefb4c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00aefb50"></a> `00aefb50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefb54"></a> `00aefb54` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefb58"></a> `00aefb58` | `0f 27 f7 97` | bl 0x008b9794 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb5c"></a> `00aefb5c` | `e0 00 00 37` | tbnz w0,#0x0,0x00aefb78 | `CONDITIONAL_JUMP`
<a id="insn-00aefb60"></a> `00aefb60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefb64"></a> `00aefb64` | `e1 0f 80 52` | mov w1,#0x7f | `FALL_THROUGH`
<a id="insn-00aefb68"></a> `00aefb68` | `e2 0f 80 52` | mov w2,#0x7f | `FALL_THROUGH`
<a id="insn-00aefb6c"></a> `00aefb6c` | `e3 0f 80 52` | mov w3,#0x7f | `FALL_THROUGH`
<a id="insn-00aefb70"></a> `00aefb70` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aefb74"></a> `00aefb74` | `fb df e5 97` | bl 0x00467b60 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb78"></a> `00aefb78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefb7c"></a> `00aefb7c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefb80"></a> `00aefb80` | `23 27 f7 97` | bl 0x008b980c | `UNCONDITIONAL_CALL`
<a id="insn-00aefb84"></a> `00aefb84` | `b6 8e 40 f9` | ldr x22,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aefb88"></a> `00aefb88` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aefb8c"></a> `00aefb8c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefb90"></a> `00aefb90` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefb94"></a> `00aefb94` | `d6 25 f7 97` | bl 0x008b92ec | `UNCONDITIONAL_CALL`
<a id="insn-00aefb98"></a> `00aefb98` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00aefb9c"></a> `00aefb9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefba0"></a> `00aefba0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefba4"></a> `00aefba4` | `d2 25 f7 97` | bl 0x008b92ec | `UNCONDITIONAL_CALL`
<a id="insn-00aefba8"></a> `00aefba8` | `a0 8e 40 f9` | ldr x0,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aefbac"></a> `00aefbac` | `f9 03 01 aa` | mov x25,x1 | `FALL_THROUGH`
<a id="insn-00aefbb0"></a> `00aefbb0` | `01 10 80 52` | mov w1,#0x80 | `FALL_THROUGH`
<a id="insn-00aefbb4"></a> `00aefbb4` | `e6 68 e6 97` | bl 0x00489f4c | `UNCONDITIONAL_CALL`
<a id="insn-00aefbb8"></a> `00aefbb8` | `08 08 40 b9` | ldr w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefbbc"></a> `00aefbbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefbc0"></a> `00aefbc0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefbc4"></a> `00aefbc4` | `28 03 08 6b` | subs w8,w25,w8 | `FALL_THROUGH`
<a id="insn-00aefbc8"></a> `00aefbc8` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-00aefbcc"></a> `00aefbcc` | `ff 02 00 71` | cmp w23,#0x0 | `FALL_THROUGH`
<a id="insn-00aefbd0"></a> `00aefbd0` | `e9 a6 97 1a` | cinc w9,w23,lt | `FALL_THROUGH`
<a id="insn-00aefbd4"></a> `00aefbd4` | `39 7d 01 13` | asr w25,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aefbd8"></a> `00aefbd8` | `09 03 19 4b` | sub w9,w24,w25 | `FALL_THROUGH`
<a id="insn-00aefbdc"></a> `00aefbdc` | `38 05 88 0b` | add w24,w9,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aefbe0"></a> `00aefbe0` | `c3 25 f7 97` | bl 0x008b92ec | `UNCONDITIONAL_CALL`
<a id="insn-00aefbe4"></a> `00aefbe4` | `1b fc 60 d3` | lsr x27,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00aefbe8"></a> `00aefbe8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefbec"></a> `00aefbec` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefbf0"></a> `00aefbf0` | `bf 25 f7 97` | bl 0x008b92ec | `UNCONDITIONAL_CALL`
<a id="insn-00aefbf4"></a> `00aefbf4` | `a0 8e 40 f9` | ldr x0,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aefbf8"></a> `00aefbf8` | `3c fc 60 d3` | lsr x28,x1,#0x20 | `FALL_THROUGH`
<a id="insn-00aefbfc"></a> `00aefbfc` | `01 10 80 52` | mov w1,#0x80 | `FALL_THROUGH`
<a id="insn-00aefc00"></a> `00aefc00` | `d3 68 e6 97` | bl 0x00489f4c | `UNCONDITIONAL_CALL`
<a id="insn-00aefc04"></a> `00aefc04` | `09 0c 40 b9` | ldr w9,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-00aefc08"></a> `00aefc08` | `a0 8e 40 f9` | ldr x0,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aefc0c"></a> `00aefc0c` | `68 03 19 4b` | sub w8,w27,w25 | `FALL_THROUGH`
<a id="insn-00aefc10"></a> `00aefc10` | `01 10 80 52` | mov w1,#0x80 | `FALL_THROUGH`
<a id="insn-00aefc14"></a> `00aefc14` | `89 03 09 6b` | subs w9,w28,w9 | `FALL_THROUGH`
<a id="insn-00aefc18"></a> `00aefc18` | `29 a5 89 1a` | cinc w9,w9,lt | `FALL_THROUGH`
<a id="insn-00aefc1c"></a> `00aefc1c` | `19 05 89 0b` | add w25,w8,w9, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aefc20"></a> `00aefc20` | `cb 68 e6 97` | bl 0x00489f4c | `UNCONDITIONAL_CALL`
<a id="insn-00aefc24"></a> `00aefc24` | `a8 8e 40 f9` | ldr x8,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aefc28"></a> `00aefc28` | `1b 08 40 b9` | ldr w27,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefc2c"></a> `00aefc2c` | `01 10 80 52` | mov w1,#0x80 | `FALL_THROUGH`
<a id="insn-00aefc30"></a> `00aefc30` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aefc34"></a> `00aefc34` | `c6 68 e6 97` | bl 0x00489f4c | `UNCONDITIONAL_CALL`
<a id="insn-00aefc38"></a> `00aefc38` | `08 0c 40 b9` | ldr w8,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-00aefc3c"></a> `00aefc3c` | `64 03 17 0b` | add w4,w27,w23 | `FALL_THROUGH`
<a id="insn-00aefc40"></a> `00aefc40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefc44"></a> `00aefc44` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00aefc48"></a> `00aefc48` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-00aefc4c"></a> `00aefc4c` | `e3 03 19 2a` | mov w3,w25 | `FALL_THROUGH`
<a id="insn-00aefc50"></a> `00aefc50` | `05 01 17 0b` | add w5,w8,w23 | `FALL_THROUGH`
<a id="insn-00aefc54"></a> `00aefc54` | `06 10 80 52` | mov w6,#0x80 | `FALL_THROUGH`
<a id="insn-00aefc58"></a> `00aefc58` | `eb e7 e5 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-00aefc5c"></a> `00aefc5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefc60"></a> `00aefc60` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aefc64"></a> `00aefc64` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-00aefc68"></a> `00aefc68` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-00aefc6c"></a> `00aefc6c` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aefc70"></a> `00aefc70` | `bc df e5 97` | bl 0x00467b60 | `UNCONDITIONAL_CALL`
<a id="insn-00aefc74"></a> `00aefc74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefc78"></a> `00aefc78` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aefc7c"></a> `00aefc7c` | `c6 26 f7 97` | bl 0x008b9794 | `UNCONDITIONAL_CALL`
<a id="insn-00aefc80"></a> `00aefc80` | `e0 00 00 37` | tbnz w0,#0x0,0x00aefc9c | `CONDITIONAL_JUMP`
<a id="insn-00aefc84"></a> `00aefc84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefc88"></a> `00aefc88` | `e1 0f 80 52` | mov w1,#0x7f | `FALL_THROUGH`
<a id="insn-00aefc8c"></a> `00aefc8c` | `e2 0f 80 52` | mov w2,#0x7f | `FALL_THROUGH`
<a id="insn-00aefc90"></a> `00aefc90` | `e3 0f 80 52` | mov w3,#0x7f | `FALL_THROUGH`
<a id="insn-00aefc94"></a> `00aefc94` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aefc98"></a> `00aefc98` | `b2 df e5 97` | bl 0x00467b60 | `UNCONDITIONAL_CALL`
<a id="insn-00aefc9c"></a> `00aefc9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefca0"></a> `00aefca0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aefca4"></a> `00aefca4` | `da 26 f7 97` | bl 0x008b980c | `UNCONDITIONAL_CALL`
<a id="insn-00aefca8"></a> `00aefca8` | `b6 8e 40 f9` | ldr x22,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aefcac"></a> `00aefcac` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aefcb0"></a> `00aefcb0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefcb4"></a> `00aefcb4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aefcb8"></a> `00aefcb8` | `8d 25 f7 97` | bl 0x008b92ec | `UNCONDITIONAL_CALL`
<a id="insn-00aefcbc"></a> `00aefcbc` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00aefcc0"></a> `00aefcc0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefcc4"></a> `00aefcc4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aefcc8"></a> `00aefcc8` | `89 25 f7 97` | bl 0x008b92ec | `UNCONDITIONAL_CALL`
<a id="insn-00aefccc"></a> `00aefccc` | `a0 8e 40 f9` | ldr x0,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aefcd0"></a> `00aefcd0` | `f9 03 01 aa` | mov x25,x1 | `FALL_THROUGH`
<a id="insn-00aefcd4"></a> `00aefcd4` | `e1 0f 80 52` | mov w1,#0x7f | `FALL_THROUGH`
<a id="insn-00aefcd8"></a> `00aefcd8` | `9d 68 e6 97` | bl 0x00489f4c | `UNCONDITIONAL_CALL`
<a id="insn-00aefcdc"></a> `00aefcdc` | `08 08 40 b9` | ldr w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefce0"></a> `00aefce0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefce4"></a> `00aefce4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aefce8"></a> `00aefce8` | `28 03 08 6b` | subs w8,w25,w8 | `FALL_THROUGH`
<a id="insn-00aefcec"></a> `00aefcec` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-00aefcf0"></a> `00aefcf0` | `ff 02 00 71` | cmp w23,#0x0 | `FALL_THROUGH`
<a id="insn-00aefcf4"></a> `00aefcf4` | `e9 a6 97 1a` | cinc w9,w23,lt | `FALL_THROUGH`
<a id="insn-00aefcf8"></a> `00aefcf8` | `39 7d 01 13` | asr w25,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aefcfc"></a> `00aefcfc` | `09 03 19 4b` | sub w9,w24,w25 | `FALL_THROUGH`
<a id="insn-00aefd00"></a> `00aefd00` | `38 05 88 0b` | add w24,w9,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aefd04"></a> `00aefd04` | `7a 25 f7 97` | bl 0x008b92ec | `UNCONDITIONAL_CALL`
<a id="insn-00aefd08"></a> `00aefd08` | `1b fc 60 d3` | lsr x27,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00aefd0c"></a> `00aefd0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefd10"></a> `00aefd10` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aefd14"></a> `00aefd14` | `76 25 f7 97` | bl 0x008b92ec | `UNCONDITIONAL_CALL`
<a id="insn-00aefd18"></a> `00aefd18` | `a0 8e 40 f9` | ldr x0,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aefd1c"></a> `00aefd1c` | `34 fc 60 d3` | lsr x20,x1,#0x20 | `FALL_THROUGH`
<a id="insn-00aefd20"></a> `00aefd20` | `e1 0f 80 52` | mov w1,#0x7f | `FALL_THROUGH`
<a id="insn-00aefd24"></a> `00aefd24` | `8a 68 e6 97` | bl 0x00489f4c | `UNCONDITIONAL_CALL`
<a id="insn-00aefd28"></a> `00aefd28` | `09 0c 40 b9` | ldr w9,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-00aefd2c"></a> `00aefd2c` | `a0 8e 40 f9` | ldr x0,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aefd30"></a> `00aefd30` | `68 03 19 4b` | sub w8,w27,w25 | `FALL_THROUGH`
<a id="insn-00aefd34"></a> `00aefd34` | `e1 0f 80 52` | mov w1,#0x7f | `FALL_THROUGH`
<a id="insn-00aefd38"></a> `00aefd38` | `89 02 09 6b` | subs w9,w20,w9 | `FALL_THROUGH`
<a id="insn-00aefd3c"></a> `00aefd3c` | `29 a5 89 1a` | cinc w9,w9,lt | `FALL_THROUGH`
<a id="insn-00aefd40"></a> `00aefd40` | `14 05 89 0b` | add w20,w8,w9, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aefd44"></a> `00aefd44` | `82 68 e6 97` | bl 0x00489f4c | `UNCONDITIONAL_CALL`
<a id="insn-00aefd48"></a> `00aefd48` | `a8 8e 40 f9` | ldr x8,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aefd4c"></a> `00aefd4c` | `15 08 40 b9` | ldr w21,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefd50"></a> `00aefd50` | `e1 0f 80 52` | mov w1,#0x7f | `FALL_THROUGH`
<a id="insn-00aefd54"></a> `00aefd54` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aefd58"></a> `00aefd58` | `7d 68 e6 97` | bl 0x00489f4c | `UNCONDITIONAL_CALL`
<a id="insn-00aefd5c"></a> `00aefd5c` | `08 0c 40 b9` | ldr w8,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-00aefd60"></a> `00aefd60` | `a4 02 17 0b` | add w4,w21,w23 | `FALL_THROUGH`
<a id="insn-00aefd64"></a> `00aefd64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefd68"></a> `00aefd68` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00aefd6c"></a> `00aefd6c` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-00aefd70"></a> `00aefd70` | `e3 03 14 2a` | mov w3,w20 | `FALL_THROUGH`
<a id="insn-00aefd74"></a> `00aefd74` | `05 01 17 0b` | add w5,w8,w23 | `FALL_THROUGH`
<a id="insn-00aefd78"></a> `00aefd78` | `e6 0f 80 52` | mov w6,#0x7f | `FALL_THROUGH`
<a id="insn-00aefd7c"></a> `00aefd7c` | `a2 e7 e5 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-00aefd80"></a> `00aefd80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefd84"></a> `00aefd84` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aefd88"></a> `00aefd88` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-00aefd8c"></a> `00aefd8c` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-00aefd90"></a> `00aefd90` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aefd94"></a> `00aefd94` | `73 df e5 97` | bl 0x00467b60 | `UNCONDITIONAL_CALL`
<a id="insn-00aefd98"></a> `00aefd98` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aefd9c"></a> `00aefd9c` | `c1 64 80 52` | mov w1,#0x326 | `FALL_THROUGH`
<a id="insn-00aefda0"></a> `00aefda0` | `40 03 08 8b` | add x0,x26,x8 | `FALL_THROUGH`
<a id="insn-00aefda4"></a> `00aefda4` | `09 1f f7 97` | bl 0x008b79c8 | `UNCONDITIONAL_CALL`
<a id="insn-00aefda8"></a> `00aefda8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefdac"></a> `00aefdac` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aefdb0"></a> `00aefdb0` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aefdb4"></a> `00aefdb4` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aefdb8"></a> `00aefdb8` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aefdbc"></a> `00aefdbc` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aefdc0"></a> `00aefdc0` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefdc4"></a> `00aefdc4` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00aefdc8"></a> `00aefdc8` | `f5 1b f7 17` | b 0x008b6d9c | `CALL_TERMINATOR`
<a id="insn-00aefdcc"></a> `00aefdcc` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aefdd0"></a> `00aefdd0` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aefdd4"></a> `00aefdd4` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aefdd8"></a> `00aefdd8` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aefddc"></a> `00aefddc` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefde0"></a> `00aefde0` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00aefde4"></a> `00aefde4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aefad8`](#insn-00aefad8) 範囲 `[['00aefad8', '00aefb0f']]`
  - `CONDITIONAL_JUMP` [`00aefb0c`](#insn-00aefb0c) → [`00aefb20`](#insn-00aefb20)
  - `FALL_THROUGH` [`00aefb0c`](#insn-00aefb0c) → [`00aefb10`](#insn-00aefb10)
- ブロック [`00aefb10`](#insn-00aefb10) 範囲 `[['00aefb10', '00aefb1f']]`
  - `CONDITIONAL_JUMP` [`00aefb1c`](#insn-00aefb1c) → [`00aefdcc`](#insn-00aefdcc)
  - `FALL_THROUGH` [`00aefb1c`](#insn-00aefb1c) → [`00aefb20`](#insn-00aefb20)
- ブロック [`00aefb20`](#insn-00aefb20) 範囲 `[['00aefb20', '00aefb2b']]`
  - `CONDITIONAL_JUMP` [`00aefb28`](#insn-00aefb28) → [`00aefb4c`](#insn-00aefb4c)
  - `FALL_THROUGH` [`00aefb28`](#insn-00aefb28) → [`00aefb2c`](#insn-00aefb2c)
- ブロック [`00aefb2c`](#insn-00aefb2c) 範囲 `[['00aefb2c', '00aefb47']]`
  - `FALL_THROUGH` [`00aefb44`](#insn-00aefb44) → [`00aefb48`](#insn-00aefb48)
- ブロック [`00aefb48`](#insn-00aefb48) 範囲 `[['00aefb48', '00aefb4b']]`
  - `UNCONDITIONAL_JUMP` [`00aefb48`](#insn-00aefb48) → [`00aefb50`](#insn-00aefb50)
- ブロック [`00aefb4c`](#insn-00aefb4c) 範囲 `[['00aefb4c', '00aefb4f']]`
  - `FALL_THROUGH` [`00aefb4c`](#insn-00aefb4c) → [`00aefb50`](#insn-00aefb50)
- ブロック [`00aefb50`](#insn-00aefb50) 範囲 `[['00aefb50', '00aefb5f']]`
  - `CONDITIONAL_JUMP` [`00aefb5c`](#insn-00aefb5c) → [`00aefb78`](#insn-00aefb78)
  - `FALL_THROUGH` [`00aefb5c`](#insn-00aefb5c) → [`00aefb60`](#insn-00aefb60)
- ブロック [`00aefb60`](#insn-00aefb60) 範囲 `[['00aefb60', '00aefb77']]`
  - `FALL_THROUGH` [`00aefb74`](#insn-00aefb74) → [`00aefb78`](#insn-00aefb78)
- ブロック [`00aefb78`](#insn-00aefb78) 範囲 `[['00aefb78', '00aefbc7']]`
  - `FALL_THROUGH` [`00aefbc4`](#insn-00aefbc4) → [`00aefbc8`](#insn-00aefbc8)
- ブロック [`00aefbc8`](#insn-00aefbc8) 範囲 `[['00aefbc8', '00aefbcf']]`
  - `FALL_THROUGH` [`00aefbcc`](#insn-00aefbcc) → [`00aefbd0`](#insn-00aefbd0)
- ブロック [`00aefbd0`](#insn-00aefbd0) 範囲 `[['00aefbd0', '00aefc43']]`
  - `FALL_THROUGH` [`00aefc40`](#insn-00aefc40) → [`00aefc44`](#insn-00aefc44)
- ブロック [`00aefc44`](#insn-00aefc44) 範囲 `[['00aefc44', '00aefc4b']]`
  - `FALL_THROUGH` [`00aefc48`](#insn-00aefc48) → [`00aefc4c`](#insn-00aefc4c)
- ブロック [`00aefc4c`](#insn-00aefc4c) 範囲 `[['00aefc4c', '00aefc83']]`
  - `CONDITIONAL_JUMP` [`00aefc80`](#insn-00aefc80) → [`00aefc9c`](#insn-00aefc9c)
  - `FALL_THROUGH` [`00aefc80`](#insn-00aefc80) → [`00aefc84`](#insn-00aefc84)
- ブロック [`00aefc84`](#insn-00aefc84) 範囲 `[['00aefc84', '00aefc9b']]`
  - `FALL_THROUGH` [`00aefc98`](#insn-00aefc98) → [`00aefc9c`](#insn-00aefc9c)
- ブロック [`00aefc9c`](#insn-00aefc9c) 範囲 `[['00aefc9c', '00aefcb7']]`
  - `FALL_THROUGH` [`00aefcb4`](#insn-00aefcb4) → [`00aefcb8`](#insn-00aefcb8)
- ブロック [`00aefcb8`](#insn-00aefcb8) 範囲 `[['00aefcb8', '00aefd0b']]`
  - `FALL_THROUGH` [`00aefd08`](#insn-00aefd08) → [`00aefd0c`](#insn-00aefd0c)
- ブロック [`00aefd0c`](#insn-00aefd0c) 範囲 `[['00aefd0c', '00aefd1f']]`
  - `FALL_THROUGH` [`00aefd1c`](#insn-00aefd1c) → [`00aefd20`](#insn-00aefd20)
- ブロック [`00aefd20`](#insn-00aefd20) 範囲 `[['00aefd20', '00aefd33']]`
  - `FALL_THROUGH` [`00aefd30`](#insn-00aefd30) → [`00aefd34`](#insn-00aefd34)
- ブロック [`00aefd34`](#insn-00aefd34) 範囲 `[['00aefd34', '00aefd47']]`
  - `FALL_THROUGH` [`00aefd44`](#insn-00aefd44) → [`00aefd48`](#insn-00aefd48)
- ブロック [`00aefd48`](#insn-00aefd48) 範囲 `[['00aefd48', '00aefd5b']]`
  - `FALL_THROUGH` [`00aefd58`](#insn-00aefd58) → [`00aefd5c`](#insn-00aefd5c)
- ブロック [`00aefd5c`](#insn-00aefd5c) 範囲 `[['00aefd5c', '00aefd6f']]`
  - `FALL_THROUGH` [`00aefd6c`](#insn-00aefd6c) → [`00aefd70`](#insn-00aefd70)
- ブロック [`00aefd70`](#insn-00aefd70) 範囲 `[['00aefd70', '00aefd83']]`
  - `FALL_THROUGH` [`00aefd80`](#insn-00aefd80) → [`00aefd84`](#insn-00aefd84)
- ブロック [`00aefd84`](#insn-00aefd84) 範囲 `[['00aefd84', '00aefd97']]`
  - `FALL_THROUGH` [`00aefd94`](#insn-00aefd94) → [`00aefd98`](#insn-00aefd98)
- ブロック [`00aefd98`](#insn-00aefd98) 範囲 `[['00aefd98', '00aefd9b']]`
  - `FALL_THROUGH` [`00aefd98`](#insn-00aefd98) → [`00aefd9c`](#insn-00aefd9c)
- ブロック [`00aefd9c`](#insn-00aefd9c) 範囲 `[['00aefd9c', '00aefd9f']]`
  - `FALL_THROUGH` [`00aefd9c`](#insn-00aefd9c) → [`00aefda0`](#insn-00aefda0)
- ブロック [`00aefda0`](#insn-00aefda0) 範囲 `[['00aefda0', '00aefda3']]`
  - `FALL_THROUGH` [`00aefda0`](#insn-00aefda0) → [`00aefda4`](#insn-00aefda4)
- ブロック [`00aefda4`](#insn-00aefda4) 範囲 `[['00aefda4', '00aefda7']]`
  - `FALL_THROUGH` [`00aefda4`](#insn-00aefda4) → [`00aefda8`](#insn-00aefda8)
- ブロック [`00aefda8`](#insn-00aefda8) 範囲 `[['00aefda8', '00aefdab']]`
  - `FALL_THROUGH` [`00aefda8`](#insn-00aefda8) → [`00aefdac`](#insn-00aefdac)
- ブロック [`00aefdac`](#insn-00aefdac) 範囲 `[['00aefdac', '00aefdaf']]`
  - `FALL_THROUGH` [`00aefdac`](#insn-00aefdac) → [`00aefdb0`](#insn-00aefdb0)
- ブロック [`00aefdb0`](#insn-00aefdb0) 範囲 `[['00aefdb0', '00aefdb3']]`
  - `FALL_THROUGH` [`00aefdb0`](#insn-00aefdb0) → [`00aefdb4`](#insn-00aefdb4)
- ブロック [`00aefdb4`](#insn-00aefdb4) 範囲 `[['00aefdb4', '00aefdb7']]`
  - `FALL_THROUGH` [`00aefdb4`](#insn-00aefdb4) → [`00aefdb8`](#insn-00aefdb8)
- ブロック [`00aefdb8`](#insn-00aefdb8) 範囲 `[['00aefdb8', '00aefdcb']]`
- ブロック [`00aefdcc`](#insn-00aefdcc) 範囲 `[['00aefdcc', '00aefde7']]`

## 命令位置別の参照

- [`00aefad8`](#insn-00aefad8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefadc`](#insn-00aefadc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefae0`](#insn-00aefae0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefae4`](#insn-00aefae4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefae8`](#insn-00aefae8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefaec`](#insn-00aefaec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb04`](#insn-00aefb04) → [`008b9290`](../008b9/008b9290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9290` · 推定シンボル `None` · 推定型 `None`
- [`00aefb0c`](#insn-00aefb0c) → [`00aefb20`](#insn-00aefb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb14`](#insn-00aefb14) → [`008b9290`](../008b9/008b9290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9290` · 推定シンボル `None` · 推定型 `None`
- [`00aefb1c`](#insn-00aefb1c) → [`00aefdcc`](#insn-00aefdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb24`](#insn-00aefb24) → `00ca4978`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aefb28`](#insn-00aefb28) → [`00aefb4c`](#insn-00aefb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb30`](#insn-00aefb30) → `00c65e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aefb38`](#insn-00aefb38) → `00c8d950`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aefb40`](#insn-00aefb40) → [`00c58610`](../00c58/00c58610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58610` · 推定シンボル `None` · 推定型 `None`
- [`00aefb48`](#insn-00aefb48) → [`00aefb50`](#insn-00aefb50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb58`](#insn-00aefb58) → [`008b9794`](../008b9/008b9794.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9794` · 推定シンボル `None` · 推定型 `None`
- [`00aefb5c`](#insn-00aefb5c) → [`00aefb78`](#insn-00aefb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb74`](#insn-00aefb74) → [`00467b60`](../00467/00467b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b60` · 推定シンボル `None` · 推定型 `None`
- [`00aefb80`](#insn-00aefb80) → [`008b980c`](../008b9/008b980c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b980c` · 推定シンボル `None` · 推定型 `None`
- [`00aefb94`](#insn-00aefb94) → [`008b92ec`](../008b9/008b92ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b92ec` · 推定シンボル `None` · 推定型 `None`
- [`00aefba4`](#insn-00aefba4) → [`008b92ec`](../008b9/008b92ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b92ec` · 推定シンボル `None` · 推定型 `None`
- [`00aefbb4`](#insn-00aefbb4) → [`00489f4c`](../00489/00489f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f4c` · 推定シンボル `None` · 推定型 `None`
- [`00aefbe0`](#insn-00aefbe0) → [`008b92ec`](../008b9/008b92ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b92ec` · 推定シンボル `None` · 推定型 `None`
- [`00aefbf0`](#insn-00aefbf0) → [`008b92ec`](../008b9/008b92ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b92ec` · 推定シンボル `None` · 推定型 `None`
- [`00aefc00`](#insn-00aefc00) → [`00489f4c`](../00489/00489f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f4c` · 推定シンボル `None` · 推定型 `None`
- [`00aefc20`](#insn-00aefc20) → [`00489f4c`](../00489/00489f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f4c` · 推定シンボル `None` · 推定型 `None`
- [`00aefc34`](#insn-00aefc34) → [`00489f4c`](../00489/00489f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f4c` · 推定シンボル `None` · 推定型 `None`
- [`00aefc58`](#insn-00aefc58) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`00aefc70`](#insn-00aefc70) → [`00467b60`](../00467/00467b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b60` · 推定シンボル `None` · 推定型 `None`
- [`00aefc7c`](#insn-00aefc7c) → [`008b9794`](../008b9/008b9794.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9794` · 推定シンボル `None` · 推定型 `None`
- [`00aefc80`](#insn-00aefc80) → [`00aefc9c`](#insn-00aefc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefc98`](#insn-00aefc98) → [`00467b60`](../00467/00467b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b60` · 推定シンボル `None` · 推定型 `None`
- [`00aefca4`](#insn-00aefca4) → [`008b980c`](../008b9/008b980c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b980c` · 推定シンボル `None` · 推定型 `None`
- [`00aefcb8`](#insn-00aefcb8) → [`008b92ec`](../008b9/008b92ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b92ec` · 推定シンボル `None` · 推定型 `None`
- [`00aefcc8`](#insn-00aefcc8) → [`008b92ec`](../008b9/008b92ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b92ec` · 推定シンボル `None` · 推定型 `None`
- [`00aefcd8`](#insn-00aefcd8) → [`00489f4c`](../00489/00489f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f4c` · 推定シンボル `None` · 推定型 `None`
- [`00aefd04`](#insn-00aefd04) → [`008b92ec`](../008b9/008b92ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b92ec` · 推定シンボル `None` · 推定型 `None`
- [`00aefd14`](#insn-00aefd14) → [`008b92ec`](../008b9/008b92ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b92ec` · 推定シンボル `None` · 推定型 `None`
- [`00aefd24`](#insn-00aefd24) → [`00489f4c`](../00489/00489f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f4c` · 推定シンボル `None` · 推定型 `None`
- [`00aefd44`](#insn-00aefd44) → [`00489f4c`](../00489/00489f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f4c` · 推定シンボル `None` · 推定型 `None`
- [`00aefd58`](#insn-00aefd58) → [`00489f4c`](../00489/00489f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f4c` · 推定シンボル `None` · 推定型 `None`
- [`00aefd7c`](#insn-00aefd7c) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`00aefd94`](#insn-00aefd94) → [`00467b60`](../00467/00467b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b60` · 推定シンボル `None` · 推定型 `None`
- [`00aefda4`](#insn-00aefda4) → [`008b79c8`](../008b7/008b79c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b79c8` · 推定シンボル `None` · 推定型 `None`
- [`00aefdb0`](#insn-00aefdb0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefdb4`](#insn-00aefdb4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefdb8`](#insn-00aefdb8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefdbc`](#insn-00aefdbc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefdc0`](#insn-00aefdc0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefdc4`](#insn-00aefdc4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefdc8`](#insn-00aefdc8) → [`008b6d9c`](../008b6/008b6d9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6d9c` · 推定シンボル `None` · 推定型 `None`
- [`00aefdcc`](#insn-00aefdcc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefdd0`](#insn-00aefdd0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefdd4`](#insn-00aefdd4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefdd8`](#insn-00aefdd8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefddc`](#insn-00aefddc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefde0`](#insn-00aefde0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aefad8`](#insn-00aefad8)

~~~json
{
  "source": "00aefad8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefadc`](#insn-00aefadc)

~~~json
{
  "source": "00aefadc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefae0`](#insn-00aefae0)

~~~json
{
  "source": "00aefae0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefae4`](#insn-00aefae4)

~~~json
{
  "source": "00aefae4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefae8`](#insn-00aefae8)

~~~json
{
  "source": "00aefae8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefaec`](#insn-00aefaec)

~~~json
{
  "source": "00aefaec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb04`](#insn-00aefb04)

~~~json
{
  "source": "00aefb04",
  "target": "008b9290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb0c`](#insn-00aefb0c)

~~~json
{
  "source": "00aefb0c",
  "target": "00aefb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb14`](#insn-00aefb14)

~~~json
{
  "source": "00aefb14",
  "target": "008b9290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb1c`](#insn-00aefb1c)

~~~json
{
  "source": "00aefb1c",
  "target": "00aefdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb24`](#insn-00aefb24)

~~~json
{
  "source": "00aefb24",
  "target": "00ca4978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4978",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aefb28`](#insn-00aefb28)

~~~json
{
  "source": "00aefb28",
  "target": "00aefb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb30`](#insn-00aefb30)

~~~json
{
  "source": "00aefb30",
  "target": "00c65e58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65e58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aefb38`](#insn-00aefb38)

~~~json
{
  "source": "00aefb38",
  "target": "00c8d950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d950",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aefb40`](#insn-00aefb40)

~~~json
{
  "source": "00aefb40",
  "target": "00c58610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb48`](#insn-00aefb48)

~~~json
{
  "source": "00aefb48",
  "target": "00aefb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb58`](#insn-00aefb58)

~~~json
{
  "source": "00aefb58",
  "target": "008b9794",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb5c`](#insn-00aefb5c)

~~~json
{
  "source": "00aefb5c",
  "target": "00aefb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb74`](#insn-00aefb74)

~~~json
{
  "source": "00aefb74",
  "target": "00467b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb80`](#insn-00aefb80)

~~~json
{
  "source": "00aefb80",
  "target": "008b980c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb94`](#insn-00aefb94)

~~~json
{
  "source": "00aefb94",
  "target": "008b92ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefba4`](#insn-00aefba4)

~~~json
{
  "source": "00aefba4",
  "target": "008b92ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefbb4`](#insn-00aefbb4)

~~~json
{
  "source": "00aefbb4",
  "target": "00489f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefbe0`](#insn-00aefbe0)

~~~json
{
  "source": "00aefbe0",
  "target": "008b92ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefbf0`](#insn-00aefbf0)

~~~json
{
  "source": "00aefbf0",
  "target": "008b92ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc00`](#insn-00aefc00)

~~~json
{
  "source": "00aefc00",
  "target": "00489f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc20`](#insn-00aefc20)

~~~json
{
  "source": "00aefc20",
  "target": "00489f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc34`](#insn-00aefc34)

~~~json
{
  "source": "00aefc34",
  "target": "00489f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc58`](#insn-00aefc58)

~~~json
{
  "source": "00aefc58",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc70`](#insn-00aefc70)

~~~json
{
  "source": "00aefc70",
  "target": "00467b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc7c`](#insn-00aefc7c)

~~~json
{
  "source": "00aefc7c",
  "target": "008b9794",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc80`](#insn-00aefc80)

~~~json
{
  "source": "00aefc80",
  "target": "00aefc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefc98`](#insn-00aefc98)

~~~json
{
  "source": "00aefc98",
  "target": "00467b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefca4`](#insn-00aefca4)

~~~json
{
  "source": "00aefca4",
  "target": "008b980c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefcb8`](#insn-00aefcb8)

~~~json
{
  "source": "00aefcb8",
  "target": "008b92ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefcc8`](#insn-00aefcc8)

~~~json
{
  "source": "00aefcc8",
  "target": "008b92ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefcd8`](#insn-00aefcd8)

~~~json
{
  "source": "00aefcd8",
  "target": "00489f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefd04`](#insn-00aefd04)

~~~json
{
  "source": "00aefd04",
  "target": "008b92ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefd14`](#insn-00aefd14)

~~~json
{
  "source": "00aefd14",
  "target": "008b92ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefd24`](#insn-00aefd24)

~~~json
{
  "source": "00aefd24",
  "target": "00489f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefd44`](#insn-00aefd44)

~~~json
{
  "source": "00aefd44",
  "target": "00489f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefd58`](#insn-00aefd58)

~~~json
{
  "source": "00aefd58",
  "target": "00489f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefd7c`](#insn-00aefd7c)

~~~json
{
  "source": "00aefd7c",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefd94`](#insn-00aefd94)

~~~json
{
  "source": "00aefd94",
  "target": "00467b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefda4`](#insn-00aefda4)

~~~json
{
  "source": "00aefda4",
  "target": "008b79c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefdb0`](#insn-00aefdb0)

~~~json
{
  "source": "00aefdb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefdb4`](#insn-00aefdb4)

~~~json
{
  "source": "00aefdb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefdb8`](#insn-00aefdb8)

~~~json
{
  "source": "00aefdb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefdbc`](#insn-00aefdbc)

~~~json
{
  "source": "00aefdbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefdc0`](#insn-00aefdc0)

~~~json
{
  "source": "00aefdc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefdc4`](#insn-00aefdc4)

~~~json
{
  "source": "00aefdc4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefdc8`](#insn-00aefdc8)

~~~json
{
  "source": "00aefdc8",
  "target": "008b6d9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefdcc`](#insn-00aefdcc)

~~~json
{
  "source": "00aefdcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefdd0`](#insn-00aefdd0)

~~~json
{
  "source": "00aefdd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefdd4`](#insn-00aefdd4)

~~~json
{
  "source": "00aefdd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefdd8`](#insn-00aefdd8)

~~~json
{
  "source": "00aefdd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefddc`](#insn-00aefddc)

~~~json
{
  "source": "00aefddc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefde0`](#insn-00aefde0)

~~~json
{
  "source": "00aefde0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
