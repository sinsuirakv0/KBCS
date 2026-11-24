# 00aa9fec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aa8ff8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa8/00aa8ff8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0065.md#compare-ea4529990dd97a4c4ba25595c0f0f46a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa9fec",
  "name": "FUN_00aa9fec",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c7411e2e1d756415dfaa541f48ec0d8b0d90858882d1744240916f02fc22cc9",
  "source_text_sha256": "9c7411e2e1d756415dfaa541f48ec0d8b0d90858882d1744240916f02fc22cc9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa9fec",
        "00aaa15b"
      ],
      [
        "00aaa1e0",
        "00aaa1e3"
      ]
    ],
    "bytes_sha256": "92f875aeee6e94fb12d1229b1784eff033690162446c330642d78e8682e98770",
    "instruction_count": 93,
    "instruction_bytes": 372,
    "body_bytes": 372,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa4e88](../00aa4/00aa4e88.md)

## 呼び出し先

- [007846b4](../00784/007846b4.md)
- [008524fc](../00852/008524fc.md)
- [0087a2a0](../0087a/0087a2a0.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c590a0](../00c59/00c590a0.md)
- [00c5b8d0](../00c5b/00c5b8d0.md)
- [00c5b8e0](../00c5b/00c5b8e0.md)
- [00c5b990](../00c5b/00c5b990.md)

## 関連文字列（未確認候補）

~~~text
"BcResBeaconCharacter"
"BcResBeaconItem"
"CharaID"
"ItemID"
"sec1_id"
"sec1_type"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1907 bytes

~~~c

void FUN_00aa9fec(int param_1,int param_2)

