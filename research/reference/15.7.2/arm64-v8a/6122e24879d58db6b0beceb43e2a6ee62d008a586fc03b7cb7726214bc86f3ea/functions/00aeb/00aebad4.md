# 00aebad4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebb9c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb9c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-a8772263fa73fc62105c15ce475a3f87)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebad4",
  "name": "_ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ac9a91b6ee60a445597b5493d385438b76184d6b4500ab2ad25fe2c60deeb6f",
  "source_text_sha256": "0ac9a91b6ee60a445597b5493d385438b76184d6b4500ab2ad25fe2c60deeb6f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebad4",
        "00aebb17"
      ]
    ],
    "bytes_sha256": "d555615b1c2411b07c7927c21cf31817d054bab23de18f1fbcfe9643e4ab4723",
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
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 470 bytes

~~~c

long _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a07f8 == 0) {
    DAT_010a07f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",param_3);
  }
  return DAT_010a07f8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebad4"></a> `00aebad4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebad8"></a> `00aebad8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebadc"></a> `00aebadc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebae0"></a> `00aebae0` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebae4"></a> `00aebae4` | `68 fe 43 f9` | ldr x8,[x19, #0x7f8] | `FALL_THROUGH`
<a id="insn-00aebae8"></a> `00aebae8` | `08 01 00 b5` | cbnz x8,0x00aebb08 | `CONDITIONAL_JUMP`
<a id="insn-00aebaec"></a> `00aebaec` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebaf0"></a> `00aebaf0` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aebaf4"></a> `00aebaf4` | `63 68 13 91` | add x3,x3,#0x4da | `FALL_THROUGH`
<a id="insn-00aebaf8"></a> `00aebaf8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebafc"></a> `00aebafc` | `25 c9 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aebb00"></a> `00aebb00` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebb04"></a> `00aebb04` | `60 fe 03 f9` | str x0,[x19, #0x7f8] | `FALL_THROUGH`
<a id="insn-00aebb08"></a> `00aebb08` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebb0c"></a> `00aebb0c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aebb10"></a> `00aebb10` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebb14"></a> `00aebb14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebad4`](#insn-00aebad4) 範囲 `[['00aebad4', '00aebaeb']]`
  - `CONDITIONAL_JUMP` [`00aebae8`](#insn-00aebae8) → [`00aebb08`](#insn-00aebb08)
  - `FALL_THROUGH` [`00aebae8`](#insn-00aebae8) → [`00aebaec`](#insn-00aebaec)
- ブロック [`00aebaec`](#insn-00aebaec) 範囲 `[['00aebaec', '00aebb07']]`
  - `FALL_THROUGH` [`00aebb04`](#insn-00aebb04) → [`00aebb08`](#insn-00aebb08)
- ブロック [`00aebb08`](#insn-00aebb08) 範囲 `[['00aebb08', '00aebb17']]`

## 命令位置別の参照

- [`00aebad4`](#insn-00aebad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebad8`](#insn-00aebad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebae4`](#insn-00aebae4) → `010a07f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebae8`](#insn-00aebae8) → [`00aebb08`](#insn-00aebb08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebaf4`](#insn-00aebaf4) → `002974da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebafc`](#insn-00aebafc) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aebb04`](#insn-00aebb04) → `010a07f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebb08`](#insn-00aebb08) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebad4`](#insn-00aebad4)

~~~json
{
  "source": "00aebad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebad8`](#insn-00aebad8)

~~~json
{
  "source": "00aebad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebae4`](#insn-00aebae4)

~~~json
{
  "source": "00aebae4",
  "target": "010a07f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebae8`](#insn-00aebae8)

~~~json
{
  "source": "00aebae8",
  "target": "00aebb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebaf4`](#insn-00aebaf4)

~~~json
{
  "source": "00aebaf4",
  "target": "002974da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974da",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "002974da",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebafc`](#insn-00aebafc)

~~~json
{
  "source": "00aebafc",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebb04`](#insn-00aebb04)

~~~json
{
  "source": "00aebb04",
  "target": "010a07f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebb08`](#insn-00aebb08)

~~~json
{
  "source": "00aebb08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
