# 00acafb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acadb8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acadb8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-8d79d6265dfbc2f5316e401da744dc0d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acb024`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb024.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-20445605167e68edd585463545cbab9c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acafb4",
  "name": "FUN_00acafb4",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3038d08e80c19faeb132d5462da0ce2621e5bedaa8b0a794ab06fc10931c483",
  "source_text_sha256": "e3038d08e80c19faeb132d5462da0ce2621e5bedaa8b0a794ab06fc10931c483",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acafb4",
        "00acaff7"
      ]
    ],
    "bytes_sha256": "f3db1378d1e8bbb3eff8f9f488f9cf1ceecbe74c3cdf30170f5e0026f4acc6ca",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00788cac](../00788/00788cac.md)
- [0082ee20](../0082e/0082ee20.md)
- [008fe9e4](../008fe/008fe9e4.md)
- [00a3de58](../00a3d/00a3de58.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 307 bytes

~~~c

void FUN_00acafb4(long param_1,uint param_2)

{
  undefined4 uVar1;
  
  if ((param_2 & 1) == 0) {
    *(undefined4 *)(param_1 + 0x9c) = 2;
    FUN_008514f8();
    uVar1 = 0xe;
  }
  else {
    uVar1 = 0;
    *(undefined4 *)(param_1 + 0x9c) = 3;
  }
  *(undefined4 *)(param_1 + 0x98) = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acafb4"></a> `00acafb4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acafb8"></a> `00acafb8` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acafbc"></a> `00acafbc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acafc0"></a> `00acafc0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acafc4"></a> `00acafc4` | `a1 00 00 36` | tbz w1,#0x0,0x00acafd8 | `CONDITIONAL_JUMP`
<a id="insn-00acafc8"></a> `00acafc8` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00acafcc"></a> `00acafcc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acafd0"></a> `00acafd0` | `69 9e 00 b9` | str w9,[x19, #0x9c] | `FALL_THROUGH`
<a id="insn-00acafd4"></a> `00acafd4` | `05 00 00 14` | b 0x00acafe8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acafd8"></a> `00acafd8` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00acafdc"></a> `00acafdc` | `68 9e 00 b9` | str w8,[x19, #0x9c] | `FALL_THROUGH`
<a id="insn-00acafe0"></a> `00acafe0` | `46 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acafe4"></a> `00acafe4` | `c8 01 80 52` | mov w8,#0xe | `FALL_THROUGH`
<a id="insn-00acafe8"></a> `00acafe8` | `68 9a 00 b9` | str w8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00acafec"></a> `00acafec` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acaff0"></a> `00acaff0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acaff4"></a> `00acaff4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acafb4`](#insn-00acafb4) 範囲 `[['00acafb4', '00acafc7']]`
  - `CONDITIONAL_JUMP` [`00acafc4`](#insn-00acafc4) → [`00acafd8`](#insn-00acafd8)
  - `FALL_THROUGH` [`00acafc4`](#insn-00acafc4) → [`00acafc8`](#insn-00acafc8)
- ブロック [`00acafc8`](#insn-00acafc8) 範囲 `[['00acafc8', '00acafd7']]`
  - `UNCONDITIONAL_JUMP` [`00acafd4`](#insn-00acafd4) → [`00acafe8`](#insn-00acafe8)
- ブロック [`00acafd8`](#insn-00acafd8) 範囲 `[['00acafd8', '00acafe7']]`
  - `FALL_THROUGH` [`00acafe4`](#insn-00acafe4) → [`00acafe8`](#insn-00acafe8)
- ブロック [`00acafe8`](#insn-00acafe8) 範囲 `[['00acafe8', '00acaff7']]`

## 命令位置別の参照

- [`00acafb4`](#insn-00acafb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafb8`](#insn-00acafb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafc4`](#insn-00acafc4) → [`00acafd8`](#insn-00acafd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafd4`](#insn-00acafd4) → [`00acafe8`](#insn-00acafe8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafe0`](#insn-00acafe0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acafec`](#insn-00acafec) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaff0`](#insn-00acaff0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acafb4`](#insn-00acafb4)

~~~json
{
  "source": "00acafb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafb8`](#insn-00acafb8)

~~~json
{
  "source": "00acafb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafc4`](#insn-00acafc4)

~~~json
{
  "source": "00acafc4",
  "target": "00acafd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafd4`](#insn-00acafd4)

~~~json
{
  "source": "00acafd4",
  "target": "00acafe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafe0`](#insn-00acafe0)

~~~json
{
  "source": "00acafe0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acafec`](#insn-00acafec)

~~~json
{
  "source": "00acafec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaff0`](#insn-00acaff0)

~~~json
{
  "source": "00acaff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
