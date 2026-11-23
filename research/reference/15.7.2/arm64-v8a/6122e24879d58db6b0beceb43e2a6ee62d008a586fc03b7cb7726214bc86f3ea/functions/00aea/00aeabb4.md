# 00aeabb4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeac7c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac7c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-759182f4faa002f93126cf36a2004a39)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeabb4",
  "name": "_ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6d7a73325400c5b21617250d187e7bf0e1ea46c61318759054a723b8c3220d4",
  "source_text_sha256": "d6d7a73325400c5b21617250d187e7bf0e1ea46c61318759054a723b8c3220d4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeabb4",
        "00aeabf3"
      ]
    ],
    "bytes_sha256": "bba250ee3eb3904e1529cc2c836b006a374e99c87dc5b8e2fdcaa33fad9b1fb1",
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

## 疑似コード / UTF-8 450 bytes

~~~c

long _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a0750 == 0) {
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
<a id="insn-00aeabb4"></a> `00aeabb4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeabb8"></a> `00aeabb8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeabbc"></a> `00aeabbc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeabc0"></a> `00aeabc0` | `b3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeabc4"></a> `00aeabc4` | `68 aa 43 f9` | ldr x8,[x19, #0x750] | `FALL_THROUGH`
<a id="insn-00aeabc8"></a> `00aeabc8` | `e8 00 00 b5` | cbnz x8,0x00aeabe4 | `CONDITIONAL_JUMP`
<a id="insn-00aeabcc"></a> `00aeabcc` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aeabd0"></a> `00aeabd0` | `63 bd ff 90` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00aeabd4"></a> `00aeabd4` | `63 54 2f 91` | add x3,x3,#0xbd5 | `FALL_THROUGH`
<a id="insn-00aeabd8"></a> `00aeabd8` | `ee cc 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeabdc"></a> `00aeabdc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeabe0"></a> `00aeabe0` | `60 aa 03 f9` | str x0,[x19, #0x750] | `FALL_THROUGH`
<a id="insn-00aeabe4"></a> `00aeabe4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeabe8"></a> `00aeabe8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeabec"></a> `00aeabec` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeabf0"></a> `00aeabf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeabb4`](#insn-00aeabb4) 範囲 `[['00aeabb4', '00aeabcb']]`
  - `CONDITIONAL_JUMP` [`00aeabc8`](#insn-00aeabc8) → [`00aeabe4`](#insn-00aeabe4)
  - `FALL_THROUGH` [`00aeabc8`](#insn-00aeabc8) → [`00aeabcc`](#insn-00aeabcc)
- ブロック [`00aeabcc`](#insn-00aeabcc) 範囲 `[['00aeabcc', '00aeabe3']]`
  - `FALL_THROUGH` [`00aeabe0`](#insn-00aeabe0) → [`00aeabe4`](#insn-00aeabe4)
- ブロック [`00aeabe4`](#insn-00aeabe4) 範囲 `[['00aeabe4', '00aeabf3']]`

## 命令位置別の参照

- [`00aeabb4`](#insn-00aeabb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeabb8`](#insn-00aeabb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeabc4`](#insn-00aeabc4) → `010a0750`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeabc8`](#insn-00aeabc8) → [`00aeabe4`](#insn-00aeabe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeabd4`](#insn-00aeabd4) → `00296bd5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeabd8`](#insn-00aeabd8) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeabe0`](#insn-00aeabe0) → `010a0750`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeabe4`](#insn-00aeabe4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeabb4`](#insn-00aeabb4)

~~~json
{
  "source": "00aeabb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeabb8`](#insn-00aeabb8)

~~~json
{
  "source": "00aeabb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeabc4`](#insn-00aeabc4)

~~~json
{
  "source": "00aeabc4",
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
- 参照命令 [`00aeabc8`](#insn-00aeabc8)

~~~json
{
  "source": "00aeabc8",
  "target": "00aeabe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeabd4`](#insn-00aeabd4)

~~~json
{
  "source": "00aeabd4",
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
- 参照命令 [`00aeabd8`](#insn-00aeabd8)

~~~json
{
  "source": "00aeabd8",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeabe0`](#insn-00aeabe0)

~~~json
{
  "source": "00aeabe0",
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
- 参照命令 [`00aeabe4`](#insn-00aeabe4)

~~~json
{
  "source": "00aeabe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
