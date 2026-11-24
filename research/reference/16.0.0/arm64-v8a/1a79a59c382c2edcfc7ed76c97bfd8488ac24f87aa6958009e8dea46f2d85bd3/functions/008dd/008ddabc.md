# 008ddabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `008a9c24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a9c24.md) · 移動量 `+0x33e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0010.md#compare-f88279078c47f363be2a65ec09fc6d3d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `008ddc58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddc58.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0002.md#compare-ce9bc011d39d9e0ad0a8512434628804)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008ddabc",
  "name": "FUN_008ddabc",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e710bd00e72cca244ed2a96407fa0790520c01418db34b061195ad45c7708c7",
  "source_text_sha256": "2e710bd00e72cca244ed2a96407fa0790520c01418db34b061195ad45c7708c7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008ddabc",
        "008ddb17"
      ]
    ],
    "bytes_sha256": "ecff9335e850dec033cc9ddb1da574ea89e1819b3a626f008f344887f8561104",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008dde04](../008dd/008dde04.md)

## 呼び出し先

- [008dbf84](../008db/008dbf84.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 367 bytes

~~~c

void FUN_008ddabc(long param_1)

{
  int *piVar1;
  undefined8 *puVar2;
  int *piVar3;
  
  puVar2 = (undefined8 *)(*(long *)(param_1 + 0x38) + (long)*(int *)(param_1 + 4) * 0x18);
  piVar1 = (int *)puVar2[1];
  for (piVar3 = (int *)*puVar2; piVar3 != piVar1; piVar3 = piVar3 + 1) {
    FUN_008dbf84(*(long *)(param_1 + 8) + (long)*piVar3 * 0x100);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008ddabc"></a> `008ddabc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-008ddac0"></a> `008ddac0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ddac4"></a> `008ddac4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ddac8"></a> `008ddac8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008ddacc"></a> `008ddacc` | `09 04 80 b9` | ldrsw x9,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-008ddad0"></a> `008ddad0` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-008ddad4"></a> `008ddad4` | `0a 1c 40 f9` | ldr x10,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-008ddad8"></a> `008ddad8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-008ddadc"></a> `008ddadc` | `28 29 28 9b` | smaddl x8,w9,w8,x10 | `FALL_THROUGH`
<a id="insn-008ddae0"></a> `008ddae0` | `14 55 40 a9` | ldp x20,x21,[x8] | `FALL_THROUGH`
<a id="insn-008ddae4"></a> `008ddae4` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-008ddae8"></a> `008ddae8` | `00 01 00 54` | b.eq 0x008ddb08 | `CONDITIONAL_JUMP`
<a id="insn-008ddaec"></a> `008ddaec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008ddaf0"></a> `008ddaf0` | `88 46 80 b8` | ldrsw x8,[x20], #0x4 | `FALL_THROUGH`
<a id="insn-008ddaf4"></a> `008ddaf4` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-008ddaf8"></a> `008ddaf8` | `20 21 08 8b` | add x0,x9,x8, LSL #0x8 | `FALL_THROUGH`
<a id="insn-008ddafc"></a> `008ddafc` | `22 f9 ff 97` | bl 0x008dbf84 | `UNCONDITIONAL_CALL`
<a id="insn-008ddb00"></a> `008ddb00` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-008ddb04"></a> `008ddb04` | `61 ff ff 54` | b.ne 0x008ddaf0 | `CONDITIONAL_JUMP`
<a id="insn-008ddb08"></a> `008ddb08` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ddb0c"></a> `008ddb0c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ddb10"></a> `008ddb10` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-008ddb14"></a> `008ddb14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008ddabc`](#insn-008ddabc) 範囲 `[['008ddabc', '008ddaeb']]`
  - `CONDITIONAL_JUMP` [`008ddae8`](#insn-008ddae8) → [`008ddb08`](#insn-008ddb08)
  - `FALL_THROUGH` [`008ddae8`](#insn-008ddae8) → [`008ddaec`](#insn-008ddaec)
- ブロック [`008ddaec`](#insn-008ddaec) 範囲 `[['008ddaec', '008ddaef']]`
  - `FALL_THROUGH` [`008ddaec`](#insn-008ddaec) → [`008ddaf0`](#insn-008ddaf0)
- ブロック [`008ddaf0`](#insn-008ddaf0) 範囲 `[['008ddaf0', '008ddb07']]`
  - `CONDITIONAL_JUMP` [`008ddb04`](#insn-008ddb04) → [`008ddaf0`](#insn-008ddaf0)
  - `FALL_THROUGH` [`008ddb04`](#insn-008ddb04) → [`008ddb08`](#insn-008ddb08)
- ブロック [`008ddb08`](#insn-008ddb08) 範囲 `[['008ddb08', '008ddb17']]`

## 命令位置別の参照

- [`008ddabc`](#insn-008ddabc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddac0`](#insn-008ddac0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddac4`](#insn-008ddac4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddae8`](#insn-008ddae8) → [`008ddb08`](#insn-008ddb08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddafc`](#insn-008ddafc) → [`008dbf84`](../008db/008dbf84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008dbf84` · 推定シンボル `None` · 推定型 `None`
- [`008ddb04`](#insn-008ddb04) → [`008ddaf0`](#insn-008ddaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddb08`](#insn-008ddb08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddb0c`](#insn-008ddb0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddb10`](#insn-008ddb10) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008ddabc`](#insn-008ddabc)

~~~json
{
  "source": "008ddabc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddac0`](#insn-008ddac0)

~~~json
{
  "source": "008ddac0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddac4`](#insn-008ddac4)

~~~json
{
  "source": "008ddac4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddae8`](#insn-008ddae8)

~~~json
{
  "source": "008ddae8",
  "target": "008ddb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddafc`](#insn-008ddafc)

~~~json
{
  "source": "008ddafc",
  "target": "008dbf84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ddb04`](#insn-008ddb04)

~~~json
{
  "source": "008ddb04",
  "target": "008ddaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddb08`](#insn-008ddb08)

~~~json
{
  "source": "008ddb08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddb0c`](#insn-008ddb0c)

~~~json
{
  "source": "008ddb0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddb10`](#insn-008ddb10)

~~~json
{
  "source": "008ddb10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
