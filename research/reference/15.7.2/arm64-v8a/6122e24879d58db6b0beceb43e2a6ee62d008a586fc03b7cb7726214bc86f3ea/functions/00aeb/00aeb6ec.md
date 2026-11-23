# 00aeb6ec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeb7b4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7b4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-0030091688161a68c06fcb939092e7b4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeb6ec",
  "name": "_ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "60649e827239e6c5737843cec954c9c8bf8f4345e021083dd48dba9ad4c541d7",
  "source_text_sha256": "60649e827239e6c5737843cec954c9c8bf8f4345e021083dd48dba9ad4c541d7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeb6ec",
        "00aeb72b"
      ]
    ],
    "bytes_sha256": "05590ed9847a0a7ecd0dd11e24bef979b920f8d6b063be048b23e02db2cf087a",
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
"java/lang/Iterable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 427 bytes

~~~c

long _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a07d8 == 0) {
    DAT_010a07d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a07d8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeb6ec"></a> `00aeb6ec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeb6f0"></a> `00aeb6f0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb6f4"></a> `00aeb6f4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeb6f8"></a> `00aeb6f8` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeb6fc"></a> `00aeb6fc` | `68 ee 43 f9` | ldr x8,[x19, #0x7d8] | `FALL_THROUGH`
<a id="insn-00aeb700"></a> `00aeb700` | `e8 00 00 b5` | cbnz x8,0x00aeb71c | `CONDITIONAL_JUMP`
<a id="insn-00aeb704"></a> `00aeb704` | `23 bd ff b0` | adrp x3,0x290000 | `FALL_THROUGH`
<a id="insn-00aeb708"></a> `00aeb708` | `63 c8 0d 91` | add x3,x3,#0x372 | `FALL_THROUGH`
<a id="insn-00aeb70c"></a> `00aeb70c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeb710"></a> `00aeb710` | `20 ca 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeb714"></a> `00aeb714` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeb718"></a> `00aeb718` | `60 ee 03 f9` | str x0,[x19, #0x7d8] | `FALL_THROUGH`
<a id="insn-00aeb71c"></a> `00aeb71c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb720"></a> `00aeb720` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeb724"></a> `00aeb724` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeb728"></a> `00aeb728` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeb6ec`](#insn-00aeb6ec) 範囲 `[['00aeb6ec', '00aeb703']]`
  - `CONDITIONAL_JUMP` [`00aeb700`](#insn-00aeb700) → [`00aeb71c`](#insn-00aeb71c)
  - `FALL_THROUGH` [`00aeb700`](#insn-00aeb700) → [`00aeb704`](#insn-00aeb704)
- ブロック [`00aeb704`](#insn-00aeb704) 範囲 `[['00aeb704', '00aeb71b']]`
  - `FALL_THROUGH` [`00aeb718`](#insn-00aeb718) → [`00aeb71c`](#insn-00aeb71c)
- ブロック [`00aeb71c`](#insn-00aeb71c) 範囲 `[['00aeb71c', '00aeb72b']]`

## 命令位置別の参照

- [`00aeb6ec`](#insn-00aeb6ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb6f0`](#insn-00aeb6f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb6fc`](#insn-00aeb6fc) → `010a07d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb700`](#insn-00aeb700) → [`00aeb71c`](#insn-00aeb71c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb708`](#insn-00aeb708) → `00290372`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeb710`](#insn-00aeb710) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeb718`](#insn-00aeb718) → `010a07d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb71c`](#insn-00aeb71c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeb6ec`](#insn-00aeb6ec)

~~~json
{
  "source": "00aeb6ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb6f0`](#insn-00aeb6f0)

~~~json
{
  "source": "00aeb6f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb6fc`](#insn-00aeb6fc)

~~~json
{
  "source": "00aeb6fc",
  "target": "010a07d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb700`](#insn-00aeb700)

~~~json
{
  "source": "00aeb700",
  "target": "00aeb71c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb708`](#insn-00aeb708)

~~~json
{
  "source": "00aeb708",
  "target": "00290372",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290372",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4974657261626c6500",
  "capture_start": "00290372",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeb710`](#insn-00aeb710)

~~~json
{
  "source": "00aeb710",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeb718`](#insn-00aeb718)

~~~json
{
  "source": "00aeb718",
  "target": "010a07d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb71c`](#insn-00aeb71c)

~~~json
{
  "source": "00aeb71c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
