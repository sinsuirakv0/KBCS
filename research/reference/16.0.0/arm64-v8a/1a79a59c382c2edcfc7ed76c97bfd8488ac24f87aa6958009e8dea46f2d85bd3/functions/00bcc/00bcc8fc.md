# 00bcc8fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5d3fc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d3fc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-5832727882e63a7e77c0f3295579c87b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bccd24`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd24.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-a99300c0b029e3b56509746f96f8b3c7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcc8fc",
  "name": "_ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "700834f3c5b6f4f44916f4a06137307859fb4edc58c2e0f3afeb3da070f6b6fa",
  "source_text_sha256": "700834f3c5b6f4f44916f4a06137307859fb4edc58c2e0f3afeb3da070f6b6fa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcc8fc",
        "00bcc93b"
      ]
    ],
    "bytes_sha256": "0df02849093048c3ca45ca11e647d9d54d38db05b6f9d01bf2ef9e080995d81e",
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
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 538 bytes

~~~c

long _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
                    /* try { // try from 00bcc90c to 00ccc9bf has its CatchHandler @ 00bcc3d4 */
  if (DAT_01126418 == 0) {
    DAT_01126418 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126418;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcc8fc"></a> `00bcc8fc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcc900"></a> `00bcc900` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc904"></a> `00bcc904` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcc908"></a> `00bcc908` | `d3 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc90c"></a> `00bcc90c` | `68 0e 42 f9` | ldr x8,[x19, #0x418] | `FALL_THROUGH`
<a id="insn-00bcc910"></a> `00bcc910` | `e8 00 00 b5` | cbnz x8,0x00bcc92c | `CONDITIONAL_JUMP`
<a id="insn-00bcc914"></a> `00bcc914` | `e3 b6 ff d0` | adrp x3,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bcc918"></a> `00bcc918` | `63 f4 22 91` | add x3,x3,#0x8bd | `FALL_THROUGH`
<a id="insn-00bcc91c"></a> `00bcc91c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bcc920"></a> `00bcc920` | `7c 38 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc924"></a> `00bcc924` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcc928"></a> `00bcc928` | `60 0e 02 f9` | str x0,[x19, #0x418] | `FALL_THROUGH`
<a id="insn-00bcc92c"></a> `00bcc92c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc930"></a> `00bcc930` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcc934"></a> `00bcc934` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcc938"></a> `00bcc938` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcc8fc`](#insn-00bcc8fc) 範囲 `[['00bcc8fc', '00bcc90b']]`
  - `FALL_THROUGH` [`00bcc908`](#insn-00bcc908) → [`00bcc90c`](#insn-00bcc90c)
- ブロック [`00bcc90c`](#insn-00bcc90c) 範囲 `[['00bcc90c', '00bcc913']]`
  - `CONDITIONAL_JUMP` [`00bcc910`](#insn-00bcc910) → [`00bcc92c`](#insn-00bcc92c)
  - `FALL_THROUGH` [`00bcc910`](#insn-00bcc910) → [`00bcc914`](#insn-00bcc914)
- ブロック [`00bcc914`](#insn-00bcc914) 範囲 `[['00bcc914', '00bcc92b']]`
  - `FALL_THROUGH` [`00bcc928`](#insn-00bcc928) → [`00bcc92c`](#insn-00bcc92c)
- ブロック [`00bcc92c`](#insn-00bcc92c) 範囲 `[['00bcc92c', '00bcc93b']]`

## 命令位置別の参照

- [`00bcc8fc`](#insn-00bcc8fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc900`](#insn-00bcc900) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc90c`](#insn-00bcc90c) → `01126418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc910`](#insn-00bcc910) → [`00bcc92c`](#insn-00bcc92c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc918`](#insn-00bcc918) → `002aa8bd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcc920`](#insn-00bcc920) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bcc928`](#insn-00bcc928) → `01126418`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc92c`](#insn-00bcc92c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcc8fc`](#insn-00bcc8fc)

~~~json
{
  "source": "00bcc8fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc900`](#insn-00bcc900)

~~~json
{
  "source": "00bcc900",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc90c`](#insn-00bcc90c)

~~~json
{
  "source": "00bcc90c",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc910`](#insn-00bcc910)

~~~json
{
  "source": "00bcc910",
  "target": "00bcc92c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc918`](#insn-00bcc918)

~~~json
{
  "source": "00bcc918",
  "target": "002aa8bd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa8bd",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa8bd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcc920`](#insn-00bcc920)

~~~json
{
  "source": "00bcc920",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc928`](#insn-00bcc928)

~~~json
{
  "source": "00bcc928",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc92c`](#insn-00bcc92c)

~~~json
{
  "source": "00bcc92c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
