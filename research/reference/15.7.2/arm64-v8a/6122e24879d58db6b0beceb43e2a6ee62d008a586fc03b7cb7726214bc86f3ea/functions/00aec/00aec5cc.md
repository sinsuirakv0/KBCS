# 00aec5cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aec694`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec694.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-fd347bdd87089798d8f288a4ea794b0d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec5cc",
  "name": "_ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b1c14d1b0eb8f3f74778d94c46d9089c7aaf3cae1f5896e859644d8b1d3cf5c",
  "source_text_sha256": "1b1c14d1b0eb8f3f74778d94c46d9089c7aaf3cae1f5896e859644d8b1d3cf5c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aec5cc",
        "00aec60f"
      ]
    ],
    "bytes_sha256": "e88366dc69bdc89111d7b1696e1b4f6221e1a9937a1d4480a09ad597349c1bbe",
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
"java/util/Map"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 460 bytes

~~~c

long _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0878 == 0) {
    DAT_010a0878 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Map",param_3);
  }
  return DAT_010a0878;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aec5cc"></a> `00aec5cc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aec5d0"></a> `00aec5d0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec5d4"></a> `00aec5d4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aec5d8"></a> `00aec5d8` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec5dc"></a> `00aec5dc` | `68 3e 44 f9` | ldr x8,[x19, #0x878] | `FALL_THROUGH`
<a id="insn-00aec5e0"></a> `00aec5e0` | `08 01 00 b5` | cbnz x8,0x00aec600 | `CONDITIONAL_JUMP`
<a id="insn-00aec5e4"></a> `00aec5e4` | `a3 bd ff 90` | adrp x3,0x2a0000 | `FALL_THROUGH`
<a id="insn-00aec5e8"></a> `00aec5e8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aec5ec"></a> `00aec5ec` | `63 b4 39 91` | add x3,x3,#0xe6d | `FALL_THROUGH`
<a id="insn-00aec5f0"></a> `00aec5f0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aec5f4"></a> `00aec5f4` | `67 c6 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aec5f8"></a> `00aec5f8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aec5fc"></a> `00aec5fc` | `60 3e 04 f9` | str x0,[x19, #0x878] | `FALL_THROUGH`
<a id="insn-00aec600"></a> `00aec600` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec604"></a> `00aec604` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aec608"></a> `00aec608` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aec60c"></a> `00aec60c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aec5cc`](#insn-00aec5cc) 範囲 `[['00aec5cc', '00aec5e3']]`
  - `CONDITIONAL_JUMP` [`00aec5e0`](#insn-00aec5e0) → [`00aec600`](#insn-00aec600)
  - `FALL_THROUGH` [`00aec5e0`](#insn-00aec5e0) → [`00aec5e4`](#insn-00aec5e4)
- ブロック [`00aec5e4`](#insn-00aec5e4) 範囲 `[['00aec5e4', '00aec5ff']]`
  - `FALL_THROUGH` [`00aec5fc`](#insn-00aec5fc) → [`00aec600`](#insn-00aec600)
- ブロック [`00aec600`](#insn-00aec600) 範囲 `[['00aec600', '00aec60f']]`

## 命令位置別の参照

- [`00aec5cc`](#insn-00aec5cc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec5d0`](#insn-00aec5d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec5dc`](#insn-00aec5dc) → `010a0878`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec5e0`](#insn-00aec5e0) → [`00aec600`](#insn-00aec600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec5ec`](#insn-00aec5ec) → `002a0e6d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aec5f4`](#insn-00aec5f4) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aec5fc`](#insn-00aec5fc) → `010a0878`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec600`](#insn-00aec600) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aec5cc`](#insn-00aec5cc)

~~~json
{
  "source": "00aec5cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec5d0`](#insn-00aec5d0)

~~~json
{
  "source": "00aec5d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec5dc`](#insn-00aec5dc)

~~~json
{
  "source": "00aec5dc",
  "target": "010a0878",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0878",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec5e0`](#insn-00aec5e0)

~~~json
{
  "source": "00aec5e0",
  "target": "00aec600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec5ec`](#insn-00aec5ec)

~~~json
{
  "source": "00aec5ec",
  "target": "002a0e6d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0e6d",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4d617000",
  "capture_start": "002a0e6d",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aec5f4`](#insn-00aec5f4)

~~~json
{
  "source": "00aec5f4",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec5fc`](#insn-00aec5fc)

~~~json
{
  "source": "00aec5fc",
  "target": "010a0878",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0878",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec600`](#insn-00aec600)

~~~json
{
  "source": "00aec600",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
