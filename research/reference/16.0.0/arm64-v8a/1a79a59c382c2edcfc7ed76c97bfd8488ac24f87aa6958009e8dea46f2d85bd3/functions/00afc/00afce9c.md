# 00afce9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0170.md#review-684b03ed2af21e686df8a7f8f549be87)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afd2c4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afd2c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0036.md#compare-fe3060f8bdbdd96927359761949a98af)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afce9c",
  "name": "FUN_00afce9c",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e4a65c799469ea73902490172707516a2f99b6640d990328d96fe2e9cfe1954",
  "source_text_sha256": "7e4a65c799469ea73902490172707516a2f99b6640d990328d96fe2e9cfe1954",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afce9c",
        "00afcf0f"
      ]
    ],
    "bytes_sha256": "29098f5ae2571affb8b07fdfe9535211d17843f5abfc6c5efb9f93fc865c9323",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
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

## 疑似コード / UTF-8 389 bytes

~~~c

void FUN_00afce9c(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008514b8();
  uVar2 = FUN_005e73e0(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514b8();
    lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
    *(int *)(lVar1 + 0x84bfc) = *(int *)(lVar1 + 0x84bfc) + param_3;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afce9c"></a> `00afce9c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afcea0"></a> `00afcea0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcea4"></a> `00afcea4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcea8"></a> `00afcea8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afceac"></a> `00afceac` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afceb0"></a> `00afceb0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afceb4"></a> `00afceb4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afceb8"></a> `00afceb8` | `80 51 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcebc"></a> `00afcebc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afcec0"></a> `00afcec0` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afcec4"></a> `00afcec4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcec8"></a> `00afcec8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afcecc"></a> `00afcecc` | `45 a9 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afced0"></a> `00afced0` | `80 01 00 37` | tbnz w0,#0x0,0x00afcf00 | `CONDITIONAL_JUMP`
<a id="insn-00afced4"></a> `00afced4` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afced8"></a> `00afced8` | `78 51 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcedc"></a> `00afcedc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcee0"></a> `00afcee0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcee4"></a> `00afcee4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcee8"></a> `00afcee8` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afceec"></a> `00afceec` | `89 7f 89 52` | mov w9,#0x4bfc | `FALL_THROUGH`
<a id="insn-00afcef0"></a> `00afcef0` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afcef4"></a> `00afcef4` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcef8"></a> `00afcef8` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00afcefc"></a> `00afcefc` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcf00"></a> `00afcf00` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcf04"></a> `00afcf04` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcf08"></a> `00afcf08` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afcf0c"></a> `00afcf0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afce9c`](#insn-00afce9c) 範囲 `[['00afce9c', '00afced3']]`
  - `CONDITIONAL_JUMP` [`00afced0`](#insn-00afced0) → [`00afcf00`](#insn-00afcf00)
  - `FALL_THROUGH` [`00afced0`](#insn-00afced0) → [`00afced4`](#insn-00afced4)
- ブロック [`00afced4`](#insn-00afced4) 範囲 `[['00afced4', '00afceff']]`
  - `FALL_THROUGH` [`00afcefc`](#insn-00afcefc) → [`00afcf00`](#insn-00afcf00)
- ブロック [`00afcf00`](#insn-00afcf00) 範囲 `[['00afcf00', '00afcf0f']]`

## 命令位置別の参照

- [`00afce9c`](#insn-00afce9c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcea0`](#insn-00afcea0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcea4`](#insn-00afcea4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afceb8`](#insn-00afceb8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afcecc`](#insn-00afcecc) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afced0`](#insn-00afced0) → [`00afcf00`](#insn-00afcf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afced8`](#insn-00afced8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afcf00`](#insn-00afcf00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf04`](#insn-00afcf04) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcf08`](#insn-00afcf08) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afce9c`](#insn-00afce9c)

~~~json
{
  "source": "00afce9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcea0`](#insn-00afcea0)

~~~json
{
  "source": "00afcea0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcea4`](#insn-00afcea4)

~~~json
{
  "source": "00afcea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afceb8`](#insn-00afceb8)

~~~json
{
  "source": "00afceb8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcecc`](#insn-00afcecc)

~~~json
{
  "source": "00afcecc",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afced0`](#insn-00afced0)

~~~json
{
  "source": "00afced0",
  "target": "00afcf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afced8`](#insn-00afced8)

~~~json
{
  "source": "00afced8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcf00`](#insn-00afcf00)

~~~json
{
  "source": "00afcf00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf04`](#insn-00afcf04)

~~~json
{
  "source": "00afcf04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcf08`](#insn-00afcf08)

~~~json
{
  "source": "00afcf08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
