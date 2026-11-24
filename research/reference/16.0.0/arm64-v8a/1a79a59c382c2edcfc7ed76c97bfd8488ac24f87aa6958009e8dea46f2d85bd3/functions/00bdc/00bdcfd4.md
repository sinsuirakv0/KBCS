# 00bdcfd4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6dad4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dad4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-f2ae0b92152e109c1c992827375e473e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd3fc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3fc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-1720f937dbe70fd872111a6dda27fb51)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfd4",
  "name": "_ZN8firebase4auth4user13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3191a158043fecd773a8ad91241e8a20dd19a95f08c6d43243ca91c6366cbd70",
  "source_text_sha256": "3191a158043fecd773a8ad91241e8a20dd19a95f08c6d43243ca91c6366cbd70",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfd4",
        "00bdd043"
      ]
    ],
    "bytes_sha256": "87f7feb30eae2cba0281e36224a690c73731f87160a73c952e194dd1d7a0085a",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aaf0](../00c5a/00c5aaf0.md)
- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUser"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 642 bytes

~~~c

void _ZN8firebase4auth4user13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126920 == 0) {
    DAT_01126920 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUser",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01126920,&DAT_003101a8,1,&DAT_011269a8,
             "com/google/firebase/auth/FirebaseUser");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcfd4"></a> `00bdcfd4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdcfd8"></a> `00bdcfd8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcfdc"></a> `00bdcfdc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcfe0"></a> `00bdcfe0` | `54 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcfe4"></a> `00bdcfe4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bdcfe8"></a> `00bdcfe8` | `81 92 44 f9` | ldr x1,[x20, #0x920] | `FALL_THROUGH`
<a id="insn-00bdcfec"></a> `00bdcfec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdcff0"></a> `00bdcff0` | `41 01 00 b5` | cbnz x1,0x00bdd018 | `CONDITIONAL_JUMP`
<a id="insn-00bdcff4"></a> `00bdcff4` | `63 b6 ff b0` | adrp x3,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdcff8"></a> `00bdcff8` | `63 e8 1e 91` | add x3,x3,#0x7ba | `FALL_THROUGH`
<a id="insn-00bdcffc"></a> `00bdcffc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd000"></a> `00bdd000` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bdd004"></a> `00bdd004` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdd008"></a> `00bdd008` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdd00c"></a> `00bdd00c` | `c1 f6 01 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd010"></a> `00bdd010` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdd014"></a> `00bdd014` | `80 92 04 f9` | str x0,[x20, #0x920] | `FALL_THROUGH`
<a id="insn-00bdd018"></a> `00bdd018` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd01c"></a> `00bdd01c` | `82 b9 ff f0` | adrp x2,0x310000 | `FALL_THROUGH`
<a id="insn-00bdd020"></a> `00bdd020` | `44 2a 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd024"></a> `00bdd024` | `65 b6 ff 90` | adrp x5,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdd028"></a> `00bdd028` | `42 a0 06 91` | add x2,x2,#0x1a8 | `FALL_THROUGH`
<a id="insn-00bdd02c"></a> `00bdd02c` | `84 a0 26 91` | add x4,x4,#0x9a8 | `FALL_THROUGH`
<a id="insn-00bdd030"></a> `00bdd030` | `a5 e8 1e 91` | add x5,x5,#0x7ba | `FALL_THROUGH`
<a id="insn-00bdd034"></a> `00bdd034` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bdd038"></a> `00bdd038` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd03c"></a> `00bdd03c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdd040"></a> `00bdd040` | `ac f6 01 14` | b 0x00c5aaf0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfd4`](#insn-00bdcfd4) 範囲 `[['00bdcfd4', '00bdcff3']]`
  - `CONDITIONAL_JUMP` [`00bdcff0`](#insn-00bdcff0) → [`00bdd018`](#insn-00bdd018)
  - `FALL_THROUGH` [`00bdcff0`](#insn-00bdcff0) → [`00bdcff4`](#insn-00bdcff4)
- ブロック [`00bdcff4`](#insn-00bdcff4) 範囲 `[['00bdcff4', '00bdd017']]`
  - `FALL_THROUGH` [`00bdd014`](#insn-00bdd014) → [`00bdd018`](#insn-00bdd018)
- ブロック [`00bdd018`](#insn-00bdd018) 範囲 `[['00bdd018', '00bdd043']]`

## 命令位置別の参照

- [`00bdcfd4`](#insn-00bdcfd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcfd8`](#insn-00bdcfd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcfe8`](#insn-00bdcfe8) → `01126920`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcff0`](#insn-00bdcff0) → [`00bdd018`](#insn-00bdd018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcff8`](#insn-00bdcff8) → `002a97ba`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdd00c`](#insn-00bdd00c) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bdd014`](#insn-00bdd014) → `01126920`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd018`](#insn-00bdd018) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd028`](#insn-00bdd028) → `003101a8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd02c`](#insn-00bdd02c) → `011269a8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd030`](#insn-00bdd030) → `002a97ba`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdd040`](#insn-00bdd040) → [`00c5aaf0`](../00c5a/00c5aaf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aaf0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfd4`](#insn-00bdcfd4)

~~~json
{
  "source": "00bdcfd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcfd8`](#insn-00bdcfd8)

~~~json
{
  "source": "00bdcfd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcfe8`](#insn-00bdcfe8)

~~~json
{
  "source": "00bdcfe8",
  "target": "01126920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcff0`](#insn-00bdcff0)

~~~json
{
  "source": "00bdcff0",
  "target": "00bdd018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcff8`](#insn-00bdcff8)

~~~json
{
  "source": "00bdcff8",
  "target": "002a97ba",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a97b6",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a97b6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdd00c`](#insn-00bdd00c)

~~~json
{
  "source": "00bdd00c",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd014`](#insn-00bdd014)

~~~json
{
  "source": "00bdd014",
  "target": "01126920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd018`](#insn-00bdd018)

~~~json
{
  "source": "00bdd018",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd028`](#insn-00bdd028)

~~~json
{
  "source": "00bdd028",
  "target": "003101a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd02c`](#insn-00bdd02c)

~~~json
{
  "source": "00bdd02c",
  "target": "011269a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd030`](#insn-00bdd030)

~~~json
{
  "source": "00bdd030",
  "target": "002a97ba",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a97b6",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a97b6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdd040`](#insn-00bdd040)

~~~json
{
  "source": "00bdd040",
  "target": "00c5aaf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
