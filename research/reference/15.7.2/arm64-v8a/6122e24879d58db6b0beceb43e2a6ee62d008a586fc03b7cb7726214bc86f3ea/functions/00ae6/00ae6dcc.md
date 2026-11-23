# 00ae6dcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae6e94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0059.md#compare-35252c0cab82494265d7bacd0d1b0c00)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae6dcc",
  "name": "_ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "178ca6a66401fad57ff14d9d14fa1c3508e3231944214c27e445c441a521a41d",
  "source_text_sha256": "178ca6a66401fad57ff14d9d14fa1c3508e3231944214c27e445c441a521a41d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae6dcc",
        "00ae6e0b"
      ]
    ],
    "bytes_sha256": "8425ad37af3735ba47a998ea7da7766615a38e7b937a5d02374461a9581f6ae7",
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

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"android/content/res/Resources"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 428 bytes

~~~c

long _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a03e8 == 0) {
    DAT_010a03e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a03e8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae6dcc"></a> `00ae6dcc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae6dd0"></a> `00ae6dd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae6dd4"></a> `00ae6dd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae6dd8"></a> `00ae6dd8` | `d3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae6ddc"></a> `00ae6ddc` | `68 f6 41 f9` | ldr x8,[x19, #0x3e8] | `FALL_THROUGH`
<a id="insn-00ae6de0"></a> `00ae6de0` | `e8 00 00 b5` | cbnz x8,0x00ae6dfc | `CONDITIONAL_JUMP`
<a id="insn-00ae6de4"></a> `00ae6de4` | `e3 bd ff d0` | adrp x3,0x2a4000 | `FALL_THROUGH`
<a id="insn-00ae6de8"></a> `00ae6de8` | `63 60 39 91` | add x3,x3,#0xe58 | `FALL_THROUGH`
<a id="insn-00ae6dec"></a> `00ae6dec` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ae6df0"></a> `00ae6df0` | `68 dc 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00ae6df4"></a> `00ae6df4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ae6df8"></a> `00ae6df8` | `60 f6 01 f9` | str x0,[x19, #0x3e8] | `FALL_THROUGH`
<a id="insn-00ae6dfc"></a> `00ae6dfc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae6e00"></a> `00ae6e00` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00ae6e04"></a> `00ae6e04` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae6e08"></a> `00ae6e08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae6dcc`](#insn-00ae6dcc) 範囲 `[['00ae6dcc', '00ae6de3']]`
  - `CONDITIONAL_JUMP` [`00ae6de0`](#insn-00ae6de0) → [`00ae6dfc`](#insn-00ae6dfc)
  - `FALL_THROUGH` [`00ae6de0`](#insn-00ae6de0) → [`00ae6de4`](#insn-00ae6de4)
- ブロック [`00ae6de4`](#insn-00ae6de4) 範囲 `[['00ae6de4', '00ae6dfb']]`
  - `FALL_THROUGH` [`00ae6df8`](#insn-00ae6df8) → [`00ae6dfc`](#insn-00ae6dfc)
- ブロック [`00ae6dfc`](#insn-00ae6dfc) 範囲 `[['00ae6dfc', '00ae6e0b']]`

## 命令位置別の参照

- [`00ae6dcc`](#insn-00ae6dcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6dd0`](#insn-00ae6dd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6ddc`](#insn-00ae6ddc) → `010a03e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae6de0`](#insn-00ae6de0) → [`00ae6dfc`](#insn-00ae6dfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae6de8`](#insn-00ae6de8) → `002a4e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae6df0`](#insn-00ae6df0) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00ae6df8`](#insn-00ae6df8) → `010a03e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae6dfc`](#insn-00ae6dfc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae6dcc`](#insn-00ae6dcc)

~~~json
{
  "source": "00ae6dcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6dd0`](#insn-00ae6dd0)

~~~json
{
  "source": "00ae6dd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6ddc`](#insn-00ae6ddc)

~~~json
{
  "source": "00ae6ddc",
  "target": "010a03e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae6de0`](#insn-00ae6de0)

~~~json
{
  "source": "00ae6de0",
  "target": "00ae6dfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae6de8`](#insn-00ae6de8)

~~~json
{
  "source": "00ae6de8",
  "target": "002a4e58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4e58",
  "offset": 0,
  "size": 30,
  "datatype": "string",
  "bytes": "616e64726f69642f636f6e74656e742f7265732f5265736f757263657300",
  "capture_start": "002a4e58",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae6df0`](#insn-00ae6df0)

~~~json
{
  "source": "00ae6df0",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae6df8`](#insn-00ae6df8)

~~~json
{
  "source": "00ae6df8",
  "target": "010a03e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a03e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae6dfc`](#insn-00ae6dfc)

~~~json
{
  "source": "00ae6dfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
