# 008dacbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `008a6e24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6e24.md) · 移動量 `+0x33e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0016.md#compare-ddfada2d30f4d634143e1faedaea75c7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `008dae58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008dae58.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0031.md#compare-6e51187d8a970c2c04f779f21bc93859)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008dacbc",
  "name": "FUN_008dacbc",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a692b6da895fb53ecf53e015d0d6f7e8fb1606f92612c8ee9db4676a74fb3f73",
  "source_text_sha256": "a692b6da895fb53ecf53e015d0d6f7e8fb1606f92612c8ee9db4676a74fb3f73",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008dacbc",
        "008dad0b"
      ]
    ],
    "bytes_sha256": "936b953fb75f5d273f1b4e1a4736c5060ff65f4ad4ecfcd5f946b1195e5a8130",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [008d6b44](../008d6/008d6b44.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 406 bytes

~~~c

void FUN_008dacbc(void *param_1)

{
  long *plVar1;
  long *plVar2;
  long lVar3;
  
  plVar1 = *(long **)((long)param_1 + 0x40);
  plVar2 = (long *)((long)param_1 + 0x20);
  if (plVar1 == plVar2) {
    lVar3 = 0x20;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_008dacfc;
    lVar3 = 0x28;
    plVar2 = plVar1;
  }
  (**(code **)(*plVar2 + lVar3))();
LAB_008dacfc:
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008dacbc"></a> `008dacbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-008dacc0"></a> `008dacc0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008dacc4"></a> `008dacc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008dacc8"></a> `008dacc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008daccc"></a> `008daccc` | `00 20 40 f9` | ldr x0,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-008dacd0"></a> `008dacd0` | `69 82 00 91` | add x9,x19,#0x20 | `FALL_THROUGH`
<a id="insn-008dacd4"></a> `008dacd4` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-008dacd8"></a> `008dacd8` | `80 00 00 54` | b.eq 0x008dace8 | `CONDITIONAL_JUMP`
<a id="insn-008dacdc"></a> `008dacdc` | `00 01 00 b4` | cbz x0,0x008dacfc | `CONDITIONAL_JUMP`
<a id="insn-008dace0"></a> `008dace0` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-008dace4"></a> `008dace4` | `03 00 00 14` | b 0x008dacf0 | `UNCONDITIONAL_JUMP`
<a id="insn-008dace8"></a> `008dace8` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-008dacec"></a> `008dacec` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-008dacf0"></a> `008dacf0` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-008dacf4"></a> `008dacf4` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008dacf8"></a> `008dacf8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008dacfc"></a> `008dacfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dad00"></a> `008dad00` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008dad04"></a> `008dad04` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-008dad08"></a> `008dad08` | `6a f3 0d 14` | b 0x00c57ab0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008dacbc`](#insn-008dacbc) 範囲 `[['008dacbc', '008dacdb']]`
  - `CONDITIONAL_JUMP` [`008dacd8`](#insn-008dacd8) → [`008dace8`](#insn-008dace8)
  - `FALL_THROUGH` [`008dacd8`](#insn-008dacd8) → [`008dacdc`](#insn-008dacdc)
- ブロック [`008dacdc`](#insn-008dacdc) 範囲 `[['008dacdc', '008dacdf']]`
  - `CONDITIONAL_JUMP` [`008dacdc`](#insn-008dacdc) → [`008dacfc`](#insn-008dacfc)
  - `FALL_THROUGH` [`008dacdc`](#insn-008dacdc) → [`008dace0`](#insn-008dace0)
- ブロック [`008dace0`](#insn-008dace0) 範囲 `[['008dace0', '008dace7']]`
  - `UNCONDITIONAL_JUMP` [`008dace4`](#insn-008dace4) → [`008dacf0`](#insn-008dacf0)
- ブロック [`008dace8`](#insn-008dace8) 範囲 `[['008dace8', '008dacef']]`
  - `FALL_THROUGH` [`008dacec`](#insn-008dacec) → [`008dacf0`](#insn-008dacf0)
- ブロック [`008dacf0`](#insn-008dacf0) 範囲 `[['008dacf0', '008dacfb']]`
  - `FALL_THROUGH` [`008dacf8`](#insn-008dacf8) → [`008dacfc`](#insn-008dacfc)
- ブロック [`008dacfc`](#insn-008dacfc) 範囲 `[['008dacfc', '008dad0b']]`

## 命令位置別の参照

- [`008dacbc`](#insn-008dacbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dacc0`](#insn-008dacc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dacd8`](#insn-008dacd8) → [`008dace8`](#insn-008dace8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dacdc`](#insn-008dacdc) → [`008dacfc`](#insn-008dacfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dace4`](#insn-008dace4) → [`008dacf0`](#insn-008dacf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dad00`](#insn-008dad00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dad04`](#insn-008dad04) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dad08`](#insn-008dad08) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008dacbc`](#insn-008dacbc)

~~~json
{
  "source": "008dacbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dacc0`](#insn-008dacc0)

~~~json
{
  "source": "008dacc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dacd8`](#insn-008dacd8)

~~~json
{
  "source": "008dacd8",
  "target": "008dace8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dacdc`](#insn-008dacdc)

~~~json
{
  "source": "008dacdc",
  "target": "008dacfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dace4`](#insn-008dace4)

~~~json
{
  "source": "008dace4",
  "target": "008dacf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dad00`](#insn-008dad00)

~~~json
{
  "source": "008dad00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dad04`](#insn-008dad04)

~~~json
{
  "source": "008dad04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dad08`](#insn-008dad08)

~~~json
{
  "source": "008dad08",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
