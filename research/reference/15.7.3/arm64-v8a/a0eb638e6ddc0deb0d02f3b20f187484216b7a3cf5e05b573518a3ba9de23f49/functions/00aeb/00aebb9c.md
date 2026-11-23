# 00aebb9c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aebad4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebad4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-a8772263fa73fc62105c15ce475a3f87)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aebbe0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebbe0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-3b70fd148556fff08870f85f15566141)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebb9c",
  "name": "_ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab13c259ee6ceaa13cc61e0dd73ee7869b616929fc56fb3f50aa72fb41b674a9",
  "source_text_sha256": "ab13c259ee6ceaa13cc61e0dd73ee7869b616929fc56fb3f50aa72fb41b674a9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebb9c",
        "00aebbdf"
      ]
    ],
    "bytes_sha256": "2341c4bef44890e33c1886960397b67ca0e5a19b263b1502c29d08aba4bd584c",
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
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 567 bytes

~~~c

long _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a08b8 == 0) {
                    /* try { // try from 00aebbc4 to 00bebbdb has its CatchHandler @ 00af1a8c */
    DAT_010a08b8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",param_3);
  }
  return DAT_010a08b8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebb9c"></a> `00aebb9c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebba0"></a> `00aebba0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebba4"></a> `00aebba4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebba8"></a> `00aebba8` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebbac"></a> `00aebbac` | `68 5e 44 f9` | ldr x8,[x19, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebbb0"></a> `00aebbb0` | `08 01 00 b5` | cbnz x8,0x00aebbd0 | `CONDITIONAL_JUMP`
<a id="insn-00aebbb4"></a> `00aebbb4` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebbb8"></a> `00aebbb8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aebbbc"></a> `00aebbbc` | `63 9c 15 91` | add x3,x3,#0x567 | `FALL_THROUGH`
<a id="insn-00aebbc0"></a> `00aebbc0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebbc4"></a> `00aebbc4` | `1f c9 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aebbc8"></a> `00aebbc8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebbcc"></a> `00aebbcc` | `60 5e 04 f9` | str x0,[x19, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebbd0"></a> `00aebbd0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebbd4"></a> `00aebbd4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aebbd8"></a> `00aebbd8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebbdc"></a> `00aebbdc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebb9c`](#insn-00aebb9c) 範囲 `[['00aebb9c', '00aebbb3']]`
  - `CONDITIONAL_JUMP` [`00aebbb0`](#insn-00aebbb0) → [`00aebbd0`](#insn-00aebbd0)
  - `FALL_THROUGH` [`00aebbb0`](#insn-00aebbb0) → [`00aebbb4`](#insn-00aebbb4)
- ブロック [`00aebbb4`](#insn-00aebbb4) 範囲 `[['00aebbb4', '00aebbc3']]`
  - `FALL_THROUGH` [`00aebbc0`](#insn-00aebbc0) → [`00aebbc4`](#insn-00aebbc4)
- ブロック [`00aebbc4`](#insn-00aebbc4) 範囲 `[['00aebbc4', '00aebbcf']]`
  - `FALL_THROUGH` [`00aebbcc`](#insn-00aebbcc) → [`00aebbd0`](#insn-00aebbd0)
- ブロック [`00aebbd0`](#insn-00aebbd0) 範囲 `[['00aebbd0', '00aebbdf']]`

## 命令位置別の参照

- [`00aebb9c`](#insn-00aebb9c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebba0`](#insn-00aebba0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebbac`](#insn-00aebbac) → `010a08b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebbb0`](#insn-00aebbb0) → [`00aebbd0`](#insn-00aebbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebbbc`](#insn-00aebbbc) → `00297567`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebbc4`](#insn-00aebbc4) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aebbcc`](#insn-00aebbcc) → `010a08b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebbd0`](#insn-00aebbd0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebb9c`](#insn-00aebb9c)

~~~json
{
  "source": "00aebb9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebba0`](#insn-00aebba0)

~~~json
{
  "source": "00aebba0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebbac`](#insn-00aebbac)

~~~json
{
  "source": "00aebbac",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebbb0`](#insn-00aebbb0)

~~~json
{
  "source": "00aebbb0",
  "target": "00aebbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebbbc`](#insn-00aebbbc)

~~~json
{
  "source": "00aebbbc",
  "target": "00297567",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297567",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "00297567",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebbc4`](#insn-00aebbc4)

~~~json
{
  "source": "00aebbc4",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebbcc`](#insn-00aebbcc)

~~~json
{
  "source": "00aebbcc",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebbd0`](#insn-00aebbd0)

~~~json
{
  "source": "00aebbd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
