# 00ae9ddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae9d14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9d14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-7da2e9d2a23cd7d4045d999017980fbc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae9e20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0063.md#compare-95aaebf95a60b80b5af7df88fb8c87f1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae9ddc",
  "name": "_ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d832228642b0847c94e85dae7478c475f73f8669f7dd8e5289573f37ab3dcf79",
  "source_text_sha256": "d832228642b0847c94e85dae7478c475f73f8669f7dd8e5289573f37ab3dcf79",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae9ddc",
        "00ae9e1b"
      ]
    ],
    "bytes_sha256": "8ceeee86589cdd82c203268b19607c533312cb4e84666839e708597698e45692",
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

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Double"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 455 bytes

~~~c

long _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a0740 == 0) {
    DAT_010a0740 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0740;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae9ddc"></a> `00ae9ddc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae9de0"></a> `00ae9de0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae9de4"></a> `00ae9de4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae9de8"></a> `00ae9de8` | `b3 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae9dec"></a> `00ae9dec` | `68 a2 43 f9` | ldr x8,[x19, #0x740] | `FALL_THROUGH`
<a id="insn-00ae9df0"></a> `00ae9df0` | `e8 00 00 b5` | cbnz x8,0x00ae9e0c | `CONDITIONAL_JUMP`
<a id="insn-00ae9df4"></a> `00ae9df4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00ae9df8"></a> `00ae9df8` | `e3 bd ff d0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00ae9dfc"></a> `00ae9dfc` | `63 ac 00 91` | add x3,x3,#0x2b | `FALL_THROUGH`
<a id="insn-00ae9e00"></a> `00ae9e00` | `90 d0 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00ae9e04"></a> `00ae9e04` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ae9e08"></a> `00ae9e08` | `60 a2 03 f9` | str x0,[x19, #0x740] | `FALL_THROUGH`
<a id="insn-00ae9e0c"></a> `00ae9e0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae9e10"></a> `00ae9e10` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00ae9e14"></a> `00ae9e14` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae9e18"></a> `00ae9e18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae9ddc`](#insn-00ae9ddc) 範囲 `[['00ae9ddc', '00ae9df3']]`
  - `CONDITIONAL_JUMP` [`00ae9df0`](#insn-00ae9df0) → [`00ae9e0c`](#insn-00ae9e0c)
  - `FALL_THROUGH` [`00ae9df0`](#insn-00ae9df0) → [`00ae9df4`](#insn-00ae9df4)
- ブロック [`00ae9df4`](#insn-00ae9df4) 範囲 `[['00ae9df4', '00ae9e0b']]`
  - `FALL_THROUGH` [`00ae9e08`](#insn-00ae9e08) → [`00ae9e0c`](#insn-00ae9e0c)
- ブロック [`00ae9e0c`](#insn-00ae9e0c) 範囲 `[['00ae9e0c', '00ae9e1b']]`

## 命令位置別の参照

- [`00ae9ddc`](#insn-00ae9ddc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae9de0`](#insn-00ae9de0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae9dec`](#insn-00ae9dec) → `010a0740`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae9df0`](#insn-00ae9df0) → [`00ae9e0c`](#insn-00ae9e0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae9dfc`](#insn-00ae9dfc) → `002a702b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae9e00`](#insn-00ae9e00) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00ae9e08`](#insn-00ae9e08) → `010a0740`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae9e0c`](#insn-00ae9e0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae9ddc`](#insn-00ae9ddc)

~~~json
{
  "source": "00ae9ddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae9de0`](#insn-00ae9de0)

~~~json
{
  "source": "00ae9de0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae9dec`](#insn-00ae9dec)

~~~json
{
  "source": "00ae9dec",
  "target": "010a0740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0740",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae9df0`](#insn-00ae9df0)

~~~json
{
  "source": "00ae9df0",
  "target": "00ae9e0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae9dfc`](#insn-00ae9dfc)

~~~json
{
  "source": "00ae9dfc",
  "target": "002a702b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a702b",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f446f75626c6500",
  "capture_start": "002a702b",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae9e00`](#insn-00ae9e00)

~~~json
{
  "source": "00ae9e00",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae9e08`](#insn-00ae9e08)

~~~json
{
  "source": "00ae9e08",
  "target": "010a0740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0740",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae9e0c`](#insn-00ae9e0c)

~~~json
{
  "source": "00ae9e0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
