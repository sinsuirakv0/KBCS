# 00bcb1dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcadb4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcadb4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-ef2551f47c204698318a9892909c5340)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcb278`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb278.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-f0b86d1c9cdd5d02efe43db52fb5a1e9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb1dc",
  "name": "_ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE",
  "size": 272,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dfa9ec5a83ba8d411efb1aec999dec819d3ef069244fbcf1e1894d15bff76130",
  "source_text_sha256": "dfa9ec5a83ba8d411efb1aec999dec819d3ef069244fbcf1e1894d15bff76130",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb1dc",
        "00bcb2eb"
      ]
    ],
    "bytes_sha256": "2b0272ac0a07102fcdf04909cf7fe27c0b7b7184825800c10c659bc7a93911b2",
    "instruction_count": 68,
    "instruction_bytes": 272,
    "body_bytes": 272,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5da70](../00c5d/00c5da70.md)

## 呼び出し先

- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2382 bytes

~~~c

void _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE
               (long *param_1,long param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  
  lVar4 = *param_1;
  if (lVar4 != 0) {
    _ZN8firebase5Mutex7AcquireEv(lVar4 + 0x268);
    plVar3 = *(long **)(lVar4 + 0x230);
    plVar2 = *(long **)(lVar4 + 0x238);
    if (plVar2 != plVar3) {
      if (*plVar3 != param_2) {
        do {
          if (plVar2 + -1 == plVar3) goto LAB_00bcb270;
          plVar1 = plVar3 + 1;
          plVar3 = plVar3 + 1;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bcb2b0 with catch @ 00bcb240
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcb2e0 with catch @ 00bcb240
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcb314 with catch @ 00bcb240
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcb33c with catch @ 00bcb240
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcb368 with catch @ 00bcb240
                        */
        } while (*plVar1 != param_2);
      }
      if (plVar3 != plVar2) {
        if (plVar2 + -1 != plVar3) {
          *plVar3 = plVar2[-1];
          plVar2 = *(long **)(lVar4 + 0x238);
        }
        *(long **)(lVar4 + 0x238) = plVar2 + -1;
      }
    }
LAB_00bcb270:
    plVar3 = *(long **)(param_2 + 8);
    plVar2 = *(long **)(param_2 + 0x10);
    if (plVar2 != plVar3) {
      if ((long *)*plVar3 != param_1) {
        do {
          if (plVar2 + -1 == plVar3) goto LAB_00bcb2d4;
          plVar1 = plVar3 + 1;
          plVar3 = plVar3 + 1;
                    /* try { // try from 00bcb2a4 to 00ccb2af has its CatchHandler @ 00bcb3a4 */
        } while ((long *)*plVar1 != param_1);
      }
                    /* try { // try from 00bcb2b0 to 00ccb2d3 has its CatchHandler @ 00bcb240 */
      if (plVar3 != plVar2) {
        if (plVar2 + -1 != plVar3) {
          *plVar3 = plVar2[-1];
          plVar2 = *(long **)(param_2 + 0x10);
        }
        *(long **)(param_2 + 0x10) = plVar2 + -1;
      }
    }
LAB_00bcb2d4:
                    /* try { // try from 00bcb2d4 to 00ccb2df has its CatchHandler @ 00bcb3a4 */
    _ZN8firebase5Mutex7ReleaseEv(lVar4 + 0x268);
  }
                    /* try { // try from 00bcb2e0 to 00ccb307 has its CatchHandler @ 00bcb240 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcb1dc"></a> `00bcb1dc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcb1e0"></a> `00bcb1e0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb1e4"></a> `00bcb1e4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb1e8"></a> `00bcb1e8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcb1ec"></a> `00bcb1ec` | `16 00 40 f9` | ldr x22,[x0] | `FALL_THROUGH`
<a id="insn-00bcb1f0"></a> `00bcb1f0` | `76 07 00 b4` | cbz x22,0x00bcb2dc | `CONDITIONAL_JUMP`
<a id="insn-00bcb1f4"></a> `00bcb1f4` | `d4 a2 09 91` | add x20,x22,#0x268 | `FALL_THROUGH`
<a id="insn-00bcb1f8"></a> `00bcb1f8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcb1fc"></a> `00bcb1fc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcb200"></a> `00bcb200` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcb204"></a> `00bcb204` | `ff 3d 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb208"></a> `00bcb208` | `c9 1a 41 f9` | ldr x9,[x22, #0x230] | `FALL_THROUGH`
<a id="insn-00bcb20c"></a> `00bcb20c` | `c8 1e 41 f9` | ldr x8,[x22, #0x238] | `FALL_THROUGH`
<a id="insn-00bcb210"></a> `00bcb210` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcb214"></a> `00bcb214` | `e0 02 00 54` | b.eq 0x00bcb270 | `CONDITIONAL_JUMP`
<a id="insn-00bcb218"></a> `00bcb218` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcb21c"></a> `00bcb21c` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00bcb220"></a> `00bcb220` | `40 01 00 54` | b.eq 0x00bcb248 | `CONDITIONAL_JUMP`
<a id="insn-00bcb224"></a> `00bcb224` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcb228"></a> `00bcb228` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcb22c"></a> `00bcb22c` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bcb230"></a> `00bcb230` | `00 02 00 54` | b.eq 0x00bcb270 | `CONDITIONAL_JUMP`
<a id="insn-00bcb234"></a> `00bcb234` | `6c 05 40 f9` | ldr x12,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb238"></a> `00bcb238` | `69 21 00 91` | add x9,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bcb23c"></a> `00bcb23c` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcb240"></a> `00bcb240` | `9f 01 13 eb` | cmp x12,x19 | `FALL_THROUGH`
<a id="insn-00bcb244"></a> `00bcb244` | `41 ff ff 54` | b.ne 0x00bcb22c | `CONDITIONAL_JUMP`
<a id="insn-00bcb248"></a> `00bcb248` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcb24c"></a> `00bcb24c` | `20 01 00 54` | b.eq 0x00bcb270 | `CONDITIONAL_JUMP`
<a id="insn-00bcb250"></a> `00bcb250` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcb254"></a> `00bcb254` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcb258"></a> `00bcb258` | `80 00 00 54` | b.eq 0x00bcb268 | `CONDITIONAL_JUMP`
<a id="insn-00bcb25c"></a> `00bcb25c` | `48 01 40 f9` | ldr x8,[x10] | `FALL_THROUGH`
<a id="insn-00bcb260"></a> `00bcb260` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00bcb264"></a> `00bcb264` | `c8 1e 41 f9` | ldr x8,[x22, #0x238] | `FALL_THROUGH`
<a id="insn-00bcb268"></a> `00bcb268` | `08 21 00 d1` | sub x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcb26c"></a> `00bcb26c` | `c8 1e 01 f9` | str x8,[x22, #0x238] | `FALL_THROUGH`
<a id="insn-00bcb270"></a> `00bcb270` | `69 a2 40 a9` | ldp x9,x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb274"></a> `00bcb274` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcb278"></a> `00bcb278` | `e0 02 00 54` | b.eq 0x00bcb2d4 | `CONDITIONAL_JUMP`
<a id="insn-00bcb27c"></a> `00bcb27c` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcb280"></a> `00bcb280` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00bcb284"></a> `00bcb284` | `40 01 00 54` | b.eq 0x00bcb2ac | `CONDITIONAL_JUMP`
<a id="insn-00bcb288"></a> `00bcb288` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcb28c"></a> `00bcb28c` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcb290"></a> `00bcb290` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bcb294"></a> `00bcb294` | `00 02 00 54` | b.eq 0x00bcb2d4 | `CONDITIONAL_JUMP`
<a id="insn-00bcb298"></a> `00bcb298` | `6c 05 40 f9` | ldr x12,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb29c"></a> `00bcb29c` | `69 21 00 91` | add x9,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bcb2a0"></a> `00bcb2a0` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcb2a4"></a> `00bcb2a4` | `9f 01 15 eb` | cmp x12,x21 | `FALL_THROUGH`
<a id="insn-00bcb2a8"></a> `00bcb2a8` | `41 ff ff 54` | b.ne 0x00bcb290 | `CONDITIONAL_JUMP`
<a id="insn-00bcb2ac"></a> `00bcb2ac` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcb2b0"></a> `00bcb2b0` | `20 01 00 54` | b.eq 0x00bcb2d4 | `CONDITIONAL_JUMP`
<a id="insn-00bcb2b4"></a> `00bcb2b4` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcb2b8"></a> `00bcb2b8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcb2bc"></a> `00bcb2bc` | `80 00 00 54` | b.eq 0x00bcb2cc | `CONDITIONAL_JUMP`
<a id="insn-00bcb2c0"></a> `00bcb2c0` | `48 01 40 f9` | ldr x8,[x10] | `FALL_THROUGH`
<a id="insn-00bcb2c4"></a> `00bcb2c4` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00bcb2c8"></a> `00bcb2c8` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb2cc"></a> `00bcb2cc` | `08 21 00 d1` | sub x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcb2d0"></a> `00bcb2d0` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb2d4"></a> `00bcb2d4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcb2d8"></a> `00bcb2d8` | `ce 3d 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb2dc"></a> `00bcb2dc` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb2e0"></a> `00bcb2e0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb2e4"></a> `00bcb2e4` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcb2e8"></a> `00bcb2e8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb1dc`](#insn-00bcb1dc) 範囲 `[['00bcb1dc', '00bcb1f3']]`
  - `CONDITIONAL_JUMP` [`00bcb1f0`](#insn-00bcb1f0) → [`00bcb2dc`](#insn-00bcb2dc)
  - `FALL_THROUGH` [`00bcb1f0`](#insn-00bcb1f0) → [`00bcb1f4`](#insn-00bcb1f4)
- ブロック [`00bcb1f4`](#insn-00bcb1f4) 範囲 `[['00bcb1f4', '00bcb217']]`
  - `CONDITIONAL_JUMP` [`00bcb214`](#insn-00bcb214) → [`00bcb270`](#insn-00bcb270)
  - `FALL_THROUGH` [`00bcb214`](#insn-00bcb214) → [`00bcb218`](#insn-00bcb218)
- ブロック [`00bcb218`](#insn-00bcb218) 範囲 `[['00bcb218', '00bcb223']]`
  - `CONDITIONAL_JUMP` [`00bcb220`](#insn-00bcb220) → [`00bcb248`](#insn-00bcb248)
  - `FALL_THROUGH` [`00bcb220`](#insn-00bcb220) → [`00bcb224`](#insn-00bcb224)
- ブロック [`00bcb224`](#insn-00bcb224) 範囲 `[['00bcb224', '00bcb22b']]`
  - `FALL_THROUGH` [`00bcb228`](#insn-00bcb228) → [`00bcb22c`](#insn-00bcb22c)
- ブロック [`00bcb22c`](#insn-00bcb22c) 範囲 `[['00bcb22c', '00bcb233']]`
  - `CONDITIONAL_JUMP` [`00bcb230`](#insn-00bcb230) → [`00bcb270`](#insn-00bcb270)
  - `FALL_THROUGH` [`00bcb230`](#insn-00bcb230) → [`00bcb234`](#insn-00bcb234)
- ブロック [`00bcb234`](#insn-00bcb234) 範囲 `[['00bcb234', '00bcb23f']]`
  - `FALL_THROUGH` [`00bcb23c`](#insn-00bcb23c) → [`00bcb240`](#insn-00bcb240)
- ブロック [`00bcb240`](#insn-00bcb240) 範囲 `[['00bcb240', '00bcb247']]`
  - `CONDITIONAL_JUMP` [`00bcb244`](#insn-00bcb244) → [`00bcb22c`](#insn-00bcb22c)
  - `FALL_THROUGH` [`00bcb244`](#insn-00bcb244) → [`00bcb248`](#insn-00bcb248)
- ブロック [`00bcb248`](#insn-00bcb248) 範囲 `[['00bcb248', '00bcb24f']]`
  - `CONDITIONAL_JUMP` [`00bcb24c`](#insn-00bcb24c) → [`00bcb270`](#insn-00bcb270)
  - `FALL_THROUGH` [`00bcb24c`](#insn-00bcb24c) → [`00bcb250`](#insn-00bcb250)
- ブロック [`00bcb250`](#insn-00bcb250) 範囲 `[['00bcb250', '00bcb25b']]`
  - `CONDITIONAL_JUMP` [`00bcb258`](#insn-00bcb258) → [`00bcb268`](#insn-00bcb268)
  - `FALL_THROUGH` [`00bcb258`](#insn-00bcb258) → [`00bcb25c`](#insn-00bcb25c)
- ブロック [`00bcb25c`](#insn-00bcb25c) 範囲 `[['00bcb25c', '00bcb267']]`
  - `FALL_THROUGH` [`00bcb264`](#insn-00bcb264) → [`00bcb268`](#insn-00bcb268)
- ブロック [`00bcb268`](#insn-00bcb268) 範囲 `[['00bcb268', '00bcb26f']]`
  - `FALL_THROUGH` [`00bcb26c`](#insn-00bcb26c) → [`00bcb270`](#insn-00bcb270)
- ブロック [`00bcb270`](#insn-00bcb270) 範囲 `[['00bcb270', '00bcb27b']]`
  - `CONDITIONAL_JUMP` [`00bcb278`](#insn-00bcb278) → [`00bcb2d4`](#insn-00bcb2d4)
  - `FALL_THROUGH` [`00bcb278`](#insn-00bcb278) → [`00bcb27c`](#insn-00bcb27c)
- ブロック [`00bcb27c`](#insn-00bcb27c) 範囲 `[['00bcb27c', '00bcb287']]`
  - `CONDITIONAL_JUMP` [`00bcb284`](#insn-00bcb284) → [`00bcb2ac`](#insn-00bcb2ac)
  - `FALL_THROUGH` [`00bcb284`](#insn-00bcb284) → [`00bcb288`](#insn-00bcb288)
- ブロック [`00bcb288`](#insn-00bcb288) 範囲 `[['00bcb288', '00bcb28f']]`
  - `FALL_THROUGH` [`00bcb28c`](#insn-00bcb28c) → [`00bcb290`](#insn-00bcb290)
- ブロック [`00bcb290`](#insn-00bcb290) 範囲 `[['00bcb290', '00bcb297']]`
  - `CONDITIONAL_JUMP` [`00bcb294`](#insn-00bcb294) → [`00bcb2d4`](#insn-00bcb2d4)
  - `FALL_THROUGH` [`00bcb294`](#insn-00bcb294) → [`00bcb298`](#insn-00bcb298)
- ブロック [`00bcb298`](#insn-00bcb298) 範囲 `[['00bcb298', '00bcb2a3']]`
  - `FALL_THROUGH` [`00bcb2a0`](#insn-00bcb2a0) → [`00bcb2a4`](#insn-00bcb2a4)
- ブロック [`00bcb2a4`](#insn-00bcb2a4) 範囲 `[['00bcb2a4', '00bcb2ab']]`
  - `CONDITIONAL_JUMP` [`00bcb2a8`](#insn-00bcb2a8) → [`00bcb290`](#insn-00bcb290)
  - `FALL_THROUGH` [`00bcb2a8`](#insn-00bcb2a8) → [`00bcb2ac`](#insn-00bcb2ac)
- ブロック [`00bcb2ac`](#insn-00bcb2ac) 範囲 `[['00bcb2ac', '00bcb2af']]`
  - `FALL_THROUGH` [`00bcb2ac`](#insn-00bcb2ac) → [`00bcb2b0`](#insn-00bcb2b0)
- ブロック [`00bcb2b0`](#insn-00bcb2b0) 範囲 `[['00bcb2b0', '00bcb2b3']]`
  - `CONDITIONAL_JUMP` [`00bcb2b0`](#insn-00bcb2b0) → [`00bcb2d4`](#insn-00bcb2d4)
  - `FALL_THROUGH` [`00bcb2b0`](#insn-00bcb2b0) → [`00bcb2b4`](#insn-00bcb2b4)
- ブロック [`00bcb2b4`](#insn-00bcb2b4) 範囲 `[['00bcb2b4', '00bcb2bf']]`
  - `CONDITIONAL_JUMP` [`00bcb2bc`](#insn-00bcb2bc) → [`00bcb2cc`](#insn-00bcb2cc)
  - `FALL_THROUGH` [`00bcb2bc`](#insn-00bcb2bc) → [`00bcb2c0`](#insn-00bcb2c0)
- ブロック [`00bcb2c0`](#insn-00bcb2c0) 範囲 `[['00bcb2c0', '00bcb2cb']]`
  - `FALL_THROUGH` [`00bcb2c8`](#insn-00bcb2c8) → [`00bcb2cc`](#insn-00bcb2cc)
- ブロック [`00bcb2cc`](#insn-00bcb2cc) 範囲 `[['00bcb2cc', '00bcb2d3']]`
  - `FALL_THROUGH` [`00bcb2d0`](#insn-00bcb2d0) → [`00bcb2d4`](#insn-00bcb2d4)
- ブロック [`00bcb2d4`](#insn-00bcb2d4) 範囲 `[['00bcb2d4', '00bcb2db']]`
  - `FALL_THROUGH` [`00bcb2d8`](#insn-00bcb2d8) → [`00bcb2dc`](#insn-00bcb2dc)
- ブロック [`00bcb2dc`](#insn-00bcb2dc) 範囲 `[['00bcb2dc', '00bcb2df']]`
  - `FALL_THROUGH` [`00bcb2dc`](#insn-00bcb2dc) → [`00bcb2e0`](#insn-00bcb2e0)
- ブロック [`00bcb2e0`](#insn-00bcb2e0) 範囲 `[['00bcb2e0', '00bcb2eb']]`

## 命令位置別の参照

- [`00bcb1dc`](#insn-00bcb1dc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb1e0`](#insn-00bcb1e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb1e4`](#insn-00bcb1e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb1f0`](#insn-00bcb1f0) → [`00bcb2dc`](#insn-00bcb2dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb204`](#insn-00bcb204) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcb214`](#insn-00bcb214) → [`00bcb270`](#insn-00bcb270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb220`](#insn-00bcb220) → [`00bcb248`](#insn-00bcb248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb230`](#insn-00bcb230) → [`00bcb270`](#insn-00bcb270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb244`](#insn-00bcb244) → [`00bcb22c`](#insn-00bcb22c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb24c`](#insn-00bcb24c) → [`00bcb270`](#insn-00bcb270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb258`](#insn-00bcb258) → [`00bcb268`](#insn-00bcb268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb278`](#insn-00bcb278) → [`00bcb2d4`](#insn-00bcb2d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb284`](#insn-00bcb284) → [`00bcb2ac`](#insn-00bcb2ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb294`](#insn-00bcb294) → [`00bcb2d4`](#insn-00bcb2d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb2a8`](#insn-00bcb2a8) → [`00bcb290`](#insn-00bcb290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb2b0`](#insn-00bcb2b0) → [`00bcb2d4`](#insn-00bcb2d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb2bc`](#insn-00bcb2bc) → [`00bcb2cc`](#insn-00bcb2cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb2d8`](#insn-00bcb2d8) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bcb2dc`](#insn-00bcb2dc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb2e0`](#insn-00bcb2e0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb1dc`](#insn-00bcb1dc)

~~~json
{
  "source": "00bcb1dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb1e0`](#insn-00bcb1e0)

~~~json
{
  "source": "00bcb1e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb1e4`](#insn-00bcb1e4)

~~~json
{
  "source": "00bcb1e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb1f0`](#insn-00bcb1f0)

~~~json
{
  "source": "00bcb1f0",
  "target": "00bcb2dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb204`](#insn-00bcb204)

~~~json
{
  "source": "00bcb204",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb214`](#insn-00bcb214)

~~~json
{
  "source": "00bcb214",
  "target": "00bcb270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb220`](#insn-00bcb220)

~~~json
{
  "source": "00bcb220",
  "target": "00bcb248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb230`](#insn-00bcb230)

~~~json
{
  "source": "00bcb230",
  "target": "00bcb270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb244`](#insn-00bcb244)

~~~json
{
  "source": "00bcb244",
  "target": "00bcb22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb24c`](#insn-00bcb24c)

~~~json
{
  "source": "00bcb24c",
  "target": "00bcb270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb258`](#insn-00bcb258)

~~~json
{
  "source": "00bcb258",
  "target": "00bcb268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb278`](#insn-00bcb278)

~~~json
{
  "source": "00bcb278",
  "target": "00bcb2d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb284`](#insn-00bcb284)

~~~json
{
  "source": "00bcb284",
  "target": "00bcb2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb294`](#insn-00bcb294)

~~~json
{
  "source": "00bcb294",
  "target": "00bcb2d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb2a8`](#insn-00bcb2a8)

~~~json
{
  "source": "00bcb2a8",
  "target": "00bcb290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb2b0`](#insn-00bcb2b0)

~~~json
{
  "source": "00bcb2b0",
  "target": "00bcb2d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb2bc`](#insn-00bcb2bc)

~~~json
{
  "source": "00bcb2bc",
  "target": "00bcb2cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb2d8`](#insn-00bcb2d8)

~~~json
{
  "source": "00bcb2d8",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb2dc`](#insn-00bcb2dc)

~~~json
{
  "source": "00bcb2dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb2e0`](#insn-00bcb2e0)

~~~json
{
  "source": "00bcb2e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
