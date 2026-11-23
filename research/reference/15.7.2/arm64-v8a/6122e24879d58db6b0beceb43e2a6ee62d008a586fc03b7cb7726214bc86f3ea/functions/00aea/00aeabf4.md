# 00aeabf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeacbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacbc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-e7516c9819af0ac89c19abd26666ec99)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeabf4",
  "name": "_ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea9ea07aa5f19d0f0811f64c8ae2062f7edc94e56548e48fdc0febf8f74ca98f",
  "source_text_sha256": "ea9ea07aa5f19d0f0811f64c8ae2062f7edc94e56548e48fdc0febf8f74ca98f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeabf4",
        "00aeac33"
      ]
    ],
    "bytes_sha256": "2cc0aec54a3944e0aba29c913bf8a64b9cfbb39425ade5fa20016de9a22cb1a8",
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
"java/util/HashMap"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 524 bytes

~~~c

long _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a0750 == 0) {
                    /* try { // try from 00aeac14 to 00beadc7 has its CatchHandler @ 00aeaa38 */
    DAT_010a0750 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0750;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeabf4"></a> `00aeabf4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeabf8"></a> `00aeabf8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeabfc"></a> `00aeabfc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeac00"></a> `00aeac00` | `b3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeac04"></a> `00aeac04` | `68 aa 43 f9` | ldr x8,[x19, #0x750] | `FALL_THROUGH`
<a id="insn-00aeac08"></a> `00aeac08` | `e8 00 00 b5` | cbnz x8,0x00aeac24 | `CONDITIONAL_JUMP`
<a id="insn-00aeac0c"></a> `00aeac0c` | `63 bd ff 90` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00aeac10"></a> `00aeac10` | `63 54 2f 91` | add x3,x3,#0xbd5 | `FALL_THROUGH`
<a id="insn-00aeac14"></a> `00aeac14` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeac18"></a> `00aeac18` | `de cc 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeac1c"></a> `00aeac1c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeac20"></a> `00aeac20` | `60 aa 03 f9` | str x0,[x19, #0x750] | `FALL_THROUGH`
<a id="insn-00aeac24"></a> `00aeac24` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeac28"></a> `00aeac28` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeac2c"></a> `00aeac2c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeac30"></a> `00aeac30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeabf4`](#insn-00aeabf4) 範囲 `[['00aeabf4', '00aeac0b']]`
  - `CONDITIONAL_JUMP` [`00aeac08`](#insn-00aeac08) → [`00aeac24`](#insn-00aeac24)
  - `FALL_THROUGH` [`00aeac08`](#insn-00aeac08) → [`00aeac0c`](#insn-00aeac0c)
- ブロック [`00aeac0c`](#insn-00aeac0c) 範囲 `[['00aeac0c', '00aeac13']]`
  - `FALL_THROUGH` [`00aeac10`](#insn-00aeac10) → [`00aeac14`](#insn-00aeac14)
- ブロック [`00aeac14`](#insn-00aeac14) 範囲 `[['00aeac14', '00aeac23']]`
  - `FALL_THROUGH` [`00aeac20`](#insn-00aeac20) → [`00aeac24`](#insn-00aeac24)
- ブロック [`00aeac24`](#insn-00aeac24) 範囲 `[['00aeac24', '00aeac33']]`

## 命令位置別の参照

- [`00aeabf4`](#insn-00aeabf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeabf8`](#insn-00aeabf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeac04`](#insn-00aeac04) → `010a0750`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeac08`](#insn-00aeac08) → [`00aeac24`](#insn-00aeac24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeac10`](#insn-00aeac10) → `00296bd5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeac18`](#insn-00aeac18) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeac20`](#insn-00aeac20) → `010a0750`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeac24`](#insn-00aeac24) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeabf4`](#insn-00aeabf4)

~~~json
{
  "source": "00aeabf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeabf8`](#insn-00aeabf8)

~~~json
{
  "source": "00aeabf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeac04`](#insn-00aeac04)

~~~json
{
  "source": "00aeac04",
  "target": "010a0750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0750",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeac08`](#insn-00aeac08)

~~~json
{
  "source": "00aeac08",
  "target": "00aeac24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeac10`](#insn-00aeac10)

~~~json
{
  "source": "00aeac10",
  "target": "00296bd5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296bd5",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "00296bd5",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeac18`](#insn-00aeac18)

~~~json
{
  "source": "00aeac18",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeac20`](#insn-00aeac20)

~~~json
{
  "source": "00aeac20",
  "target": "010a0750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0750",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeac24`](#insn-00aeac24)

~~~json
{
  "source": "00aeac24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
