# 00aecde4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aecd1c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd1c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-fecec2368226fac118abdebf88274e8a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aece28`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece28.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-bf9d7cd9508017201a0667d8b1b7382a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecde4",
  "name": "_ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "477142a766c9a7398e9fb61e3b16ac462e0d1b918e7dcc78d244372d39535d26",
  "source_text_sha256": "477142a766c9a7398e9fb61e3b16ac462e0d1b918e7dcc78d244372d39535d26",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecde4",
        "00aece27"
      ]
    ],
    "bytes_sha256": "81dc53dbf993b07ce901603a0b0faa1c038210ae94a01b461e999925d26fb443",
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

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 460 bytes

~~~c

long _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0988 == 0) {
    DAT_010a0988 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Set",param_3);
  }
  return DAT_010a0988;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecde4"></a> `00aecde4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecde8"></a> `00aecde8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecdec"></a> `00aecdec` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecdf0"></a> `00aecdf0` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecdf4"></a> `00aecdf4` | `68 c6 44 f9` | ldr x8,[x19, #0x988] | `FALL_THROUGH`
<a id="insn-00aecdf8"></a> `00aecdf8` | `08 01 00 b5` | cbnz x8,0x00aece18 | `CONDITIONAL_JUMP`
<a id="insn-00aecdfc"></a> `00aecdfc` | `83 bd ff f0` | adrp x3,0x29f000 | `FALL_THROUGH`
<a id="insn-00aece00"></a> `00aece00` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aece04"></a> `00aece04` | `63 fc 3e 91` | add x3,x3,#0xfbf | `FALL_THROUGH`
<a id="insn-00aece08"></a> `00aece08` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aece0c"></a> `00aece0c` | `8d c4 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aece10"></a> `00aece10` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aece14"></a> `00aece14` | `60 c6 04 f9` | str x0,[x19, #0x988] | `FALL_THROUGH`
<a id="insn-00aece18"></a> `00aece18` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aece1c"></a> `00aece1c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aece20"></a> `00aece20` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aece24"></a> `00aece24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecde4`](#insn-00aecde4) 範囲 `[['00aecde4', '00aecdfb']]`
  - `CONDITIONAL_JUMP` [`00aecdf8`](#insn-00aecdf8) → [`00aece18`](#insn-00aece18)
  - `FALL_THROUGH` [`00aecdf8`](#insn-00aecdf8) → [`00aecdfc`](#insn-00aecdfc)
- ブロック [`00aecdfc`](#insn-00aecdfc) 範囲 `[['00aecdfc', '00aece17']]`
  - `FALL_THROUGH` [`00aece14`](#insn-00aece14) → [`00aece18`](#insn-00aece18)
- ブロック [`00aece18`](#insn-00aece18) 範囲 `[['00aece18', '00aece27']]`

## 命令位置別の参照

- [`00aecde4`](#insn-00aecde4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecde8`](#insn-00aecde8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecdf4`](#insn-00aecdf4) → `010a0988`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecdf8`](#insn-00aecdf8) → [`00aece18`](#insn-00aece18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece04`](#insn-00aece04) → `0029ffbf`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aece0c`](#insn-00aece0c) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aece14`](#insn-00aece14) → `010a0988`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aece18`](#insn-00aece18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecde4`](#insn-00aecde4)

~~~json
{
  "source": "00aecde4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecde8`](#insn-00aecde8)

~~~json
{
  "source": "00aecde8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecdf4`](#insn-00aecdf4)

~~~json
{
  "source": "00aecdf4",
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
- 参照命令 [`00aecdf8`](#insn-00aecdf8)

~~~json
{
  "source": "00aecdf8",
  "target": "00aece18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece04`](#insn-00aece04)

~~~json
{
  "source": "00aece04",
  "target": "0029ffbf",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ffbf",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "0029ffbf",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aece0c`](#insn-00aece0c)

~~~json
{
  "source": "00aece0c",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aece14`](#insn-00aece14)

~~~json
{
  "source": "00aece14",
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
- 参照命令 [`00aece18`](#insn-00aece18)

~~~json
{
  "source": "00aece18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
