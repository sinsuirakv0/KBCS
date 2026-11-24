# 00ab7cac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0161.md#review-eed2ca62cb98a36ba1bded07a933ae4e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ab7ea8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab7/00ab7ea8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-ec8136bd18dabade8a5b457843b7a938)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ab7cac",
  "name": "FUN_00ab7cac",
  "size": 540,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35006a8305655a0f6249d86bb946ef2acc38b3bec5b169c540eefea63a7ebd9b",
  "source_text_sha256": "35006a8305655a0f6249d86bb946ef2acc38b3bec5b169c540eefea63a7ebd9b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ab7cac",
        "00ab7ec7"
      ]
    ],
    "bytes_sha256": "cb815922742f3ea8976b9991d2d82461888b5ce783e1b8640d0c23061a9ad9f6",
    "instruction_count": 135,
    "instruction_bytes": 540,
    "body_bytes": 540,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0046c984](../0046c/0046c984.md)
- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [00800320](../00800/00800320.md)
- [00800338](../00800/00800338.md)
- [008005ec](../00800/008005ec.md)
- [008070c4](../00807/008070c4.md)
- [0085b294](../0085b/0085b294.md)
- [008b9134](../008b9/008b9134.md)
- [008b924c](../008b9/008b924c.md)
- [009dcca4](../009dc/009dcca4.md)
- [00ab8fbc](../00ab8/00ab8fbc.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3580 bytes

~~~c

void FUN_00ab7cac(long param_1,undefined8 *param_2)

{
  undefined4 *puVar1;
  int iVar2;
  long lVar3;
  int iVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  int iVar7;
  ulong uVar8;
  long lVar9;
  undefined8 uVar10;
  undefined1 auStack_78 [8];
  void *local_70;
  void *local_68;
  long local_48;
  
                    /* try { // try from 00ab7cb4 to 00bb7dbf has its CatchHandler @ 00ab7c48 */
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  uVar10 = *param_2;
  lVar9 = *(long *)(param_1 + 8);
  iVar4 = FUN_008b924c(uVar10);
  if ((iVar4 != 0) && (iVar4 = FUN_008b924c(uVar10), iVar4 != 2)) {
    iVar4 = FUN_0046c984(lVar9);
    iVar7 = *(int *)((long)&fde_table_entry_00333c08.data_loc + lVar9);
    if (iVar4 < 0) {
      iVar4 = iVar4 + 1;
    }
    iVar2 = iVar7 + 3;
    if (-1 < iVar7) {
      iVar2 = iVar7;
    }
    uVar8 = FUN_009dcca4(lVar9,(iVar7 % 4) * 0x7f + (iVar4 >> 1) + -0xf6,(iVar2 >> 2) * 0x5a + 0x150
                         ,0x70,0x58);
    if ((uVar8 & 1) != 0) {
      *(undefined1 *)((long)&fde_table_entry_00332a28.initial_loc + lVar9 + 1) = 1;
      uVar8 = FUN_0085b294(lVar9);
      if ((uVar8 & 1) != 0) {
        puVar1 = (undefined4 *)((long)&fde_table_entry_00333970.data_loc + lVar9);
                    /* catch() { ... } // from try @ 00ab7ca8 with catch @ 00ab7d78 */
        uVar5 = FUN_00800320(*puVar1);
        if (*(int *)(lVar9 + 0x8dc) == *(int *)((long)&fde_table_entry_00333c08.data_loc + lVar9)) {
          iVar4 = *(int *)(lVar9 + 0x8e4);
          *(undefined4 *)(lVar9 + 0x8dc) = 0xffffffff;
          uVar6 = FUN_00800338();
          uVar5 = FUN_008005ec(uVar5);
          iVar7 = FUN_008070c4(uVar6,uVar5,0,0);
          if (iVar7 < iVar4) {
            uVar10 = FUN_0047acb4();
            if (*(long *)(lVar3 + 0x28) == local_48) {
              FUN_0047cd94(uVar10,0xf,0);
              return;
            }
          }
          else {
            *(undefined1 *)(lVar9 + 0x921) = 1;
            *(undefined4 *)((long)&fde_table_entry_00331680.initial_loc + lVar9) =
                 *(undefined4 *)(lVar9 + 0x8e4);
            if (*(long *)(lVar3 + 0x28) == local_48) {
                    /* try { // try from 00ab7ea8 to 00bb7ec3 has its CatchHandler @ 00ab7ed4 */
              FUN_008b9134(uVar10);
              return;
            }
          }
          goto LAB_00ab7ec4;
        }
        FUN_00ab8fbc(auStack_78,&uleb128_0029a6e0 + lVar9,*puVar1,
                     *(undefined4 *)((long)&fde_table_entry_00333c08.initial_loc + lVar9));
        local_68 = local_70;
        *(undefined4 *)(lVar9 + 0x8e4) =
             (&DAT_00ca3d8c)
             [*(int *)((long)local_70 +
                      (long)*(int *)((long)&fde_table_entry_00333c08.data_loc + lVar9) * 4)];
        _ZdlPv(local_70);
        uVar5 = *(undefined4 *)((long)&fde_table_entry_00333c08.data_loc + lVar9);
        *(undefined4 *)(lVar9 + 0x8e0) = 0;
        *(undefined4 *)(lVar9 + 0x8dc) = uVar5;
        uVar10 = FUN_0047acb4();
        FUN_0047cd94(uVar10,10,0);
      }
    }
  }
                    /* try { // try from 00ab7e60 to 00bb7ea7 has its CatchHandler @ 00ab7e60
                       catch() { ... } // from try @ 00ab7e60 with catch @ 00ab7e60
                       catch() { ... } // from try @ 00ab7ec4 with catch @ 00ab7e60 */
  if (*(long *)(lVar3 + 0x28) == local_48) {
    return;
  }
LAB_00ab7ec4:
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00ab7ec4 to 00bb7ee7 has its CatchHandler @ 00ab7e60 */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ab7cac"></a> `00ab7cac` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00ab7cb0"></a> `00ab7cb0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ab7cb4"></a> `00ab7cb4` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ab7cb8"></a> `00ab7cb8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ab7cbc"></a> `00ab7cbc` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ab7cc0"></a> `00ab7cc0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ab7cc4"></a> `00ab7cc4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ab7cc8"></a> `00ab7cc8` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00ab7ccc"></a> `00ab7ccc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ab7cd0"></a> `00ab7cd0` | `34 00 40 f9` | ldr x20,[x1] | `FALL_THROUGH`
<a id="insn-00ab7cd4"></a> `00ab7cd4` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00ab7cd8"></a> `00ab7cd8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ab7cdc"></a> `00ab7cdc` | `5c 05 f8 97` | bl 0x008b924c | `UNCONDITIONAL_CALL`
<a id="insn-00ab7ce0"></a> `00ab7ce0` | `c0 0b 00 34` | cbz w0,0x00ab7e58 | `CONDITIONAL_JUMP`
<a id="insn-00ab7ce4"></a> `00ab7ce4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ab7ce8"></a> `00ab7ce8` | `59 05 f8 97` | bl 0x008b924c | `UNCONDITIONAL_CALL`
<a id="insn-00ab7cec"></a> `00ab7cec` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00ab7cf0"></a> `00ab7cf0` | `40 0b 00 54` | b.eq 0x00ab7e58 | `CONDITIONAL_JUMP`
<a id="insn-00ab7cf4"></a> `00ab7cf4` | `68 ce 4c 91` | add x8,x19,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab7cf8"></a> `00ab7cf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ab7cfc"></a> `00ab7cfc` | `15 21 30 91` | add x21,x8,#0xc08 | `FALL_THROUGH`
<a id="insn-00ab7d00"></a> `00ab7d00` | `21 d3 e6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-00ab7d04"></a> `00ab7d04` | `a8 06 40 b9` | ldr w8,[x21, #0x4] | `FALL_THROUGH`
<a id="insn-00ab7d08"></a> `00ab7d08` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ab7d0c"></a> `00ab7d0c` | `03 0e 80 52` | mov w3,#0x70 | `FALL_THROUGH`
<a id="insn-00ab7d10"></a> `00ab7d10` | `09 a4 80 1a` | cinc w9,w0,lt | `FALL_THROUGH`
<a id="insn-00ab7d14"></a> `00ab7d14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ab7d18"></a> `00ab7d18` | `04 0b 80 52` | mov w4,#0x58 | `FALL_THROUGH`
<a id="insn-00ab7d1c"></a> `00ab7d1c` | `0a 0d 00 11` | add w10,w8,#0x3 | `FALL_THROUGH`
<a id="insn-00ab7d20"></a> `00ab7d20` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00ab7d24"></a> `00ab7d24` | `4a b1 88 1a` | csel w10,w10,w8,lt | `FALL_THROUGH`
<a id="insn-00ab7d28"></a> `00ab7d28` | `4b 75 1e 12` | and w11,w10,#0xfffffffc | `FALL_THROUGH`
<a id="insn-00ab7d2c"></a> `00ab7d2c` | `4a 7d 02 13` | asr w10,w10,#0x2 | `FALL_THROUGH`
<a id="insn-00ab7d30"></a> `00ab7d30` | `08 01 0b 4b` | sub w8,w8,w11 | `FALL_THROUGH`
<a id="insn-00ab7d34"></a> `00ab7d34` | `0b 61 19 53` | lsl w11,w8,#0x7 | `FALL_THROUGH`
<a id="insn-00ab7d38"></a> `00ab7d38` | `68 01 08 4b` | sub w8,w11,w8 | `FALL_THROUGH`
<a id="insn-00ab7d3c"></a> `00ab7d3c` | `4b 0b 80 52` | mov w11,#0x5a | `FALL_THROUGH`
<a id="insn-00ab7d40"></a> `00ab7d40` | `08 05 89 0b` | add w8,w8,w9, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00ab7d44"></a> `00ab7d44` | `09 2a 80 52` | mov w9,#0x150 | `FALL_THROUGH`
<a id="insn-00ab7d48"></a> `00ab7d48` | `42 25 0b 1b` | madd w2,w10,w11,w9 | `FALL_THROUGH`
<a id="insn-00ab7d4c"></a> `00ab7d4c` | `01 d9 03 51` | sub w1,w8,#0xf6 | `FALL_THROUGH`
<a id="insn-00ab7d50"></a> `00ab7d50` | `d5 93 fc 97` | bl 0x009dcca4 | `UNCONDITIONAL_CALL`
<a id="insn-00ab7d54"></a> `00ab7d54` | `20 08 00 36` | tbz w0,#0x0,0x00ab7e58 | `CONDITIONAL_JUMP`
<a id="insn-00ab7d58"></a> `00ab7d58` | `68 ca 4c 91` | add x8,x19,#0x332, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab7d5c"></a> `00ab7d5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ab7d60"></a> `00ab7d60` | `16 a5 28 91` | add x22,x8,#0xa29 | `FALL_THROUGH`
<a id="insn-00ab7d64"></a> `00ab7d64` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab7d68"></a> `00ab7d68` | `c8 02 00 39` | strb w8,[x22] | `FALL_THROUGH`
<a id="insn-00ab7d6c"></a> `00ab7d6c` | `4a 8d f6 97` | bl 0x0085b294 | `UNCONDITIONAL_CALL`
<a id="insn-00ab7d70"></a> `00ab7d70` | `40 07 00 36` | tbz w0,#0x0,0x00ab7e58 | `CONDITIONAL_JUMP`
<a id="insn-00ab7d74"></a> `00ab7d74` | `d6 2e 3d 91` | add x22,x22,#0xf4b | `FALL_THROUGH`
<a id="insn-00ab7d78"></a> `00ab7d78` | `c0 02 40 b9` | ldr w0,[x22] | `FALL_THROUGH`
<a id="insn-00ab7d7c"></a> `00ab7d7c` | `69 21 f5 97` | bl 0x00800320 | `UNCONDITIONAL_CALL`
<a id="insn-00ab7d80"></a> `00ab7d80` | `68 de 48 b9` | ldr w8,[x19, #0x8dc] | `FALL_THROUGH`
<a id="insn-00ab7d84"></a> `00ab7d84` | `a9 06 40 b9` | ldr w9,[x21, #0x4] | `FALL_THROUGH`
<a id="insn-00ab7d88"></a> `00ab7d88` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00ab7d8c"></a> `00ab7d8c` | `a1 03 00 54` | b.ne 0x00ab7e00 | `CONDITIONAL_JUMP`
<a id="insn-00ab7d90"></a> `00ab7d90` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab7d94"></a> `00ab7d94` | `78 e6 48 b9` | ldr w24,[x19, #0x8e4] | `FALL_THROUGH`
<a id="insn-00ab7d98"></a> `00ab7d98` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00ab7d9c"></a> `00ab7d9c` | `68 de 08 b9` | str w8,[x19, #0x8dc] | `FALL_THROUGH`
<a id="insn-00ab7da0"></a> `00ab7da0` | `66 21 f5 97` | bl 0x00800338 | `UNCONDITIONAL_CALL`
<a id="insn-00ab7da4"></a> `00ab7da4` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00ab7da8"></a> `00ab7da8` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00ab7dac"></a> `00ab7dac` | `10 22 f5 97` | bl 0x008005ec | `UNCONDITIONAL_CALL`
<a id="insn-00ab7db0"></a> `00ab7db0` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00ab7db4"></a> `00ab7db4` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00ab7db8"></a> `00ab7db8` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00ab7dbc"></a> `00ab7dbc` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00ab7dc0"></a> `00ab7dc0` | `c1 3c f5 97` | bl 0x008070c4 | `UNCONDITIONAL_CALL`
<a id="insn-00ab7dc4"></a> `00ab7dc4` | `1f 03 00 6b` | cmp w24,w0 | `FALL_THROUGH`
<a id="insn-00ab7dc8"></a> `00ab7dc8` | `cd 05 00 54` | b.le 0x00ab7e80 | `CONDITIONAL_JUMP`
<a id="insn-00ab7dcc"></a> `00ab7dcc` | `ba 0b e7 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00ab7dd0"></a> `00ab7dd0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00ab7dd4"></a> `00ab7dd4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ab7dd8"></a> `00ab7dd8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab7ddc"></a> `00ab7ddc` | `41 07 00 54` | b.ne 0x00ab7ec4 | `CONDITIONAL_JUMP`
<a id="insn-00ab7de0"></a> `00ab7de0` | `e1 01 80 52` | mov w1,#0xf | `FALL_THROUGH`
<a id="insn-00ab7de4"></a> `00ab7de4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ab7de8"></a> `00ab7de8` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ab7dec"></a> `00ab7dec` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ab7df0"></a> `00ab7df0` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ab7df4"></a> `00ab7df4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ab7df8"></a> `00ab7df8` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00ab7dfc"></a> `00ab7dfc` | `e6 13 e7 17` | b 0x0047cd94 | `CALL_TERMINATOR`
<a id="insn-00ab7e00"></a> `00ab7e00` | `c1 02 40 b9` | ldr w1,[x22] | `FALL_THROUGH`
<a id="insn-00ab7e04"></a> `00ab7e04` | `a2 02 40 b9` | ldr w2,[x21] | `FALL_THROUGH`
<a id="insn-00ab7e08"></a> `00ab7e08` | `69 6a 4a 91` | add x9,x19,#0x29a, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab7e0c"></a> `00ab7e0c` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ab7e10"></a> `00ab7e10` | `20 81 1b 91` | add x0,x9,#0x6e0 | `FALL_THROUGH`
<a id="insn-00ab7e14"></a> `00ab7e14` | `6a 04 00 94` | bl 0x00ab8fbc | `UNCONDITIONAL_CALL`
<a id="insn-00ab7e18"></a> `00ab7e18` | `a8 06 80 b9` | ldrsw x8,[x21, #0x4] | `FALL_THROUGH`
<a id="insn-00ab7e1c"></a> `00ab7e1c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab7e20"></a> `00ab7e20` | `69 0f 00 90` | adrp x9,0xca3000 | `FALL_THROUGH`
<a id="insn-00ab7e24"></a> `00ab7e24` | `29 31 36 91` | add x9,x9,#0xd8c | `FALL_THROUGH`
<a id="insn-00ab7e28"></a> `00ab7e28` | `08 78 a8 b8` | ldrsw x8,[x0, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ab7e2c"></a> `00ab7e2c` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ab7e30"></a> `00ab7e30` | `28 79 68 b8` | ldr w8,[x9, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ab7e34"></a> `00ab7e34` | `68 e6 08 b9` | str w8,[x19, #0x8e4] | `FALL_THROUGH`
<a id="insn-00ab7e38"></a> `00ab7e38` | `1e 7f 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab7e3c"></a> `00ab7e3c` | `a8 06 40 b9` | ldr w8,[x21, #0x4] | `FALL_THROUGH`
<a id="insn-00ab7e40"></a> `00ab7e40` | `7f e2 08 b9` | str wzr,[x19, #0x8e0] | `FALL_THROUGH`
<a id="insn-00ab7e44"></a> `00ab7e44` | `68 de 08 b9` | str w8,[x19, #0x8dc] | `FALL_THROUGH`
<a id="insn-00ab7e48"></a> `00ab7e48` | `9b 0b e7 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00ab7e4c"></a> `00ab7e4c` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00ab7e50"></a> `00ab7e50` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ab7e54"></a> `00ab7e54` | `d0 13 e7 97` | bl 0x0047cd94 | `UNCONDITIONAL_CALL`
<a id="insn-00ab7e58"></a> `00ab7e58` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00ab7e5c"></a> `00ab7e5c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ab7e60"></a> `00ab7e60` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab7e64"></a> `00ab7e64` | `01 03 00 54` | b.ne 0x00ab7ec4 | `CONDITIONAL_JUMP`
<a id="insn-00ab7e68"></a> `00ab7e68` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ab7e6c"></a> `00ab7e6c` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ab7e70"></a> `00ab7e70` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ab7e74"></a> `00ab7e74` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ab7e78"></a> `00ab7e78` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00ab7e7c"></a> `00ab7e7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ab7e80"></a> `00ab7e80` | `08 d0 82 52` | mov w8,#0x1680 | `FALL_THROUGH`
<a id="insn-00ab7e84"></a> `00ab7e84` | `69 e6 48 b9` | ldr w9,[x19, #0x8e4] | `FALL_THROUGH`
<a id="insn-00ab7e88"></a> `00ab7e88` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00ab7e8c"></a> `00ab7e8c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab7e90"></a> `00ab7e90` | `6a 86 24 39` | strb w10,[x19, #0x921] | `FALL_THROUGH`
<a id="insn-00ab7e94"></a> `00ab7e94` | `69 6a 28 b8` | str w9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab7e98"></a> `00ab7e98` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00ab7e9c"></a> `00ab7e9c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ab7ea0"></a> `00ab7ea0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab7ea4"></a> `00ab7ea4` | `01 01 00 54` | b.ne 0x00ab7ec4 | `CONDITIONAL_JUMP`
<a id="insn-00ab7ea8"></a> `00ab7ea8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ab7eac"></a> `00ab7eac` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ab7eb0"></a> `00ab7eb0` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ab7eb4"></a> `00ab7eb4` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ab7eb8"></a> `00ab7eb8` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ab7ebc"></a> `00ab7ebc` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00ab7ec0"></a> `00ab7ec0` | `9d 04 f8 17` | b 0x008b9134 | `CALL_TERMINATOR`
<a id="insn-00ab7ec4"></a> `00ab7ec4` | `07 7f 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ab7cac`](#insn-00ab7cac) 範囲 `[['00ab7cac', '00ab7cb3']]`
  - `FALL_THROUGH` [`00ab7cb0`](#insn-00ab7cb0) → [`00ab7cb4`](#insn-00ab7cb4)
- ブロック [`00ab7cb4`](#insn-00ab7cb4) 範囲 `[['00ab7cb4', '00ab7ce3']]`
  - `CONDITIONAL_JUMP` [`00ab7ce0`](#insn-00ab7ce0) → [`00ab7e58`](#insn-00ab7e58)
  - `FALL_THROUGH` [`00ab7ce0`](#insn-00ab7ce0) → [`00ab7ce4`](#insn-00ab7ce4)
- ブロック [`00ab7ce4`](#insn-00ab7ce4) 範囲 `[['00ab7ce4', '00ab7cf3']]`
  - `CONDITIONAL_JUMP` [`00ab7cf0`](#insn-00ab7cf0) → [`00ab7e58`](#insn-00ab7e58)
  - `FALL_THROUGH` [`00ab7cf0`](#insn-00ab7cf0) → [`00ab7cf4`](#insn-00ab7cf4)
- ブロック [`00ab7cf4`](#insn-00ab7cf4) 範囲 `[['00ab7cf4', '00ab7d57']]`
  - `CONDITIONAL_JUMP` [`00ab7d54`](#insn-00ab7d54) → [`00ab7e58`](#insn-00ab7e58)
  - `FALL_THROUGH` [`00ab7d54`](#insn-00ab7d54) → [`00ab7d58`](#insn-00ab7d58)
- ブロック [`00ab7d58`](#insn-00ab7d58) 範囲 `[['00ab7d58', '00ab7d73']]`
  - `CONDITIONAL_JUMP` [`00ab7d70`](#insn-00ab7d70) → [`00ab7e58`](#insn-00ab7e58)
  - `FALL_THROUGH` [`00ab7d70`](#insn-00ab7d70) → [`00ab7d74`](#insn-00ab7d74)
- ブロック [`00ab7d74`](#insn-00ab7d74) 範囲 `[['00ab7d74', '00ab7d77']]`
  - `FALL_THROUGH` [`00ab7d74`](#insn-00ab7d74) → [`00ab7d78`](#insn-00ab7d78)
- ブロック [`00ab7d78`](#insn-00ab7d78) 範囲 `[['00ab7d78', '00ab7d8f']]`
  - `CONDITIONAL_JUMP` [`00ab7d8c`](#insn-00ab7d8c) → [`00ab7e00`](#insn-00ab7e00)
  - `FALL_THROUGH` [`00ab7d8c`](#insn-00ab7d8c) → [`00ab7d90`](#insn-00ab7d90)
- ブロック [`00ab7d90`](#insn-00ab7d90) 範囲 `[['00ab7d90', '00ab7dcb']]`
  - `CONDITIONAL_JUMP` [`00ab7dc8`](#insn-00ab7dc8) → [`00ab7e80`](#insn-00ab7e80)
  - `FALL_THROUGH` [`00ab7dc8`](#insn-00ab7dc8) → [`00ab7dcc`](#insn-00ab7dcc)
- ブロック [`00ab7dcc`](#insn-00ab7dcc) 範囲 `[['00ab7dcc', '00ab7ddf']]`
  - `CONDITIONAL_JUMP` [`00ab7ddc`](#insn-00ab7ddc) → [`00ab7ec4`](#insn-00ab7ec4)
  - `FALL_THROUGH` [`00ab7ddc`](#insn-00ab7ddc) → [`00ab7de0`](#insn-00ab7de0)
- ブロック [`00ab7de0`](#insn-00ab7de0) 範囲 `[['00ab7de0', '00ab7dff']]`
- ブロック [`00ab7e00`](#insn-00ab7e00) 範囲 `[['00ab7e00', '00ab7e57']]`
  - `FALL_THROUGH` [`00ab7e54`](#insn-00ab7e54) → [`00ab7e58`](#insn-00ab7e58)
- ブロック [`00ab7e58`](#insn-00ab7e58) 範囲 `[['00ab7e58', '00ab7e5f']]`
  - `FALL_THROUGH` [`00ab7e5c`](#insn-00ab7e5c) → [`00ab7e60`](#insn-00ab7e60)
- ブロック [`00ab7e60`](#insn-00ab7e60) 範囲 `[['00ab7e60', '00ab7e67']]`
  - `CONDITIONAL_JUMP` [`00ab7e64`](#insn-00ab7e64) → [`00ab7ec4`](#insn-00ab7ec4)
  - `FALL_THROUGH` [`00ab7e64`](#insn-00ab7e64) → [`00ab7e68`](#insn-00ab7e68)
- ブロック [`00ab7e68`](#insn-00ab7e68) 範囲 `[['00ab7e68', '00ab7e7f']]`
- ブロック [`00ab7e80`](#insn-00ab7e80) 範囲 `[['00ab7e80', '00ab7ea7']]`
  - `CONDITIONAL_JUMP` [`00ab7ea4`](#insn-00ab7ea4) → [`00ab7ec4`](#insn-00ab7ec4)
  - `FALL_THROUGH` [`00ab7ea4`](#insn-00ab7ea4) → [`00ab7ea8`](#insn-00ab7ea8)
- ブロック [`00ab7ea8`](#insn-00ab7ea8) 範囲 `[['00ab7ea8', '00ab7ec3']]`
- ブロック [`00ab7ec4`](#insn-00ab7ec4) 範囲 `[['00ab7ec4', '00ab7ec7']]`

## 命令位置別の参照

- [`00ab7cb0`](#insn-00ab7cb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7cb4`](#insn-00ab7cb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7cb8`](#insn-00ab7cb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7cbc`](#insn-00ab7cbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7ccc`](#insn-00ab7ccc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7cdc`](#insn-00ab7cdc) → [`008b924c`](../008b9/008b924c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b924c` · 推定シンボル `None` · 推定型 `None`
- [`00ab7ce0`](#insn-00ab7ce0) → [`00ab7e58`](#insn-00ab7e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7ce8`](#insn-00ab7ce8) → [`008b924c`](../008b9/008b924c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b924c` · 推定シンボル `None` · 推定型 `None`
- [`00ab7cf0`](#insn-00ab7cf0) → [`00ab7e58`](#insn-00ab7e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7d00`](#insn-00ab7d00) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`00ab7d04`](#insn-00ab7d04) → `00333c0c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab7d50`](#insn-00ab7d50) → [`009dcca4`](../009dc/009dcca4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009dcca4` · 推定シンボル `None` · 推定型 `None`
- [`00ab7d54`](#insn-00ab7d54) → [`00ab7e58`](#insn-00ab7e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7d68`](#insn-00ab7d68) → `00332a29`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab7d6c`](#insn-00ab7d6c) → [`0085b294`](../0085b/0085b294.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b294` · 推定シンボル `None` · 推定型 `None`
- [`00ab7d70`](#insn-00ab7d70) → [`00ab7e58`](#insn-00ab7e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7d78`](#insn-00ab7d78) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab7d7c`](#insn-00ab7d7c) → [`00800320`](../00800/00800320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00800320` · 推定シンボル `None` · 推定型 `None`
- [`00ab7d84`](#insn-00ab7d84) → `00333c0c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab7d8c`](#insn-00ab7d8c) → [`00ab7e00`](#insn-00ab7e00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7da0`](#insn-00ab7da0) → [`00800338`](../00800/00800338.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00800338` · 推定シンボル `None` · 推定型 `None`
- [`00ab7dac`](#insn-00ab7dac) → [`008005ec`](../00800/008005ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008005ec` · 推定シンボル `None` · 推定型 `None`
- [`00ab7dc0`](#insn-00ab7dc0) → [`008070c4`](../00807/008070c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008070c4` · 推定シンボル `None` · 推定型 `None`
- [`00ab7dc8`](#insn-00ab7dc8) → [`00ab7e80`](#insn-00ab7e80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7dcc`](#insn-00ab7dcc) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00ab7dd4`](#insn-00ab7dd4) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7ddc`](#insn-00ab7ddc) → [`00ab7ec4`](#insn-00ab7ec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7de8`](#insn-00ab7de8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7dec`](#insn-00ab7dec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7df0`](#insn-00ab7df0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7df4`](#insn-00ab7df4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7dfc`](#insn-00ab7dfc) → [`0047cd94`](../0047c/0047cd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cd94` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e00`](#insn-00ab7e00) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab7e04`](#insn-00ab7e04) → `00333c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab7e14`](#insn-00ab7e14) → [`00ab8fbc`](../00ab8/00ab8fbc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab8fbc` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e18`](#insn-00ab7e18) → `00333c0c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab7e1c`](#insn-00ab7e1c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e2c`](#insn-00ab7e2c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e30`](#insn-00ab7e30) → `00ca3d8c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00ab7e38`](#insn-00ab7e38) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e3c`](#insn-00ab7e3c) → `00333c0c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab7e48`](#insn-00ab7e48) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e54`](#insn-00ab7e54) → [`0047cd94`](../0047c/0047cd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cd94` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e5c`](#insn-00ab7e5c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e64`](#insn-00ab7e64) → [`00ab7ec4`](#insn-00ab7ec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e68`](#insn-00ab7e68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e6c`](#insn-00ab7e6c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e70`](#insn-00ab7e70) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e74`](#insn-00ab7e74) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7e94`](#insn-00ab7e94) → `00331680`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab7e9c`](#insn-00ab7e9c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7ea4`](#insn-00ab7ea4) → [`00ab7ec4`](#insn-00ab7ec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7eac`](#insn-00ab7eac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7eb0`](#insn-00ab7eb0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7eb4`](#insn-00ab7eb4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7eb8`](#insn-00ab7eb8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab7ec0`](#insn-00ab7ec0) → [`008b9134`](../008b9/008b9134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9134` · 推定シンボル `None` · 推定型 `None`
- [`00ab7ec4`](#insn-00ab7ec4) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ab7cb0`](#insn-00ab7cb0)

~~~json
{
  "source": "00ab7cb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7cb4`](#insn-00ab7cb4)

~~~json
{
  "source": "00ab7cb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7cb8`](#insn-00ab7cb8)

~~~json
{
  "source": "00ab7cb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7cbc`](#insn-00ab7cbc)

~~~json
{
  "source": "00ab7cbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7ccc`](#insn-00ab7ccc)

~~~json
{
  "source": "00ab7ccc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7cdc`](#insn-00ab7cdc)

~~~json
{
  "source": "00ab7cdc",
  "target": "008b924c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7ce0`](#insn-00ab7ce0)

~~~json
{
  "source": "00ab7ce0",
  "target": "00ab7e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7ce8`](#insn-00ab7ce8)

~~~json
{
  "source": "00ab7ce8",
  "target": "008b924c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7cf0`](#insn-00ab7cf0)

~~~json
{
  "source": "00ab7cf0",
  "target": "00ab7e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7d00`](#insn-00ab7d00)

~~~json
{
  "source": "00ab7d00",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7d04`](#insn-00ab7d04)

~~~json
{
  "source": "00ab7d04",
  "target": "00333c0c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333c08",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6ceb6a00201d1100",
  "capture_start": "00333c08",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab7d50`](#insn-00ab7d50)

~~~json
{
  "source": "00ab7d50",
  "target": "009dcca4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7d54`](#insn-00ab7d54)

~~~json
{
  "source": "00ab7d54",
  "target": "00ab7e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7d68`](#insn-00ab7d68)

~~~json
{
  "source": "00ab7d68",
  "target": "00332a29",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "3cf9680098480900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab7d6c`](#insn-00ab7d6c)

~~~json
{
  "source": "00ab7d6c",
  "target": "0085b294",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7d70`](#insn-00ab7d70)

~~~json
{
  "source": "00ab7d70",
  "target": "00ab7e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7d78`](#insn-00ab7d78)

~~~json
{
  "source": "00ab7d78",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4c06a0040780900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab7d7c`](#insn-00ab7d7c)

~~~json
{
  "source": "00ab7d7c",
  "target": "00800320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7d84`](#insn-00ab7d84)

~~~json
{
  "source": "00ab7d84",
  "target": "00333c0c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333c08",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6ceb6a00201d1100",
  "capture_start": "00333c08",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab7d8c`](#insn-00ab7d8c)

~~~json
{
  "source": "00ab7d8c",
  "target": "00ab7e00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7da0`](#insn-00ab7da0)

~~~json
{
  "source": "00ab7da0",
  "target": "00800338",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7dac`](#insn-00ab7dac)

~~~json
{
  "source": "00ab7dac",
  "target": "008005ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7dc0`](#insn-00ab7dc0)

~~~json
{
  "source": "00ab7dc0",
  "target": "008070c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7dc8`](#insn-00ab7dc8)

~~~json
{
  "source": "00ab7dc8",
  "target": "00ab7e80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7dcc`](#insn-00ab7dcc)

~~~json
{
  "source": "00ab7dcc",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7dd4`](#insn-00ab7dd4)

~~~json
{
  "source": "00ab7dd4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7ddc`](#insn-00ab7ddc)

~~~json
{
  "source": "00ab7ddc",
  "target": "00ab7ec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7de8`](#insn-00ab7de8)

~~~json
{
  "source": "00ab7de8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7dec`](#insn-00ab7dec)

~~~json
{
  "source": "00ab7dec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7df0`](#insn-00ab7df0)

~~~json
{
  "source": "00ab7df0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7df4`](#insn-00ab7df4)

~~~json
{
  "source": "00ab7df4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7dfc`](#insn-00ab7dfc)

~~~json
{
  "source": "00ab7dfc",
  "target": "0047cd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7e00`](#insn-00ab7e00)

~~~json
{
  "source": "00ab7e00",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4c06a0040780900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab7e04`](#insn-00ab7e04)

~~~json
{
  "source": "00ab7e04",
  "target": "00333c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333c08",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6ceb6a00201d1100",
  "capture_start": "00333c08",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab7e14`](#insn-00ab7e14)

~~~json
{
  "source": "00ab7e14",
  "target": "00ab8fbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7e18`](#insn-00ab7e18)

~~~json
{
  "source": "00ab7e18",
  "target": "00333c0c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333c08",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6ceb6a00201d1100",
  "capture_start": "00333c08",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab7e1c`](#insn-00ab7e1c)

~~~json
{
  "source": "00ab7e1c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7e2c`](#insn-00ab7e2c)

~~~json
{
  "source": "00ab7e2c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7e30`](#insn-00ab7e30)

~~~json
{
  "source": "00ab7e30",
  "target": "00ca3d8c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca3d8c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ab7e38`](#insn-00ab7e38)

~~~json
{
  "source": "00ab7e38",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7e3c`](#insn-00ab7e3c)

~~~json
{
  "source": "00ab7e3c",
  "target": "00333c0c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333c08",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6ceb6a00201d1100",
  "capture_start": "00333c08",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab7e48`](#insn-00ab7e48)

~~~json
{
  "source": "00ab7e48",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7e54`](#insn-00ab7e54)

~~~json
{
  "source": "00ab7e54",
  "target": "0047cd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7e5c`](#insn-00ab7e5c)

~~~json
{
  "source": "00ab7e5c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7e64`](#insn-00ab7e64)

~~~json
{
  "source": "00ab7e64",
  "target": "00ab7ec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7e68`](#insn-00ab7e68)

~~~json
{
  "source": "00ab7e68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7e6c`](#insn-00ab7e6c)

~~~json
{
  "source": "00ab7e6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7e70`](#insn-00ab7e70)

~~~json
{
  "source": "00ab7e70",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7e74`](#insn-00ab7e74)

~~~json
{
  "source": "00ab7e74",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7e94`](#insn-00ab7e94)

~~~json
{
  "source": "00ab7e94",
  "target": "00331680",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00331680",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e05b61008c050900",
  "capture_start": "00331680",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab7e9c`](#insn-00ab7e9c)

~~~json
{
  "source": "00ab7e9c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7ea4`](#insn-00ab7ea4)

~~~json
{
  "source": "00ab7ea4",
  "target": "00ab7ec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7eac`](#insn-00ab7eac)

~~~json
{
  "source": "00ab7eac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7eb0`](#insn-00ab7eb0)

~~~json
{
  "source": "00ab7eb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7eb4`](#insn-00ab7eb4)

~~~json
{
  "source": "00ab7eb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7eb8`](#insn-00ab7eb8)

~~~json
{
  "source": "00ab7eb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab7ec0`](#insn-00ab7ec0)

~~~json
{
  "source": "00ab7ec0",
  "target": "008b9134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab7ec4`](#insn-00ab7ec4)

~~~json
{
  "source": "00ab7ec4",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
