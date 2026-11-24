# 00b4dbac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b4db10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0074.md#compare-a9dcc1fe4505cb2be099ffc03a0eb0b5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b4eba0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4eba0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0076.md#compare-21b8ec428375ade1638e198ef92c29ff)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4dbac",
  "name": "_ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "463fcd7d434be28a9f46068f2dda534c979ddb3e4330e8b79cef38d3b7a7eea6",
  "source_text_sha256": "463fcd7d434be28a9f46068f2dda534c979ddb3e4330e8b79cef38d3b7a7eea6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4dbac",
        "00b4dbef"
      ]
    ],
    "bytes_sha256": "f922d2c62f5c9c24a09eb836bc11fea70a95aa0ebda628693ab1313753ec98fa",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Throwable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 424 bytes

~~~c

long _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01125df0 == 0) {
    DAT_01125df0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Throwable",0);
  }
  return DAT_01125df0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4dbac"></a> `00b4dbac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4dbb0"></a> `00b4dbb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4dbb4"></a> `00b4dbb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4dbb8"></a> `00b4dbb8` | `d3 2e 00 90` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4dbbc"></a> `00b4dbbc` | `68 fa 46 f9` | ldr x8,[x19, #0xdf0] | `FALL_THROUGH`
<a id="insn-00b4dbc0"></a> `00b4dbc0` | `08 01 00 b5` | cbnz x8,0x00b4dbe0 | `CONDITIONAL_JUMP`
<a id="insn-00b4dbc4"></a> `00b4dbc4` | `63 bb ff 90` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00b4dbc8"></a> `00b4dbc8` | `63 64 25 91` | add x3,x3,#0x959 | `FALL_THROUGH`
<a id="insn-00b4dbcc"></a> `00b4dbcc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4dbd0"></a> `00b4dbd0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4dbd4"></a> `00b4dbd4` | `03 35 04 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dbd8"></a> `00b4dbd8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4dbdc"></a> `00b4dbdc` | `60 fa 06 f9` | str x0,[x19, #0xdf0] | `FALL_THROUGH`
<a id="insn-00b4dbe0"></a> `00b4dbe0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4dbe4"></a> `00b4dbe4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4dbe8"></a> `00b4dbe8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4dbec"></a> `00b4dbec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4dbac`](#insn-00b4dbac) 範囲 `[['00b4dbac', '00b4dbc3']]`
  - `CONDITIONAL_JUMP` [`00b4dbc0`](#insn-00b4dbc0) → [`00b4dbe0`](#insn-00b4dbe0)
  - `FALL_THROUGH` [`00b4dbc0`](#insn-00b4dbc0) → [`00b4dbc4`](#insn-00b4dbc4)
- ブロック [`00b4dbc4`](#insn-00b4dbc4) 範囲 `[['00b4dbc4', '00b4dbdf']]`
  - `FALL_THROUGH` [`00b4dbdc`](#insn-00b4dbdc) → [`00b4dbe0`](#insn-00b4dbe0)
- ブロック [`00b4dbe0`](#insn-00b4dbe0) 範囲 `[['00b4dbe0', '00b4dbef']]`

## 命令位置別の参照

- [`00b4dbac`](#insn-00b4dbac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbb0`](#insn-00b4dbb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbbc`](#insn-00b4dbbc) → `01125df0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4dbc0`](#insn-00b4dbc0) → [`00b4dbe0`](#insn-00b4dbe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbc8`](#insn-00b4dbc8) → `002b9959`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4dbd4`](#insn-00b4dbd4) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbdc`](#insn-00b4dbdc) → `01125df0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4dbe0`](#insn-00b4dbe0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4dbac`](#insn-00b4dbac)

~~~json
{
  "source": "00b4dbac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbb0`](#insn-00b4dbb0)

~~~json
{
  "source": "00b4dbb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbbc`](#insn-00b4dbbc)

~~~json
{
  "source": "00b4dbbc",
  "target": "01125df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125df0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4dbc0`](#insn-00b4dbc0)

~~~json
{
  "source": "00b4dbc0",
  "target": "00b4dbe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbc8`](#insn-00b4dbc8)

~~~json
{
  "source": "00b4dbc8",
  "target": "002b9959",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9959",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f5468726f7761626c6500",
  "capture_start": "002b9959",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4dbd4`](#insn-00b4dbd4)

~~~json
{
  "source": "00b4dbd4",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dbdc`](#insn-00b4dbdc)

~~~json
{
  "source": "00b4dbdc",
  "target": "01125df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125df0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4dbe0`](#insn-00b4dbe0)

~~~json
{
  "source": "00b4dbe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
