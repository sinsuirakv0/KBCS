# 00aeac7c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeabb4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeabb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-759182f4faa002f93126cf36a2004a39)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeacc0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeacc0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-9b92b0169bbc66d218e74754acb25e88)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeac7c",
  "name": "_ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0beb8523fff0aad2ea7e8adf233e8aa24cea732993ad12f76e6ad219e964a45f",
  "source_text_sha256": "0beb8523fff0aad2ea7e8adf233e8aa24cea732993ad12f76e6ad219e964a45f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeac7c",
        "00aeacbb"
      ]
    ],
    "bytes_sha256": "480fde6db5c1b9dd5e4dff2ceab711ff1a5c052cbdade9f01ff556b1f567aaac",
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
"java/util/HashMap"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 450 bytes

~~~c

long _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a0810 == 0) {
    DAT_010a0810 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0810;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeac7c"></a> `00aeac7c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeac80"></a> `00aeac80` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeac84"></a> `00aeac84` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeac88"></a> `00aeac88` | `b3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeac8c"></a> `00aeac8c` | `68 0a 44 f9` | ldr x8,[x19, #0x810] | `FALL_THROUGH`
<a id="insn-00aeac90"></a> `00aeac90` | `e8 00 00 b5` | cbnz x8,0x00aeacac | `CONDITIONAL_JUMP`
<a id="insn-00aeac94"></a> `00aeac94` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aeac98"></a> `00aeac98` | `63 bd ff 90` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00aeac9c"></a> `00aeac9c` | `63 88 31 91` | add x3,x3,#0xc62 | `FALL_THROUGH`
<a id="insn-00aeaca0"></a> `00aeaca0` | `e8 cc 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaca4"></a> `00aeaca4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeaca8"></a> `00aeaca8` | `60 0a 04 f9` | str x0,[x19, #0x810] | `FALL_THROUGH`
<a id="insn-00aeacac"></a> `00aeacac` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeacb0"></a> `00aeacb0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeacb4"></a> `00aeacb4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeacb8"></a> `00aeacb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeac7c`](#insn-00aeac7c) 範囲 `[['00aeac7c', '00aeac93']]`
  - `CONDITIONAL_JUMP` [`00aeac90`](#insn-00aeac90) → [`00aeacac`](#insn-00aeacac)
  - `FALL_THROUGH` [`00aeac90`](#insn-00aeac90) → [`00aeac94`](#insn-00aeac94)
- ブロック [`00aeac94`](#insn-00aeac94) 範囲 `[['00aeac94', '00aeacab']]`
  - `FALL_THROUGH` [`00aeaca8`](#insn-00aeaca8) → [`00aeacac`](#insn-00aeacac)
- ブロック [`00aeacac`](#insn-00aeacac) 範囲 `[['00aeacac', '00aeacbb']]`

## 命令位置別の参照

- [`00aeac7c`](#insn-00aeac7c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeac80`](#insn-00aeac80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeac8c`](#insn-00aeac8c) → `010a0810`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeac90`](#insn-00aeac90) → [`00aeacac`](#insn-00aeacac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeac9c`](#insn-00aeac9c) → `00296c62`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaca0`](#insn-00aeaca0) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aeaca8`](#insn-00aeaca8) → `010a0810`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeacac`](#insn-00aeacac) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeac7c`](#insn-00aeac7c)

~~~json
{
  "source": "00aeac7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeac80`](#insn-00aeac80)

~~~json
{
  "source": "00aeac80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeac8c`](#insn-00aeac8c)

~~~json
{
  "source": "00aeac8c",
  "target": "010a0810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0810",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeac90`](#insn-00aeac90)

~~~json
{
  "source": "00aeac90",
  "target": "00aeacac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeac9c`](#insn-00aeac9c)

~~~json
{
  "source": "00aeac9c",
  "target": "00296c62",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296c62",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "00296c62",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeaca0`](#insn-00aeaca0)

~~~json
{
  "source": "00aeaca0",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaca8`](#insn-00aeaca8)

~~~json
{
  "source": "00aeaca8",
  "target": "010a0810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0810",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeacac`](#insn-00aeacac)

~~~json
{
  "source": "00aeacac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
