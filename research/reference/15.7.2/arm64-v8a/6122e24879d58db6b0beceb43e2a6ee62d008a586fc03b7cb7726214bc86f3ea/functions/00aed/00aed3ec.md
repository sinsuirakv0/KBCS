# 00aed3ec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aed4b4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4b4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-7263ea936dbbcfde531044e0dafc6060)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed3ec",
  "name": "_ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dfaac930225efdfbf42def4b92b7d8d69f34e93cc1a2500a1a48f4aa59a8bac2",
  "source_text_sha256": "dfaac930225efdfbf42def4b92b7d8d69f34e93cc1a2500a1a48f4aa59a8bac2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aed3ec",
        "00aed42b"
      ]
    ],
    "bytes_sha256": "65b3749b9193e39568e5d171841d4a1fa31864e3fdff5207a42840ee927ce869",
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
"java/lang/String"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 448 bytes

~~~c

long _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a0910 == 0) {
    DAT_010a0910 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0910;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aed3ec"></a> `00aed3ec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aed3f0"></a> `00aed3f0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed3f4"></a> `00aed3f4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aed3f8"></a> `00aed3f8` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aed3fc"></a> `00aed3fc` | `68 8a 44 f9` | ldr x8,[x19, #0x910] | `FALL_THROUGH`
<a id="insn-00aed400"></a> `00aed400` | `e8 00 00 b5` | cbnz x8,0x00aed41c | `CONDITIONAL_JUMP`
<a id="insn-00aed404"></a> `00aed404` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aed408"></a> `00aed408` | `83 bd ff b0` | adrp x3,0x29e000 | `FALL_THROUGH`
<a id="insn-00aed40c"></a> `00aed40c` | `63 0c 17 91` | add x3,x3,#0x5c3 | `FALL_THROUGH`
<a id="insn-00aed410"></a> `00aed410` | `e0 c2 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aed414"></a> `00aed414` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aed418"></a> `00aed418` | `60 8a 04 f9` | str x0,[x19, #0x910] | `FALL_THROUGH`
<a id="insn-00aed41c"></a> `00aed41c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed420"></a> `00aed420` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aed424"></a> `00aed424` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aed428"></a> `00aed428` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aed3ec`](#insn-00aed3ec) 範囲 `[['00aed3ec', '00aed403']]`
  - `CONDITIONAL_JUMP` [`00aed400`](#insn-00aed400) → [`00aed41c`](#insn-00aed41c)
  - `FALL_THROUGH` [`00aed400`](#insn-00aed400) → [`00aed404`](#insn-00aed404)
- ブロック [`00aed404`](#insn-00aed404) 範囲 `[['00aed404', '00aed41b']]`
  - `FALL_THROUGH` [`00aed418`](#insn-00aed418) → [`00aed41c`](#insn-00aed41c)
- ブロック [`00aed41c`](#insn-00aed41c) 範囲 `[['00aed41c', '00aed42b']]`

## 命令位置別の参照

- [`00aed3ec`](#insn-00aed3ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed3f0`](#insn-00aed3f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed3fc`](#insn-00aed3fc) → `010a0910`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed400`](#insn-00aed400) → [`00aed41c`](#insn-00aed41c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed40c`](#insn-00aed40c) → `0029e5c3`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aed410`](#insn-00aed410) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aed418`](#insn-00aed418) → `010a0910`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed41c`](#insn-00aed41c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aed3ec`](#insn-00aed3ec)

~~~json
{
  "source": "00aed3ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed3f0`](#insn-00aed3f0)

~~~json
{
  "source": "00aed3f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed3fc`](#insn-00aed3fc)

~~~json
{
  "source": "00aed3fc",
  "target": "010a0910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0910",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed400`](#insn-00aed400)

~~~json
{
  "source": "00aed400",
  "target": "00aed41c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed40c`](#insn-00aed40c)

~~~json
{
  "source": "00aed40c",
  "target": "0029e5c3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029e5c3",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f537472696e6700",
  "capture_start": "0029e5c3",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aed410`](#insn-00aed410)

~~~json
{
  "source": "00aed410",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed418`](#insn-00aed418)

~~~json
{
  "source": "00aed418",
  "target": "010a0910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0910",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed41c`](#insn-00aed41c)

~~~json
{
  "source": "00aed41c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
