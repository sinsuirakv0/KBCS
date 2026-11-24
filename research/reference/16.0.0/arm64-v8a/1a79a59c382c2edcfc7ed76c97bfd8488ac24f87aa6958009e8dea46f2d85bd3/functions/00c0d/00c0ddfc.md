# 00c0ddfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b913b4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b913b4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0073.md#compare-349cedd0be3cc11c1109787ed5bb7a16)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c0e224`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e224.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-9731231fe01bae91eb09295fcf5dbaaa)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c0ddfc",
  "name": "_ZNSt6__ndk19__num_getIcE19__stage2_float_loopEcRbRcPcRS4_ccRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSE_RjS4_",
  "size": 636,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9fe7b9923d69c95e3661ff0d6f49d220d061e99b40e2a1feb6525dda3b4013c2",
  "source_text_sha256": "9fe7b9923d69c95e3661ff0d6f49d220d061e99b40e2a1feb6525dda3b4013c2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c0ddfc",
        "00c0e077"
      ]
    ],
    "bytes_sha256": "6692153cfd23a6432dcbe9a0df14080afb13c8a9b525ef0982e34d011a477841",
    "instruction_count": 159,
    "instruction_bytes": 636,
    "body_bytes": 636,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e160](../00c5e/00c5e160.md)

## 呼び出し先

- [00c57bd0](../00c57/00c57bd0.md)

## 関連文字列（未確認候補）

~~~text
"0123456789abcdefABCDEFxX+-pPiInN"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5309 bytes

~~~c

undefined8
_ZNSt6__ndk19__num_getIcE19__stage2_float_loopEcRbRcPcRS4_ccRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSE_RjS4_
          (byte param_1,char *param_2,byte *param_3,byte *param_4,long *param_5,byte param_6,
          byte param_7,byte *param_8,long param_9,undefined8 *param_10,int *param_11,void *param_12)

