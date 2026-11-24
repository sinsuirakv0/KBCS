# 00a1fbfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a1fbb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fbb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0054.md#compare-f89655f6520185a15c91cd2479b97268)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a7da8c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7da8c.md) · 移動量 `+0x5de90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0051.md#compare-9ca1edfad218eb29396322e5cb16dd08)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a1fbfc",
  "name": "FUN_00a1fbfc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "98bdd9b385e3e40723d856df45b1fdbfa866e71c21f54929f550e65052adae55",
  "source_text_sha256": "98bdd9b385e3e40723d856df45b1fdbfa866e71c21f54929f550e65052adae55",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a1fbfc",
        "00a1fc2f"
      ]
    ],
    "bytes_sha256": "094cb9e1b88407ecfbc0d2578fc4cd01c85a66c4b9ec17fbe61b44cd0945ea88",
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

- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_00a1fbfc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c0c300;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a1fbfc"></a> `00a1fbfc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a1fc00"></a> `00a1fc00` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a1fc04"></a> `00a1fc04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a1fc08"></a> `00a1fc08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a1fc0c"></a> `00a1fc0c` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00a1fc10"></a> `00a1fc10` | `0c ed 06 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00a1fc14"></a> `00a1fc14` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a1fc18"></a> `00a1fc18` | `68 0f 00 b0` | adrp x8,0xc0c000 | `FALL_THROUGH`
<a id="insn-00a1fc1c"></a> `00a1fc1c` | `08 01 0c 91` | add x8,x8,#0x300 | `FALL_THROUGH`
<a id="insn-00a1fc20"></a> `00a1fc20` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00a1fc24"></a> `00a1fc24` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a1fc28"></a> `00a1fc28` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a1fc2c"></a> `00a1fc2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a1fbfc`](#insn-00a1fbfc) 範囲 `[['00a1fbfc', '00a1fc2f']]`

## 命令位置別の参照

- [`00a1fbfc`](#insn-00a1fbfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1fc00`](#insn-00a1fc00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1fc10`](#insn-00a1fc10) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00a1fc20`](#insn-00a1fc20) → `00c0c300`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a1fc24`](#insn-00a1fc24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1fc28`](#insn-00a1fc28) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a1fbfc`](#insn-00a1fbfc)

~~~json
{
  "source": "00a1fbfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1fc00`](#insn-00a1fc00)

~~~json
{
  "source": "00a1fc00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1fc10`](#insn-00a1fc10)

~~~json
{
  "source": "00a1fc10",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1fc20`](#insn-00a1fc20)

~~~json
{
  "source": "00a1fc20",
  "target": "00c0c300",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0c300",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a1fc24`](#insn-00a1fc24)

~~~json
{
  "source": "00a1fc24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1fc28`](#insn-00a1fc28)

~~~json
{
  "source": "00a1fc28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
