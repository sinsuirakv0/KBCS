# 00aebe7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebf44`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf44.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-52b8f36aec095ef18c31914d8f6881d9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebe7c",
  "name": "_ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "248258c2ada0069e4a67ae1b5bd668f4014cc81db4da93ccdecf3ffd380b7f7f",
  "source_text_sha256": "248258c2ada0069e4a67ae1b5bd668f4014cc81db4da93ccdecf3ffd380b7f7f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebe7c",
        "00aebebf"
      ]
    ],
    "bytes_sha256": "79016b85feba4e7327aafd40977a018626785ded2f4a3206b9a4175ca0fe42c2",
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
"java/util/List"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 559 bytes

~~~c

long _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0820 == 0) {
                    /* try { // try from 00aebe9c to 00bebeaf has its CatchHandler @ 00af1bd4 */
    DAT_010a0820 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/List",param_3);
  }
  return DAT_010a0820;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebe7c"></a> `00aebe7c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebe80"></a> `00aebe80` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebe84"></a> `00aebe84` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebe88"></a> `00aebe88` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebe8c"></a> `00aebe8c` | `68 12 44 f9` | ldr x8,[x19, #0x820] | `FALL_THROUGH`
<a id="insn-00aebe90"></a> `00aebe90` | `08 01 00 b5` | cbnz x8,0x00aebeb0 | `CONDITIONAL_JUMP`
<a id="insn-00aebe94"></a> `00aebe94` | `23 bd ff b0` | adrp x3,0x290000 | `FALL_THROUGH`
<a id="insn-00aebe98"></a> `00aebe98` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aebe9c"></a> `00aebe9c` | `63 14 0e 91` | add x3,x3,#0x385 | `FALL_THROUGH`
<a id="insn-00aebea0"></a> `00aebea0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebea4"></a> `00aebea4` | `3b c8 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aebea8"></a> `00aebea8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebeac"></a> `00aebeac` | `60 12 04 f9` | str x0,[x19, #0x820] | `FALL_THROUGH`
<a id="insn-00aebeb0"></a> `00aebeb0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebeb4"></a> `00aebeb4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aebeb8"></a> `00aebeb8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebebc"></a> `00aebebc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebe7c`](#insn-00aebe7c) 範囲 `[['00aebe7c', '00aebe93']]`
  - `CONDITIONAL_JUMP` [`00aebe90`](#insn-00aebe90) → [`00aebeb0`](#insn-00aebeb0)
  - `FALL_THROUGH` [`00aebe90`](#insn-00aebe90) → [`00aebe94`](#insn-00aebe94)
- ブロック [`00aebe94`](#insn-00aebe94) 範囲 `[['00aebe94', '00aebe9b']]`
  - `FALL_THROUGH` [`00aebe98`](#insn-00aebe98) → [`00aebe9c`](#insn-00aebe9c)
- ブロック [`00aebe9c`](#insn-00aebe9c) 範囲 `[['00aebe9c', '00aebeaf']]`
  - `FALL_THROUGH` [`00aebeac`](#insn-00aebeac) → [`00aebeb0`](#insn-00aebeb0)
- ブロック [`00aebeb0`](#insn-00aebeb0) 範囲 `[['00aebeb0', '00aebebf']]`

## 命令位置別の参照

- [`00aebe7c`](#insn-00aebe7c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe80`](#insn-00aebe80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe8c`](#insn-00aebe8c) → `010a0820`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebe90`](#insn-00aebe90) → [`00aebeb0`](#insn-00aebeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe9c`](#insn-00aebe9c) → `00290385`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebea4`](#insn-00aebea4) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aebeac`](#insn-00aebeac) → `010a0820`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebeb0`](#insn-00aebeb0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebe7c`](#insn-00aebe7c)

~~~json
{
  "source": "00aebe7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe80`](#insn-00aebe80)

~~~json
{
  "source": "00aebe80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe8c`](#insn-00aebe8c)

~~~json
{
  "source": "00aebe8c",
  "target": "010a0820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebe90`](#insn-00aebe90)

~~~json
{
  "source": "00aebe90",
  "target": "00aebeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe9c`](#insn-00aebe9c)

~~~json
{
  "source": "00aebe9c",
  "target": "00290385",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290385",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4c69737400",
  "capture_start": "00290385",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebea4`](#insn-00aebea4)

~~~json
{
  "source": "00aebea4",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebeac`](#insn-00aebeac)

~~~json
{
  "source": "00aebeac",
  "target": "010a0820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebeb0`](#insn-00aebeb0)

~~~json
{
  "source": "00aebeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
