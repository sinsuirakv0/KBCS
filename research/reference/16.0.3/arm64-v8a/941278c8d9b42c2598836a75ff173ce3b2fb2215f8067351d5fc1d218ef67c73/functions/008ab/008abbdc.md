# 008abbdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `008aac30`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008aa/008aac30.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0009.md#compare-3863d75ee66ec254ea6350406a0c9930)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008abbdc",
  "name": "FUN_008abbdc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "416173823db69eb6e565bfda268bb04afd2d49599764125c7ad53f4356a3f034",
  "source_text_sha256": "416173823db69eb6e565bfda268bb04afd2d49599764125c7ad53f4356a3f034",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008abbdc",
        "008abc0f"
      ]
    ],
    "bytes_sha256": "1172c3ef4413663514b95af9f37b911d168d09a282baf36398e70cf636c8c878",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
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

## 疑似コード / UTF-8 321 bytes

~~~c

void FUN_008abbdc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 008abc00 to 009abc03 has its CatchHandler @ 008ac07c */
  *puVar1 = &PTR_FUN_00c844d0;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008abbdc"></a> `008abbdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-008abbe0"></a> `008abbe0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008abbe4"></a> `008abbe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008abbe8"></a> `008abbe8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008abbec"></a> `008abbec` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-008abbf0"></a> `008abbf0` | `d0 b4 0e 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-008abbf4"></a> `008abbf4` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-008abbf8"></a> `008abbf8` | `c8 1e 00 b0` | adrp x8,0xc84000 | `FALL_THROUGH`
<a id="insn-008abbfc"></a> `008abbfc` | `08 41 13 91` | add x8,x8,#0x4d0 | `FALL_THROUGH`
<a id="insn-008abc00"></a> `008abc00` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-008abc04"></a> `008abc04` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008abc08"></a> `008abc08` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-008abc0c"></a> `008abc0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008abbdc`](#insn-008abbdc) 範囲 `[['008abbdc', '008abbff']]`
  - `FALL_THROUGH` [`008abbfc`](#insn-008abbfc) → [`008abc00`](#insn-008abc00)
- ブロック [`008abc00`](#insn-008abc00) 範囲 `[['008abc00', '008abc0f']]`

## 命令位置別の参照

- [`008abbdc`](#insn-008abbdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008abbe0`](#insn-008abbe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008abbf0`](#insn-008abbf0) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`008abc00`](#insn-008abc00) → `00c844d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`008abc04`](#insn-008abc04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008abc08`](#insn-008abc08) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008abbdc`](#insn-008abbdc)

~~~json
{
  "source": "008abbdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008abbe0`](#insn-008abbe0)

~~~json
{
  "source": "008abbe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008abbf0`](#insn-008abbf0)

~~~json
{
  "source": "008abbf0",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008abc00`](#insn-008abc00)

~~~json
{
  "source": "008abc00",
  "target": "00c844d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c844d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008abc04`](#insn-008abc04)

~~~json
{
  "source": "008abc04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008abc08`](#insn-008abc08)

~~~json
{
  "source": "008abc08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
