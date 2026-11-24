# 008dabac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `008d9c00`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9c00.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0053.md#compare-c885888f4b4bcf4b553eb2ef67e14c35)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008dabac",
  "name": "FUN_008dabac",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "11ba77ac0a9c7985a64287fb8202819f2c1e2fe2e6abb13035a82cac8571bbac",
  "source_text_sha256": "11ba77ac0a9c7985a64287fb8202819f2c1e2fe2e6abb13035a82cac8571bbac",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008dabac",
        "008dabe3"
      ]
    ],
    "bytes_sha256": "87f20fd12c5625ae9c1020704b77179dd94460f6f5092e588786ec536e91fb68",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 308 bytes

~~~c

void FUN_008dabac(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  puVar1 = (undefined8 *)_Znwm(0x18);
  uVar3 = *(undefined8 *)(param_1 + 0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c85dc8;
  puVar1[2] = uVar3;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008dabac"></a> `008dabac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-008dabb0"></a> `008dabb0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008dabb4"></a> `008dabb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008dabb8"></a> `008dabb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008dabbc"></a> `008dabbc` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-008dabc0"></a> `008dabc0` | `dc f8 0d 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-008dabc4"></a> `008dabc4` | `60 82 c0 3c` | ldur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-008dabc8"></a> `008dabc8` | `48 1d 00 f0` | adrp x8,0xc85000 | `FALL_THROUGH`
<a id="insn-008dabcc"></a> `008dabcc` | `08 21 37 91` | add x8,x8,#0xdc8 | `FALL_THROUGH`
<a id="insn-008dabd0"></a> `008dabd0` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-008dabd4"></a> `008dabd4` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-008dabd8"></a> `008dabd8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008dabdc"></a> `008dabdc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-008dabe0"></a> `008dabe0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008dabac`](#insn-008dabac) 範囲 `[['008dabac', '008dabe3']]`

## 命令位置別の参照

- [`008dabac`](#insn-008dabac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dabb0`](#insn-008dabb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dabc0`](#insn-008dabc0) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`008dabd0`](#insn-008dabd0) → `00c85dc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`008dabd8`](#insn-008dabd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dabdc`](#insn-008dabdc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008dabac`](#insn-008dabac)

~~~json
{
  "source": "008dabac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dabb0`](#insn-008dabb0)

~~~json
{
  "source": "008dabb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dabc0`](#insn-008dabc0)

~~~json
{
  "source": "008dabc0",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dabd0`](#insn-008dabd0)

~~~json
{
  "source": "008dabd0",
  "target": "00c85dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c85dc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008dabd8`](#insn-008dabd8)

~~~json
{
  "source": "008dabd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dabdc`](#insn-008dabdc)

~~~json
{
  "source": "008dabdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
