# 00b4cbac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4c784`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c784.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0073.md#compare-751b5e150dd6d203a24e93946ca77c6c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4cc48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0073.md#compare-1ef701b296bbbedeb4deaac07f2e6612)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4cbac",
  "name": "_ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8458567d38397f8ec5fb075e971cb6fa9b11c5a24488eaaaa8e40e6dd206de7",
  "source_text_sha256": "d8458567d38397f8ec5fb075e971cb6fa9b11c5a24488eaaaa8e40e6dd206de7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4cbac",
        "00b4cbeb"
      ]
    ],
    "bytes_sha256": "b1810b86444ff6d692b116ef49a1317d99dccf1aa0cdb880c55d462675b920ec",
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

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 465 bytes

~~~c

long _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_01125c68 == 0) {
    DAT_01125c68 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01125c68;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4cbac"></a> `00b4cbac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4cbb0"></a> `00b4cbb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cbb4"></a> `00b4cbb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4cbb8"></a> `00b4cbb8` | `d3 2e 00 b0` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4cbbc"></a> `00b4cbbc` | `68 36 46 f9` | ldr x8,[x19, #0xc68] | `FALL_THROUGH`
<a id="insn-00b4cbc0"></a> `00b4cbc0` | `e8 00 00 b5` | cbnz x8,0x00b4cbdc | `CONDITIONAL_JUMP`
<a id="insn-00b4cbc4"></a> `00b4cbc4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00b4cbc8"></a> `00b4cbc8` | `a3 ba ff f0` | adrp x3,0x2a3000 | `FALL_THROUGH`
<a id="insn-00b4cbcc"></a> `00b4cbcc` | `63 bc 2c 91` | add x3,x3,#0xb2f | `FALL_THROUGH`
<a id="insn-00b4cbd0"></a> `00b4cbd0` | `d0 38 04 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00b4cbd4"></a> `00b4cbd4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4cbd8"></a> `00b4cbd8` | `60 36 06 f9` | str x0,[x19, #0xc68] | `FALL_THROUGH`
<a id="insn-00b4cbdc"></a> `00b4cbdc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cbe0"></a> `00b4cbe0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4cbe4"></a> `00b4cbe4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4cbe8"></a> `00b4cbe8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4cbac`](#insn-00b4cbac) 範囲 `[['00b4cbac', '00b4cbc3']]`
  - `CONDITIONAL_JUMP` [`00b4cbc0`](#insn-00b4cbc0) → [`00b4cbdc`](#insn-00b4cbdc)
  - `FALL_THROUGH` [`00b4cbc0`](#insn-00b4cbc0) → [`00b4cbc4`](#insn-00b4cbc4)
- ブロック [`00b4cbc4`](#insn-00b4cbc4) 範囲 `[['00b4cbc4', '00b4cbdb']]`
  - `FALL_THROUGH` [`00b4cbd8`](#insn-00b4cbd8) → [`00b4cbdc`](#insn-00b4cbdc)
- ブロック [`00b4cbdc`](#insn-00b4cbdc) 範囲 `[['00b4cbdc', '00b4cbeb']]`

## 命令位置別の参照

- [`00b4cbac`](#insn-00b4cbac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cbb0`](#insn-00b4cbb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cbbc`](#insn-00b4cbbc) → `01125c68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cbc0`](#insn-00b4cbc0) → [`00b4cbdc`](#insn-00b4cbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cbcc`](#insn-00b4cbcc) → `002a3b2f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4cbd0`](#insn-00b4cbd0) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00b4cbd8`](#insn-00b4cbd8) → `01125c68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cbdc`](#insn-00b4cbdc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4cbac`](#insn-00b4cbac)

~~~json
{
  "source": "00b4cbac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cbb0`](#insn-00b4cbb0)

~~~json
{
  "source": "00b4cbb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cbbc`](#insn-00b4cbbc)

~~~json
{
  "source": "00b4cbbc",
  "target": "01125c68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125c68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cbc0`](#insn-00b4cbc0)

~~~json
{
  "source": "00b4cbc0",
  "target": "00b4cbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cbcc`](#insn-00b4cbcc)

~~~json
{
  "source": "00b4cbcc",
  "target": "002a3b2f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3b2f",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "002a3b2f",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4cbd0`](#insn-00b4cbd0)

~~~json
{
  "source": "00b4cbd0",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4cbd8`](#insn-00b4cbd8)

~~~json
{
  "source": "00b4cbd8",
  "target": "01125c68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125c68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cbdc`](#insn-00b4cbdc)

~~~json
{
  "source": "00b4cbdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