{
  void *pvVar1;
  ulong uVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  void *pvVar6;
  undefined1 *puVar7;
  int *piVar8;
  ulong uVar9;
  byte *pbVar10;
  uint uVar11;
  uint uVar12;
  
                    /* try { // try from 00c0de2c to 00d0de47 has its CatchHandler @ 00c0e0e8 */
  if (param_1 == param_6) {
    if (*param_2 != '\0') {
      puVar7 = (undefined1 *)*param_5;
      *param_2 = '\0';
                    /* try { // try from 00c0de48 to 00d0de53 has its CatchHandler @ 00c0e04c */
      *param_5 = (long)(puVar7 + 1);
      *puVar7 = 0x2e;
      uVar9 = (ulong)(*param_8 >> 1);
      if ((*param_8 & 1) != 0) {
        uVar9 = *(ulong *)(param_8 + 8);
      }
      if ((uVar9 != 0) && (piVar8 = (int *)*param_10, (long)piVar8 - param_9 < 0xa0)) {
        *piVar8 = *param_11;
        *param_10 = piVar8 + 1;
        return 0;
                    /* try { // try from 00c0de88 to 00d0de8f has its CatchHandler @ 00c0e0e4 */
      }
      return 0;
    }
  }
  else {
                    /* try { // try from 00c0de90 to 00d0de9b has its CatchHandler @ 00c0e0b4 */
    if (param_1 == param_7) {
      uVar9 = (ulong)(*param_8 >> 1);
      if ((*param_8 & 1) != 0) {
        uVar9 = *(ulong *)(param_8 + 8);
      }
      if (uVar9 != 0) {
        if (*param_2 == '\0') {
          return 0xffffffff;
        }
        piVar8 = (int *)*param_10;
                    /* try { // try from 00c0debc to 00d0dec3 has its CatchHandler @ 00c0e0e0 */
        if (0x9f < (long)piVar8 - param_9) {
          return 0;
        }
                    /* try { // try from 00c0dec4 to 00d0decf has its CatchHandler @ 00c0e0b0 */
        *piVar8 = *param_11;
        *param_10 = piVar8 + 1;
        *param_11 = 0;
        return 0;
      }
    }
                    /* try { // try from 00c0def0 to 00d0def7 has its CatchHandler @ 00c0e010 */
                    /* try { // try from 00c0def8 to 00d0df07 has its CatchHandler @ 00c0e050 */
    pvVar6 = memchr(param_12,(uint)param_1,0x20);
    pvVar1 = (void *)((long)param_12 + 0x20);
    if (pvVar6 != (void *)0x0) {
      pvVar1 = pvVar6;
    }
    uVar9 = (long)pvVar1 - (long)param_12;
    if ((long)uVar9 < 0x20) {
                    /* try { // try from 00c0df48 to 00d0df4f has its CatchHandler @ 00c0e008 */
                    /* try { // try from 00c0df50 to 00d0df63 has its CatchHandler @ 00c0e01c */
      bVar4 = PTR__ZNSt6__ndk114__num_get_base5__srcE_00c9b7c0[uVar9];
      uVar11 = (uint)bVar4;
      if ((uVar9 & 0xfffffffffffffffe) == 0x16) {
        *param_3 = 0x50;
        pbVar10 = (byte *)*param_5;
        *param_5 = (long)(pbVar10 + 1);
        *pbVar10 = bVar4;
        return 0;
      }
                    /* try { // try from 00c0df64 to 00d0e17b has its CatchHandler @ 00c0dadc */
      if ((uVar9 & 0xfffffffffffffffe) == 0x18) {
        pbVar10 = (byte *)*param_5;
        if (pbVar10 != param_4) {
          bVar5 = pbVar10[-1];
          bVar3 = *param_3;
          uVar11 = bVar5 ^ 0x20;
          if (0x19 < bVar5 - 0x61) {
            uVar11 = (uint)bVar5;
          }
          uVar12 = bVar3 ^ 0x20;
          if (0x19 < bVar3 - 0x61) {
            uVar12 = (uint)bVar3;
          }
          if (uVar11 != uVar12) {
            return 0xffffffff;
          }
        }
        *param_5 = (long)(pbVar10 + 1);
        *pbVar10 = bVar4;
        return 0;
      }
      bVar3 = *param_3;
      uVar12 = uVar11 ^ 0x20;
      if (0x19 < uVar11 - 0x61) {
        uVar12 = uVar11;
      }
      if (uVar12 == bVar3) {
        bVar5 = bVar3 | 0x20;
        if (0x19 < uVar12 - 0x41) {
          bVar5 = bVar3;
        }
                    /* catch() { ... } // from try @ 00c0df48 with catch @ 00c0e008 */
        *param_3 = bVar5;
                    /* catch() { ... } // from try @ 00c0df1c with catch @ 00c0e00c */
                    /* catch() { ... } // from try @ 00c0def0 with catch @ 00c0e010 */
        if (*param_2 != '\0') {
          *param_2 = '\0';
                    /* catch() { ... } // from try @ 00c0df50 with catch @ 00c0e01c */
          uVar2 = (ulong)(*param_8 >> 1);
          if ((*param_8 & 1) != 0) {
            uVar2 = *(ulong *)(param_8 + 8);
          }
                    /* catch() { ... } // from try @ 00c0df24 with catch @ 00c0e034 */
          if ((uVar2 != 0) && (piVar8 = (int *)*param_10, (long)piVar8 - param_9 < 0xa0)) {
            *piVar8 = *param_11;
            *param_10 = piVar8 + 1;
          }
        }
      }
                    /* catch() { ... } // from try @ 00c0de48 with catch @ 00c0e04c */
      pbVar10 = (byte *)*param_5;
                    /* catch() { ... } // from try @ 00c0def8 with catch @ 00c0e050 */
      *param_5 = (long)(pbVar10 + 1);
      *pbVar10 = bVar4;
      if ((long)uVar9 < 0x16) {
        *param_11 = *param_11 + 1;
        return 0;
      }
      return 0;
    }
  }
                    /* try { // try from 00c0df1c to 00d0df23 has its CatchHandler @ 00c0e00c */
  return 0xffffffff;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c0ddfc"></a> `00c0ddfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c0de00"></a> `00c0de00` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00c0de04"></a> `00c0de04` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c0de08"></a> `00c0de08` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c0de0c"></a> `00c0de0c` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c0de10"></a> `00c0de10` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c0de14"></a> `00c0de14` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c0de18"></a> `00c0de18` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c0de1c"></a> `00c0de1c` | `b5 d3 46 a9` | ldp x21,x20,[x29, #0x68] | `FALL_THROUGH`
<a id="insn-00c0de20"></a> `00c0de20` | `08 1c 00 12` | and w8,w0,#0xff | `FALL_THROUGH`
<a id="insn-00c0de24"></a> `00c0de24` | `b6 33 40 f9` | ldr x22,[x29, #0x60] | `FALL_THROUGH`
<a id="insn-00c0de28"></a> `00c0de28` | `1f 01 25 6b` | cmp w8,w5, UXTB  | `FALL_THROUGH`
<a id="insn-00c0de2c"></a> `00c0de2c` | `01 03 00 54` | b.ne 0x00c0de8c | `CONDITIONAL_JUMP`
<a id="insn-00c0de30"></a> `00c0de30` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00c0de34"></a> `00c0de34` | `48 07 00 34` | cbz w8,0x00c0df1c | `CONDITIONAL_JUMP`
<a id="insn-00c0de38"></a> `00c0de38` | `88 00 40 f9` | ldr x8,[x4] | `FALL_THROUGH`
<a id="insn-00c0de3c"></a> `00c0de3c` | `ca 05 80 52` | mov w10,#0x2e | `FALL_THROUGH`
<a id="insn-00c0de40"></a> `00c0de40` | `3f 00 00 39` | strb wzr,[x1] | `FALL_THROUGH`
<a id="insn-00c0de44"></a> `00c0de44` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0de48"></a> `00c0de48` | `89 00 00 f9` | str x9,[x4] | `FALL_THROUGH`
<a id="insn-00c0de4c"></a> `00c0de4c` | `0a 01 00 39` | strb w10,[x8] | `FALL_THROUGH`
<a id="insn-00c0de50"></a> `00c0de50` | `e8 00 40 39` | ldrb w8,[x7] | `FALL_THROUGH`
<a id="insn-00c0de54"></a> `00c0de54` | `e9 04 40 f9` | ldr x9,[x7, #0x8] | `FALL_THROUGH`
<a id="insn-00c0de58"></a> `00c0de58` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0de5c"></a> `00c0de5c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0de60"></a> `00c0de60` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00c0de64"></a> `00c0de64` | `08 06 00 b4` | cbz x8,0x00c0df24 | `CONDITIONAL_JUMP`
<a id="insn-00c0de68"></a> `00c0de68` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0de6c"></a> `00c0de6c` | `09 01 16 cb` | sub x9,x8,x22 | `FALL_THROUGH`
<a id="insn-00c0de70"></a> `00c0de70` | `3f 7d 02 f1` | cmp x9,#0x9f | `FALL_THROUGH`
<a id="insn-00c0de74"></a> `00c0de74` | `8c 05 00 54` | b.gt 0x00c0df24 | `CONDITIONAL_JUMP`
<a id="insn-00c0de78"></a> `00c0de78` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00c0de7c"></a> `00c0de7c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00c0de80"></a> `00c0de80` | `09 45 00 b8` | str w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00c0de84"></a> `00c0de84` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0de88"></a> `00c0de88` | `28 00 00 14` | b 0x00c0df28 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0de8c"></a> `00c0de8c` | `1f 01 26 6b` | cmp w8,w6, UXTB  | `FALL_THROUGH`
<a id="insn-00c0de90"></a> `00c0de90` | `61 02 00 54` | b.ne 0x00c0dedc | `CONDITIONAL_JUMP`
<a id="insn-00c0de94"></a> `00c0de94` | `e8 00 40 39` | ldrb w8,[x7] | `FALL_THROUGH`
<a id="insn-00c0de98"></a> `00c0de98` | `e9 04 40 f9` | ldr x9,[x7, #0x8] | `FALL_THROUGH`
<a id="insn-00c0de9c"></a> `00c0de9c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0dea0"></a> `00c0dea0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0dea4"></a> `00c0dea4` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00c0dea8"></a> `00c0dea8` | `a8 01 00 b4` | cbz x8,0x00c0dedc | `CONDITIONAL_JUMP`
<a id="insn-00c0deac"></a> `00c0deac` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00c0deb0"></a> `00c0deb0` | `68 03 00 34` | cbz w8,0x00c0df1c | `CONDITIONAL_JUMP`
<a id="insn-00c0deb4"></a> `00c0deb4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0deb8"></a> `00c0deb8` | `09 01 16 cb` | sub x9,x8,x22 | `FALL_THROUGH`
<a id="insn-00c0debc"></a> `00c0debc` | `3f 7d 02 f1` | cmp x9,#0x9f | `FALL_THROUGH`
<a id="insn-00c0dec0"></a> `00c0dec0` | `2c 03 00 54` | b.gt 0x00c0df24 | `CONDITIONAL_JUMP`
<a id="insn-00c0dec4"></a> `00c0dec4` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00c0dec8"></a> `00c0dec8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00c0decc"></a> `00c0decc` | `09 45 00 b8` | str w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00c0ded0"></a> `00c0ded0` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00c0ded4"></a> `00c0ded4` | `9f 02 00 b9` | str wzr,[x20] | `FALL_THROUGH`
<a id="insn-00c0ded8"></a> `00c0ded8` | `14 00 00 14` | b 0x00c0df28 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0dedc"></a> `00c0dedc` | `b3 3f 40 f9` | ldr x19,[x29, #0x78] | `FALL_THROUGH`
<a id="insn-00c0dee0"></a> `00c0dee0` | `f8 03 01 aa` | mov x24,x1 | `FALL_THROUGH`
<a id="insn-00c0dee4"></a> `00c0dee4` | `fa 03 02 aa` | mov x26,x2 | `FALL_THROUGH`
<a id="insn-00c0dee8"></a> `00c0dee8` | `01 1c 00 12` | and w1,w0,#0xff | `FALL_THROUGH`
<a id="insn-00c0deec"></a> `00c0deec` | `02 04 80 52` | mov w2,#0x20 | `FALL_THROUGH`
<a id="insn-00c0def0"></a> `00c0def0` | `fb 03 03 aa` | mov x27,x3 | `FALL_THROUGH`
<a id="insn-00c0def4"></a> `00c0def4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c0def8"></a> `00c0def8` | `f7 03 07 aa` | mov x23,x7 | `FALL_THROUGH`
<a id="insn-00c0defc"></a> `00c0defc` | `f9 03 04 aa` | mov x25,x4 | `FALL_THROUGH`
<a id="insn-00c0df00"></a> `00c0df00` | `7c 82 00 91` | add x28,x19,#0x20 | `FALL_THROUGH`
<a id="insn-00c0df04"></a> `00c0df04` | `33 27 01 94` | bl 0x00c57bd0 | `UNCONDITIONAL_CALL`
<a id="insn-00c0df08"></a> `00c0df08` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00c0df0c"></a> `00c0df0c` | `88 03 80 9a` | csel x8,x28,x0,eq | `FALL_THROUGH`
<a id="insn-00c0df10"></a> `00c0df10` | `0a 01 13 cb` | sub x10,x8,x19 | `FALL_THROUGH`
<a id="insn-00c0df14"></a> `00c0df14` | `5f 7d 00 f1` | cmp x10,#0x1f | `FALL_THROUGH`
<a id="insn-00c0df18"></a> `00c0df18` | `8d 01 00 54` | b.le 0x00c0df48 | `CONDITIONAL_JUMP`
<a id="insn-00c0df1c"></a> `00c0df1c` | `00 00 80 12` | mov w0,#0xffffffff | `FALL_THROUGH`
<a id="insn-00c0df20"></a> `00c0df20` | `02 00 00 14` | b 0x00c0df28 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0df24"></a> `00c0df24` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00c0df28"></a> `00c0df28` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c0df2c"></a> `00c0df2c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c0df30"></a> `00c0df30` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c0df34"></a> `00c0df34` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c0df38"></a> `00c0df38` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c0df3c"></a> `00c0df3c` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00c0df40"></a> `00c0df40` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c0df44"></a> `00c0df44` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c0df48"></a> `00c0df48` | `68 04 00 d0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c0df4c"></a> `00c0df4c` | `49 f9 7f 92` | and x9,x10,#-0x2 | `FALL_THROUGH`
<a id="insn-00c0df50"></a> `00c0df50` | `08 e1 43 f9` | ldr x8,[x8, #0x7c0] | `FALL_THROUGH`
<a id="insn-00c0df54"></a> `00c0df54` | `3f 59 00 f1` | cmp x9,#0x16 | `FALL_THROUGH`
<a id="insn-00c0df58"></a> `00c0df58` | `08 69 6a 38` | ldrb w8,[x8, x10, LSL ] | `FALL_THROUGH`
<a id="insn-00c0df5c"></a> `00c0df5c` | `00 03 00 54` | b.eq 0x00c0dfbc | `CONDITIONAL_JUMP`
<a id="insn-00c0df60"></a> `00c0df60` | `3f 61 00 f1` | cmp x9,#0x18 | `FALL_THROUGH`
<a id="insn-00c0df64"></a> `00c0df64` | `e9 03 19 aa` | mov x9,x25 | `FALL_THROUGH`
<a id="insn-00c0df68"></a> `00c0df68` | `a1 03 00 54` | b.ne 0x00c0dfdc | `CONDITIONAL_JUMP`
<a id="insn-00c0df6c"></a> `00c0df6c` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00c0df70"></a> `00c0df70` | `5f 01 1b eb` | cmp x10,x27 | `FALL_THROUGH`
<a id="insn-00c0df74"></a> `00c0df74` | `a0 01 00 54` | b.eq 0x00c0dfa8 | `CONDITIONAL_JUMP`
<a id="insn-00c0df78"></a> `00c0df78` | `4b f1 5f 38` | ldurb w11,[x10, #-0x1] | `FALL_THROUGH`
<a id="insn-00c0df7c"></a> `00c0df7c` | `4c 03 40 39` | ldrb w12,[x26] | `FALL_THROUGH`
<a id="insn-00c0df80"></a> `00c0df80` | `6d 85 01 51` | sub w13,w11,#0x61 | `FALL_THROUGH`
<a id="insn-00c0df84"></a> `00c0df84` | `6e 01 1b 52` | eor w14,w11,#0x20 | `FALL_THROUGH`
<a id="insn-00c0df88"></a> `00c0df88` | `bf 69 00 71` | cmp w13,#0x1a | `FALL_THROUGH`
<a id="insn-00c0df8c"></a> `00c0df8c` | `8d 85 01 51` | sub w13,w12,#0x61 | `FALL_THROUGH`
<a id="insn-00c0df90"></a> `00c0df90` | `cb 31 8b 1a` | csel w11,w14,w11,cc | `FALL_THROUGH`
<a id="insn-00c0df94"></a> `00c0df94` | `8e 01 1b 52` | eor w14,w12,#0x20 | `FALL_THROUGH`
<a id="insn-00c0df98"></a> `00c0df98` | `bf 69 00 71` | cmp w13,#0x1a | `FALL_THROUGH`
<a id="insn-00c0df9c"></a> `00c0df9c` | `cc 31 8c 1a` | csel w12,w14,w12,cc | `FALL_THROUGH`
<a id="insn-00c0dfa0"></a> `00c0dfa0` | `7f 01 0c 6b` | cmp w11,w12 | `FALL_THROUGH`
<a id="insn-00c0dfa4"></a> `00c0dfa4` | `c1 fb ff 54` | b.ne 0x00c0df1c | `CONDITIONAL_JUMP`
<a id="insn-00c0dfa8"></a> `00c0dfa8` | `4b 05 00 91` | add x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c0dfac"></a> `00c0dfac` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00c0dfb0"></a> `00c0dfb0` | `2b 01 00 f9` | str x11,[x9] | `FALL_THROUGH`
<a id="insn-00c0dfb4"></a> `00c0dfb4` | `48 01 00 39` | strb w8,[x10] | `FALL_THROUGH`
<a id="insn-00c0dfb8"></a> `00c0dfb8` | `dc ff ff 17` | b 0x00c0df28 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0dfbc"></a> `00c0dfbc` | `09 0a 80 52` | mov w9,#0x50 | `FALL_THROUGH`
<a id="insn-00c0dfc0"></a> `00c0dfc0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00c0dfc4"></a> `00c0dfc4` | `49 03 00 39` | strb w9,[x26] | `FALL_THROUGH`
<a id="insn-00c0dfc8"></a> `00c0dfc8` | `29 03 40 f9` | ldr x9,[x25] | `FALL_THROUGH`
<a id="insn-00c0dfcc"></a> `00c0dfcc` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c0dfd0"></a> `00c0dfd0` | `2a 03 00 f9` | str x10,[x25] | `FALL_THROUGH`
<a id="insn-00c0dfd4"></a> `00c0dfd4` | `28 01 00 39` | strb w8,[x9] | `FALL_THROUGH`
<a id="insn-00c0dfd8"></a> `00c0dfd8` | `d4 ff ff 17` | b 0x00c0df28 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0dfdc"></a> `00c0dfdc` | `0b 85 01 51` | sub w11,w8,#0x61 | `FALL_THROUGH`
<a id="insn-00c0dfe0"></a> `00c0dfe0` | `0c 01 1b 52` | eor w12,w8,#0x20 | `FALL_THROUGH`
<a id="insn-00c0dfe4"></a> `00c0dfe4` | `7f 69 00 71` | cmp w11,#0x1a | `FALL_THROUGH`
<a id="insn-00c0dfe8"></a> `00c0dfe8` | `4b 03 40 39` | ldrb w11,[x26] | `FALL_THROUGH`
<a id="insn-00c0dfec"></a> `00c0dfec` | `8c 31 88 1a` | csel w12,w12,w8,cc | `FALL_THROUGH`
<a id="insn-00c0dff0"></a> `00c0dff0` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00c0dff4"></a> `00c0dff4` | `c1 02 00 54` | b.ne 0x00c0e04c | `CONDITIONAL_JUMP`
<a id="insn-00c0dff8"></a> `00c0dff8` | `8c 05 01 51` | sub w12,w12,#0x41 | `FALL_THROUGH`
<a id="insn-00c0dffc"></a> `00c0dffc` | `6d 01 1b 32` | orr w13,w11,#0x20 | `FALL_THROUGH`
<a id="insn-00c0e000"></a> `00c0e000` | `9f 69 00 71` | cmp w12,#0x1a | `FALL_THROUGH`
<a id="insn-00c0e004"></a> `00c0e004` | `ab 31 8b 1a` | csel w11,w13,w11,cc | `FALL_THROUGH`
<a id="insn-00c0e008"></a> `00c0e008` | `4b 03 00 39` | strb w11,[x26] | `FALL_THROUGH`
<a id="insn-00c0e00c"></a> `00c0e00c` | `0b 03 40 39` | ldrb w11,[x24] | `FALL_THROUGH`
<a id="insn-00c0e010"></a> `00c0e010` | `eb 01 00 34` | cbz w11,0x00c0e04c | `CONDITIONAL_JUMP`
<a id="insn-00c0e014"></a> `00c0e014` | `1f 03 00 39` | strb wzr,[x24] | `FALL_THROUGH`
<a id="insn-00c0e018"></a> `00c0e018` | `eb 02 40 39` | ldrb w11,[x23] | `FALL_THROUGH`
<a id="insn-00c0e01c"></a> `00c0e01c` | `ec 06 40 f9` | ldr x12,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00c0e020"></a> `00c0e020` | `6d fd 41 d3` | lsr x13,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00c0e024"></a> `00c0e024` | `7f 01 00 72` | tst w11,#0x1 | `FALL_THROUGH`
<a id="insn-00c0e028"></a> `00c0e028` | `ab 01 8c 9a` | csel x11,x13,x12,eq | `FALL_THROUGH`
<a id="insn-00c0e02c"></a> `00c0e02c` | `0b 01 00 b4` | cbz x11,0x00c0e04c | `CONDITIONAL_JUMP`
<a id="insn-00c0e030"></a> `00c0e030` | `ab 02 40 f9` | ldr x11,[x21] | `FALL_THROUGH`
<a id="insn-00c0e034"></a> `00c0e034` | `6c 01 16 cb` | sub x12,x11,x22 | `FALL_THROUGH`
<a id="insn-00c0e038"></a> `00c0e038` | `9f 7d 02 f1` | cmp x12,#0x9f | `FALL_THROUGH`
<a id="insn-00c0e03c"></a> `00c0e03c` | `8c 00 00 54` | b.gt 0x00c0e04c | `CONDITIONAL_JUMP`
<a id="insn-00c0e040"></a> `00c0e040` | `8c 02 40 b9` | ldr w12,[x20] | `FALL_THROUGH`
<a id="insn-00c0e044"></a> `00c0e044` | `6c 45 00 b8` | str w12,[x11], #0x4 | `FALL_THROUGH`
<a id="insn-00c0e048"></a> `00c0e048` | `ab 02 00 f9` | str x11,[x21] | `FALL_THROUGH`
<a id="insn-00c0e04c"></a> `00c0e04c` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00c0e050"></a> `00c0e050` | `5f 55 00 f1` | cmp x10,#0x15 | `FALL_THROUGH`
<a id="insn-00c0e054"></a> `00c0e054` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00c0e058"></a> `00c0e058` | `6c 05 00 91` | add x12,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00c0e05c"></a> `00c0e05c` | `2c 01 00 f9` | str x12,[x9] | `FALL_THROUGH`
<a id="insn-00c0e060"></a> `00c0e060` | `68 01 00 39` | strb w8,[x11] | `FALL_THROUGH`
<a id="insn-00c0e064"></a> `00c0e064` | `2c f6 ff 54` | b.gt 0x00c0df28 | `CONDITIONAL_JUMP`
<a id="insn-00c0e068"></a> `00c0e068` | `88 02 40 b9` | ldr w8,[x20] | `FALL_THROUGH`
<a id="insn-00c0e06c"></a> `00c0e06c` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0e070"></a> `00c0e070` | `88 02 00 b9` | str w8,[x20] | `FALL_THROUGH`
<a id="insn-00c0e074"></a> `00c0e074` | `ad ff ff 17` | b 0x00c0df28 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00c0ddfc`](#insn-00c0ddfc) 範囲 `[['00c0ddfc', '00c0de2b']]`
  - `FALL_THROUGH` [`00c0de28`](#insn-00c0de28) → [`00c0de2c`](#insn-00c0de2c)
- ブロック [`00c0de2c`](#insn-00c0de2c) 範囲 `[['00c0de2c', '00c0de2f']]`
  - `CONDITIONAL_JUMP` [`00c0de2c`](#insn-00c0de2c) → [`00c0de8c`](#insn-00c0de8c)
  - `FALL_THROUGH` [`00c0de2c`](#insn-00c0de2c) → [`00c0de30`](#insn-00c0de30)
- ブロック [`00c0de30`](#insn-00c0de30) 範囲 `[['00c0de30', '00c0de37']]`
  - `CONDITIONAL_JUMP` [`00c0de34`](#insn-00c0de34) → [`00c0df1c`](#insn-00c0df1c)
  - `FALL_THROUGH` [`00c0de34`](#insn-00c0de34) → [`00c0de38`](#insn-00c0de38)
- ブロック [`00c0de38`](#insn-00c0de38) 範囲 `[['00c0de38', '00c0de47']]`
  - `FALL_THROUGH` [`00c0de44`](#insn-00c0de44) → [`00c0de48`](#insn-00c0de48)
- ブロック [`00c0de48`](#insn-00c0de48) 範囲 `[['00c0de48', '00c0de67']]`
  - `CONDITIONAL_JUMP` [`00c0de64`](#insn-00c0de64) → [`00c0df24`](#insn-00c0df24)
  - `FALL_THROUGH` [`00c0de64`](#insn-00c0de64) → [`00c0de68`](#insn-00c0de68)
- ブロック [`00c0de68`](#insn-00c0de68) 範囲 `[['00c0de68', '00c0de77']]`
  - `CONDITIONAL_JUMP` [`00c0de74`](#insn-00c0de74) → [`00c0df24`](#insn-00c0df24)
  - `FALL_THROUGH` [`00c0de74`](#insn-00c0de74) → [`00c0de78`](#insn-00c0de78)
- ブロック [`00c0de78`](#insn-00c0de78) 範囲 `[['00c0de78', '00c0de87']]`
  - `FALL_THROUGH` [`00c0de84`](#insn-00c0de84) → [`00c0de88`](#insn-00c0de88)
- ブロック [`00c0de88`](#insn-00c0de88) 範囲 `[['00c0de88', '00c0de8b']]`
  - `UNCONDITIONAL_JUMP` [`00c0de88`](#insn-00c0de88) → [`00c0df28`](#insn-00c0df28)
- ブロック [`00c0de8c`](#insn-00c0de8c) 範囲 `[['00c0de8c', '00c0de8f']]`
  - `FALL_THROUGH` [`00c0de8c`](#insn-00c0de8c) → [`00c0de90`](#insn-00c0de90)
- ブロック [`00c0de90`](#insn-00c0de90) 範囲 `[['00c0de90', '00c0de93']]`
  - `CONDITIONAL_JUMP` [`00c0de90`](#insn-00c0de90) → [`00c0dedc`](#insn-00c0dedc)
  - `FALL_THROUGH` [`00c0de90`](#insn-00c0de90) → [`00c0de94`](#insn-00c0de94)
- ブロック [`00c0de94`](#insn-00c0de94) 範囲 `[['00c0de94', '00c0deab']]`
  - `CONDITIONAL_JUMP` [`00c0dea8`](#insn-00c0dea8) → [`00c0dedc`](#insn-00c0dedc)
  - `FALL_THROUGH` [`00c0dea8`](#insn-00c0dea8) → [`00c0deac`](#insn-00c0deac)
- ブロック [`00c0deac`](#insn-00c0deac) 範囲 `[['00c0deac', '00c0deb3']]`
  - `CONDITIONAL_JUMP` [`00c0deb0`](#insn-00c0deb0) → [`00c0df1c`](#insn-00c0df1c)
  - `FALL_THROUGH` [`00c0deb0`](#insn-00c0deb0) → [`00c0deb4`](#insn-00c0deb4)
- ブロック [`00c0deb4`](#insn-00c0deb4) 範囲 `[['00c0deb4', '00c0debb']]`
  - `FALL_THROUGH` [`00c0deb8`](#insn-00c0deb8) → [`00c0debc`](#insn-00c0debc)
- ブロック [`00c0debc`](#insn-00c0debc) 範囲 `[['00c0debc', '00c0dec3']]`
  - `CONDITIONAL_JUMP` [`00c0dec0`](#insn-00c0dec0) → [`00c0df24`](#insn-00c0df24)
  - `FALL_THROUGH` [`00c0dec0`](#insn-00c0dec0) → [`00c0dec4`](#insn-00c0dec4)
- ブロック [`00c0dec4`](#insn-00c0dec4) 範囲 `[['00c0dec4', '00c0dedb']]`
  - `UNCONDITIONAL_JUMP` [`00c0ded8`](#insn-00c0ded8) → [`00c0df28`](#insn-00c0df28)
- ブロック [`00c0dedc`](#insn-00c0dedc) 範囲 `[['00c0dedc', '00c0deef']]`
  - `FALL_THROUGH` [`00c0deec`](#insn-00c0deec) → [`00c0def0`](#insn-00c0def0)
- ブロック [`00c0def0`](#insn-00c0def0) 範囲 `[['00c0def0', '00c0def7']]`
  - `FALL_THROUGH` [`00c0def4`](#insn-00c0def4) → [`00c0def8`](#insn-00c0def8)
- ブロック [`00c0def8`](#insn-00c0def8) 範囲 `[['00c0def8', '00c0df1b']]`
  - `CONDITIONAL_JUMP` [`00c0df18`](#insn-00c0df18) → [`00c0df48`](#insn-00c0df48)
  - `FALL_THROUGH` [`00c0df18`](#insn-00c0df18) → [`00c0df1c`](#insn-00c0df1c)
- ブロック [`00c0df1c`](#insn-00c0df1c) 範囲 `[['00c0df1c', '00c0df23']]`
  - `UNCONDITIONAL_JUMP` [`00c0df20`](#insn-00c0df20) → [`00c0df28`](#insn-00c0df28)
- ブロック [`00c0df24`](#insn-00c0df24) 範囲 `[['00c0df24', '00c0df27']]`
  - `FALL_THROUGH` [`00c0df24`](#insn-00c0df24) → [`00c0df28`](#insn-00c0df28)
- ブロック [`00c0df28`](#insn-00c0df28) 範囲 `[['00c0df28', '00c0df47']]`
- ブロック [`00c0df48`](#insn-00c0df48) 範囲 `[['00c0df48', '00c0df4f']]`
  - `FALL_THROUGH` [`00c0df4c`](#insn-00c0df4c) → [`00c0df50`](#insn-00c0df50)
- ブロック [`00c0df50`](#insn-00c0df50) 範囲 `[['00c0df50', '00c0df5f']]`
  - `CONDITIONAL_JUMP` [`00c0df5c`](#insn-00c0df5c) → [`00c0dfbc`](#insn-00c0dfbc)
  - `FALL_THROUGH` [`00c0df5c`](#insn-00c0df5c) → [`00c0df60`](#insn-00c0df60)
- ブロック [`00c0df60`](#insn-00c0df60) 範囲 `[['00c0df60', '00c0df63']]`
  - `FALL_THROUGH` [`00c0df60`](#insn-00c0df60) → [`00c0df64`](#insn-00c0df64)
- ブロック [`00c0df64`](#insn-00c0df64) 範囲 `[['00c0df64', '00c0df6b']]`
  - `CONDITIONAL_JUMP` [`00c0df68`](#insn-00c0df68) → [`00c0dfdc`](#insn-00c0dfdc)
  - `FALL_THROUGH` [`00c0df68`](#insn-00c0df68) → [`00c0df6c`](#insn-00c0df6c)
- ブロック [`00c0df6c`](#insn-00c0df6c) 範囲 `[['00c0df6c', '00c0df77']]`
  - `CONDITIONAL_JUMP` [`00c0df74`](#insn-00c0df74) → [`00c0dfa8`](#insn-00c0dfa8)
  - `FALL_THROUGH` [`00c0df74`](#insn-00c0df74) → [`00c0df78`](#insn-00c0df78)
- ブロック [`00c0df78`](#insn-00c0df78) 範囲 `[['00c0df78', '00c0dfa7']]`
  - `CONDITIONAL_JUMP` [`00c0dfa4`](#insn-00c0dfa4) → [`00c0df1c`](#insn-00c0df1c)
  - `FALL_THROUGH` [`00c0dfa4`](#insn-00c0dfa4) → [`00c0dfa8`](#insn-00c0dfa8)
- ブロック [`00c0dfa8`](#insn-00c0dfa8) 範囲 `[['00c0dfa8', '00c0dfbb']]`
  - `UNCONDITIONAL_JUMP` [`00c0dfb8`](#insn-00c0dfb8) → [`00c0df28`](#insn-00c0df28)
- ブロック [`00c0dfbc`](#insn-00c0dfbc) 範囲 `[['00c0dfbc', '00c0dfdb']]`
  - `UNCONDITIONAL_JUMP` [`00c0dfd8`](#insn-00c0dfd8) → [`00c0df28`](#insn-00c0df28)
- ブロック [`00c0dfdc`](#insn-00c0dfdc) 範囲 `[['00c0dfdc', '00c0dff7']]`
  - `CONDITIONAL_JUMP` [`00c0dff4`](#insn-00c0dff4) → [`00c0e04c`](#insn-00c0e04c)
  - `FALL_THROUGH` [`00c0dff4`](#insn-00c0dff4) → [`00c0dff8`](#insn-00c0dff8)
- ブロック [`00c0dff8`](#insn-00c0dff8) 範囲 `[['00c0dff8', '00c0e007']]`
  - `FALL_THROUGH` [`00c0e004`](#insn-00c0e004) → [`00c0e008`](#insn-00c0e008)
- ブロック [`00c0e008`](#insn-00c0e008) 範囲 `[['00c0e008', '00c0e00b']]`
  - `FALL_THROUGH` [`00c0e008`](#insn-00c0e008) → [`00c0e00c`](#insn-00c0e00c)
- ブロック [`00c0e00c`](#insn-00c0e00c) 範囲 `[['00c0e00c', '00c0e00f']]`
  - `FALL_THROUGH` [`00c0e00c`](#insn-00c0e00c) → [`00c0e010`](#insn-00c0e010)
- ブロック [`00c0e010`](#insn-00c0e010) 範囲 `[['00c0e010', '00c0e013']]`
  - `CONDITIONAL_JUMP` [`00c0e010`](#insn-00c0e010) → [`00c0e04c`](#insn-00c0e04c)
  - `FALL_THROUGH` [`00c0e010`](#insn-00c0e010) → [`00c0e014`](#insn-00c0e014)
- ブロック [`00c0e014`](#insn-00c0e014) 範囲 `[['00c0e014', '00c0e01b']]`
  - `FALL_THROUGH` [`00c0e018`](#insn-00c0e018) → [`00c0e01c`](#insn-00c0e01c)
- ブロック [`00c0e01c`](#insn-00c0e01c) 範囲 `[['00c0e01c', '00c0e02f']]`
  - `CONDITIONAL_JUMP` [`00c0e02c`](#insn-00c0e02c) → [`00c0e04c`](#insn-00c0e04c)
  - `FALL_THROUGH` [`00c0e02c`](#insn-00c0e02c) → [`00c0e030`](#insn-00c0e030)
- ブロック [`00c0e030`](#insn-00c0e030) 範囲 `[['00c0e030', '00c0e033']]`
  - `FALL_THROUGH` [`00c0e030`](#insn-00c0e030) → [`00c0e034`](#insn-00c0e034)
- ブロック [`00c0e034`](#insn-00c0e034) 範囲 `[['00c0e034', '00c0e03f']]`
  - `CONDITIONAL_JUMP` [`00c0e03c`](#insn-00c0e03c) → [`00c0e04c`](#insn-00c0e04c)
  - `FALL_THROUGH` [`00c0e03c`](#insn-00c0e03c) → [`00c0e040`](#insn-00c0e040)
- ブロック [`00c0e040`](#insn-00c0e040) 範囲 `[['00c0e040', '00c0e04b']]`
  - `FALL_THROUGH` [`00c0e048`](#insn-00c0e048) → [`00c0e04c`](#insn-00c0e04c)
- ブロック [`00c0e04c`](#insn-00c0e04c) 範囲 `[['00c0e04c', '00c0e04f']]`
  - `FALL_THROUGH` [`00c0e04c`](#insn-00c0e04c) → [`00c0e050`](#insn-00c0e050)
- ブロック [`00c0e050`](#insn-00c0e050) 範囲 `[['00c0e050', '00c0e067']]`
  - `CONDITIONAL_JUMP` [`00c0e064`](#insn-00c0e064) → [`00c0df28`](#insn-00c0df28)
  - `FALL_THROUGH` [`00c0e064`](#insn-00c0e064) → [`00c0e068`](#insn-00c0e068)
- ブロック [`00c0e068`](#insn-00c0e068) 範囲 `[['00c0e068', '00c0e077']]`
  - `UNCONDITIONAL_JUMP` [`00c0e074`](#insn-00c0e074) → [`00c0df28`](#insn-00c0df28)

## 命令位置別の参照

- [`00c0de00`](#insn-00c0de00) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de04`](#insn-00c0de04) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de08`](#insn-00c0de08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de0c`](#insn-00c0de0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de10`](#insn-00c0de10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de14`](#insn-00c0de14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de1c`](#insn-00c0de1c) → `Stack[0x8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de24`](#insn-00c0de24) → `Stack[0x0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de2c`](#insn-00c0de2c) → [`00c0de8c`](#insn-00c0de8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de34`](#insn-00c0de34) → [`00c0df1c`](#insn-00c0df1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de64`](#insn-00c0de64) → [`00c0df24`](#insn-00c0df24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de74`](#insn-00c0de74) → [`00c0df24`](#insn-00c0df24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de88`](#insn-00c0de88) → [`00c0df28`](#insn-00c0df28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0de90`](#insn-00c0de90) → [`00c0dedc`](#insn-00c0dedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0dea8`](#insn-00c0dea8) → [`00c0dedc`](#insn-00c0dedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0deb0`](#insn-00c0deb0) → [`00c0df1c`](#insn-00c0df1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0dec0`](#insn-00c0dec0) → [`00c0df24`](#insn-00c0df24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ded8`](#insn-00c0ded8) → [`00c0df28`](#insn-00c0df28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0dedc`](#insn-00c0dedc) → `Stack[0x18]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df04`](#insn-00c0df04) → [`00c57bd0`](../00c57/00c57bd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57bd0` · 推定シンボル `None` · 推定型 `None`
- [`00c0df18`](#insn-00c0df18) → [`00c0df48`](#insn-00c0df48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df20`](#insn-00c0df20) → [`00c0df28`](#insn-00c0df28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df28`](#insn-00c0df28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df2c`](#insn-00c0df2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df30`](#insn-00c0df30) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df34`](#insn-00c0df34) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df38`](#insn-00c0df38) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df3c`](#insn-00c0df3c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df50`](#insn-00c0df50) → `00c9b7c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c0df58`](#insn-00c0df58) → `00310e5e`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk114__num_get_base5__srcE` · 推定型 `string`
- [`00c0df5c`](#insn-00c0df5c) → [`00c0dfbc`](#insn-00c0dfbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df68`](#insn-00c0df68) → [`00c0dfdc`](#insn-00c0dfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0df74`](#insn-00c0df74) → [`00c0dfa8`](#insn-00c0dfa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0dfa4`](#insn-00c0dfa4) → [`00c0df1c`](#insn-00c0df1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0dfb8`](#insn-00c0dfb8) → [`00c0df28`](#insn-00c0df28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0dfd8`](#insn-00c0dfd8) → [`00c0df28`](#insn-00c0df28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0dff4`](#insn-00c0dff4) → [`00c0e04c`](#insn-00c0e04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0e010`](#insn-00c0e010) → [`00c0e04c`](#insn-00c0e04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0e02c`](#insn-00c0e02c) → [`00c0e04c`](#insn-00c0e04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0e03c`](#insn-00c0e03c) → [`00c0e04c`](#insn-00c0e04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0e064`](#insn-00c0e064) → [`00c0df28`](#insn-00c0df28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0e074`](#insn-00c0e074) → [`00c0df28`](#insn-00c0df28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c0de00`](#insn-00c0de00)

~~~json
{
  "source": "00c0de00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de04`](#insn-00c0de04)

~~~json
{
  "source": "00c0de04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de08`](#insn-00c0de08)

~~~json
{
  "source": "00c0de08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de0c`](#insn-00c0de0c)

~~~json
{
  "source": "00c0de0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de10`](#insn-00c0de10)

~~~json
{
  "source": "00c0de10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de14`](#insn-00c0de14)

~~~json
{
  "source": "00c0de14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de1c`](#insn-00c0de1c)

~~~json
{
  "source": "00c0de1c",
  "target": "Stack[0x8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de24`](#insn-00c0de24)

~~~json
{
  "source": "00c0de24",
  "target": "Stack[0x0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de2c`](#insn-00c0de2c)

~~~json
{
  "source": "00c0de2c",
  "target": "00c0de8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de34`](#insn-00c0de34)

~~~json
{
  "source": "00c0de34",
  "target": "00c0df1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de64`](#insn-00c0de64)

~~~json
{
  "source": "00c0de64",
  "target": "00c0df24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de74`](#insn-00c0de74)

~~~json
{
  "source": "00c0de74",
  "target": "00c0df24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de88`](#insn-00c0de88)

~~~json
{
  "source": "00c0de88",
  "target": "00c0df28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0de90`](#insn-00c0de90)

~~~json
{
  "source": "00c0de90",
  "target": "00c0dedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0dea8`](#insn-00c0dea8)

~~~json
{
  "source": "00c0dea8",
  "target": "00c0dedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0deb0`](#insn-00c0deb0)

~~~json
{
  "source": "00c0deb0",
  "target": "00c0df1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0dec0`](#insn-00c0dec0)

~~~json
{
  "source": "00c0dec0",
  "target": "00c0df24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ded8`](#insn-00c0ded8)

~~~json
{
  "source": "00c0ded8",
  "target": "00c0df28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0dedc`](#insn-00c0dedc)

~~~json
{
  "source": "00c0dedc",
  "target": "Stack[0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df04`](#insn-00c0df04)

~~~json
{
  "source": "00c0df04",
  "target": "00c57bd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0df18`](#insn-00c0df18)

~~~json
{
  "source": "00c0df18",
  "target": "00c0df48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df20`](#insn-00c0df20)

~~~json
{
  "source": "00c0df20",
  "target": "00c0df28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df28`](#insn-00c0df28)

~~~json
{
  "source": "00c0df28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df2c`](#insn-00c0df2c)

~~~json
{
  "source": "00c0df2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df30`](#insn-00c0df30)

~~~json
{
  "source": "00c0df30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df34`](#insn-00c0df34)

~~~json
{
  "source": "00c0df34",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df38`](#insn-00c0df38)

~~~json
{
  "source": "00c0df38",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df3c`](#insn-00c0df3c)

~~~json
{
  "source": "00c0df3c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df50`](#insn-00c0df50)

~~~json
{
  "source": "00c0df50",
  "target": "00c9b7c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b7c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c0df58`](#insn-00c0df58)

~~~json
{
  "source": "00c0df58",
  "target": "00310e5e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00310e5e",
  "offset": 0,
  "size": 33,
  "datatype": "string",
  "bytes": "3031323334353637383961626364656641424344454678582b2d705069496e4e",
  "capture_start": "00310e5e",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00c0df5c`](#insn-00c0df5c)

~~~json
{
  "source": "00c0df5c",
  "target": "00c0dfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df68`](#insn-00c0df68)

~~~json
{
  "source": "00c0df68",
  "target": "00c0dfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0df74`](#insn-00c0df74)

~~~json
{
  "source": "00c0df74",
  "target": "00c0dfa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0dfa4`](#insn-00c0dfa4)

~~~json
{
  "source": "00c0dfa4",
  "target": "00c0df1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0dfb8`](#insn-00c0dfb8)

~~~json
{
  "source": "00c0dfb8",
  "target": "00c0df28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0dfd8`](#insn-00c0dfd8)

~~~json
{
  "source": "00c0dfd8",
  "target": "00c0df28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0dff4`](#insn-00c0dff4)

~~~json
{
  "source": "00c0dff4",
  "target": "00c0e04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0e010`](#insn-00c0e010)

~~~json
{
  "source": "00c0e010",
  "target": "00c0e04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0e02c`](#insn-00c0e02c)

~~~json
{
  "source": "00c0e02c",
  "target": "00c0e04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0e03c`](#insn-00c0e03c)

~~~json
{
  "source": "00c0e03c",
  "target": "00c0e04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0e064`](#insn-00c0e064)

~~~json
{
  "source": "00c0e064",
  "target": "00c0df28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0e074`](#insn-00c0e074)

~~~json
{
  "source": "00c0e074",
  "target": "00c0df28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