{
  size_t __n;
  char *pcVar1;
  long lVar2;
  bool bVar3;
  long lVar4;
  undefined1 auStack_d0 [24];
  byte local_b8 [16];
  void *local_a8;
  undefined4 local_a0 [2];
  long local_98;
  char *local_88;
  undefined4 local_80 [2];
  undefined8 local_78;
  char *local_68;
  undefined4 local_60 [2];
  undefined8 local_58;
  long local_48;
  
  lVar2 = tpidr_el0;
  bVar3 = param_1 != 0x34;
  local_48 = *(long *)(lVar2 + 0x28);
  __n = 6;
  if (bVar3) {
    __n = 7;
  }
                    /* try { // try from 00aaa028 to 00baa0af has its CatchHandler @ 00aaa230 */
  pcVar1 = "ItemID";
  if (bVar3) {
    pcVar1 = "CharaID";
  }
  local_b8[0] = (byte)((int)__n << 1);
  lVar4 = 7;
  if (bVar3) {
    lVar4 = 8;
  }
  memcpy((void *)((ulong)local_b8 | 1),pcVar1,__n);
  local_b8[lVar4] = 0;
  FUN_007846b4(auStack_d0,local_b8);
  local_88 = "sec1_type";
  local_80[0] = 0;
  local_78 = 0;
  _ZN8firebase7VariantaSERKS0_(local_80,auStack_d0);
  local_60[0] = 0;
  local_68 = "sec1_id";
  local_58 = 0;
  local_a0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_a0,1);
  local_98 = (long)param_2;
                    /* try { // try from 00aaa0b0 to 00baa2ff has its CatchHandler @ 00aa9ed4 */
  _ZN8firebase7VariantaSEOS0_(local_60,local_a0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_a0,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_d0,0);
  lVar4 = FUN_008524fc();
  pcVar1 = "BcResBeaconItem";
  if (param_1 != 0x34) {
    pcVar1 = "BcResBeaconCharacter";
  }
  FUN_0087a2a0(*(undefined8 *)(lVar4 + 0x22b0),pcVar1,&local_88,2);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_60,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_80,0);
  if ((local_b8[0] & 1) != 0) {
    _ZdlPv(local_a8);
  }
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa9fec"></a> `00aa9fec` | `ff 43 03 d1` | sub sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aa9ff0"></a> `00aa9ff0` | `fd 7b 09 a9` | stp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aa9ff4"></a> `00aa9ff4` | `f7 53 00 f9` | str x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aa9ff8"></a> `00aa9ff8` | `f6 57 0b a9` | stp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aa9ffc"></a> `00aa9ffc` | `f4 4f 0c a9` | stp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aaa000"></a> `00aaa000` | `fd 43 02 91` | add x29,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aaa004"></a> `00aaa004` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aaa008"></a> `00aaa008` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00aaa00c"></a> `00aaa00c` | `f6 63 00 91` | add x22,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aaa010"></a> `00aaa010` | `1f d0 00 71` | cmp w0,#0x34 | `FALL_THROUGH`
<a id="insn-00aaa014"></a> `00aaa014` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aaa018"></a> `00aaa018` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aaa01c"></a> `00aaa01c` | `02 05 88 9a` | cinc x2,x8,ne | `FALL_THROUGH`
<a id="insn-00aaa020"></a> `00aaa020` | `e8 bf ff d0` | adrp x8,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aaa024"></a> `00aaa024` | `08 71 00 91` | add x8,x8,#0x1c | `FALL_THROUGH`
<a id="insn-00aaa028"></a> `00aaa028` | `4a 78 1f 53` | lsl w10,w2,#0x1 | `FALL_THROUGH`
<a id="insn-00aaa02c"></a> `00aaa02c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaa030"></a> `00aaa030` | `29 c0 ff d0` | adrp x9,0x2b0000 | `FALL_THROUGH`
<a id="insn-00aaa034"></a> `00aaa034` | `29 31 3e 91` | add x9,x9,#0xf8c | `FALL_THROUGH`
<a id="insn-00aaa038"></a> `00aaa038` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aaa03c"></a> `00aaa03c` | `c0 02 40 b2` | orr x0,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00aaa040"></a> `00aaa040` | `21 01 88 9a` | csel x1,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00aaa044"></a> `00aaa044` | `e8 00 80 52` | mov w8,#0x7 | `FALL_THROUGH`
<a id="insn-00aaa048"></a> `00aaa048` | `ea 63 00 39` | strb w10,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aaa04c"></a> `00aaa04c` | `17 05 88 9a` | cinc x23,x8,ne | `FALL_THROUGH`
<a id="insn-00aaa050"></a> `00aaa050` | `14 bc 06 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa054"></a> `00aaa054` | `df 6a 37 38` | strb wzr,[x22, x23, LSL ] | `FALL_THROUGH`
<a id="insn-00aaa058"></a> `00aaa058` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aaa05c"></a> `00aaa05c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aaa060"></a> `00aaa060` | `95 69 f3 97` | bl 0x007846b4 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa064"></a> `00aaa064` | `28 c0 ff 90` | adrp x8,0x2ae000 | `FALL_THROUGH`
<a id="insn-00aaa068"></a> `00aaa068` | `08 bd 2d 91` | add x8,x8,#0xb6f | `FALL_THROUGH`
<a id="insn-00aaa06c"></a> `00aaa06c` | `f6 23 01 91` | add x22,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aaa070"></a> `00aaa070` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aaa074"></a> `00aaa074` | `ff 53 00 b9` | str wzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aaa078"></a> `00aaa078` | `ff 2f 00 f9` | str xzr,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00aaa07c"></a> `00aaa07c` | `c0 22 00 91` | add x0,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aaa080"></a> `00aaa080` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aaa084"></a> `00aaa084` | `43 c6 06 94` | bl 0x00c5b990 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa088"></a> `00aaa088` | `28 c0 ff f0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00aaa08c"></a> `00aaa08c` | `08 0d 3b 91` | add x8,x8,#0xec3 | `FALL_THROUGH`
<a id="insn-00aaa090"></a> `00aaa090` | `ff 73 00 b9` | str wzr,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aaa094"></a> `00aaa094` | `e8 37 00 f9` | str x8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aaa098"></a> `00aaa098` | `ff 3f 00 f9` | str xzr,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aaa09c"></a> `00aaa09c` | `ff 33 00 b9` | str wzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaa0a0"></a> `00aaa0a0` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaa0a4"></a> `00aaa0a4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aaa0a8"></a> `00aaa0a8` | `0a c6 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa0ac"></a> `00aaa0ac` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00aaa0b0"></a> `00aaa0b0` | `c0 a2 00 91` | add x0,x22,#0x28 | `FALL_THROUGH`
<a id="insn-00aaa0b4"></a> `00aaa0b4` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaa0b8"></a> `00aaa0b8` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aaa0bc"></a> `00aaa0bc` | `09 c6 06 94` | bl 0x00c5b8e0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa0c0"></a> `00aaa0c0` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaa0c4"></a> `00aaa0c4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aaa0c8"></a> `00aaa0c8` | `02 c6 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa0cc"></a> `00aaa0cc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aaa0d0"></a> `00aaa0d0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aaa0d4"></a> `00aaa0d4` | `ff c5 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa0d8"></a> `00aaa0d8` | `09 a1 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aaa0dc"></a> `00aaa0dc` | `00 58 51 f9` | ldr x0,[x0, #0x22b0] | `FALL_THROUGH`
<a id="insn-00aaa0e0"></a> `00aaa0e0` | `88 c0 ff f0` | adrp x8,0x2bd000 | `FALL_THROUGH`
<a id="insn-00aaa0e4"></a> `00aaa0e4` | `08 5d 04 91` | add x8,x8,#0x117 | `FALL_THROUGH`
<a id="insn-00aaa0e8"></a> `00aaa0e8` | `7f d2 00 71` | cmp w19,#0x34 | `FALL_THROUGH`
<a id="insn-00aaa0ec"></a> `00aaa0ec` | `29 c0 ff b0` | adrp x9,0x2af000 | `FALL_THROUGH`
<a id="insn-00aaa0f0"></a> `00aaa0f0` | `29 35 09 91` | add x9,x9,#0x24d | `FALL_THROUGH`
<a id="insn-00aaa0f4"></a> `00aaa0f4` | `21 01 88 9a` | csel x1,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00aaa0f8"></a> `00aaa0f8` | `e2 23 01 91` | add x2,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aaa0fc"></a> `00aaa0fc` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00aaa100"></a> `00aaa100` | `f3 23 01 91` | add x19,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aaa104"></a> `00aaa104` | `67 40 f7 97` | bl 0x0087a2a0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa108"></a> `00aaa108` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00aaa10c"></a> `00aaa10c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aaa110"></a> `00aaa110` | `f0 c5 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa114"></a> `00aaa114` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aaa118"></a> `00aaa118` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00aaa11c"></a> `00aaa11c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aaa120"></a> `00aaa120` | `ec c5 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa124"></a> `00aaa124` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aaa128"></a> `00aaa128` | `68 00 00 36` | tbz w8,#0x0,0x00aaa134 | `CONDITIONAL_JUMP`
<a id="insn-00aaa12c"></a> `00aaa12c` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aaa130"></a> `00aaa130` | `88 bb 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa134"></a> `00aaa134` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aaa138"></a> `00aaa138` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaa13c"></a> `00aaa13c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aaa140"></a> `00aaa140` | `01 05 00 54` | b.ne 0x00aaa1e0 | `CONDITIONAL_JUMP`
<a id="insn-00aaa144"></a> `00aaa144` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aaa148"></a> `00aaa148` | `f7 53 40 f9` | ldr x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aaa14c"></a> `00aaa14c` | `f6 57 4b a9` | ldp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aaa150"></a> `00aaa150` | `fd 7b 49 a9` | ldp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aaa154"></a> `00aaa154` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aaa158"></a> `00aaa158` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aaa1e0"></a> `00aaa1e0` | `68 bb 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa9fec`](#insn-00aa9fec) 範囲 `[['00aa9fec', '00aaa027']]`
  - `FALL_THROUGH` [`00aaa024`](#insn-00aaa024) → [`00aaa028`](#insn-00aaa028)
- ブロック [`00aaa028`](#insn-00aaa028) 範囲 `[['00aaa028', '00aaa0af']]`
  - `FALL_THROUGH` [`00aaa0ac`](#insn-00aaa0ac) → [`00aaa0b0`](#insn-00aaa0b0)
- ブロック [`00aaa0b0`](#insn-00aaa0b0) 範囲 `[['00aaa0b0', '00aaa12b']]`
  - `CONDITIONAL_JUMP` [`00aaa128`](#insn-00aaa128) → [`00aaa134`](#insn-00aaa134)
  - `FALL_THROUGH` [`00aaa128`](#insn-00aaa128) → [`00aaa12c`](#insn-00aaa12c)
- ブロック [`00aaa12c`](#insn-00aaa12c) 範囲 `[['00aaa12c', '00aaa133']]`
  - `FALL_THROUGH` [`00aaa130`](#insn-00aaa130) → [`00aaa134`](#insn-00aaa134)
- ブロック [`00aaa134`](#insn-00aaa134) 範囲 `[['00aaa134', '00aaa143']]`
  - `CONDITIONAL_JUMP` [`00aaa140`](#insn-00aaa140) → [`00aaa1e0`](#insn-00aaa1e0)
  - `FALL_THROUGH` [`00aaa140`](#insn-00aaa140) → [`00aaa144`](#insn-00aaa144)
- ブロック [`00aaa144`](#insn-00aaa144) 範囲 `[['00aaa144', '00aaa15b']]`
- ブロック [`00aaa1e0`](#insn-00aaa1e0) 範囲 `[['00aaa1e0', '00aaa1e3']]`

## 命令位置別の参照

- [`00aa9ff0`](#insn-00aa9ff0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9ff4`](#insn-00aa9ff4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9ff8`](#insn-00aa9ff8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9ffc`](#insn-00aa9ffc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa02c`](#insn-00aaa02c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa040`](#insn-00aaa040) → `002a801c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaa040`](#insn-00aaa040) → `002b0f8c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaa048`](#insn-00aaa048) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa050`](#insn-00aaa050) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa060`](#insn-00aaa060) → [`007846b4`](../00784/007846b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007846b4` · 推定シンボル `None` · 推定型 `None`
- [`00aaa070`](#insn-00aaa070) → `002aeb6f`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaa070`](#insn-00aaa070) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa074`](#insn-00aaa074) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa078`](#insn-00aaa078) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa084`](#insn-00aaa084) → [`00c5b990`](../00c5b/00c5b990.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b990` · 推定シンボル `None` · 推定型 `None`
- [`00aaa090`](#insn-00aaa090) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa094`](#insn-00aaa094) → `002b1ec3`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaa094`](#insn-00aaa094) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa098`](#insn-00aaa098) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa09c`](#insn-00aaa09c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa0a8`](#insn-00aaa0a8) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa0b8`](#insn-00aaa0b8) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa0bc`](#insn-00aaa0bc) → [`00c5b8e0`](../00c5b/00c5b8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8e0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa0c8`](#insn-00aaa0c8) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa0d4`](#insn-00aaa0d4) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa0d8`](#insn-00aaa0d8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aaa0f4`](#insn-00aaa0f4) → `002bd117`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaa0f4`](#insn-00aaa0f4) → `002af24d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaa104`](#insn-00aaa104) → [`0087a2a0`](../0087a/0087a2a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087a2a0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa110`](#insn-00aaa110) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa120`](#insn-00aaa120) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa124`](#insn-00aaa124) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa128`](#insn-00aaa128) → [`00aaa134`](#insn-00aaa134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa12c`](#insn-00aaa12c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa130`](#insn-00aaa130) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00aaa138`](#insn-00aaa138) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa140`](#insn-00aaa140) → [`00aaa1e0`](#insn-00aaa1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa144`](#insn-00aaa144) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa148`](#insn-00aaa148) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa14c`](#insn-00aaa14c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa150`](#insn-00aaa150) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa1e0`](#insn-00aaa1e0) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa9ff0`](#insn-00aa9ff0)

~~~json
{
  "source": "00aa9ff0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9ff4`](#insn-00aa9ff4)

~~~json
{
  "source": "00aa9ff4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9ff8`](#insn-00aa9ff8)

~~~json
{
  "source": "00aa9ff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9ffc`](#insn-00aa9ffc)

~~~json
{
  "source": "00aa9ffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa02c`](#insn-00aaa02c)

~~~json
{
  "source": "00aaa02c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa040`](#insn-00aaa040)

~~~json
{
  "source": "00aaa040",
  "target": "002a801c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a801c",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "4368617261494400",
  "capture_start": "002a801c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaa040`](#insn-00aaa040)

~~~json
{
  "source": "00aaa040",
  "target": "002b0f8c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0f8c",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "4974656d494400",
  "capture_start": "002b0f8c",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaa048`](#insn-00aaa048)

~~~json
{
  "source": "00aaa048",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa050`](#insn-00aaa050)

~~~json
{
  "source": "00aaa050",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa060`](#insn-00aaa060)

~~~json
{
  "source": "00aaa060",
  "target": "007846b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa070`](#insn-00aaa070)

~~~json
{
  "source": "00aaa070",
  "target": "002aeb6f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeb6f",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563315f7479706500",
  "capture_start": "002aeb6f",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaa070`](#insn-00aaa070)

~~~json
{
  "source": "00aaa070",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa074`](#insn-00aaa074)

~~~json
{
  "source": "00aaa074",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa078`](#insn-00aaa078)

~~~json
{
  "source": "00aaa078",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa084`](#insn-00aaa084)

~~~json
{
  "source": "00aaa084",
  "target": "00c5b990",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa090`](#insn-00aaa090)

~~~json
{
  "source": "00aaa090",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa094`](#insn-00aaa094)

~~~json
{
  "source": "00aaa094",
  "target": "002b1ec3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1ec3",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563315f696400",
  "capture_start": "002b1ec3",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaa094`](#insn-00aaa094)

~~~json
{
  "source": "00aaa094",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa098`](#insn-00aaa098)

~~~json
{
  "source": "00aaa098",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa09c`](#insn-00aaa09c)

~~~json
{
  "source": "00aaa09c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa0a8`](#insn-00aaa0a8)

~~~json
{
  "source": "00aaa0a8",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa0b8`](#insn-00aaa0b8)

~~~json
{
  "source": "00aaa0b8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa0bc`](#insn-00aaa0bc)

~~~json
{
  "source": "00aaa0bc",
  "target": "00c5b8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa0c8`](#insn-00aaa0c8)

~~~json
{
  "source": "00aaa0c8",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa0d4`](#insn-00aaa0d4)

~~~json
{
  "source": "00aaa0d4",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa0d8`](#insn-00aaa0d8)

~~~json
{
  "source": "00aaa0d8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa0f4`](#insn-00aaa0f4)

~~~json
{
  "source": "00aaa0f4",
  "target": "002bd117",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bd117",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "4263526573426561636f6e43686172616374657200",
  "capture_start": "002bd117",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaa0f4`](#insn-00aaa0f4)

~~~json
{
  "source": "00aaa0f4",
  "target": "002af24d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af24d",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "4263526573426561636f6e4974656d00",
  "capture_start": "002af24d",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaa104`](#insn-00aaa104)

~~~json
{
  "source": "00aaa104",
  "target": "0087a2a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa110`](#insn-00aaa110)

~~~json
{
  "source": "00aaa110",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa120`](#insn-00aaa120)

~~~json
{
  "source": "00aaa120",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa124`](#insn-00aaa124)

~~~json
{
  "source": "00aaa124",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa128`](#insn-00aaa128)

~~~json
{
  "source": "00aaa128",
  "target": "00aaa134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa12c`](#insn-00aaa12c)

~~~json
{
  "source": "00aaa12c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa130`](#insn-00aaa130)

~~~json
{
  "source": "00aaa130",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa138`](#insn-00aaa138)

~~~json
{
  "source": "00aaa138",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa140`](#insn-00aaa140)

~~~json
{
  "source": "00aaa140",
  "target": "00aaa1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa144`](#insn-00aaa144)

~~~json
{
  "source": "00aaa144",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa148`](#insn-00aaa148)

~~~json
{
  "source": "00aaa148",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa14c`](#insn-00aaa14c)

~~~json
{
  "source": "00aaa14c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa150`](#insn-00aaa150)

~~~json
{
  "source": "00aaa150",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa1e0`](#insn-00aaa1e0)

~~~json
{
  "source": "00aaa1e0",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
