# 006bffdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0120.md#review-6425f40a2e17ff4753e04f9a06b88666)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0019.md#review-6425f40a2e17ff4753e04f9a06b88666)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006bffdc",
  "name": "FUN_006bffdc",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3e19cccad81cb0b0aa8307e1f154eaebb0908321e17e2b3ea57460638eb10f5",
  "source_text_sha256": "d3e19cccad81cb0b0aa8307e1f154eaebb0908321e17e2b3ea57460638eb10f5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006bffdc",
        "006c0067"
      ]
    ],
    "bytes_sha256": "377c1983d6d87542582d5c3a44d8038172a02cc08c7cd5e7e6ce4c05e36a4397",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006bed1c](../006be/006bed1c.md)

## 呼び出し先

- [005e8158](../005e8/005e8158.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1846 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined8 FUN_006bffdc(int *param_1)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined1 auVar3 [16];
  undefined1 auVar4 [16];
  
                    /* try { // try from 006bffe0 to 007bffe3 has its CatchHandler @ 006c02cc */
  uVar1 = *(undefined8 *)param_1;
  auVar3._8_8_ = uVar1;
  auVar3._0_8_ = uVar1;
                    /* try { // try from 006bfff8 to 007bfffb has its CatchHandler @ 006c02ac */
  auVar4 = NEON_ushl(auVar3,_DAT_002c2d50,8);
                    /* try { // try from 006c0010 to 007c0017 has its CatchHandler @ 006c0274 */
  auVar3 = NEON_ushl(auVar3,_DAT_002c26e0,8);
                    /* try { // try from 006c002c to 007c002f has its CatchHandler @ 006c027c */
  uVar2 = NEON_ushl(CONCAT44(CONCAT13(auVar3[0xb] ^ auVar4[0xb],
                                      CONCAT12(auVar3[10] ^ auVar4[10],
                                               CONCAT11(auVar3[9] ^ auVar4[9],auVar3[8] ^ auVar4[8])
                                              )),
                             CONCAT13(auVar3[3] ^ auVar4[3],
                                      CONCAT12(auVar3[2] ^ auVar4[2],
                                               CONCAT11(auVar3[1] ^ auVar4[1],auVar3[0] ^ auVar4[0])
                                              ))),DAT_002c40c8,4);
                    /* try { // try from 006c0044 to 007c004b has its CatchHandler @ 006c025c */
  *param_1 = (((uint)(byte)((ulong)uVar1 >> 0x38) ^ (uint)uVar1) & 0xff |
              (uint)(uVar2 & 0xff00000000ff00) | (uint)((uVar2 & 0xff00000000ff00) >> 0x20) |
             ((uint)((ulong)uVar1 >> 0x20) ^ (uint)uVar1 >> 0x18) << 0x18) + 1;
  FUN_005e8158();
                    /* try { // try from 006c0060 to 007c0067 has its CatchHandler @ 006c0258 */
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006bffdc"></a> `006bffdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-006bffe0"></a> `006bffe0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006bffe4"></a> `006bffe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006bffe8"></a> `006bffe8` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-006bffec"></a> `006bffec` | `08 e0 ff f0` | adrp x8,0x2c2000 | `FALL_THROUGH`
<a id="insn-006bfff0"></a> `006bfff0` | `09 e0 ff f0` | adrp x9,0x2c2000 | `FALL_THROUGH`
<a id="insn-006bfff4"></a> `006bfff4` | `01 55 c3 3d` | ldr q1,[x8, #0xd50] | `FALL_THROUGH`
<a id="insn-006bfff8"></a> `006bfff8` | `22 b9 c1 3d` | ldr q2,[x9, #0x6e0] | `FALL_THROUGH`
<a id="insn-006bfffc"></a> `006bfffc` | `28 e0 ff b0` | adrp x8,0x2c4000 | `FALL_THROUGH`
<a id="insn-006c0000"></a> `006c0000` | `60 0e 08 4e` | dup v0.2D,x19 | `FALL_THROUGH`
<a id="insn-006c0004"></a> `006c0004` | `6a fe 60 d3` | lsr x10,x19,#0x20 | `FALL_THROUGH`
<a id="insn-006c0008"></a> `006c0008` | `4a 61 53 4a` | eor w10,w10,w19, LSR #0x18 | `FALL_THROUGH`
<a id="insn-006c000c"></a> `006c000c` | `01 44 e1 6e` | ushl v1.2D,v0.2D,v1.2D | `FALL_THROUGH`
<a id="insn-006c0010"></a> `006c0010` | `00 44 e2 6e` | ushl v0.2D,v0.2D,v2.2D | `FALL_THROUGH`
<a id="insn-006c0014"></a> `006c0014` | `42 e4 02 2f` | movi d2,#0xff00000000ff00 | `FALL_THROUGH`
<a id="insn-006c0018"></a> `006c0018` | `00 1c 21 6e` | eor v0.16B,v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-006c001c"></a> `006c001c` | `01 65 40 fd` | ldr d1,[x8, #0xc8] | `FALL_THROUGH`
<a id="insn-006c0020"></a> `006c0020` | `68 fe 78 d3` | lsr x8,x19,#0x38 | `FALL_THROUGH`
<a id="insn-006c0024"></a> `006c0024` | `08 01 13 4a` | eor w8,w8,w19 | `FALL_THROUGH`
<a id="insn-006c0028"></a> `006c0028` | `00 28 a1 0e` | xtn v0.2S,v0.2D | `FALL_THROUGH`
<a id="insn-006c002c"></a> `006c002c` | `08 1d 00 12` | and w8,w8,#0xff | `FALL_THROUGH`
<a id="insn-006c0030"></a> `006c0030` | `00 44 a1 2e` | ushl v0.2S,v0.2S,v1.2S | `FALL_THROUGH`
<a id="insn-006c0034"></a> `006c0034` | `00 1c 22 0e` | and v0.8B,v0.8B,v2.8B | `FALL_THROUGH`
<a id="insn-006c0038"></a> `006c0038` | `09 3c 0c 0e` | mov w9,v0.S[0x1] | `FALL_THROUGH`
<a id="insn-006c003c"></a> `006c003c` | `0b 00 26 1e` | fmov w11,s0 | `FALL_THROUGH`
<a id="insn-006c0040"></a> `006c0040` | `08 01 0b 2a` | orr w8,w8,w11 | `FALL_THROUGH`
<a id="insn-006c0044"></a> `006c0044` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006c0048"></a> `006c0048` | `08 61 0a 2a` | orr w8,w8,w10, LSL #0x18 | `FALL_THROUGH`
<a id="insn-006c004c"></a> `006c004c` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006c0050"></a> `006c0050` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-006c0054"></a> `006c0054` | `41 a0 fc 97` | bl 0x005e8158 | `UNCONDITIONAL_CALL`
<a id="insn-006c0058"></a> `006c0058` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006c005c"></a> `006c005c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006c0060"></a> `006c0060` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-006c0064"></a> `006c0064` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006bffdc`](#insn-006bffdc) 範囲 `[['006bffdc', '006bffdf']]`
  - `FALL_THROUGH` [`006bffdc`](#insn-006bffdc) → [`006bffe0`](#insn-006bffe0)
- ブロック [`006bffe0`](#insn-006bffe0) 範囲 `[['006bffe0', '006bfff7']]`
  - `FALL_THROUGH` [`006bfff4`](#insn-006bfff4) → [`006bfff8`](#insn-006bfff8)
- ブロック [`006bfff8`](#insn-006bfff8) 範囲 `[['006bfff8', '006c000f']]`
  - `FALL_THROUGH` [`006c000c`](#insn-006c000c) → [`006c0010`](#insn-006c0010)
- ブロック [`006c0010`](#insn-006c0010) 範囲 `[['006c0010', '006c002b']]`
  - `FALL_THROUGH` [`006c0028`](#insn-006c0028) → [`006c002c`](#insn-006c002c)
- ブロック [`006c002c`](#insn-006c002c) 範囲 `[['006c002c', '006c0043']]`
  - `FALL_THROUGH` [`006c0040`](#insn-006c0040) → [`006c0044`](#insn-006c0044)
- ブロック [`006c0044`](#insn-006c0044) 範囲 `[['006c0044', '006c005f']]`
  - `FALL_THROUGH` [`006c005c`](#insn-006c005c) → [`006c0060`](#insn-006c0060)
- ブロック [`006c0060`](#insn-006c0060) 範囲 `[['006c0060', '006c0067']]`

## 命令位置別の参照

- [`006bffdc`](#insn-006bffdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bffe0`](#insn-006bffe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bfff4`](#insn-006bfff4) → `002c2d50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bfff8`](#insn-006bfff8) → `002c26e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006c001c`](#insn-006c001c) → `002c40c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006c0054`](#insn-006c0054) → [`005e8158`](../005e8/005e8158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e8158` · 推定シンボル `None` · 推定型 `None`
- [`006c005c`](#insn-006c005c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006c0060`](#insn-006c0060) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006bffdc`](#insn-006bffdc)

~~~json
{
  "source": "006bffdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bffe0`](#insn-006bffe0)

~~~json
{
  "source": "006bffe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bfff4`](#insn-006bfff4)

~~~json
{
  "source": "006bfff4",
  "target": "002c2d50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bfff8`](#insn-006bfff8)

~~~json
{
  "source": "006bfff8",
  "target": "002c26e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006c001c`](#insn-006c001c)

~~~json
{
  "source": "006c001c",
  "target": "002c40c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c40c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0800000010000000",
  "capture_start": "002c40c8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006c0054`](#insn-006c0054)

~~~json
{
  "source": "006c0054",
  "target": "005e8158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006c005c`](#insn-006c005c)

~~~json
{
  "source": "006c005c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006c0060`](#insn-006c0060)

~~~json
{
  "source": "006c0060",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
