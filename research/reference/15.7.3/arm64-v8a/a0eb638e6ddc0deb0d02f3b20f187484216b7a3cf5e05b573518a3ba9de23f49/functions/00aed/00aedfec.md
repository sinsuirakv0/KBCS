# 00aedfec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aedf24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-dbea1896b652210580c99556e10fbcbe)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aee030`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aee/00aee030.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-3d7fa74bbd0cd3085976280229c4f5c5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedfec",
  "name": "_ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afca692c3423af462f3274cc564d43622315a8b7268408f618d6fe3ce15237b3",
  "source_text_sha256": "afca692c3423af462f3274cc564d43622315a8b7268408f618d6fe3ce15237b3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedfec",
        "00aee02b"
      ]
    ],
    "bytes_sha256": "e8812cec21cbef3b3ecb78c3d78b3d09131f13abb139bf60945d95b798e8006d",
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

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Object"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 425 bytes

~~~c

long _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a0a48 == 0) {
    DAT_010a0a48 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0a48;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedfec"></a> `00aedfec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedff0"></a> `00aedff0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedff4"></a> `00aedff4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedff8"></a> `00aedff8` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedffc"></a> `00aedffc` | `68 26 45 f9` | ldr x8,[x19, #0xa48] | `FALL_THROUGH`
<a id="insn-00aee000"></a> `00aee000` | `e8 00 00 b5` | cbnz x8,0x00aee01c | `CONDITIONAL_JUMP`
<a id="insn-00aee004"></a> `00aee004` | `63 bd ff f0` | adrp x3,0x29d000 | `FALL_THROUGH`
<a id="insn-00aee008"></a> `00aee008` | `63 b0 35 91` | add x3,x3,#0xd6c | `FALL_THROUGH`
<a id="insn-00aee00c"></a> `00aee00c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aee010"></a> `00aee010` | `0c c0 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aee014"></a> `00aee014` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aee018"></a> `00aee018` | `60 26 05 f9` | str x0,[x19, #0xa48] | `FALL_THROUGH`
<a id="insn-00aee01c"></a> `00aee01c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aee020"></a> `00aee020` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aee024"></a> `00aee024` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aee028"></a> `00aee028` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedfec`](#insn-00aedfec) 範囲 `[['00aedfec', '00aee003']]`
  - `CONDITIONAL_JUMP` [`00aee000`](#insn-00aee000) → [`00aee01c`](#insn-00aee01c)
  - `FALL_THROUGH` [`00aee000`](#insn-00aee000) → [`00aee004`](#insn-00aee004)
- ブロック [`00aee004`](#insn-00aee004) 範囲 `[['00aee004', '00aee01b']]`
  - `FALL_THROUGH` [`00aee018`](#insn-00aee018) → [`00aee01c`](#insn-00aee01c)
- ブロック [`00aee01c`](#insn-00aee01c) 範囲 `[['00aee01c', '00aee02b']]`

## 命令位置別の参照

- [`00aedfec`](#insn-00aedfec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedff0`](#insn-00aedff0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedffc`](#insn-00aedffc) → `010a0a48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee000`](#insn-00aee000) → [`00aee01c`](#insn-00aee01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aee008`](#insn-00aee008) → `0029dd6c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aee010`](#insn-00aee010) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aee018`](#insn-00aee018) → `010a0a48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aee01c`](#insn-00aee01c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedfec`](#insn-00aedfec)

~~~json
{
  "source": "00aedfec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedff0`](#insn-00aedff0)

~~~json
{
  "source": "00aedff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedffc`](#insn-00aedffc)

~~~json
{
  "source": "00aedffc",
  "target": "010a0a48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee000`](#insn-00aee000)

~~~json
{
  "source": "00aee000",
  "target": "00aee01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aee008`](#insn-00aee008)

~~~json
{
  "source": "00aee008",
  "target": "0029dd6c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029dd6c",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4f626a65637400",
  "capture_start": "0029dd6c",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aee010`](#insn-00aee010)

~~~json
{
  "source": "00aee010",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aee018`](#insn-00aee018)

~~~json
{
  "source": "00aee018",
  "target": "010a0a48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aee01c`](#insn-00aee01c)

~~~json
{
  "source": "00aee01c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
