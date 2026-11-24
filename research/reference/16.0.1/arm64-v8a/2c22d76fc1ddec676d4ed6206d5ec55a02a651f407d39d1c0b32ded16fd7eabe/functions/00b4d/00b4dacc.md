# 00b4dacc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4d6a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0073.md#compare-42440bac0ec50d13ef2e965605269c9a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4db68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4db68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0074.md#compare-fe17ddc031858901c4230e96e28a4fe3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4dacc",
  "name": "_ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "13d5fdc1b187ad7a9fe69ca837a2bf146998de685e2b43d1bb4942e70e67f68d",
  "source_text_sha256": "13d5fdc1b187ad7a9fe69ca837a2bf146998de685e2b43d1bb4942e70e67f68d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4dacc",
        "00b4db0f"
      ]
    ],
    "bytes_sha256": "8a60a0df225a01a3a751e04d3d02c0388f34ebb28c33bb5ab23e3d6ef5cbadf3",
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

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Throwable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 472 bytes

~~~c

long _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_01125cf0 == 0) {
    DAT_01125cf0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Throwable",param_3);
  }
  return DAT_01125cf0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4dacc"></a> `00b4dacc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4dad0"></a> `00b4dad0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4dad4"></a> `00b4dad4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4dad8"></a> `00b4dad8` | `d3 2e 00 90` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4dadc"></a> `00b4dadc` | `68 7a 46 f9` | ldr x8,[x19, #0xcf0] | `FALL_THROUGH`
<a id="insn-00b4dae0"></a> `00b4dae0` | `08 01 00 b5` | cbnz x8,0x00b4db00 | `CONDITIONAL_JUMP`
<a id="insn-00b4dae4"></a> `00b4dae4` | `63 bb ff 90` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00b4dae8"></a> `00b4dae8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00b4daec"></a> `00b4daec` | `63 b4 26 91` | add x3,x3,#0x9ad | `FALL_THROUGH`
<a id="insn-00b4daf0"></a> `00b4daf0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4daf4"></a> `00b4daf4` | `07 35 04 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00b4daf8"></a> `00b4daf8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4dafc"></a> `00b4dafc` | `60 7a 06 f9` | str x0,[x19, #0xcf0] | `FALL_THROUGH`
<a id="insn-00b4db00"></a> `00b4db00` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4db04"></a> `00b4db04` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4db08"></a> `00b4db08` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4db0c"></a> `00b4db0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4dacc`](#insn-00b4dacc) 範囲 `[['00b4dacc', '00b4dae3']]`
  - `CONDITIONAL_JUMP` [`00b4dae0`](#insn-00b4dae0) → [`00b4db00`](#insn-00b4db00)
  - `FALL_THROUGH` [`00b4dae0`](#insn-00b4dae0) → [`00b4dae4`](#insn-00b4dae4)
- ブロック [`00b4dae4`](#insn-00b4dae4) 範囲 `[['00b4dae4', '00b4daff']]`
  - `FALL_THROUGH` [`00b4dafc`](#insn-00b4dafc) → [`00b4db00`](#insn-00b4db00)
- ブロック [`00b4db00`](#insn-00b4db00) 範囲 `[['00b4db00', '00b4db0f']]`

## 命令位置別の参照

- [`00b4dacc`](#insn-00b4dacc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dad0`](#insn-00b4dad0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dadc`](#insn-00b4dadc) → `01125cf0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4dae0`](#insn-00b4dae0) → [`00b4db00`](#insn-00b4db00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4daec`](#insn-00b4daec) → `002b99ad`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4daf4`](#insn-00b4daf4) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00b4dafc`](#insn-00b4dafc) → `01125cf0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4db00`](#insn-00b4db00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4dacc`](#insn-00b4dacc)

~~~json
{
  "source": "00b4dacc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dad0`](#insn-00b4dad0)

~~~json
{
  "source": "00b4dad0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dadc`](#insn-00b4dadc)

~~~json
{
  "source": "00b4dadc",
  "target": "01125cf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125cf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4dae0`](#insn-00b4dae0)

~~~json
{
  "source": "00b4dae0",
  "target": "00b4db00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4daec`](#insn-00b4daec)

~~~json
{
  "source": "00b4daec",
  "target": "002b99ad",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b99ad",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f5468726f7761626c6500",
  "capture_start": "002b99ad",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4daf4`](#insn-00b4daf4)

~~~json
{
  "source": "00b4daf4",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dafc`](#insn-00b4dafc)

~~~json
{
  "source": "00b4dafc",
  "target": "01125cf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125cf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4db00`](#insn-00b4db00)

~~~json
{
  "source": "00b4db00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
