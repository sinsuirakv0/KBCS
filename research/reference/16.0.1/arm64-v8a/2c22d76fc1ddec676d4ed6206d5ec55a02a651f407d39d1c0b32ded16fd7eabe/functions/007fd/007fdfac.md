# 007fdfac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `007fdf6c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdf6c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0041.md#compare-ac4ab41f40278c8264a6b533627d55fc)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `007fe004`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fe/007fe004.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0042.md#compare-dfb9ea1f38ed92f3b72b54402ded05f7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fdfac",
  "name": "FUN_007fdfac",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "01e65834fdd0acad5185817c1ec499c9f3795cc560a4d2b4959686d8f25e8f16",
  "source_text_sha256": "01e65834fdd0acad5185817c1ec499c9f3795cc560a4d2b4959686d8f25e8f16",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fdfac",
        "007fe07b"
      ]
    ],
    "bytes_sha256": "b4a8c7e0e8740a5cd3ab6ef185f4e49256a89f259dfc1f1ce05abc65721e5ab4",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008514f8](../00851/008514f8.md)
- [008b9178](../008b9/008b9178.md)
- [008b9298](../008b9/008b9298.md)
- [009dce40](../009dc/009dce40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1837 bytes

~~~c

void FUN_007fdfac(long param_1,undefined8 *param_2,int *param_3)

{
  byte bVar1;
  ulong uVar2;
  int iVar3;
  long lVar4;
  undefined8 uVar5;
  undefined1 auVar6 [12];
  
                    /* catch() { ... } // from try @ 007fdb4c with catch @ 007fdfbc */
  if (*param_3 == 2) {
    uVar5 = *param_2;
    lVar4 = *(long *)(param_1 + 8);
                    /* catch() { ... } // from try @ 007fdd94 with catch @ 007fdfd0 */
    auVar6 = FUN_008b9298(uVar5);
    iVar3 = auVar6._8_4_;
                    /* catch() { ... } // from try @ 007fdd80 with catch @ 007fdfd8 */
                    /* catch() { ... } // from try @ 007fdc78 with catch @ 007fdfe0 */
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
                    /* catch() { ... } // from try @ 007fdc4c with catch @ 007fdff0 */
    uVar2 = FUN_009dce40(lVar4,auVar6._0_4_ + (iVar3 >> 1) + -299,auVar6._4_4_ + -0x2d,0x29b,0x34);
    if ((uVar2 & 1) == 0) {
      if (*(char *)((long)&fde_table_entry_003374a8.data_loc + lVar4) != '\0') {
        FUN_008b9178(uVar5);
        uVar5 = FUN_0047acf4();
        FUN_0047cdd4(uVar5,0xb,0);
        return;
      }
      *(undefined1 *)((long)&fde_table_entry_003374a8.data_loc + lVar4) = 1;
      *(undefined1 *)(lVar4 + 0x33a4) = 1;
    }
    else {
                    /* catch() { ... } // from try @ 007fddc4 with catch @ 007fe000 */
      uVar5 = FUN_0047acf4();
      FUN_0047cdd4(uVar5,0xb,0);
      lVar4 = FUN_008514f8();
      bVar1 = *(byte *)((long)&fde_table_entry_003374a8.data_loc + lVar4 + 1);
      lVar4 = FUN_008514f8();
      *(byte *)((long)&fde_table_entry_003374a8.data_loc + lVar4 + 1) = bVar1 ^ 1;
    }
  }
                    /* catch() { ... } // from try @ 007fdc84 with catch @ 007fe070 */
                    /* catch() { ... } // from try @ 007fdd34 with catch @ 007fe078 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fdfac"></a> `007fdfac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fdfb0"></a> `007fdfb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fdfb4"></a> `007fdfb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fdfb8"></a> `007fdfb8` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-007fdfbc"></a> `007fdfbc` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-007fdfc0"></a> `007fdfc0` | `81 05 00 54` | b.ne 0x007fe070 | `CONDITIONAL_JUMP`
<a id="insn-007fdfc4"></a> `007fdfc4` | `34 00 40 f9` | ldr x20,[x1] | `FALL_THROUGH`
<a id="insn-007fdfc8"></a> `007fdfc8` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007fdfcc"></a> `007fdfcc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007fdfd0"></a> `007fdfd0` | `b2 ec 02 94` | bl 0x008b9298 | `UNCONDITIONAL_CALL`
<a id="insn-007fdfd4"></a> `007fdfd4` | `3f 00 00 71` | cmp w1,#0x0 | `FALL_THROUGH`
<a id="insn-007fdfd8"></a> `007fdfd8` | `09 fc 60 d3` | lsr x9,x0,#0x20 | `FALL_THROUGH`
<a id="insn-007fdfdc"></a> `007fdfdc` | `63 53 80 52` | mov w3,#0x29b | `FALL_THROUGH`
<a id="insn-007fdfe0"></a> `007fdfe0` | `28 a4 81 1a` | cinc w8,w1,lt | `FALL_THROUGH`
<a id="insn-007fdfe4"></a> `007fdfe4` | `84 06 80 52` | mov w4,#0x34 | `FALL_THROUGH`
<a id="insn-007fdfe8"></a> `007fdfe8` | `08 04 88 0b` | add w8,w0,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-007fdfec"></a> `007fdfec` | `22 b5 00 51` | sub w2,w9,#0x2d | `FALL_THROUGH`
<a id="insn-007fdff0"></a> `007fdff0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fdff4"></a> `007fdff4` | `01 ad 04 51` | sub w1,w8,#0x12b | `FALL_THROUGH`
<a id="insn-007fdff8"></a> `007fdff8` | `92 7b 07 94` | bl 0x009dce40 | `UNCONDITIONAL_CALL`
<a id="insn-007fdffc"></a> `007fdffc` | `a0 01 00 36` | tbz w0,#0x0,0x007fe030 | `CONDITIONAL_JUMP`
<a id="insn-007fe000"></a> `007fe000` | `3d f3 f1 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-007fe004"></a> `007fe004` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-007fe008"></a> `007fe008` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-007fe00c"></a> `007fe00c` | `72 fb f1 97` | bl 0x0047cdd4 | `UNCONDITIONAL_CALL`
<a id="insn-007fe010"></a> `007fe010` | `3a 4d 01 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-007fe014"></a> `007fe014` | `b3 95 8e 52` | mov w19,#0x74ad | `FALL_THROUGH`
<a id="insn-007fe018"></a> `007fe018` | `73 06 a0 72` | movk w19,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-007fe01c"></a> `007fe01c` | `14 68 73 38` | ldrb w20,[x0, x19, LSL ] | `FALL_THROUGH`
<a id="insn-007fe020"></a> `007fe020` | `36 4d 01 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-007fe024"></a> `007fe024` | `88 02 00 52` | eor w8,w20,#0x1 | `FALL_THROUGH`
<a id="insn-007fe028"></a> `007fe028` | `08 68 33 38` | strb w8,[x0, x19, LSL ] | `FALL_THROUGH`
<a id="insn-007fe02c"></a> `007fe02c` | `11 00 00 14` | b 0x007fe070 | `UNCONDITIONAL_JUMP`
<a id="insn-007fe030"></a> `007fe030` | `88 95 8e 52` | mov w8,#0x74ac | `FALL_THROUGH`
<a id="insn-007fe034"></a> `007fe034` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-007fe038"></a> `007fe038` | `69 6a 68 38` | ldrb w9,[x19, x8, LSL ] | `FALL_THROUGH`
<a id="insn-007fe03c"></a> `007fe03c` | `29 01 00 34` | cbz w9,0x007fe060 | `CONDITIONAL_JUMP`
<a id="insn-007fe040"></a> `007fe040` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007fe044"></a> `007fe044` | `4d ec 02 94` | bl 0x008b9178 | `UNCONDITIONAL_CALL`
<a id="insn-007fe048"></a> `007fe048` | `2b f3 f1 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-007fe04c"></a> `007fe04c` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-007fe050"></a> `007fe050` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-007fe054"></a> `007fe054` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fe058"></a> `007fe058` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fe05c"></a> `007fe05c` | `5e fb f1 17` | b 0x0047cdd4 | `CALL_TERMINATOR`
<a id="insn-007fe060"></a> `007fe060` | `89 74 86 52` | mov w9,#0x33a4 | `FALL_THROUGH`
<a id="insn-007fe064"></a> `007fe064` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-007fe068"></a> `007fe068` | `6a 6a 28 38` | strb w10,[x19, x8, LSL ] | `FALL_THROUGH`
<a id="insn-007fe06c"></a> `007fe06c` | `6a 6a 29 38` | strb w10,[x19, x9, LSL ] | `FALL_THROUGH`
<a id="insn-007fe070"></a> `007fe070` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fe074"></a> `007fe074` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fe078"></a> `007fe078` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fdfac`](#insn-007fdfac) 範囲 `[['007fdfac', '007fdfbb']]`
  - `FALL_THROUGH` [`007fdfb8`](#insn-007fdfb8) → [`007fdfbc`](#insn-007fdfbc)
- ブロック [`007fdfbc`](#insn-007fdfbc) 範囲 `[['007fdfbc', '007fdfc3']]`
  - `CONDITIONAL_JUMP` [`007fdfc0`](#insn-007fdfc0) → [`007fe070`](#insn-007fe070)
  - `FALL_THROUGH` [`007fdfc0`](#insn-007fdfc0) → [`007fdfc4`](#insn-007fdfc4)
- ブロック [`007fdfc4`](#insn-007fdfc4) 範囲 `[['007fdfc4', '007fdfcf']]`
  - `FALL_THROUGH` [`007fdfcc`](#insn-007fdfcc) → [`007fdfd0`](#insn-007fdfd0)
- ブロック [`007fdfd0`](#insn-007fdfd0) 範囲 `[['007fdfd0', '007fdfd7']]`
  - `FALL_THROUGH` [`007fdfd4`](#insn-007fdfd4) → [`007fdfd8`](#insn-007fdfd8)
- ブロック [`007fdfd8`](#insn-007fdfd8) 範囲 `[['007fdfd8', '007fdfdf']]`
  - `FALL_THROUGH` [`007fdfdc`](#insn-007fdfdc) → [`007fdfe0`](#insn-007fdfe0)
- ブロック [`007fdfe0`](#insn-007fdfe0) 範囲 `[['007fdfe0', '007fdfef']]`
  - `FALL_THROUGH` [`007fdfec`](#insn-007fdfec) → [`007fdff0`](#insn-007fdff0)
- ブロック [`007fdff0`](#insn-007fdff0) 範囲 `[['007fdff0', '007fdfff']]`
  - `CONDITIONAL_JUMP` [`007fdffc`](#insn-007fdffc) → [`007fe030`](#insn-007fe030)
  - `FALL_THROUGH` [`007fdffc`](#insn-007fdffc) → [`007fe000`](#insn-007fe000)
- ブロック [`007fe000`](#insn-007fe000) 範囲 `[['007fe000', '007fe02f']]`
  - `UNCONDITIONAL_JUMP` [`007fe02c`](#insn-007fe02c) → [`007fe070`](#insn-007fe070)
- ブロック [`007fe030`](#insn-007fe030) 範囲 `[['007fe030', '007fe03f']]`
  - `CONDITIONAL_JUMP` [`007fe03c`](#insn-007fe03c) → [`007fe060`](#insn-007fe060)
  - `FALL_THROUGH` [`007fe03c`](#insn-007fe03c) → [`007fe040`](#insn-007fe040)
- ブロック [`007fe040`](#insn-007fe040) 範囲 `[['007fe040', '007fe05f']]`
- ブロック [`007fe060`](#insn-007fe060) 範囲 `[['007fe060', '007fe06f']]`
  - `FALL_THROUGH` [`007fe06c`](#insn-007fe06c) → [`007fe070`](#insn-007fe070)
- ブロック [`007fe070`](#insn-007fe070) 範囲 `[['007fe070', '007fe077']]`
  - `FALL_THROUGH` [`007fe074`](#insn-007fe074) → [`007fe078`](#insn-007fe078)
- ブロック [`007fe078`](#insn-007fe078) 範囲 `[['007fe078', '007fe07b']]`

## 命令位置別の参照

- [`007fdfac`](#insn-007fdfac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdfb0`](#insn-007fdfb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdfc0`](#insn-007fdfc0) → [`007fe070`](#insn-007fe070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdfd0`](#insn-007fdfd0) → [`008b9298`](../008b9/008b9298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9298` · 推定シンボル `None` · 推定型 `None`
- [`007fdff8`](#insn-007fdff8) → [`009dce40`](../009dc/009dce40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009dce40` · 推定シンボル `None` · 推定型 `None`
- [`007fdffc`](#insn-007fdffc) → [`007fe030`](#insn-007fe030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fe000`](#insn-007fe000) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`007fe00c`](#insn-007fe00c) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`007fe010`](#insn-007fe010) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`007fe01c`](#insn-007fe01c) → `003374ad`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`007fe020`](#insn-007fe020) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`007fe028`](#insn-007fe028) → `003374ad`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`007fe02c`](#insn-007fe02c) → [`007fe070`](#insn-007fe070) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fe038`](#insn-007fe038) → `003374ac`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`007fe03c`](#insn-007fe03c) → [`007fe060`](#insn-007fe060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fe044`](#insn-007fe044) → [`008b9178`](../008b9/008b9178.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9178` · 推定シンボル `None` · 推定型 `None`
- [`007fe048`](#insn-007fe048) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`007fe054`](#insn-007fe054) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fe058`](#insn-007fe058) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fe05c`](#insn-007fe05c) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`007fe068`](#insn-007fe068) → `003374ac`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`007fe070`](#insn-007fe070) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fe074`](#insn-007fe074) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fdfac`](#insn-007fdfac)

~~~json
{
  "source": "007fdfac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdfb0`](#insn-007fdfb0)

~~~json
{
  "source": "007fdfb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdfc0`](#insn-007fdfc0)

~~~json
{
  "source": "007fdfc0",
  "target": "007fe070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdfd0`](#insn-007fdfd0)

~~~json
{
  "source": "007fdfd0",
  "target": "008b9298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdff8`](#insn-007fdff8)

~~~json
{
  "source": "007fdff8",
  "target": "009dce40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdffc`](#insn-007fdffc)

~~~json
{
  "source": "007fdffc",
  "target": "007fe030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fe000`](#insn-007fe000)

~~~json
{
  "source": "007fe000",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fe00c`](#insn-007fe00c)

~~~json
{
  "source": "007fe00c",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fe010`](#insn-007fe010)

~~~json
{
  "source": "007fe010",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fe01c`](#insn-007fe01c)

~~~json
{
  "source": "007fe01c",
  "target": "003374ad",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003374a8",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8b47a0070440a00",
  "capture_start": "003374a8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007fe020`](#insn-007fe020)

~~~json
{
  "source": "007fe020",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fe028`](#insn-007fe028)

~~~json
{
  "source": "007fe028",
  "target": "003374ad",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003374a8",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8b47a0070440a00",
  "capture_start": "003374a8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007fe02c`](#insn-007fe02c)

~~~json
{
  "source": "007fe02c",
  "target": "007fe070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fe038`](#insn-007fe038)

~~~json
{
  "source": "007fe038",
  "target": "003374ac",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003374a8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8b47a0070440a00",
  "capture_start": "003374a8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007fe03c`](#insn-007fe03c)

~~~json
{
  "source": "007fe03c",
  "target": "007fe060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fe044`](#insn-007fe044)

~~~json
{
  "source": "007fe044",
  "target": "008b9178",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fe048`](#insn-007fe048)

~~~json
{
  "source": "007fe048",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fe054`](#insn-007fe054)

~~~json
{
  "source": "007fe054",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fe058`](#insn-007fe058)

~~~json
{
  "source": "007fe058",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fe05c`](#insn-007fe05c)

~~~json
{
  "source": "007fe05c",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fe068`](#insn-007fe068)

~~~json
{
  "source": "007fe068",
  "target": "003374ac",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003374a8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8b47a0070440a00",
  "capture_start": "003374a8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007fe070`](#insn-007fe070)

~~~json
{
  "source": "007fe070",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fe074`](#insn-007fe074)

~~~json
{
  "source": "007fe074",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
