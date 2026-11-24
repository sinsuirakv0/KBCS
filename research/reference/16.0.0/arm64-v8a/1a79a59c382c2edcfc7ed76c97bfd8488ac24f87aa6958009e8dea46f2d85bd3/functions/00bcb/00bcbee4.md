# 00bcbee4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c9e4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9e4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-ea31c0e0e9900b48769f24b968503d5f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc30c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc30c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-19f352c0c3f4cd80b2d6559d6109df89)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbee4",
  "name": "_ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2acdc2d2c45e8ab642857b73edf37a23d8b673d51a2bbde1acaf181ea55803d8",
  "source_text_sha256": "2acdc2d2c45e8ab642857b73edf37a23d8b673d51a2bbde1acaf181ea55803d8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbee4",
        "00bcbf23"
      ]
    ],
    "bytes_sha256": "36d6042f7766023772075cff8166768ef536a2cc0a8ad7dcb5f96ea391e491d8",
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

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuth"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 450 bytes

~~~c

long _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01126328 == 0) {
    DAT_01126328 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126328;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbee4"></a> `00bcbee4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcbee8"></a> `00bcbee8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbeec"></a> `00bcbeec` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcbef0"></a> `00bcbef0` | `d3 2a 00 f0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcbef4"></a> `00bcbef4` | `68 96 41 f9` | ldr x8,[x19, #0x328] | `FALL_THROUGH`
<a id="insn-00bcbef8"></a> `00bcbef8` | `e8 00 00 b5` | cbnz x8,0x00bcbf14 | `CONDITIONAL_JUMP`
<a id="insn-00bcbefc"></a> `00bcbefc` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bcbf00"></a> `00bcbf00` | `03 b7 ff b0` | adrp x3,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcbf04"></a> `00bcbf04` | `63 f0 07 91` | add x3,x3,#0x1fc | `FALL_THROUGH`
<a id="insn-00bcbf08"></a> `00bcbf08` | `02 3b 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbf0c"></a> `00bcbf0c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcbf10"></a> `00bcbf10` | `60 96 01 f9` | str x0,[x19, #0x328] | `FALL_THROUGH`
<a id="insn-00bcbf14"></a> `00bcbf14` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf18"></a> `00bcbf18` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbf1c"></a> `00bcbf1c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcbf20"></a> `00bcbf20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbee4`](#insn-00bcbee4) 範囲 `[['00bcbee4', '00bcbefb']]`
  - `CONDITIONAL_JUMP` [`00bcbef8`](#insn-00bcbef8) → [`00bcbf14`](#insn-00bcbf14)
  - `FALL_THROUGH` [`00bcbef8`](#insn-00bcbef8) → [`00bcbefc`](#insn-00bcbefc)
- ブロック [`00bcbefc`](#insn-00bcbefc) 範囲 `[['00bcbefc', '00bcbf13']]`
  - `FALL_THROUGH` [`00bcbf10`](#insn-00bcbf10) → [`00bcbf14`](#insn-00bcbf14)
- ブロック [`00bcbf14`](#insn-00bcbf14) 範囲 `[['00bcbf14', '00bcbf23']]`

## 命令位置別の参照

- [`00bcbee4`](#insn-00bcbee4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbee8`](#insn-00bcbee8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbef4`](#insn-00bcbef4) → `01126328`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbef8`](#insn-00bcbef8) → [`00bcbf14`](#insn-00bcbf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf04`](#insn-00bcbf04) → `002ac1fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbf08`](#insn-00bcbf08) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf10`](#insn-00bcbf10) → `01126328`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbf14`](#insn-00bcbf14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbee4`](#insn-00bcbee4)

~~~json
{
  "source": "00bcbee4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbee8`](#insn-00bcbee8)

~~~json
{
  "source": "00bcbee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbef4`](#insn-00bcbef4)

~~~json
{
  "source": "00bcbef4",
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
- 参照命令 [`00bcbef8`](#insn-00bcbef8)

~~~json
{
  "source": "00bcbef8",
  "target": "00bcbf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf04`](#insn-00bcbf04)

~~~json
{
  "source": "00bcbf04",
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
- 参照命令 [`00bcbf08`](#insn-00bcbf08)

~~~json
{
  "source": "00bcbf08",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf10`](#insn-00bcbf10)

~~~json
{
  "source": "00bcbf10",
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
- 参照命令 [`00bcbf14`](#insn-00bcbf14)

~~~json
{
  "source": "00bcbf14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
