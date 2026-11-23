# 00afcffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afd0c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd0c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-62a5bd49ef0de3e8342651aabef42ed9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcffc",
  "name": "_ZN8firebase4PathC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e61b2db7963c91682f6842f5ef530544b6a2609a167fed726f17950c918b1c41",
  "source_text_sha256": "e61b2db7963c91682f6842f5ef530544b6a2609a167fed726f17950c918b1c41",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcffc",
        "00afd12f"
      ]
    ],
    "bytes_sha256": "c2865996bfd6d419f27a530db2e23053ac11da7f37b4d5f68065b73c57f740e1",
    "instruction_count": 77,
    "instruction_bytes": 308,
    "body_bytes": 308,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00afd1a0](../00afd/00afd1a0.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bde1c0](../00bde/00bde1c0.md)
- [00bde630](../00bde/00bde630.md)
- [00bdec30](../00bde/00bdec30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2256 bytes

~~~c

void _ZN8firebase4PathC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE
               (undefined8 param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  byte bVar3;
  long lVar4;
  long lVar5;
  byte *pbVar6;
  byte *pbVar7;
  byte *__ptr;
  byte *pbVar8;
  byte local_60 [16];
  void *local_50;
  long local_48;
  
                    /* try { // try from 00afd010 to 00bfd03f has its CatchHandler @ 00af560c */
  lVar5 = tpidr_el0;
  local_48 = *(long *)(lVar5 + 0x28);
  lVar1 = *param_2;
  lVar2 = param_2[1];
  lVar4 = lVar2 - lVar1;
  if (lVar4 == 0) {
    __ptr = (byte *)0x0;
    pbVar8 = (byte *)0x0;
  }
  else {
                    /* try { // try from 00afd040 to 00bfd047 has its CatchHandler @ 00aff388 */
    if (0xaaaaaaaaaaaaaaa < (ulong)((lVar4 >> 3) * -0x5555555555555555)) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    __ptr = (byte *)_Znwm(lVar4);
    pbVar8 = __ptr;
    for (; lVar1 != lVar2; lVar1 = lVar1 + 0x18) {
                    /* try { // try from 00afd070 to 00bfd087 has its CatchHandler @ 00aff384 */
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_(pbVar8,lVar1);
      pbVar8 = pbVar8 + 0x18;
    }
  }
  FUN_00afd1a0(local_60,__ptr,pbVar8);
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,local_60);
  if ((local_60[0] & 1) != 0) {
    _ZdlPv(local_50);
  }
                    /* try { // try from 00afd0c0 to 00bfd0d7 has its CatchHandler @ 00aff380 */
  if (__ptr != (byte *)0x0) {
    if (pbVar8 != __ptr) {
      bVar3 = pbVar8[-0x18];
      pbVar7 = pbVar8 + -0x18;
      while( true ) {
        pbVar6 = pbVar7;
        if ((bVar3 & 1) != 0) {
          _ZdlPv(*(void **)(pbVar8 + -8));
        }
        if (__ptr == pbVar6) break;
        bVar3 = pbVar6[-0x18];
        pbVar7 = pbVar6 + -0x18;
        pbVar8 = pbVar6;
      }
    }
    _ZdlPv(__ptr);
  }
  if (*(long *)(lVar5 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 00afd110 to 00bfd11b has its CatchHandler @ 00aff37c */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcffc"></a> `00afcffc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00afd000"></a> `00afd000` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afd004"></a> `00afd004` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afd008"></a> `00afd008` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afd00c"></a> `00afd00c` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afd010"></a> `00afd010` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afd014"></a> `00afd014` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afd018"></a> `00afd018` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00afd01c"></a> `00afd01c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00afd020"></a> `00afd020` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00afd024"></a> `00afd024` | `36 60 40 a9` | ldp x22,x24,[x1] | `FALL_THROUGH`
<a id="insn-00afd028"></a> `00afd028` | `08 03 16 eb` | subs x8,x24,x22 | `FALL_THROUGH`
<a id="insn-00afd02c"></a> `00afd02c` | `00 03 00 54` | b.eq 0x00afd08c | `CONDITIONAL_JUMP`
<a id="insn-00afd030"></a> `00afd030` | `ea f3 01 b2` | orr x10,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00afd034"></a> `00afd034` | `09 fd 43 93` | asr x9,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00afd038"></a> `00afd038` | `6a 55 95 f2` | movk x10,#0xaaab | `FALL_THROUGH`
<a id="insn-00afd03c"></a> `00afd03c` | `29 7d 0a 9b` | mul x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00afd040"></a> `00afd040` | `ea f3 01 b2` | orr x10,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00afd044"></a> `00afd044` | `6a 55 95 f2` | movk x10,#0xaaab | `FALL_THROUGH`
<a id="insn-00afd048"></a> `00afd048` | `4a 55 e1 f2` | movk x10,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00afd04c"></a> `00afd04c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00afd050"></a> `00afd050` | `e2 06 00 54` | b.cs 0x00afd12c | `CONDITIONAL_JUMP`
<a id="insn-00afd054"></a> `00afd054` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00afd058"></a> `00afd058` | `ba 77 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00afd05c"></a> `00afd05c` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00afd060"></a> `00afd060` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afd064"></a> `00afd064` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afd068"></a> `00afd068` | `60 01 00 54` | b.eq 0x00afd094 | `CONDITIONAL_JUMP`
<a id="insn-00afd06c"></a> `00afd06c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afd070"></a> `00afd070` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afd074"></a> `00afd074` | `6f 85 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00afd078"></a> `00afd078` | `d6 62 00 91` | add x22,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00afd07c"></a> `00afd07c` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00afd080"></a> `00afd080` | `94 62 00 91` | add x20,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00afd084"></a> `00afd084` | `41 ff ff 54` | b.ne 0x00afd06c | `CONDITIONAL_JUMP`
<a id="insn-00afd088"></a> `00afd088` | `03 00 00 14` | b 0x00afd094 | `UNCONDITIONAL_JUMP`
<a id="insn-00afd08c"></a> `00afd08c` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00afd090"></a> `00afd090` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00afd094"></a> `00afd094` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00afd098"></a> `00afd098` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afd09c"></a> `00afd09c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00afd0a0"></a> `00afd0a0` | `40 00 00 94` | bl 0x00afd1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00afd0a4"></a> `00afd0a4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00afd0a8"></a> `00afd0a8` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00afd0ac"></a> `00afd0ac` | `e1 86 03 94` | bl 0x00bdec30 | `UNCONDITIONAL_CALL`
<a id="insn-00afd0b0"></a> `00afd0b0` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00afd0b4"></a> `00afd0b4` | `68 00 00 36` | tbz w8,#0x0,0x00afd0c0 | `CONDITIONAL_JUMP`
<a id="insn-00afd0b8"></a> `00afd0b8` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd0bc"></a> `00afd0bc` | `a9 77 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afd0c0"></a> `00afd0c0` | `13 02 00 b4` | cbz x19,0x00afd100 | `CONDITIONAL_JUMP`
<a id="insn-00afd0c4"></a> `00afd0c4` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00afd0c8"></a> `00afd0c8` | `80 01 00 54` | b.eq 0x00afd0f8 | `CONDITIONAL_JUMP`
<a id="insn-00afd0cc"></a> `00afd0cc` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00afd0d0"></a> `00afd0d0` | `a8 8e 5e 38` | ldrb w8,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afd0d4"></a> `00afd0d4` | `c8 00 00 37` | tbnz w8,#0x0,0x00afd0ec | `CONDITIONAL_JUMP`
<a id="insn-00afd0d8"></a> `00afd0d8` | `7f 02 15 eb` | cmp x19,x21 | `FALL_THROUGH`
<a id="insn-00afd0dc"></a> `00afd0dc` | `f4 03 15 aa` | mov x20,x21 | `FALL_THROUGH`
<a id="insn-00afd0e0"></a> `00afd0e0` | `c0 00 00 54` | b.eq 0x00afd0f8 | `CONDITIONAL_JUMP`
<a id="insn-00afd0e4"></a> `00afd0e4` | `a8 8e 5e 38` | ldrb w8,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afd0e8"></a> `00afd0e8` | `88 ff 07 36` | tbz w8,#0x0,0x00afd0d8 | `CONDITIONAL_JUMP`
<a id="insn-00afd0ec"></a> `00afd0ec` | `80 82 5f f8` | ldur x0,[x20, #-0x8] | `FALL_THROUGH`
<a id="insn-00afd0f0"></a> `00afd0f0` | `9c 77 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afd0f4"></a> `00afd0f4` | `f9 ff ff 17` | b 0x00afd0d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afd0f8"></a> `00afd0f8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afd0fc"></a> `00afd0fc` | `99 77 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afd100"></a> `00afd100` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00afd104"></a> `00afd104` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00afd108"></a> `00afd108` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afd10c"></a> `00afd10c` | `e1 00 00 54` | b.ne 0x00afd128 | `CONDITIONAL_JUMP`
<a id="insn-00afd110"></a> `00afd110` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afd114"></a> `00afd114` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afd118"></a> `00afd118` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afd11c"></a> `00afd11c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afd120"></a> `00afd120` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00afd124"></a> `00afd124` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afd128"></a> `00afd128` | `9a 77 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`
<a id="insn-00afd12c"></a> `00afd12c` | `25 84 03 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcffc`](#insn-00afcffc) 範囲 `[['00afcffc', '00afd00f']]`
  - `FALL_THROUGH` [`00afd00c`](#insn-00afd00c) → [`00afd010`](#insn-00afd010)
- ブロック [`00afd010`](#insn-00afd010) 範囲 `[['00afd010', '00afd02f']]`
  - `CONDITIONAL_JUMP` [`00afd02c`](#insn-00afd02c) → [`00afd08c`](#insn-00afd08c)
  - `FALL_THROUGH` [`00afd02c`](#insn-00afd02c) → [`00afd030`](#insn-00afd030)
- ブロック [`00afd030`](#insn-00afd030) 範囲 `[['00afd030', '00afd03f']]`
  - `FALL_THROUGH` [`00afd03c`](#insn-00afd03c) → [`00afd040`](#insn-00afd040)
- ブロック [`00afd040`](#insn-00afd040) 範囲 `[['00afd040', '00afd053']]`
  - `CONDITIONAL_JUMP` [`00afd050`](#insn-00afd050) → [`00afd12c`](#insn-00afd12c)
  - `FALL_THROUGH` [`00afd050`](#insn-00afd050) → [`00afd054`](#insn-00afd054)
- ブロック [`00afd054`](#insn-00afd054) 範囲 `[['00afd054', '00afd06b']]`
  - `CONDITIONAL_JUMP` [`00afd068`](#insn-00afd068) → [`00afd094`](#insn-00afd094)
  - `FALL_THROUGH` [`00afd068`](#insn-00afd068) → [`00afd06c`](#insn-00afd06c)
- ブロック [`00afd06c`](#insn-00afd06c) 範囲 `[['00afd06c', '00afd06f']]`
  - `FALL_THROUGH` [`00afd06c`](#insn-00afd06c) → [`00afd070`](#insn-00afd070)
- ブロック [`00afd070`](#insn-00afd070) 範囲 `[['00afd070', '00afd087']]`
  - `CONDITIONAL_JUMP` [`00afd084`](#insn-00afd084) → [`00afd06c`](#insn-00afd06c)
  - `FALL_THROUGH` [`00afd084`](#insn-00afd084) → [`00afd088`](#insn-00afd088)
- ブロック [`00afd088`](#insn-00afd088) 範囲 `[['00afd088', '00afd08b']]`
  - `UNCONDITIONAL_JUMP` [`00afd088`](#insn-00afd088) → [`00afd094`](#insn-00afd094)
- ブロック [`00afd08c`](#insn-00afd08c) 範囲 `[['00afd08c', '00afd093']]`
  - `FALL_THROUGH` [`00afd090`](#insn-00afd090) → [`00afd094`](#insn-00afd094)
- ブロック [`00afd094`](#insn-00afd094) 範囲 `[['00afd094', '00afd0b7']]`
  - `CONDITIONAL_JUMP` [`00afd0b4`](#insn-00afd0b4) → [`00afd0c0`](#insn-00afd0c0)
  - `FALL_THROUGH` [`00afd0b4`](#insn-00afd0b4) → [`00afd0b8`](#insn-00afd0b8)
- ブロック [`00afd0b8`](#insn-00afd0b8) 範囲 `[['00afd0b8', '00afd0bf']]`
  - `FALL_THROUGH` [`00afd0bc`](#insn-00afd0bc) → [`00afd0c0`](#insn-00afd0c0)
- ブロック [`00afd0c0`](#insn-00afd0c0) 範囲 `[['00afd0c0', '00afd0c3']]`
  - `CONDITIONAL_JUMP` [`00afd0c0`](#insn-00afd0c0) → [`00afd100`](#insn-00afd100)
  - `FALL_THROUGH` [`00afd0c0`](#insn-00afd0c0) → [`00afd0c4`](#insn-00afd0c4)
- ブロック [`00afd0c4`](#insn-00afd0c4) 範囲 `[['00afd0c4', '00afd0cb']]`
  - `CONDITIONAL_JUMP` [`00afd0c8`](#insn-00afd0c8) → [`00afd0f8`](#insn-00afd0f8)
  - `FALL_THROUGH` [`00afd0c8`](#insn-00afd0c8) → [`00afd0cc`](#insn-00afd0cc)
- ブロック [`00afd0cc`](#insn-00afd0cc) 範囲 `[['00afd0cc', '00afd0d7']]`
  - `CONDITIONAL_JUMP` [`00afd0d4`](#insn-00afd0d4) → [`00afd0ec`](#insn-00afd0ec)
  - `FALL_THROUGH` [`00afd0d4`](#insn-00afd0d4) → [`00afd0d8`](#insn-00afd0d8)
- ブロック [`00afd0d8`](#insn-00afd0d8) 範囲 `[['00afd0d8', '00afd0e3']]`
  - `CONDITIONAL_JUMP` [`00afd0e0`](#insn-00afd0e0) → [`00afd0f8`](#insn-00afd0f8)
  - `FALL_THROUGH` [`00afd0e0`](#insn-00afd0e0) → [`00afd0e4`](#insn-00afd0e4)
- ブロック [`00afd0e4`](#insn-00afd0e4) 範囲 `[['00afd0e4', '00afd0eb']]`
  - `CONDITIONAL_JUMP` [`00afd0e8`](#insn-00afd0e8) → [`00afd0d8`](#insn-00afd0d8)
  - `FALL_THROUGH` [`00afd0e8`](#insn-00afd0e8) → [`00afd0ec`](#insn-00afd0ec)
- ブロック [`00afd0ec`](#insn-00afd0ec) 範囲 `[['00afd0ec', '00afd0f7']]`
  - `UNCONDITIONAL_JUMP` [`00afd0f4`](#insn-00afd0f4) → [`00afd0d8`](#insn-00afd0d8)
- ブロック [`00afd0f8`](#insn-00afd0f8) 範囲 `[['00afd0f8', '00afd0ff']]`
  - `FALL_THROUGH` [`00afd0fc`](#insn-00afd0fc) → [`00afd100`](#insn-00afd100)
- ブロック [`00afd100`](#insn-00afd100) 範囲 `[['00afd100', '00afd10f']]`
  - `CONDITIONAL_JUMP` [`00afd10c`](#insn-00afd10c) → [`00afd128`](#insn-00afd128)
  - `FALL_THROUGH` [`00afd10c`](#insn-00afd10c) → [`00afd110`](#insn-00afd110)
- ブロック [`00afd110`](#insn-00afd110) 範囲 `[['00afd110', '00afd127']]`
- ブロック [`00afd128`](#insn-00afd128) 範囲 `[['00afd128', '00afd12b']]`
- ブロック [`00afd12c`](#insn-00afd12c) 範囲 `[['00afd12c', '00afd12f']]`

## 命令位置別の参照

- [`00afd000`](#insn-00afd000) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd004`](#insn-00afd004) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd008`](#insn-00afd008) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd00c`](#insn-00afd00c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd020`](#insn-00afd020) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd02c`](#insn-00afd02c) → [`00afd08c`](#insn-00afd08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd050`](#insn-00afd050) → [`00afd12c`](#insn-00afd12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd058`](#insn-00afd058) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00afd068`](#insn-00afd068) → [`00afd094`](#insn-00afd094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd074`](#insn-00afd074) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00afd084`](#insn-00afd084) → [`00afd06c`](#insn-00afd06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd088`](#insn-00afd088) → [`00afd094`](#insn-00afd094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0a0`](#insn-00afd0a0) → [`00afd1a0`](../00afd/00afd1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afd1a0` · 推定シンボル `None` · 推定型 `None`
- [`00afd0ac`](#insn-00afd0ac) → [`00bdec30`](../00bde/00bdec30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec30` · 推定シンボル `None` · 推定型 `None`
- [`00afd0b0`](#insn-00afd0b0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0b4`](#insn-00afd0b4) → [`00afd0c0`](#insn-00afd0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0b8`](#insn-00afd0b8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0bc`](#insn-00afd0bc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afd0c0`](#insn-00afd0c0) → [`00afd100`](#insn-00afd100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0c8`](#insn-00afd0c8) → [`00afd0f8`](#insn-00afd0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0d4`](#insn-00afd0d4) → [`00afd0ec`](#insn-00afd0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0e0`](#insn-00afd0e0) → [`00afd0f8`](#insn-00afd0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0e8`](#insn-00afd0e8) → [`00afd0d8`](#insn-00afd0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0f0`](#insn-00afd0f0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afd0f4`](#insn-00afd0f4) → [`00afd0d8`](#insn-00afd0d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd0fc`](#insn-00afd0fc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afd104`](#insn-00afd104) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd10c`](#insn-00afd10c) → [`00afd128`](#insn-00afd128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd110`](#insn-00afd110) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd114`](#insn-00afd114) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd118`](#insn-00afd118) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd11c`](#insn-00afd11c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd128`](#insn-00afd128) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`00afd12c`](#insn-00afd12c) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afd000`](#insn-00afd000)

~~~json
{
  "source": "00afd000",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd004`](#insn-00afd004)

~~~json
{
  "source": "00afd004",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd008`](#insn-00afd008)

~~~json
{
  "source": "00afd008",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd00c`](#insn-00afd00c)

~~~json
{
  "source": "00afd00c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd020`](#insn-00afd020)

~~~json
{
  "source": "00afd020",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd02c`](#insn-00afd02c)

~~~json
{
  "source": "00afd02c",
  "target": "00afd08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd050`](#insn-00afd050)

~~~json
{
  "source": "00afd050",
  "target": "00afd12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd058`](#insn-00afd058)

~~~json
{
  "source": "00afd058",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd068`](#insn-00afd068)

~~~json
{
  "source": "00afd068",
  "target": "00afd094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd074`](#insn-00afd074)

~~~json
{
  "source": "00afd074",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd084`](#insn-00afd084)

~~~json
{
  "source": "00afd084",
  "target": "00afd06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd088`](#insn-00afd088)

~~~json
{
  "source": "00afd088",
  "target": "00afd094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0a0`](#insn-00afd0a0)

~~~json
{
  "source": "00afd0a0",
  "target": "00afd1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd0ac`](#insn-00afd0ac)

~~~json
{
  "source": "00afd0ac",
  "target": "00bdec30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd0b0`](#insn-00afd0b0)

~~~json
{
  "source": "00afd0b0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0b4`](#insn-00afd0b4)

~~~json
{
  "source": "00afd0b4",
  "target": "00afd0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0b8`](#insn-00afd0b8)

~~~json
{
  "source": "00afd0b8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0bc`](#insn-00afd0bc)

~~~json
{
  "source": "00afd0bc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd0c0`](#insn-00afd0c0)

~~~json
{
  "source": "00afd0c0",
  "target": "00afd100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0c8`](#insn-00afd0c8)

~~~json
{
  "source": "00afd0c8",
  "target": "00afd0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0d4`](#insn-00afd0d4)

~~~json
{
  "source": "00afd0d4",
  "target": "00afd0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0e0`](#insn-00afd0e0)

~~~json
{
  "source": "00afd0e0",
  "target": "00afd0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0e8`](#insn-00afd0e8)

~~~json
{
  "source": "00afd0e8",
  "target": "00afd0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0f0`](#insn-00afd0f0)

~~~json
{
  "source": "00afd0f0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd0f4`](#insn-00afd0f4)

~~~json
{
  "source": "00afd0f4",
  "target": "00afd0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd0fc`](#insn-00afd0fc)

~~~json
{
  "source": "00afd0fc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd104`](#insn-00afd104)

~~~json
{
  "source": "00afd104",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd10c`](#insn-00afd10c)

~~~json
{
  "source": "00afd10c",
  "target": "00afd128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd110`](#insn-00afd110)

~~~json
{
  "source": "00afd110",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd114`](#insn-00afd114)

~~~json
{
  "source": "00afd114",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd118`](#insn-00afd118)

~~~json
{
  "source": "00afd118",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd11c`](#insn-00afd11c)

~~~json
{
  "source": "00afd11c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd128`](#insn-00afd128)

~~~json
{
  "source": "00afd128",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd12c`](#insn-00afd12c)

~~~json
{
  "source": "00afd12c",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
