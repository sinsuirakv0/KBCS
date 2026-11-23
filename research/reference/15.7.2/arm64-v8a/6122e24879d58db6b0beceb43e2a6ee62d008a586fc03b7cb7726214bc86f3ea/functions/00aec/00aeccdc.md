# 00aeccdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aecda4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecda4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-323a174726694e610ef43a6d1be04f1a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeccdc",
  "name": "_ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97fddd63b995ef48894ee8cc37e685a6343e044a4d722a92ce59136381473cf7",
  "source_text_sha256": "97fddd63b995ef48894ee8cc37e685a6343e044a4d722a92ce59136381473cf7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeccdc",
        "00aecd1b"
      ]
    ],
    "bytes_sha256": "75e2ebe51775b5f5ae0b88c1328e83e62e643297c1c81984f46e814d69bbc73a",
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

## 疑似コード / UTF-8 422 bytes

~~~c

long _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a08c8 == 0) {
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
<a id="insn-00aeccdc"></a> `00aeccdc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecce0"></a> `00aecce0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecce4"></a> `00aecce4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecce8"></a> `00aecce8` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeccec"></a> `00aeccec` | `68 66 44 f9` | ldr x8,[x19, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aeccf0"></a> `00aeccf0` | `e8 00 00 b5` | cbnz x8,0x00aecd0c | `CONDITIONAL_JUMP`
<a id="insn-00aeccf4"></a> `00aeccf4` | `83 bd ff f0` | adrp x3,0x29f000 | `FALL_THROUGH`
<a id="insn-00aeccf8"></a> `00aeccf8` | `63 c8 3c 91` | add x3,x3,#0xf32 | `FALL_THROUGH`
<a id="insn-00aeccfc"></a> `00aeccfc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aecd00"></a> `00aecd00` | `a4 c4 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aecd04"></a> `00aecd04` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aecd08"></a> `00aecd08` | `60 66 04 f9` | str x0,[x19, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aecd0c"></a> `00aecd0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecd10"></a> `00aecd10` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aecd14"></a> `00aecd14` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aecd18"></a> `00aecd18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeccdc`](#insn-00aeccdc) 範囲 `[['00aeccdc', '00aeccf3']]`
  - `CONDITIONAL_JUMP` [`00aeccf0`](#insn-00aeccf0) → [`00aecd0c`](#insn-00aecd0c)
  - `FALL_THROUGH` [`00aeccf0`](#insn-00aeccf0) → [`00aeccf4`](#insn-00aeccf4)
- ブロック [`00aeccf4`](#insn-00aeccf4) 範囲 `[['00aeccf4', '00aecd0b']]`
  - `FALL_THROUGH` [`00aecd08`](#insn-00aecd08) → [`00aecd0c`](#insn-00aecd0c)
- ブロック [`00aecd0c`](#insn-00aecd0c) 範囲 `[['00aecd0c', '00aecd1b']]`

## 命令位置別の参照

- [`00aeccdc`](#insn-00aeccdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecce0`](#insn-00aecce0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccec`](#insn-00aeccec) → `010a08c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeccf0`](#insn-00aeccf0) → [`00aecd0c`](#insn-00aecd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccf8`](#insn-00aeccf8) → `0029ff32`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecd00`](#insn-00aecd00) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aecd08`](#insn-00aecd08) → `010a08c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecd0c`](#insn-00aecd0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeccdc`](#insn-00aeccdc)

~~~json
{
  "source": "00aeccdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecce0`](#insn-00aecce0)

~~~json
{
  "source": "00aecce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccec`](#insn-00aeccec)

~~~json
{
  "source": "00aeccec",
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
- 参照命令 [`00aeccf0`](#insn-00aeccf0)

~~~json
{
  "source": "00aeccf0",
  "target": "00aecd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccf8`](#insn-00aeccf8)

~~~json
{
  "source": "00aeccf8",
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
- 参照命令 [`00aecd00`](#insn-00aecd00)

~~~json
{
  "source": "00aecd00",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecd08`](#insn-00aecd08)

~~~json
{
  "source": "00aecd08",
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
- 参照命令 [`00aecd0c`](#insn-00aecd0c)

~~~json
{
  "source": "00aecd0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
