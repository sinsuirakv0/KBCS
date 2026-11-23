# 00aedfac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aedee4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedee4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-4112494e9d2ac7dc951273a9cfaa6601)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aedff0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedff0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-d3e3f07bd416bf04def6c7b531e0827c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedfac",
  "name": "_ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9425e0ae930585570ecc8965c68c7ad130bad3be1af3481b4a10731c73e1c012",
  "source_text_sha256": "9425e0ae930585570ecc8965c68c7ad130bad3be1af3481b4a10731c73e1c012",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedfac",
        "00aedfeb"
      ]
    ],
    "bytes_sha256": "ae2837a3f55b5ed5f56dd872ebbe0fb8cf9fe542c6593075dd606d7e119b7962",
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

## 疑似コード / UTF-8 448 bytes

~~~c

long _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
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
<a id="insn-00aedfac"></a> `00aedfac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedfb0"></a> `00aedfb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedfb4"></a> `00aedfb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedfb8"></a> `00aedfb8` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedfbc"></a> `00aedfbc` | `68 26 45 f9` | ldr x8,[x19, #0xa48] | `FALL_THROUGH`
<a id="insn-00aedfc0"></a> `00aedfc0` | `e8 00 00 b5` | cbnz x8,0x00aedfdc | `CONDITIONAL_JUMP`
<a id="insn-00aedfc4"></a> `00aedfc4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aedfc8"></a> `00aedfc8` | `83 bd ff 90` | adrp x3,0x29d000 | `FALL_THROUGH`
<a id="insn-00aedfcc"></a> `00aedfcc` | `63 b0 35 91` | add x3,x3,#0xd6c | `FALL_THROUGH`
<a id="insn-00aedfd0"></a> `00aedfd0` | `1c c0 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aedfd4"></a> `00aedfd4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aedfd8"></a> `00aedfd8` | `60 26 05 f9` | str x0,[x19, #0xa48] | `FALL_THROUGH`
<a id="insn-00aedfdc"></a> `00aedfdc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedfe0"></a> `00aedfe0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aedfe4"></a> `00aedfe4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedfe8"></a> `00aedfe8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedfac`](#insn-00aedfac) 範囲 `[['00aedfac', '00aedfc3']]`
  - `CONDITIONAL_JUMP` [`00aedfc0`](#insn-00aedfc0) → [`00aedfdc`](#insn-00aedfdc)
  - `FALL_THROUGH` [`00aedfc0`](#insn-00aedfc0) → [`00aedfc4`](#insn-00aedfc4)
- ブロック [`00aedfc4`](#insn-00aedfc4) 範囲 `[['00aedfc4', '00aedfdb']]`
  - `FALL_THROUGH` [`00aedfd8`](#insn-00aedfd8) → [`00aedfdc`](#insn-00aedfdc)
- ブロック [`00aedfdc`](#insn-00aedfdc) 範囲 `[['00aedfdc', '00aedfeb']]`

## 命令位置別の参照

- [`00aedfac`](#insn-00aedfac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedfb0`](#insn-00aedfb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedfbc`](#insn-00aedfbc) → `010a0a48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedfc0`](#insn-00aedfc0) → [`00aedfdc`](#insn-00aedfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedfcc`](#insn-00aedfcc) → `0029dd6c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedfd0`](#insn-00aedfd0) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aedfd8`](#insn-00aedfd8) → `010a0a48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedfdc`](#insn-00aedfdc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedfac`](#insn-00aedfac)

~~~json
{
  "source": "00aedfac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedfb0`](#insn-00aedfb0)

~~~json
{
  "source": "00aedfb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedfbc`](#insn-00aedfbc)

~~~json
{
  "source": "00aedfbc",
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
- 参照命令 [`00aedfc0`](#insn-00aedfc0)

~~~json
{
  "source": "00aedfc0",
  "target": "00aedfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedfcc`](#insn-00aedfcc)

~~~json
{
  "source": "00aedfcc",
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
- 参照命令 [`00aedfd0`](#insn-00aedfd0)

~~~json
{
  "source": "00aedfd0",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedfd8`](#insn-00aedfd8)

~~~json
{
  "source": "00aedfd8",
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
- 参照命令 [`00aedfdc`](#insn-00aedfdc)

~~~json
{
  "source": "00aedfdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
