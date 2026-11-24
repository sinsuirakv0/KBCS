# 00bcbfa8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5caa8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caa8.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-b3984014534fc7391625cfcedba4bc71)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc3d0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc3d0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-9a2bd508e3b7be7a9537149be081f117)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbfa8",
  "name": "_ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "211ae8b90d8a825a56727b64351a80e2f7fd3737342d3be468d1db09c72d47b0",
  "source_text_sha256": "211ae8b90d8a825a56727b64351a80e2f7fd3737342d3be468d1db09c72d47b0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbfa8",
        "00bcbfeb"
      ]
    ],
    "bytes_sha256": "d28183926bb11da8f7d9ac296955d899e7ba6dfddaa51eba310085f4c793ea6b",
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

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuth"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 421 bytes

~~~c

long _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126328 == 0) {
    DAT_01126328 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseAuth",0);
  }
  return DAT_01126328;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbfa8"></a> `00bcbfa8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcbfac"></a> `00bcbfac` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbfb0"></a> `00bcbfb0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcbfb4"></a> `00bcbfb4` | `d3 2a 00 f0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcbfb8"></a> `00bcbfb8` | `68 96 41 f9` | ldr x8,[x19, #0x328] | `FALL_THROUGH`
<a id="insn-00bcbfbc"></a> `00bcbfbc` | `08 01 00 b5` | cbnz x8,0x00bcbfdc | `CONDITIONAL_JUMP`
<a id="insn-00bcbfc0"></a> `00bcbfc0` | `03 b7 ff b0` | adrp x3,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcbfc4"></a> `00bcbfc4` | `63 f0 07 91` | add x3,x3,#0x1fc | `FALL_THROUGH`
<a id="insn-00bcbfc8"></a> `00bcbfc8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bcbfcc"></a> `00bcbfcc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bcbfd0"></a> `00bcbfd0` | `d0 3a 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbfd4"></a> `00bcbfd4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcbfd8"></a> `00bcbfd8` | `60 96 01 f9` | str x0,[x19, #0x328] | `FALL_THROUGH`
<a id="insn-00bcbfdc"></a> `00bcbfdc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbfe0"></a> `00bcbfe0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbfe4"></a> `00bcbfe4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcbfe8"></a> `00bcbfe8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbfa8`](#insn-00bcbfa8) 範囲 `[['00bcbfa8', '00bcbfbf']]`
  - `CONDITIONAL_JUMP` [`00bcbfbc`](#insn-00bcbfbc) → [`00bcbfdc`](#insn-00bcbfdc)
  - `FALL_THROUGH` [`00bcbfbc`](#insn-00bcbfbc) → [`00bcbfc0`](#insn-00bcbfc0)
- ブロック [`00bcbfc0`](#insn-00bcbfc0) 範囲 `[['00bcbfc0', '00bcbfdb']]`
  - `FALL_THROUGH` [`00bcbfd8`](#insn-00bcbfd8) → [`00bcbfdc`](#insn-00bcbfdc)
- ブロック [`00bcbfdc`](#insn-00bcbfdc) 範囲 `[['00bcbfdc', '00bcbfeb']]`

## 命令位置別の参照

- [`00bcbfa8`](#insn-00bcbfa8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfac`](#insn-00bcbfac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfb8`](#insn-00bcbfb8) → `01126328`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbfbc`](#insn-00bcbfbc) → [`00bcbfdc`](#insn-00bcbfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfc4`](#insn-00bcbfc4) → `002ac1fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbfd0`](#insn-00bcbfd0) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfd8`](#insn-00bcbfd8) → `01126328`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbfdc`](#insn-00bcbfdc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbfa8`](#insn-00bcbfa8)

~~~json
{
  "source": "00bcbfa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfac`](#insn-00bcbfac)

~~~json
{
  "source": "00bcbfac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfb8`](#insn-00bcbfb8)

~~~json
{
  "source": "00bcbfb8",
  "target": "01126328",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126328",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbfbc`](#insn-00bcbfbc)

~~~json
{
  "source": "00bcbfbc",
  "target": "00bcbfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfc4`](#insn-00bcbfc4)

~~~json
{
  "source": "00bcbfc4",
  "target": "002ac1fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac1f8",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002ac1f8",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcbfd0`](#insn-00bcbfd0)

~~~json
{
  "source": "00bcbfd0",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbfd8`](#insn-00bcbfd8)

~~~json
{
  "source": "00bcbfd8",
  "target": "01126328",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126328",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbfdc`](#insn-00bcbfdc)

~~~json
{
  "source": "00bcbfdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
