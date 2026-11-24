# 006fddcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `006fda1c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda1c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0035.md#compare-a6fabe4cadf91ae834ad7852a8d444e6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fddcc",
  "name": "FUN_006fddcc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45a345925de7be0fdd082fd936be3bf8722eef7161d2fa52e6b316175e2ca269",
  "source_text_sha256": "45a345925de7be0fdd082fd936be3bf8722eef7161d2fa52e6b316175e2ca269",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006fddcc",
        "006fde0b"
      ]
    ],
    "bytes_sha256": "f759083c178c89abb402babf2afbbbd984acb65b5ed7e5d55578202887ec6706",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
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

## 疑似コード / UTF-8 392 bytes

~~~c

void FUN_006fddcc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  
  puVar1 = (undefined8 *)_Znwm(0x20);
  uVar4 = *(undefined8 *)(param_1 + 0x10);
  uVar3 = *(undefined8 *)(param_1 + 8);
  uVar2 = *(undefined8 *)(param_1 + 0x18);
  *puVar1 = &PTR_FUN_00c77db8;
  puVar1[2] = uVar4;
  puVar1[1] = uVar3;
  puVar1[3] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006fddcc"></a> `006fddcc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-006fddd0"></a> `006fddd0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fddd4"></a> `006fddd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006fddd8"></a> `006fddd8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006fdddc"></a> `006fdddc` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-006fdde0"></a> `006fdde0` | `54 6c 15 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-006fdde4"></a> `006fdde4` | `60 82 c0 3c` | ldur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006fdde8"></a> `006fdde8` | `69 0e 40 f9` | ldr x9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-006fddec"></a> `006fddec` | `c8 2b 00 d0` | adrp x8,0xc77000 | `FALL_THROUGH`
<a id="insn-006fddf0"></a> `006fddf0` | `08 e1 36 91` | add x8,x8,#0xdb8 | `FALL_THROUGH`
<a id="insn-006fddf4"></a> `006fddf4` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-006fddf8"></a> `006fddf8` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-006fddfc"></a> `006fddfc` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-006fde00"></a> `006fde00` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fde04"></a> `006fde04` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-006fde08"></a> `006fde08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006fddcc`](#insn-006fddcc) 範囲 `[['006fddcc', '006fde0b']]`

## 命令位置別の参照

- [`006fddcc`](#insn-006fddcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fddd0`](#insn-006fddd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdde0`](#insn-006fdde0) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`006fddf4`](#insn-006fddf4) → `00c77db8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`006fde00`](#insn-006fde00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fde04`](#insn-006fde04) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006fddcc`](#insn-006fddcc)

~~~json
{
  "source": "006fddcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fddd0`](#insn-006fddd0)

~~~json
{
  "source": "006fddd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdde0`](#insn-006fdde0)

~~~json
{
  "source": "006fdde0",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fddf4`](#insn-006fddf4)

~~~json
{
  "source": "006fddf4",
  "target": "00c77db8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c77db8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006fde00`](#insn-006fde00)

~~~json
{
  "source": "006fde00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fde04`](#insn-006fde04)

~~~json
{
  "source": "006fde04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
