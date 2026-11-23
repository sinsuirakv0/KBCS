# 00aedbbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aedc84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-50be6e852c3ed834e6d275e66109b14b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedbbc",
  "name": "_ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae0f1114cddfd75ad423ce192bd243b4dfa58979397b3c45517882d11562e3d5",
  "source_text_sha256": "ae0f1114cddfd75ad423ce192bd243b4dfa58979397b3c45517882d11562e3d5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedbbc",
        "00aedbff"
      ]
    ],
    "bytes_sha256": "7488c30f9bbd732465e5f25d502111cec5bdccc898195f6571a3f59f595b540f",
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
"android/net/Uri"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 462 bytes

~~~c

long _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0960 == 0) {
    DAT_010a0960 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/net/Uri",param_3);
  }
  return DAT_010a0960;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedbbc"></a> `00aedbbc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedbc0"></a> `00aedbc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedbc4"></a> `00aedbc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedbc8"></a> `00aedbc8` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedbcc"></a> `00aedbcc` | `68 b2 44 f9` | ldr x8,[x19, #0x960] | `FALL_THROUGH`
<a id="insn-00aedbd0"></a> `00aedbd0` | `08 01 00 b5` | cbnz x8,0x00aedbf0 | `CONDITIONAL_JUMP`
<a id="insn-00aedbd4"></a> `00aedbd4` | `43 bd ff d0` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aedbd8"></a> `00aedbd8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aedbdc"></a> `00aedbdc` | `63 e0 13 91` | add x3,x3,#0x4f8 | `FALL_THROUGH`
<a id="insn-00aedbe0"></a> `00aedbe0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aedbe4"></a> `00aedbe4` | `eb c0 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aedbe8"></a> `00aedbe8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aedbec"></a> `00aedbec` | `60 b2 04 f9` | str x0,[x19, #0x960] | `FALL_THROUGH`
<a id="insn-00aedbf0"></a> `00aedbf0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedbf4"></a> `00aedbf4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aedbf8"></a> `00aedbf8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedbfc"></a> `00aedbfc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedbbc`](#insn-00aedbbc) 範囲 `[['00aedbbc', '00aedbd3']]`
  - `CONDITIONAL_JUMP` [`00aedbd0`](#insn-00aedbd0) → [`00aedbf0`](#insn-00aedbf0)
  - `FALL_THROUGH` [`00aedbd0`](#insn-00aedbd0) → [`00aedbd4`](#insn-00aedbd4)
- ブロック [`00aedbd4`](#insn-00aedbd4) 範囲 `[['00aedbd4', '00aedbef']]`
  - `FALL_THROUGH` [`00aedbec`](#insn-00aedbec) → [`00aedbf0`](#insn-00aedbf0)
- ブロック [`00aedbf0`](#insn-00aedbf0) 範囲 `[['00aedbf0', '00aedbff']]`

## 命令位置別の参照

- [`00aedbbc`](#insn-00aedbbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbc0`](#insn-00aedbc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbcc`](#insn-00aedbcc) → `010a0960`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedbd0`](#insn-00aedbd0) → [`00aedbf0`](#insn-00aedbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbdc`](#insn-00aedbdc) → `002974f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedbe4`](#insn-00aedbe4) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aedbec`](#insn-00aedbec) → `010a0960`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedbf0`](#insn-00aedbf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedbbc`](#insn-00aedbbc)

~~~json
{
  "source": "00aedbbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbc0`](#insn-00aedbc0)

~~~json
{
  "source": "00aedbc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbcc`](#insn-00aedbcc)

~~~json
{
  "source": "00aedbcc",
  "target": "010a0960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedbd0`](#insn-00aedbd0)

~~~json
{
  "source": "00aedbd0",
  "target": "00aedbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbdc`](#insn-00aedbdc)

~~~json
{
  "source": "00aedbdc",
  "target": "002974f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974f8",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "616e64726f69642f6e65742f55726900",
  "capture_start": "002974f8",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedbe4`](#insn-00aedbe4)

~~~json
{
  "source": "00aedbe4",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedbec`](#insn-00aedbec)

~~~json
{
  "source": "00aedbec",
  "target": "010a0960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedbf0`](#insn-00aedbf0)

~~~json
{
  "source": "00aedbf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
