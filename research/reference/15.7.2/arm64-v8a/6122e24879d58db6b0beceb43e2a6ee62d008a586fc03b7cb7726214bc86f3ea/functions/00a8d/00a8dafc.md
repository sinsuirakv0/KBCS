# 00a8dafc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a8dafc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8dafc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0055.md#compare-618927de8d45063f2d0655b5340c8f57)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a8dafc",
  "name": "FUN_00a8dafc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "52cdd0fbe409164d4ee2d6b80a2b20e0cc17630fc8885aa46a4f4f5b696079c6",
  "source_text_sha256": "52cdd0fbe409164d4ee2d6b80a2b20e0cc17630fc8885aa46a4f4f5b696079c6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a8dafc",
        "00a8db2f"
      ]
    ],
    "bytes_sha256": "84bd98467820ae063eb1dbb85ad9048495ae400658840be68378e63069b12a6f",
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

- [00bdaf40](../00bda/00bdaf40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_00a8dafc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c0df58;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a8dafc"></a> `00a8dafc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a8db00"></a> `00a8db00` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a8db04"></a> `00a8db04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a8db08"></a> `00a8db08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a8db0c"></a> `00a8db0c` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00a8db10"></a> `00a8db10` | `0c 35 05 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00a8db14"></a> `00a8db14` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a8db18"></a> `00a8db18` | `08 0c 00 90` | adrp x8,0xc0d000 | `FALL_THROUGH`
<a id="insn-00a8db1c"></a> `00a8db1c` | `08 61 3d 91` | add x8,x8,#0xf58 | `FALL_THROUGH`
<a id="insn-00a8db20"></a> `00a8db20` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00a8db24"></a> `00a8db24` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a8db28"></a> `00a8db28` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a8db2c"></a> `00a8db2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a8dafc`](#insn-00a8dafc) 範囲 `[['00a8dafc', '00a8db2f']]`

## 命令位置別の参照

- [`00a8dafc`](#insn-00a8dafc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8db00`](#insn-00a8db00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8db10`](#insn-00a8db10) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00a8db20`](#insn-00a8db20) → `00c0df58`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a8db24`](#insn-00a8db24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8db28`](#insn-00a8db28) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a8dafc`](#insn-00a8dafc)

~~~json
{
  "source": "00a8dafc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8db00`](#insn-00a8db00)

~~~json
{
  "source": "00a8db00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8db10`](#insn-00a8db10)

~~~json
{
  "source": "00a8db10",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8db20`](#insn-00a8db20)

~~~json
{
  "source": "00a8db20",
  "target": "00c0df58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0df58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a8db24`](#insn-00a8db24)

~~~json
{
  "source": "00a8db24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8db28`](#insn-00a8db28)

~~~json
{
  "source": "00a8db28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
