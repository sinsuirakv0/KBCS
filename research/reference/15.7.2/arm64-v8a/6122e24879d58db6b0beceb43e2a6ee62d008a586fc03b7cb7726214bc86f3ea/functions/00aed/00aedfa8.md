# 00aedfa8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aee070`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee070.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-2d4414fad330da9bc395e61bc850eeff)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedfa8",
  "name": "_ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0e8e6c8738e2fc024be2ab1c3c72cd69eca064105d4f1d1987a747a358b51b8",
  "source_text_sha256": "d0e8e6c8738e2fc024be2ab1c3c72cd69eca064105d4f1d1987a747a358b51b8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedfa8",
        "00aedfeb"
      ]
    ],
    "bytes_sha256": "a4bd428005113492feb979c0ec5b3a8c27f2b5f26a180a8aff0fdc0afd5a3b52",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
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
"java/lang/Object"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 402 bytes

~~~c

long _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0988 == 0) {
    DAT_010a0988 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Object",0);
  }
  return DAT_010a0988;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedfa8"></a> `00aedfa8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedfac"></a> `00aedfac` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedfb0"></a> `00aedfb0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedfb4"></a> `00aedfb4` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedfb8"></a> `00aedfb8` | `68 c6 44 f9` | ldr x8,[x19, #0x988] | `FALL_THROUGH`
<a id="insn-00aedfbc"></a> `00aedfbc` | `08 01 00 b5` | cbnz x8,0x00aedfdc | `CONDITIONAL_JUMP`
<a id="insn-00aedfc0"></a> `00aedfc0` | `83 bd ff 90` | adrp x3,0x29d000 | `FALL_THROUGH`
<a id="insn-00aedfc4"></a> `00aedfc4` | `63 7c 33 91` | add x3,x3,#0xcdf | `FALL_THROUGH`
<a id="insn-00aedfc8"></a> `00aedfc8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aedfcc"></a> `00aedfcc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aedfd0"></a> `00aedfd0` | `f0 bf 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aedfd4"></a> `00aedfd4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aedfd8"></a> `00aedfd8` | `60 c6 04 f9` | str x0,[x19, #0x988] | `FALL_THROUGH`
<a id="insn-00aedfdc"></a> `00aedfdc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedfe0"></a> `00aedfe0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aedfe4"></a> `00aedfe4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedfe8"></a> `00aedfe8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedfa8`](#insn-00aedfa8) 範囲 `[['00aedfa8', '00aedfbf']]`
  - `CONDITIONAL_JUMP` [`00aedfbc`](#insn-00aedfbc) → [`00aedfdc`](#insn-00aedfdc)
  - `FALL_THROUGH` [`00aedfbc`](#insn-00aedfbc) → [`00aedfc0`](#insn-00aedfc0)
- ブロック [`00aedfc0`](#insn-00aedfc0) 範囲 `[['00aedfc0', '00aedfdb']]`
  - `FALL_THROUGH` [`00aedfd8`](#insn-00aedfd8) → [`00aedfdc`](#insn-00aedfdc)
- ブロック [`00aedfdc`](#insn-00aedfdc) 範囲 `[['00aedfdc', '00aedfeb']]`

## 命令位置別の参照

- [`00aedfa8`](#insn-00aedfa8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedfac`](#insn-00aedfac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedfb8`](#insn-00aedfb8) → `010a0988`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedfbc`](#insn-00aedfbc) → [`00aedfdc`](#insn-00aedfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedfc4`](#insn-00aedfc4) → `0029dcdf`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedfd0`](#insn-00aedfd0) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aedfd8`](#insn-00aedfd8) → `010a0988`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedfdc`](#insn-00aedfdc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedfa8`](#insn-00aedfa8)

~~~json
{
  "source": "00aedfa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedfac`](#insn-00aedfac)

~~~json
{
  "source": "00aedfac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedfb8`](#insn-00aedfb8)

~~~json
{
  "source": "00aedfb8",
  "target": "010a0988",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0988",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedfbc`](#insn-00aedfbc)

~~~json
{
  "source": "00aedfbc",
  "target": "00aedfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedfc4`](#insn-00aedfc4)

~~~json
{
  "source": "00aedfc4",
  "target": "0029dcdf",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029dcdf",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4f626a65637400",
  "capture_start": "0029dcdf",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedfd0`](#insn-00aedfd0)

~~~json
{
  "source": "00aedfd0",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedfd8`](#insn-00aedfd8)

~~~json
{
  "source": "00aedfd8",
  "target": "010a0988",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0988",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedfdc`](#insn-00aedfdc)

~~~json
{
  "source": "00aedfdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
