# 00aeafdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeb0a4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0a4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-25d7836624807975c1e342814d9c6f74)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeafdc",
  "name": "_ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2dd0861f05df9117f05f0fc200b559637ed6afa55d5c66038636670a92228ecc",
  "source_text_sha256": "2dd0861f05df9117f05f0fc200b559637ed6afa55d5c66038636670a92228ecc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeafdc",
        "00aeb01f"
      ]
    ],
    "bytes_sha256": "869fca92aa048680028cbf3d2be75ccb33972ebe30ba662e0ce0ac3cfd9ce3f6",
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
"java/lang/Integer"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 475 bytes

~~~c

long _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0770 == 0) {
    DAT_010a0770 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Integer",param_3);
  }
  return DAT_010a0770;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeafdc"></a> `00aeafdc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeafe0"></a> `00aeafe0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeafe4"></a> `00aeafe4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeafe8"></a> `00aeafe8` | `b3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeafec"></a> `00aeafec` | `68 ba 43 f9` | ldr x8,[x19, #0x770] | `FALL_THROUGH`
<a id="insn-00aeaff0"></a> `00aeaff0` | `08 01 00 b5` | cbnz x8,0x00aeb010 | `CONDITIONAL_JUMP`
<a id="insn-00aeaff4"></a> `00aeaff4` | `63 bd ff d0` | adrp x3,0x298000 | `FALL_THROUGH`
<a id="insn-00aeaff8"></a> `00aeaff8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aeaffc"></a> `00aeaffc` | `63 48 18 91` | add x3,x3,#0x612 | `FALL_THROUGH`
<a id="insn-00aeb000"></a> `00aeb000` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeb004"></a> `00aeb004` | `e3 cb 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeb008"></a> `00aeb008` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aeb00c"></a> `00aeb00c` | `60 ba 03 f9` | str x0,[x19, #0x770] | `FALL_THROUGH`
<a id="insn-00aeb010"></a> `00aeb010` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb014"></a> `00aeb014` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeb018"></a> `00aeb018` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeb01c"></a> `00aeb01c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeafdc`](#insn-00aeafdc) 範囲 `[['00aeafdc', '00aeaff3']]`
  - `CONDITIONAL_JUMP` [`00aeaff0`](#insn-00aeaff0) → [`00aeb010`](#insn-00aeb010)
  - `FALL_THROUGH` [`00aeaff0`](#insn-00aeaff0) → [`00aeaff4`](#insn-00aeaff4)
- ブロック [`00aeaff4`](#insn-00aeaff4) 範囲 `[['00aeaff4', '00aeb00f']]`
  - `FALL_THROUGH` [`00aeb00c`](#insn-00aeb00c) → [`00aeb010`](#insn-00aeb010)
- ブロック [`00aeb010`](#insn-00aeb010) 範囲 `[['00aeb010', '00aeb01f']]`

## 命令位置別の参照

- [`00aeafdc`](#insn-00aeafdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafe0`](#insn-00aeafe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafec`](#insn-00aeafec) → `010a0770`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaff0`](#insn-00aeaff0) → [`00aeb010`](#insn-00aeb010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaffc`](#insn-00aeaffc) → `00298612`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeb004`](#insn-00aeb004) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeb00c`](#insn-00aeb00c) → `010a0770`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb010`](#insn-00aeb010) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeafdc`](#insn-00aeafdc)

~~~json
{
  "source": "00aeafdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafe0`](#insn-00aeafe0)

~~~json
{
  "source": "00aeafe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafec`](#insn-00aeafec)

~~~json
{
  "source": "00aeafec",
  "target": "010a0770",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0770",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaff0`](#insn-00aeaff0)

~~~json
{
  "source": "00aeaff0",
  "target": "00aeb010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaffc`](#insn-00aeaffc)

~~~json
{
  "source": "00aeaffc",
  "target": "00298612",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298612",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f496e746567657200",
  "capture_start": "00298612",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeb004`](#insn-00aeb004)

~~~json
{
  "source": "00aeb004",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeb00c`](#insn-00aeb00c)

~~~json
{
  "source": "00aeb00c",
  "target": "010a0770",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0770",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb010`](#insn-00aeb010)

~~~json
{
  "source": "00aeb010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
