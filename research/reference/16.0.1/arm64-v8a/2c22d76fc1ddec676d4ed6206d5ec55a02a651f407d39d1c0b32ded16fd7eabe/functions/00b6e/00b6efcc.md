# 00b6efcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b6eba4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eba4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-1534e55c9905829a90a9a7b961903e8a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b6f068`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f068.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-5f8977d24a191d8adc3a1f680136597f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6efcc",
  "name": "_ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e42bdacabc3da6933f4e5126fe43aa7b1ba20bbd3c7f038e5fba35d51fd2959",
  "source_text_sha256": "0e42bdacabc3da6933f4e5126fe43aa7b1ba20bbd3c7f038e5fba35d51fd2959",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6efcc",
        "00b6f0ab"
      ]
    ],
    "bytes_sha256": "0bcc76995d4e33276a392813fa5f5b0a88a71298b9867b7d7336e4422a32e149",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c580b0](../00c58/00c580b0.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c58000](../00c58/00c58000.md)
- [00c5b140](../00c5b/00c5b140.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1242 bytes

~~~c

void _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
               (ulong *param_1,char *param_2,byte *param_3)

{
  ulong uVar1;
  byte bVar2;
  size_t __n;
  byte *pbVar3;
  void *__dest;
  ulong uVar4;
  
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  __n = strlen(param_2);
  bVar2 = *param_3;
  uVar1 = (ulong)(bVar2 >> 1);
  if ((bVar2 & 1) != 0) {
    uVar1 = *(ulong *)(param_3 + 8);
  }
  uVar4 = uVar1 + __n;
  if (uVar4 < 0xfffffffffffffff0) {
    if (uVar4 < 0x17) {
      __dest = (void *)((long)param_1 + 1);
      *(char *)param_1 = (char)((int)__n << 1);
    }
    else {
      uVar4 = uVar4 + 0x10 & 0xfffffffffffffff0;
      __dest = (void *)_Znwm(uVar4);
      param_1[1] = __n;
      param_1[2] = (ulong)__dest;
      *param_1 = uVar4 | 1;
    }
    if (__n != 0) {
      memcpy(__dest,param_2,__n);
    }
    *(undefined1 *)((long)__dest + __n) = 0;
    pbVar3 = *(byte **)(param_3 + 0x10);
    if ((bVar2 & 1) == 0) {
      pbVar3 = param_3 + 1;
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
              (param_1,pbVar3,uVar1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6efcc"></a> `00b6efcc` | `fa 67 bb a9` | stp x26,x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00b6efd0"></a> `00b6efd0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6efd4"></a> `00b6efd4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6efd8"></a> `00b6efd8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6efdc"></a> `00b6efdc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b6efe0"></a> `00b6efe0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b6efe4"></a> `00b6efe4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b6efe8"></a> `00b6efe8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6efec"></a> `00b6efec` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00b6eff0"></a> `00b6eff0` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00b6eff4"></a> `00b6eff4` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b6eff8"></a> `00b6eff8` | `fa a3 03 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6effc"></a> `00b6effc` | `7a 02 40 39` | ldrb w26,[x19] | `FALL_THROUGH`
<a id="insn-00b6f000"></a> `00b6f000` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b6f004"></a> `00b6f004` | `49 ff 41 d3` | lsr x9,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00b6f008"></a> `00b6f008` | `5f 03 00 72` | tst w26,#0x1 | `FALL_THROUGH`
<a id="insn-00b6f00c"></a> `00b6f00c` | `37 01 88 9a` | csel x23,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00b6f010"></a> `00b6f010` | `e8 02 00 8b` | add x8,x23,x0 | `FALL_THROUGH`
<a id="insn-00b6f014"></a> `00b6f014` | `1f 41 00 b1` | cmn x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b6f018"></a> `00b6f018` | `82 04 00 54` | b.cs 0x00b6f0a8 | `CONDITIONAL_JUMP`
<a id="insn-00b6f01c"></a> `00b6f01c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b6f020"></a> `00b6f020` | `1f 59 00 f1` | cmp x8,#0x16 | `FALL_THROUGH`
<a id="insn-00b6f024"></a> `00b6f024` | `e8 00 00 54` | b.hi 0x00b6f040 | `CONDITIONAL_JUMP`
<a id="insn-00b6f028"></a> `00b6f028` | `c8 7a 1f 53` | lsl w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00b6f02c"></a> `00b6f02c` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00b6f030"></a> `00b6f030` | `08 17 00 38` | strb w8,[x24], #0x1 | `FALL_THROUGH`
<a id="insn-00b6f034"></a> `00b6f034` | `59 03 00 12` | and w25,w26,#0x1 | `FALL_THROUGH`
<a id="insn-00b6f038"></a> `00b6f038` | `96 01 00 b5` | cbnz x22,0x00b6f068 | `CONDITIONAL_JUMP`
<a id="insn-00b6f03c"></a> `00b6f03c` | `0f 00 00 14` | b 0x00b6f078 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6f040"></a> `00b6f040` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b6f044"></a> `00b6f044` | `19 ed 7c 92` | and x25,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00b6f048"></a> `00b6f048` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00b6f04c"></a> `00b6f04c` | `91 a3 03 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00b6f050"></a> `00b6f050` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00b6f054"></a> `00b6f054` | `28 03 40 b2` | orr x8,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00b6f058"></a> `00b6f058` | `96 82 00 a9` | stp x22,x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b6f05c"></a> `00b6f05c` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00b6f060"></a> `00b6f060` | `59 03 00 12` | and w25,w26,#0x1 | `FALL_THROUGH`
<a id="insn-00b6f064"></a> `00b6f064` | `b6 00 00 b4` | cbz x22,0x00b6f078 | `CONDITIONAL_JUMP`
<a id="insn-00b6f068"></a> `00b6f068` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b6f06c"></a> `00b6f06c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6f070"></a> `00b6f070` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b6f074"></a> `00b6f074` | `e3 a3 03 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00b6f078"></a> `00b6f078` | `1f 6b 36 38` | strb wzr,[x24, x22, LSL ] | `FALL_THROUGH`
<a id="insn-00b6f07c"></a> `00b6f07c` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b6f080"></a> `00b6f080` | `3f 03 00 71` | cmp w25,#0x0 | `FALL_THROUGH`
<a id="insn-00b6f084"></a> `00b6f084` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6f088"></a> `00b6f088` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00b6f08c"></a> `00b6f08c` | `01 15 93 9a` | csinc x1,x8,x19,ne | `FALL_THROUGH`
<a id="insn-00b6f090"></a> `00b6f090` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b6f094"></a> `00b6f094` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6f098"></a> `00b6f098` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6f09c"></a> `00b6f09c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6f0a0"></a> `00b6f0a0` | `fa 67 c5 a8` | ldp x26,x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00b6f0a4"></a> `00b6f0a4` | `b7 a3 03 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00b6f0a8"></a> `00b6f0a8` | `26 b0 03 94` | bl 0x00c5b140 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6efcc`](#insn-00b6efcc) 範囲 `[['00b6efcc', '00b6f01b']]`
  - `CONDITIONAL_JUMP` [`00b6f018`](#insn-00b6f018) → [`00b6f0a8`](#insn-00b6f0a8)
  - `FALL_THROUGH` [`00b6f018`](#insn-00b6f018) → [`00b6f01c`](#insn-00b6f01c)
- ブロック [`00b6f01c`](#insn-00b6f01c) 範囲 `[['00b6f01c', '00b6f027']]`
  - `CONDITIONAL_JUMP` [`00b6f024`](#insn-00b6f024) → [`00b6f040`](#insn-00b6f040)
  - `FALL_THROUGH` [`00b6f024`](#insn-00b6f024) → [`00b6f028`](#insn-00b6f028)
- ブロック [`00b6f028`](#insn-00b6f028) 範囲 `[['00b6f028', '00b6f03b']]`
  - `CONDITIONAL_JUMP` [`00b6f038`](#insn-00b6f038) → [`00b6f068`](#insn-00b6f068)
  - `FALL_THROUGH` [`00b6f038`](#insn-00b6f038) → [`00b6f03c`](#insn-00b6f03c)
- ブロック [`00b6f03c`](#insn-00b6f03c) 範囲 `[['00b6f03c', '00b6f03f']]`
  - `UNCONDITIONAL_JUMP` [`00b6f03c`](#insn-00b6f03c) → [`00b6f078`](#insn-00b6f078)
- ブロック [`00b6f040`](#insn-00b6f040) 範囲 `[['00b6f040', '00b6f067']]`
  - `CONDITIONAL_JUMP` [`00b6f064`](#insn-00b6f064) → [`00b6f078`](#insn-00b6f078)
  - `FALL_THROUGH` [`00b6f064`](#insn-00b6f064) → [`00b6f068`](#insn-00b6f068)
- ブロック [`00b6f068`](#insn-00b6f068) 範囲 `[['00b6f068', '00b6f077']]`
  - `FALL_THROUGH` [`00b6f074`](#insn-00b6f074) → [`00b6f078`](#insn-00b6f078)
- ブロック [`00b6f078`](#insn-00b6f078) 範囲 `[['00b6f078', '00b6f0a7']]`
- ブロック [`00b6f0a8`](#insn-00b6f0a8) 範囲 `[['00b6f0a8', '00b6f0ab']]`

## 命令位置別の参照

- [`00b6efcc`](#insn-00b6efcc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6efd0`](#insn-00b6efd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6efd4`](#insn-00b6efd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6efd8`](#insn-00b6efd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6efdc`](#insn-00b6efdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eff8`](#insn-00b6eff8) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00b6f018`](#insn-00b6f018) → [`00b6f0a8`](#insn-00b6f0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f024`](#insn-00b6f024) → [`00b6f040`](#insn-00b6f040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f038`](#insn-00b6f038) → [`00b6f068`](#insn-00b6f068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f03c`](#insn-00b6f03c) → [`00b6f078`](#insn-00b6f078) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f04c`](#insn-00b6f04c) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00b6f064`](#insn-00b6f064) → [`00b6f078`](#insn-00b6f078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f074`](#insn-00b6f074) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00b6f090`](#insn-00b6f090) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f094`](#insn-00b6f094) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f098`](#insn-00b6f098) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f09c`](#insn-00b6f09c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6f0a4`](#insn-00b6f0a4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b6f0a8`](#insn-00b6f0a8) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6efcc`](#insn-00b6efcc)

~~~json
{
  "source": "00b6efcc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6efd0`](#insn-00b6efd0)

~~~json
{
  "source": "00b6efd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6efd4`](#insn-00b6efd4)

~~~json
{
  "source": "00b6efd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6efd8`](#insn-00b6efd8)

~~~json
{
  "source": "00b6efd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6efdc`](#insn-00b6efdc)

~~~json
{
  "source": "00b6efdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eff8`](#insn-00b6eff8)

~~~json
{
  "source": "00b6eff8",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f018`](#insn-00b6f018)

~~~json
{
  "source": "00b6f018",
  "target": "00b6f0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f024`](#insn-00b6f024)

~~~json
{
  "source": "00b6f024",
  "target": "00b6f040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f038`](#insn-00b6f038)

~~~json
{
  "source": "00b6f038",
  "target": "00b6f068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f03c`](#insn-00b6f03c)

~~~json
{
  "source": "00b6f03c",
  "target": "00b6f078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f04c`](#insn-00b6f04c)

~~~json
{
  "source": "00b6f04c",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f064`](#insn-00b6f064)

~~~json
{
  "source": "00b6f064",
  "target": "00b6f078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f074`](#insn-00b6f074)

~~~json
{
  "source": "00b6f074",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f090`](#insn-00b6f090)

~~~json
{
  "source": "00b6f090",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f094`](#insn-00b6f094)

~~~json
{
  "source": "00b6f094",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f098`](#insn-00b6f098)

~~~json
{
  "source": "00b6f098",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f09c`](#insn-00b6f09c)

~~~json
{
  "source": "00b6f09c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6f0a4`](#insn-00b6f0a4)

~~~json
{
  "source": "00b6f0a4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6f0a8`](#insn-00b6f0a8)

~~~json
{
  "source": "00b6f0a8",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
