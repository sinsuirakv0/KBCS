# 00aecc9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aecd64`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd64.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-0cbd124299ec00ee6100090f552e98c3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecc9c",
  "name": "_ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3dbf280f4aaeeb7b436dd734ac56086f31fffd653ea7f76ecbaa6f1d7a8d68c5",
  "source_text_sha256": "3dbf280f4aaeeb7b436dd734ac56086f31fffd653ea7f76ecbaa6f1d7a8d68c5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecc9c",
        "00aeccdb"
      ]
    ],
    "bytes_sha256": "80b7f08cbf9a65c8654a1535855dc38d7f32190db9cc239dfa2b140d67596740",
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
"java/util/Set"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 542 bytes

~~~c

long _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a08c8 == 0) {
                    /* try { // try from 00aeccbc to 00becd27 has its CatchHandler @ 00af1a38 */
    DAT_010a08c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a08c8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecc9c"></a> `00aecc9c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecca0"></a> `00aecca0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecca4"></a> `00aecca4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecca8"></a> `00aecca8` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeccac"></a> `00aeccac` | `68 66 44 f9` | ldr x8,[x19, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aeccb0"></a> `00aeccb0` | `e8 00 00 b5` | cbnz x8,0x00aecccc | `CONDITIONAL_JUMP`
<a id="insn-00aeccb4"></a> `00aeccb4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aeccb8"></a> `00aeccb8` | `83 bd ff f0` | adrp x3,0x29f000 | `FALL_THROUGH`
<a id="insn-00aeccbc"></a> `00aeccbc` | `63 c8 3c 91` | add x3,x3,#0xf32 | `FALL_THROUGH`
<a id="insn-00aeccc0"></a> `00aeccc0` | `b4 c4 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeccc4"></a> `00aeccc4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeccc8"></a> `00aeccc8` | `60 66 04 f9` | str x0,[x19, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aecccc"></a> `00aecccc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeccd0"></a> `00aeccd0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeccd4"></a> `00aeccd4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeccd8"></a> `00aeccd8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecc9c`](#insn-00aecc9c) 範囲 `[['00aecc9c', '00aeccb3']]`
  - `CONDITIONAL_JUMP` [`00aeccb0`](#insn-00aeccb0) → [`00aecccc`](#insn-00aecccc)
  - `FALL_THROUGH` [`00aeccb0`](#insn-00aeccb0) → [`00aeccb4`](#insn-00aeccb4)
- ブロック [`00aeccb4`](#insn-00aeccb4) 範囲 `[['00aeccb4', '00aeccbb']]`
  - `FALL_THROUGH` [`00aeccb8`](#insn-00aeccb8) → [`00aeccbc`](#insn-00aeccbc)
- ブロック [`00aeccbc`](#insn-00aeccbc) 範囲 `[['00aeccbc', '00aecccb']]`
  - `FALL_THROUGH` [`00aeccc8`](#insn-00aeccc8) → [`00aecccc`](#insn-00aecccc)
- ブロック [`00aecccc`](#insn-00aecccc) 範囲 `[['00aecccc', '00aeccdb']]`

## 命令位置別の参照

- [`00aecc9c`](#insn-00aecc9c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecca0`](#insn-00aecca0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccac`](#insn-00aeccac) → `010a08c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeccb0`](#insn-00aeccb0) → [`00aecccc`](#insn-00aecccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccbc`](#insn-00aeccbc) → `0029ff32`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeccc0`](#insn-00aeccc0) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeccc8`](#insn-00aeccc8) → `010a08c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecccc`](#insn-00aecccc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecc9c`](#insn-00aecc9c)

~~~json
{
  "source": "00aecc9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecca0`](#insn-00aecca0)

~~~json
{
  "source": "00aecca0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccac`](#insn-00aeccac)

~~~json
{
  "source": "00aeccac",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeccb0`](#insn-00aeccb0)

~~~json
{
  "source": "00aeccb0",
  "target": "00aecccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccbc`](#insn-00aeccbc)

~~~json
{
  "source": "00aeccbc",
  "target": "0029ff32",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ff32",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "0029ff32",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeccc0`](#insn-00aeccc0)

~~~json
{
  "source": "00aeccc0",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeccc8`](#insn-00aeccc8)

~~~json
{
  "source": "00aeccc8",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecccc`](#insn-00aecccc)

~~~json
{
  "source": "00aecccc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
