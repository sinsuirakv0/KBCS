# 00aeaf9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeb064`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb064.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-f008f7da819a5a403016ce19aa07b5f3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeaf9c",
  "name": "_ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f97a7fdb5464721e0d58cc6717fef49cdf4b5696451e5185beadacdc91c1ad9",
  "source_text_sha256": "9f97a7fdb5464721e0d58cc6717fef49cdf4b5696451e5185beadacdc91c1ad9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeaf9c",
        "00aeafdb"
      ]
    ],
    "bytes_sha256": "1949350f8bce6dc703c57fca3c5a20ab93428d3edc1e9053a30fb69d9df98762",
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
"java/lang/Integer"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 433 bytes

~~~c

long _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a0770 == 0) {
    DAT_010a0770 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0770;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeaf9c"></a> `00aeaf9c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeafa0"></a> `00aeafa0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeafa4"></a> `00aeafa4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeafa8"></a> `00aeafa8` | `b3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeafac"></a> `00aeafac` | `68 ba 43 f9` | ldr x8,[x19, #0x770] | `FALL_THROUGH`
<a id="insn-00aeafb0"></a> `00aeafb0` | `e8 00 00 b5` | cbnz x8,0x00aeafcc | `CONDITIONAL_JUMP`
<a id="insn-00aeafb4"></a> `00aeafb4` | `63 bd ff d0` | adrp x3,0x298000 | `FALL_THROUGH`
<a id="insn-00aeafb8"></a> `00aeafb8` | `63 48 18 91` | add x3,x3,#0x612 | `FALL_THROUGH`
<a id="insn-00aeafbc"></a> `00aeafbc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeafc0"></a> `00aeafc0` | `f4 cb 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeafc4"></a> `00aeafc4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeafc8"></a> `00aeafc8` | `60 ba 03 f9` | str x0,[x19, #0x770] | `FALL_THROUGH`
<a id="insn-00aeafcc"></a> `00aeafcc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeafd0"></a> `00aeafd0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeafd4"></a> `00aeafd4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeafd8"></a> `00aeafd8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeaf9c`](#insn-00aeaf9c) 範囲 `[['00aeaf9c', '00aeafb3']]`
  - `CONDITIONAL_JUMP` [`00aeafb0`](#insn-00aeafb0) → [`00aeafcc`](#insn-00aeafcc)
  - `FALL_THROUGH` [`00aeafb0`](#insn-00aeafb0) → [`00aeafb4`](#insn-00aeafb4)
- ブロック [`00aeafb4`](#insn-00aeafb4) 範囲 `[['00aeafb4', '00aeafcb']]`
  - `FALL_THROUGH` [`00aeafc8`](#insn-00aeafc8) → [`00aeafcc`](#insn-00aeafcc)
- ブロック [`00aeafcc`](#insn-00aeafcc) 範囲 `[['00aeafcc', '00aeafdb']]`

## 命令位置別の参照

- [`00aeaf9c`](#insn-00aeaf9c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafa0`](#insn-00aeafa0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafac`](#insn-00aeafac) → `010a0770`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeafb0`](#insn-00aeafb0) → [`00aeafcc`](#insn-00aeafcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafb8`](#insn-00aeafb8) → `00298612`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeafc0`](#insn-00aeafc0) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeafc8`](#insn-00aeafc8) → `010a0770`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeafcc`](#insn-00aeafcc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeaf9c`](#insn-00aeaf9c)

~~~json
{
  "source": "00aeaf9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafa0`](#insn-00aeafa0)

~~~json
{
  "source": "00aeafa0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafac`](#insn-00aeafac)

~~~json
{
  "source": "00aeafac",
  "target": "010a0770",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0770",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeafb0`](#insn-00aeafb0)

~~~json
{
  "source": "00aeafb0",
  "target": "00aeafcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafb8`](#insn-00aeafb8)

~~~json
{
  "source": "00aeafb8",
  "target": "00298612",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298612",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f496e746567657200",
  "capture_start": "00298612",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeafc0`](#insn-00aeafc0)

~~~json
{
  "source": "00aeafc0",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeafc8`](#insn-00aeafc8)

~~~json
{
  "source": "00aeafc8",
  "target": "010a0770",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0770",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeafcc`](#insn-00aeafcc)

~~~json
{
  "source": "00aeafcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
