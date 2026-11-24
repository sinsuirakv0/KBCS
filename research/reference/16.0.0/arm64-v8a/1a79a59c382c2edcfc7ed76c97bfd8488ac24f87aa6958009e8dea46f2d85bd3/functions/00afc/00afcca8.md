# 00afcca8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0169.md#review-7a7b866a66bb29d016478b6a58e030bd)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afd0d0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afd0d0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0007.md#compare-755227afb26d76985ce6ed3e387de39f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcca8",
  "name": "FUN_00afcca8",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1903bf37be3ec40bd9b7346685dfbd32a3a4eef88b8e2af6c8ecede9f2aaa090",
  "source_text_sha256": "1903bf37be3ec40bd9b7346685dfbd32a3a4eef88b8e2af6c8ecede9f2aaa090",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcca8",
        "00afcd0f"
      ]
    ],
    "bytes_sha256": "0f234928fb2d5904acf7b831b808afe5561f42c5c1b75b520173c233860efe07",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00716d50](../00716/00716d50.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 395 bytes

~~~c

undefined4 FUN_00afcca8(int param_1,int param_2)

{
  undefined4 uVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514b8();
  uVar3 = FUN_005e73e0(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    lVar2 = FUN_008514b8();
    uVar1 = *(undefined4 *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a64);
  }
  else {
    uVar1 = 0;
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcca8"></a> `00afcca8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afccac"></a> `00afccac` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afccb0"></a> `00afccb0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afccb4"></a> `00afccb4` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afccb8"></a> `00afccb8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afccbc"></a> `00afccbc` | `ff 51 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afccc0"></a> `00afccc0` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afccc4"></a> `00afccc4` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afccc8"></a> `00afccc8` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcccc"></a> `00afcccc` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afccd0"></a> `00afccd0` | `c4 a9 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afccd4"></a> `00afccd4` | `60 01 00 37` | tbnz w0,#0x0,0x00afcd00 | `CONDITIONAL_JUMP`
<a id="insn-00afccd8"></a> `00afccd8` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00afccdc"></a> `00afccdc` | `f7 51 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcce0"></a> `00afcce0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcce4"></a> `00afcce4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcce8"></a> `00afcce8` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afccec"></a> `00afccec` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afccf0"></a> `00afccf0` | `89 4c 89 52` | mov w9,#0x4a64 | `FALL_THROUGH`
<a id="insn-00afccf4"></a> `00afccf4` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afccf8"></a> `00afccf8` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afccfc"></a> `00afccfc` | `02 00 00 14` | b 0x00afcd04 | `UNCONDITIONAL_JUMP`
<a id="insn-00afcd00"></a> `00afcd00` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afcd04"></a> `00afcd04` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcd08"></a> `00afcd08` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afcd0c"></a> `00afcd0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcca8`](#insn-00afcca8) 範囲 `[['00afcca8', '00afccd7']]`
  - `CONDITIONAL_JUMP` [`00afccd4`](#insn-00afccd4) → [`00afcd00`](#insn-00afcd00)
  - `FALL_THROUGH` [`00afccd4`](#insn-00afccd4) → [`00afccd8`](#insn-00afccd8)
- ブロック [`00afccd8`](#insn-00afccd8) 範囲 `[['00afccd8', '00afccff']]`
  - `UNCONDITIONAL_JUMP` [`00afccfc`](#insn-00afccfc) → [`00afcd04`](#insn-00afcd04)
- ブロック [`00afcd00`](#insn-00afcd00) 範囲 `[['00afcd00', '00afcd03']]`
  - `FALL_THROUGH` [`00afcd00`](#insn-00afcd00) → [`00afcd04`](#insn-00afcd04)
- ブロック [`00afcd04`](#insn-00afcd04) 範囲 `[['00afcd04', '00afcd0f']]`

## 命令位置別の参照

- [`00afcca8`](#insn-00afcca8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afccac`](#insn-00afccac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afccbc`](#insn-00afccbc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afccd0`](#insn-00afccd0) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afccd4`](#insn-00afccd4) → [`00afcd00`](#insn-00afcd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afccdc`](#insn-00afccdc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afccfc`](#insn-00afccfc) → [`00afcd04`](#insn-00afcd04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcd04`](#insn-00afcd04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcd08`](#insn-00afcd08) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcca8`](#insn-00afcca8)

~~~json
{
  "source": "00afcca8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afccac`](#insn-00afccac)

~~~json
{
  "source": "00afccac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afccbc`](#insn-00afccbc)

~~~json
{
  "source": "00afccbc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afccd0`](#insn-00afccd0)

~~~json
{
  "source": "00afccd0",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afccd4`](#insn-00afccd4)

~~~json
{
  "source": "00afccd4",
  "target": "00afcd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afccdc`](#insn-00afccdc)

~~~json
{
  "source": "00afccdc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afccfc`](#insn-00afccfc)

~~~json
{
  "source": "00afccfc",
  "target": "00afcd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcd04`](#insn-00afcd04)

~~~json
{
  "source": "00afcd04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcd08`](#insn-00afcd08)

~~~json
{
  "source": "00afcd08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
