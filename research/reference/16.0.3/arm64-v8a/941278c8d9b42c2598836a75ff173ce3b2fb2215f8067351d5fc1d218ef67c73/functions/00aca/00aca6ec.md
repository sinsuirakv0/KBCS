# 00aca6ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac96f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac96f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-ad2ae2acf2a4dc4d930fe247674a66b4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aca6ec",
  "name": "FUN_00aca6ec",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e64074fff561147f3a22e79b20931296e40b99026e35dc8110766298caaa051",
  "source_text_sha256": "5e64074fff561147f3a22e79b20931296e40b99026e35dc8110766298caaa051",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aca6ec",
        "00aca7df"
      ]
    ],
    "bytes_sha256": "0d279548b937bcf23fbcfc514c39d5f1151af2b324f66c41c4d1af23136340b7",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00839a78](../00839/00839a78.md)
- [008c0858](../008c0/008c0858.md)
- [008d3aa4](../008d3/008d3aa4.md)
- [008d970c](../008d9/008d970c.md)
- [008dac04](../008da/008dac04.md)
- [008fe500](../008fe/008fe500.md)
- [00a3de60](../00a3d/00a3de60.md)
- [00ac0514](../00ac0/00ac0514.md)
- [00ac9524](../00ac9/00ac9524.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)
- [008b7f1c](../008b7/008b7f1c.md)
- [008b89cc](../008b8/008b89cc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1573 bytes

~~~c

void FUN_00aca6ec(long param_1)

{
  long lVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00aca6f4 to 00bca703 has its CatchHandler @ 00acaaf0 */
  lVar1 = FUN_008524fc();
  lVar1 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 4));
  if (lVar1 != 0) {
    lVar1 = FUN_008524fc();
    uVar2 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 4));
    FUN_008b7f1c(uVar2,1);
  }
                    /* try { // try from 00aca730 to 00bca743 has its CatchHandler @ 00acaae8 */
  lVar1 = FUN_008524fc();
  lVar1 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 8));
  if (lVar1 != 0) {
    lVar1 = FUN_008524fc();
    uVar2 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 8));
    FUN_008b7f1c(uVar2,1);
  }
                    /* try { // try from 00aca764 to 00bca777 has its CatchHandler @ 00acab08 */
  lVar1 = FUN_008524fc();
  lVar1 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 0xc));
  if (lVar1 != 0) {
                    /* try { // try from 00aca77c to 00bca7af has its CatchHandler @ 00acab28 */
    lVar1 = FUN_008524fc();
    uVar2 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 0xc));
    FUN_008b7f1c(uVar2,1);
  }
  lVar1 = FUN_008524fc();
  lVar1 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 0x10));
  if (lVar1 != 0) {
    lVar1 = FUN_008524fc();
                    /* try { // try from 00aca7b8 to 00bca7bf has its CatchHandler @ 00acab40 */
    uVar2 = FUN_008b89cc(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 0x10));
    FUN_008b7f1c(uVar2,1);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aca6ec"></a> `00aca6ec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aca6f0"></a> `00aca6f0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca6f4"></a> `00aca6f4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aca6f8"></a> `00aca6f8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aca6fc"></a> `00aca6fc` | `80 1f f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aca700"></a> `00aca700` | `61 06 40 b9` | ldr w1,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00aca704"></a> `00aca704` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aca708"></a> `00aca708` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aca70c"></a> `00aca70c` | `b0 b8 f7 97` | bl 0x008b89cc | `UNCONDITIONAL_CALL`
<a id="insn-00aca710"></a> `00aca710` | `00 01 00 b4` | cbz x0,0x00aca730 | `CONDITIONAL_JUMP`
<a id="insn-00aca714"></a> `00aca714` | `7a 1f f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aca718"></a> `00aca718` | `61 06 40 b9` | ldr w1,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00aca71c"></a> `00aca71c` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aca720"></a> `00aca720` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aca724"></a> `00aca724` | `aa b8 f7 97` | bl 0x008b89cc | `UNCONDITIONAL_CALL`
<a id="insn-00aca728"></a> `00aca728` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aca72c"></a> `00aca72c` | `fc b5 f7 97` | bl 0x008b7f1c | `UNCONDITIONAL_CALL`
<a id="insn-00aca730"></a> `00aca730` | `73 1f f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aca734"></a> `00aca734` | `61 0a 40 b9` | ldr w1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aca738"></a> `00aca738` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aca73c"></a> `00aca73c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aca740"></a> `00aca740` | `a3 b8 f7 97` | bl 0x008b89cc | `UNCONDITIONAL_CALL`
<a id="insn-00aca744"></a> `00aca744` | `00 01 00 b4` | cbz x0,0x00aca764 | `CONDITIONAL_JUMP`
<a id="insn-00aca748"></a> `00aca748` | `6d 1f f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aca74c"></a> `00aca74c` | `61 0a 40 b9` | ldr w1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aca750"></a> `00aca750` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aca754"></a> `00aca754` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aca758"></a> `00aca758` | `9d b8 f7 97` | bl 0x008b89cc | `UNCONDITIONAL_CALL`
<a id="insn-00aca75c"></a> `00aca75c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aca760"></a> `00aca760` | `ef b5 f7 97` | bl 0x008b7f1c | `UNCONDITIONAL_CALL`
<a id="insn-00aca764"></a> `00aca764` | `66 1f f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aca768"></a> `00aca768` | `61 0e 40 b9` | ldr w1,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00aca76c"></a> `00aca76c` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aca770"></a> `00aca770` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aca774"></a> `00aca774` | `96 b8 f7 97` | bl 0x008b89cc | `UNCONDITIONAL_CALL`
<a id="insn-00aca778"></a> `00aca778` | `00 01 00 b4` | cbz x0,0x00aca798 | `CONDITIONAL_JUMP`
<a id="insn-00aca77c"></a> `00aca77c` | `60 1f f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aca780"></a> `00aca780` | `61 0e 40 b9` | ldr w1,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00aca784"></a> `00aca784` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aca788"></a> `00aca788` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aca78c"></a> `00aca78c` | `90 b8 f7 97` | bl 0x008b89cc | `UNCONDITIONAL_CALL`
<a id="insn-00aca790"></a> `00aca790` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aca794"></a> `00aca794` | `e2 b5 f7 97` | bl 0x008b7f1c | `UNCONDITIONAL_CALL`
<a id="insn-00aca798"></a> `00aca798` | `59 1f f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aca79c"></a> `00aca79c` | `61 12 40 b9` | ldr w1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aca7a0"></a> `00aca7a0` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aca7a4"></a> `00aca7a4` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aca7a8"></a> `00aca7a8` | `89 b8 f7 97` | bl 0x008b89cc | `UNCONDITIONAL_CALL`
<a id="insn-00aca7ac"></a> `00aca7ac` | `40 01 00 b4` | cbz x0,0x00aca7d4 | `CONDITIONAL_JUMP`
<a id="insn-00aca7b0"></a> `00aca7b0` | `53 1f f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aca7b4"></a> `00aca7b4` | `61 12 40 b9` | ldr w1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aca7b8"></a> `00aca7b8` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aca7bc"></a> `00aca7bc` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aca7c0"></a> `00aca7c0` | `83 b8 f7 97` | bl 0x008b89cc | `UNCONDITIONAL_CALL`
<a id="insn-00aca7c4"></a> `00aca7c4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aca7c8"></a> `00aca7c8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca7cc"></a> `00aca7cc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aca7d0"></a> `00aca7d0` | `d3 b5 f7 17` | b 0x008b7f1c | `CALL_TERMINATOR`
<a id="insn-00aca7d4"></a> `00aca7d4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca7d8"></a> `00aca7d8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aca7dc"></a> `00aca7dc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aca6ec`](#insn-00aca6ec) 範囲 `[['00aca6ec', '00aca6f3']]`
  - `FALL_THROUGH` [`00aca6f0`](#insn-00aca6f0) → [`00aca6f4`](#insn-00aca6f4)
- ブロック [`00aca6f4`](#insn-00aca6f4) 範囲 `[['00aca6f4', '00aca713']]`
  - `CONDITIONAL_JUMP` [`00aca710`](#insn-00aca710) → [`00aca730`](#insn-00aca730)
  - `FALL_THROUGH` [`00aca710`](#insn-00aca710) → [`00aca714`](#insn-00aca714)
- ブロック [`00aca714`](#insn-00aca714) 範囲 `[['00aca714', '00aca72f']]`
  - `FALL_THROUGH` [`00aca72c`](#insn-00aca72c) → [`00aca730`](#insn-00aca730)
- ブロック [`00aca730`](#insn-00aca730) 範囲 `[['00aca730', '00aca747']]`
  - `CONDITIONAL_JUMP` [`00aca744`](#insn-00aca744) → [`00aca764`](#insn-00aca764)
  - `FALL_THROUGH` [`00aca744`](#insn-00aca744) → [`00aca748`](#insn-00aca748)
- ブロック [`00aca748`](#insn-00aca748) 範囲 `[['00aca748', '00aca763']]`
  - `FALL_THROUGH` [`00aca760`](#insn-00aca760) → [`00aca764`](#insn-00aca764)
- ブロック [`00aca764`](#insn-00aca764) 範囲 `[['00aca764', '00aca77b']]`
  - `CONDITIONAL_JUMP` [`00aca778`](#insn-00aca778) → [`00aca798`](#insn-00aca798)
  - `FALL_THROUGH` [`00aca778`](#insn-00aca778) → [`00aca77c`](#insn-00aca77c)
- ブロック [`00aca77c`](#insn-00aca77c) 範囲 `[['00aca77c', '00aca797']]`
  - `FALL_THROUGH` [`00aca794`](#insn-00aca794) → [`00aca798`](#insn-00aca798)
- ブロック [`00aca798`](#insn-00aca798) 範囲 `[['00aca798', '00aca7af']]`
  - `CONDITIONAL_JUMP` [`00aca7ac`](#insn-00aca7ac) → [`00aca7d4`](#insn-00aca7d4)
  - `FALL_THROUGH` [`00aca7ac`](#insn-00aca7ac) → [`00aca7b0`](#insn-00aca7b0)
- ブロック [`00aca7b0`](#insn-00aca7b0) 範囲 `[['00aca7b0', '00aca7b7']]`
  - `FALL_THROUGH` [`00aca7b4`](#insn-00aca7b4) → [`00aca7b8`](#insn-00aca7b8)
- ブロック [`00aca7b8`](#insn-00aca7b8) 範囲 `[['00aca7b8', '00aca7d3']]`
- ブロック [`00aca7d4`](#insn-00aca7d4) 範囲 `[['00aca7d4', '00aca7df']]`

## 命令位置別の参照

- [`00aca6ec`](#insn-00aca6ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca6f0`](#insn-00aca6f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca6fc`](#insn-00aca6fc) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aca70c`](#insn-00aca70c) → [`008b89cc`](../008b8/008b89cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b89cc` · 推定シンボル `None` · 推定型 `None`
- [`00aca710`](#insn-00aca710) → [`00aca730`](#insn-00aca730) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca714`](#insn-00aca714) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aca724`](#insn-00aca724) → [`008b89cc`](../008b8/008b89cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b89cc` · 推定シンボル `None` · 推定型 `None`
- [`00aca72c`](#insn-00aca72c) → [`008b7f1c`](../008b7/008b7f1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7f1c` · 推定シンボル `None` · 推定型 `None`
- [`00aca730`](#insn-00aca730) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aca740`](#insn-00aca740) → [`008b89cc`](../008b8/008b89cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b89cc` · 推定シンボル `None` · 推定型 `None`
- [`00aca744`](#insn-00aca744) → [`00aca764`](#insn-00aca764) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca748`](#insn-00aca748) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aca758`](#insn-00aca758) → [`008b89cc`](../008b8/008b89cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b89cc` · 推定シンボル `None` · 推定型 `None`
- [`00aca760`](#insn-00aca760) → [`008b7f1c`](../008b7/008b7f1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7f1c` · 推定シンボル `None` · 推定型 `None`
- [`00aca764`](#insn-00aca764) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aca774`](#insn-00aca774) → [`008b89cc`](../008b8/008b89cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b89cc` · 推定シンボル `None` · 推定型 `None`
- [`00aca778`](#insn-00aca778) → [`00aca798`](#insn-00aca798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca77c`](#insn-00aca77c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aca78c`](#insn-00aca78c) → [`008b89cc`](../008b8/008b89cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b89cc` · 推定シンボル `None` · 推定型 `None`
- [`00aca794`](#insn-00aca794) → [`008b7f1c`](../008b7/008b7f1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7f1c` · 推定シンボル `None` · 推定型 `None`
- [`00aca798`](#insn-00aca798) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aca7a8`](#insn-00aca7a8) → [`008b89cc`](../008b8/008b89cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b89cc` · 推定シンボル `None` · 推定型 `None`
- [`00aca7ac`](#insn-00aca7ac) → [`00aca7d4`](#insn-00aca7d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca7b0`](#insn-00aca7b0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aca7c0`](#insn-00aca7c0) → [`008b89cc`](../008b8/008b89cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b89cc` · 推定シンボル `None` · 推定型 `None`
- [`00aca7c8`](#insn-00aca7c8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca7cc`](#insn-00aca7cc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca7d0`](#insn-00aca7d0) → [`008b7f1c`](../008b7/008b7f1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7f1c` · 推定シンボル `None` · 推定型 `None`
- [`00aca7d4`](#insn-00aca7d4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca7d8`](#insn-00aca7d8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aca6ec`](#insn-00aca6ec)

~~~json
{
  "source": "00aca6ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca6f0`](#insn-00aca6f0)

~~~json
{
  "source": "00aca6f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca6fc`](#insn-00aca6fc)

~~~json
{
  "source": "00aca6fc",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca70c`](#insn-00aca70c)

~~~json
{
  "source": "00aca70c",
  "target": "008b89cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca710`](#insn-00aca710)

~~~json
{
  "source": "00aca710",
  "target": "00aca730",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca714`](#insn-00aca714)

~~~json
{
  "source": "00aca714",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca724`](#insn-00aca724)

~~~json
{
  "source": "00aca724",
  "target": "008b89cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca72c`](#insn-00aca72c)

~~~json
{
  "source": "00aca72c",
  "target": "008b7f1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca730`](#insn-00aca730)

~~~json
{
  "source": "00aca730",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca740`](#insn-00aca740)

~~~json
{
  "source": "00aca740",
  "target": "008b89cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca744`](#insn-00aca744)

~~~json
{
  "source": "00aca744",
  "target": "00aca764",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca748`](#insn-00aca748)

~~~json
{
  "source": "00aca748",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca758`](#insn-00aca758)

~~~json
{
  "source": "00aca758",
  "target": "008b89cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca760`](#insn-00aca760)

~~~json
{
  "source": "00aca760",
  "target": "008b7f1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca764`](#insn-00aca764)

~~~json
{
  "source": "00aca764",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca774`](#insn-00aca774)

~~~json
{
  "source": "00aca774",
  "target": "008b89cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca778`](#insn-00aca778)

~~~json
{
  "source": "00aca778",
  "target": "00aca798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca77c`](#insn-00aca77c)

~~~json
{
  "source": "00aca77c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca78c`](#insn-00aca78c)

~~~json
{
  "source": "00aca78c",
  "target": "008b89cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca794`](#insn-00aca794)

~~~json
{
  "source": "00aca794",
  "target": "008b7f1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca798`](#insn-00aca798)

~~~json
{
  "source": "00aca798",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca7a8`](#insn-00aca7a8)

~~~json
{
  "source": "00aca7a8",
  "target": "008b89cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca7ac`](#insn-00aca7ac)

~~~json
{
  "source": "00aca7ac",
  "target": "00aca7d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca7b0`](#insn-00aca7b0)

~~~json
{
  "source": "00aca7b0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca7c0`](#insn-00aca7c0)

~~~json
{
  "source": "00aca7c0",
  "target": "008b89cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca7c8`](#insn-00aca7c8)

~~~json
{
  "source": "00aca7c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca7cc`](#insn-00aca7cc)

~~~json
{
  "source": "00aca7cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca7d0`](#insn-00aca7d0)

~~~json
{
  "source": "00aca7d0",
  "target": "008b7f1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca7d4`](#insn-00aca7d4)

~~~json
{
  "source": "00aca7d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca7d8`](#insn-00aca7d8)

~~~json
{
  "source": "00aca7d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
