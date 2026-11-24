# 00aeeccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a8f8a0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f8a0.md) · 移動量 `+0x5f42c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-1c8ea8c370753f3b4c97fd75657ff032)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aef0f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef0f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-ca8845b7815236ee3ee5dd2e507a1d4e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeeccc",
  "name": "FUN_00aeeccc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d07cb4795ab23533a7d53a056b19854188a10390a5b72fcc0a76f2a2f7ce7ac3",
  "source_text_sha256": "d07cb4795ab23533a7d53a056b19854188a10390a5b72fcc0a76f2a2f7ce7ac3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeeccc",
        "00aeed03"
      ]
    ],
    "bytes_sha256": "199e94b03f0c15c23e56a66019505e2fc6ce50825c56a37a6f8c6375633b6c02",
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

- [00c57a90](../00c57/00c57a90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 308 bytes

~~~c

void FUN_00aeeccc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  puVar1 = (undefined8 *)_Znwm(0x18);
  uVar3 = *(undefined8 *)(param_1 + 0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c8dbf8;
  puVar1[2] = uVar3;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeeccc"></a> `00aeeccc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeecd0"></a> `00aeecd0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeecd4"></a> `00aeecd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aeecd8"></a> `00aeecd8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeecdc"></a> `00aeecdc` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-00aeece0"></a> `00aeece0` | `6c a3 05 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeece4"></a> `00aeece4` | `60 82 c0 3c` | ldur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aeece8"></a> `00aeece8` | `e8 0c 00 f0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeecec"></a> `00aeecec` | `08 e1 2f 91` | add x8,x8,#0xbf8 | `FALL_THROUGH`
<a id="insn-00aeecf0"></a> `00aeecf0` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00aeecf4"></a> `00aeecf4` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aeecf8"></a> `00aeecf8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeecfc"></a> `00aeecfc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeed00"></a> `00aeed00` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeeccc`](#insn-00aeeccc) 範囲 `[['00aeeccc', '00aeed03']]`

## 命令位置別の参照

- [`00aeeccc`](#insn-00aeeccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeecd0`](#insn-00aeecd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeece0`](#insn-00aeece0) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00aeecf0`](#insn-00aeecf0) → `00c8dbf8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeecf8`](#insn-00aeecf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeecfc`](#insn-00aeecfc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeeccc`](#insn-00aeeccc)

~~~json
{
  "source": "00aeeccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeecd0`](#insn-00aeecd0)

~~~json
{
  "source": "00aeecd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeece0`](#insn-00aeece0)

~~~json
{
  "source": "00aeece0",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeecf0`](#insn-00aeecf0)

~~~json
{
  "source": "00aeecf0",
  "target": "00c8dbf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8dbf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeecf8`](#insn-00aeecf8)

~~~json
{
  "source": "00aeecf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeecfc`](#insn-00aeecfc)

~~~json
{
  "source": "00aeecfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
